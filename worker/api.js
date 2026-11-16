// First-party analytics: POST /api/hit counts a page view, POST /api/like records a like.
// hit.js (repo root) is the only intended caller. These are public write endpoints, so a
// request is validated hard before anything is written, and only aggregates are stored:
// no cookies, no raw IPs, no user agents. The schema is in migrations/.

const MAX_BODY = 512; // a real body is {"path":"/blog/<slug>/","referrer":"<hostname>"}
// Every page is a directory index ("/", "/blog/", "/blog/<slug>/"). Anything else (assets,
// "..", "//other-host/", query strings) is refused before the asset store is even asked.
const PAGE_PATH = /^\/([\w-]+\/)*$/;
const HOSTNAME = /^[a-z0-9.-]{0,253}$/;
// Crawlers mostly don't run JS, so this only has to catch the obvious ones that do, plus
// scripts. "http" covers the "+http://..." in bot UAs and most HTTP libraries.
const BOT = /bot|crawl|spider|headless|http|curl|wget|python/i;

export async function api(request, env) {
  const url = new URL(request.url);
  const isLike = url.pathname === "/api/like";
  if (!isLike && url.pathname !== "/api/hit") return status(404);
  if (request.method !== "POST")
    return new Response(null, { status: 405, headers: { Allow: "POST" } });
  if (!sameOrigin(request, url)) return status(403);
  if (BOT.test(request.headers.get("User-Agent") || "bot")) return status(403); // no UA at all: also a bot

  // Content-Length turns away a big upload before reading it; the length check after
  // covers a missing or wrong header.
  if (Number(request.headers.get("Content-Length")) > MAX_BODY) return status(413);
  const text = await request.text();
  if (text.length > MAX_BODY) return status(413);
  const body = parseJson(text);
  const referrer = isLike ? "" : referrerBucket(body?.referrer, url);
  if (referrer === null || !(await isPage(body?.path, url, env))) return status(400);

  const day = new Date().toISOString().slice(0, 10); // UTC
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
