// The site's write endpoints, plus the one read (comments). hit.js and comments.js (repo
// root) are the only intended callers. These are public write endpoints, so a request is
// validated hard before anything is written. Analytics stores only aggregates: no cookies,
// no raw IPs, no user agents. The schema is in migrations/.
//
//   POST /api/hit, /api/like    page views and likes (hit.js)
//   GET  /api/comments?path=    a post's comments, oldest first
//   POST /api/comment           add a comment; emails Robbie
//   POST /api/comment/delete    delete one, with Robbie's key

const MAX_BODY = 512; // a real body is {"path":"/blog/<slug>/","referrer":"<hostname>"}
const MAX_COMMENT_BODY = 32 * 1024; // room for a 5,000-character comment once JSON-escaped
const MAX_NAME = 40; // comments.js and the form's maxlength (build.js) use the same caps
const MAX_COMMENT = 5000;
// Every page is a directory index ("/", "/blog/", "/blog/<slug>/"). Anything else (assets,
// "..", "//other-host/", query strings) is refused before the asset store is even asked.
const PAGE_PATH = /^\/([\w-]+\/)*$/;
const POST_PATH = /^\/blog\/[\w-]+\/$/; // comments are on posts only
const HOSTNAME = /^[a-z0-9.-]{0,253}$/;
// Crawlers mostly don't run JS, so this only has to catch the obvious ones that do, plus
// scripts. "http" covers the "+http://..." in bot UAs and most HTTP libraries.
const BOT = /bot|crawl|spider|headless|http|curl|wget|python/i;
// Robbie's name, once a name is lowercased and stripped to letters: "Robbie",
// "robbie thompson", "Robbie W. M. Thompson". Only a request with his key may use it.
// Lookalike letters get past this; the author badge is what can't be faked.
const RESERVED_NAME = /^robbie(w?m?thompson)?$/;

export async function api(request, env, ctx) {
  const url = new URL(request.url);
  switch (url.pathname) {
    case "/api/hit":
    case "/api/like":
      return count(request, url, env);
    case "/api/comments":
      return listComments(request, url, env);
    case "/api/comment":
      return addComment(request, url, env, ctx);
    case "/api/comment/delete":
      return deleteComment(request, url, env);
  }
  return status(404);
}

// The checks every write shares. Returns the parsed JSON body (null if it isn't JSON), or
// the Response that turns the request away.
async function posted(request, url, maxBody) {
  if (request.method !== "POST")
    return new Response(null, { status: 405, headers: { Allow: "POST" } });
  if (!sameOrigin(request, url)) return status(403);
  if (BOT.test(request.headers.get("User-Agent") || "bot")) return status(403); // no UA at all: also a bot

  // Content-Length turns away a big upload before reading it; the length check after
  // covers a missing or wrong header.
  if (Number(request.headers.get("Content-Length")) > maxBody) return status(413);
  const text = await request.text();
  if (text.length > maxBody) return status(413);
  return parseJson(text);
}

async function count(request, url, env) {
  const isLike = url.pathname === "/api/like";
  const body = await posted(request, url, MAX_BODY);
  if (body instanceof Response) return body;
  const referrer = isLike ? "" : referrerBucket(body?.referrer, url);
  if (referrer === null || !(await isPage(body?.path, url, env))) return status(400);

  const day = today();
  const visitor = await visitorHash(request, await dailySalt(env.DB, day));
  // visitors and likes have the same shape: at most one row per visitor per page per day.
  const key = [day, body.path, visitor];
  const once = (table) =>
    env.DB.prepare(`INSERT OR IGNORE INTO ${table} (day, path, visitor) VALUES (?, ?, ?)`).bind(
      ...key,
    );
  if (isLike) {
    await once("likes").run();
  } else {
    await env.DB.batch([
      env.DB.prepare(
        "INSERT INTO views (day, path, referrer, count) VALUES (?, ?, ?, 1) " +
          "ON CONFLICT (day, path, referrer) DO UPDATE SET count = count + 1",
      ).bind(day, body.path, referrer),
      once("visitors"),
    ]);
  }
  return status(204);
}

// --- comments ---
// No accounts and no rate limit: anyone can post under any name but Robbie's, and it is
// public at once. What keeps that safe is that a comment is only ever plain text: stored
// as typed, sent as JSON, and put on the page with textContent (comments.js), so it can't
// carry markup or a clickable link.

async function listComments(request, url, env) {
  if (request.method !== "GET")
    return new Response(null, { status: 405, headers: { Allow: "GET" } });
  const path = url.searchParams.get("path") || "";
  if (!POST_PATH.test(path)) return status(400);
  const { results } = await env.DB.prepare(
    "SELECT id, name, body, created, author FROM comments WHERE path = ? ORDER BY id",
  )
    .bind(path)
    .all();
  return json(results);
}

async function addComment(request, url, env, ctx) {
  const body = await posted(request, url, MAX_COMMENT_BODY);
  if (body instanceof Response) return body;
  if (typeof body?.name !== "string" || typeof body?.body !== "string") return status(400);
  // A name is one line; a comment keeps its line breaks, but not runs of blank lines.
  const name = body.name.trim().replace(/\s+/g, " ") || "Anonymous";
  const text = body.body
    .replace(/\r\n?/g, "\n")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
  if (!text || text.length > MAX_COMMENT || name.length > MAX_NAME) return status(400);
  if (!POST_PATH.test(body.path) || !(await isPage(body.path, url, env))) return status(400);

  const author = isRobbie(body.key, env);
  if (body.key !== undefined && !author) return status(403);
  if (!author && isReserved(name)) return status(403);

  const visitor = await visitorHash(request, await dailySalt(env.DB, today()));
  const comment = await env.DB.prepare(
    "INSERT INTO comments (path, name, body, created, author, visitor) VALUES (?, ?, ?, ?, ?, ?) " +
      "RETURNING id, name, body, created, author",
  )
    .bind(body.path, name, text, new Date().toISOString(), author ? 1 : 0, visitor)
    .first();
  // The comment is saved whether or not the email goes out, and the commenter doesn't wait for it.
  if (!author) ctx.waitUntil(notify(env, url, body.path, comment));
  return json(comment, 201);
}

async function deleteComment(request, url, env) {
  const body = await posted(request, url, MAX_BODY);
  if (body instanceof Response) return body;
  if (!isRobbie(body?.key, env)) return status(403);
  if (!Number.isInteger(body.id)) return status(400);
  await env.DB.prepare("DELETE FROM comments WHERE id = ?").bind(body.id).run();
  return status(204);
}

// AUTHOR_KEY is a Worker secret (worker/CLAUDE.md). With it unset nobody is Robbie.
const isRobbie = (key, env) => !!env.AUTHOR_KEY && key === env.AUTHOR_KEY;

// NFKC folds fullwidth and other compatibility letters to the plain ones first.
const isReserved = (name) =>
  RESERVED_NAME.test(
    name
      .normalize("NFKC")
      .toLowerCase()
      .replace(/[^a-z]/g, ""),
  );

// Tell Robbie. The recipient is NOTIFY_EMAIL (wrangler.jsonc) and the subject holds only
// the path, which POST_PATH has already checked, so nothing a commenter sends reaches a
// header. A failed send is logged, never surfaced.
async function notify(env, url, path, comment) {
  const text = [
    `${comment.name} commented on ${url.origin}${path}#comments`,
    "",
    comment.body,
    "",
    "To delete it, open the post in a browser that has your author key, or run:",
    `wrangler d1 execute personal-website --remote --command="DELETE FROM comments WHERE id = ${comment.id}"`,
  ].join("\n");
  try {
    await env.EMAIL.send({
      to: env.NOTIFY_EMAIL,
      from: `comments@${url.hostname}`,
      subject: `New comment on ${path}`,
      text,
    });
  } catch (err) {
    console.error("comment email failed:", err.code, err.message);
  }
}

const json = (data, code = 200) =>
  new Response(JSON.stringify(data), {
    status: code,
    headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" },
  });

const today = () => new Date().toISOString().slice(0, 10); // UTC

const status = (code) => new Response(null, { status: code });

function parseJson(text) {
  try {
    return JSON.parse(text);
  } catch {
    return null;
  }
}

// Browsers put Origin on every POST, and newer ones add Sec-Fetch-Site. This stops other
// sites from making their visitors' browsers inflate the counts; it does not stop curl,
// which can forge both. Nothing can, short of a login.
function sameOrigin(request, url) {
  const site = request.headers.get("Sec-Fetch-Site");
  return request.headers.get("Origin") === url.origin && (!site || site === "same-origin");
}

// hit.js sends the hostname of document.referrer. Returns the bucket to count it under,
// or null if it isn't a hostname at all.
function referrerBucket(host, url) {
  if (typeof host !== "string" || !HOSTNAME.test(host)) return null;
  const bare = host.replace(/^www\./, "");
  return bare === url.hostname ? "internal" : bare;
}

// Only paths the asset store serves as an HTML page get counted, so the tables can't be
// filled with junk paths. It must be a plain 200: "/dateme" and "/dateme/index.html"
// answer with a redirect to "/dateme/", which keeps one page from splitting into three rows.
async function isPage(path, url, env) {
  if (typeof path !== "string" || !PAGE_PATH.test(path)) return false;
  const res = await env.ASSETS.fetch(new Request(url.origin + path, { method: "HEAD" }));
  return res.status === 200 && (res.headers.get("Content-Type") || "").startsWith("text/html");
}

// The salt is random, made on the first request of each UTC day, and the previous days'
// salts are deleted in the same breath. Once a salt is gone, that day's visitor hashes
// can't be recomputed from an IP, and can't be matched against any other day's.
async function dailySalt(db, day) {
  const read = () => db.prepare("SELECT salt FROM salts WHERE day = ?").bind(day).first("salt");
  const salt = await read();
  if (salt) return salt;
  await db.batch([
    // OR IGNORE: two first-requests can race; both then read back whichever salt won.
    db
      .prepare("INSERT OR IGNORE INTO salts (day, salt) VALUES (?, ?)")
      .bind(day, hex(crypto.getRandomValues(new Uint8Array(16)))),
    db.prepare("DELETE FROM salts WHERE day < ?").bind(day),
  ]);
  return read();
}

async function visitorHash(request, salt) {
  const who = [
    salt,
    request.headers.get("CF-Connecting-IP"),
    request.headers.get("User-Agent"),
  ].join("|");
  const digest = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(who));
  return hex(new Uint8Array(digest).slice(0, 16));
}

const hex = (bytes) => [...bytes].map((b) => b.toString(16).padStart(2, "0")).join("");
