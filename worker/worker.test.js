// Integration tests for the Worker (`npm test`). They boot `wrangler dev` on a spare port
// against a throwaway local D1, so nothing here touches the deployed Worker or its data.
// Each test owns a page path, which keeps the tests independent without wiping tables.

import { test, before, beforeEach, after } from "node:test";
import assert from "node:assert/strict";
import { spawn, execFileSync } from "node:child_process";
import { mkdtempSync, rmSync } from "node:fs";
import { createServer } from "node:net";
import { tmpdir } from "node:os";
import { join } from "node:path";

const BROWSER =
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/18.0 Safari/605.1.15";
const OTHER_BROWSER = "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0";
const VIDEO = "/blog/a-touch-feral/butter-haul.mp4";

const state = mkdtempSync(join(tmpdir(), "personal-website-d1-"));
const AUTHOR_KEY = "test-author-key"; // stands in for the Worker secret
let base, wrangler;
let log = ""; // wrangler dev's output: its local send_email binding prints each email there

function freePort() {
  return new Promise((resolve) => {
    const srv = createServer().listen(0, "127.0.0.1", () => {
      const { port } = srv.address();
      srv.close(() => resolve(port));
    });
  });
}

// Query the same local D1 file the dev server writes to.
function db(sql) {
  const out = execFileSync(
    "wrangler",
    [
      "d1",
      "execute",
      "personal-website",
      "--local",
      "--persist-to",
      state,
      "--json",
      "--command",
      sql,
    ],
    { encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] },
  );
  return JSON.parse(out)[0].results;
}

// A request as hit.js would send it; `headers` overrides (null deletes) for the rejection tests.
function post(endpoint, body, headers = {}) {
  const all = { Origin: base, "Sec-Fetch-Site": "same-origin", "User-Agent": BROWSER, ...headers };
  for (const k of Object.keys(all)) if (all[k] === null) delete all[k];
  return fetch(base + endpoint, {
    method: "POST",
    headers: all,
    body: typeof body === "string" ? body : JSON.stringify(body),
  });
}

before(async () => {
  execFileSync(
    "wrangler",
    ["d1", "migrations", "apply", "personal-website", "--local", "--persist-to", state],
    {
      stdio: "ignore",
    },
  );
  const [port, inspectorPort] = [await freePort(), await freePort()];
  base = `http://127.0.0.1:${port}`;
  wrangler = spawn(
    "wrangler",
    [
      "dev",
      "--ip",
      "127.0.0.1",
      "--port",
      port,
      "--inspector-port",
      inspectorPort,
      "--persist-to",
      state,
      "--var",
      `AUTHOR_KEY:${AUTHOR_KEY}`,
    ],
    { stdio: ["ignore", "pipe", "pipe"], detached: true }, // detached: its own process group, so after() can kill workerd too
  );
  for (const stream of [wrangler.stdout, wrangler.stderr])
    stream.on("data", (chunk) => (log += chunk));
  for (let i = 0; i < 300; i++) {
    const up = await fetch(base + "/").then(
      (r) => r.ok,
      () => false,
    );
    if (up) return;
    await new Promise((r) => setTimeout(r, 200));
  }
  throw new Error("wrangler dev did not come up");
});

// db() blocks the event loop for a second or more per call. If the dev server closes its
// idle keep-alive connection meanwhile, Node hasn't seen that yet when the next test
// starts, and its first fetch dies with ECONNRESET on the dead socket. One turn of the
// event loop lets Node notice and open a fresh connection.
beforeEach(() => new Promise((resolve) => setImmediate(resolve)));

after(() => {
  if (wrangler) process.kill(-wrangler.pid);
  rmSync(state, { recursive: true, force: true });
});

test("a hit counts one view", async () => {
  const res = await post("/api/hit", { path: "/dateme/", referrer: "" });
  assert.equal(res.status, 204);
  assert.deepEqual(db("SELECT path, referrer, count FROM views WHERE path = '/dateme/'"), [
    { path: "/dateme/", referrer: "", count: 1 },
  ]);
});

test("repeat hits from one visitor are views, not new unique visitors", async () => {
  await post("/api/hit", { path: "/blog/", referrer: "" });
  await post("/api/hit", { path: "/blog/", referrer: "" });
  assert.equal(db("SELECT SUM(count) AS n FROM views WHERE path = '/blog/'")[0].n, 2);
  assert.equal(db("SELECT COUNT(*) AS n FROM visitors WHERE path = '/blog/'")[0].n, 1);

  await post("/api/hit", { path: "/blog/", referrer: "" }, { "User-Agent": OTHER_BROWSER });
  assert.equal(db("SELECT SUM(count) AS n FROM views WHERE path = '/blog/'")[0].n, 3);
  assert.equal(db("SELECT COUNT(*) AS n FROM visitors WHERE path = '/blog/'")[0].n, 2);
});

test("referrers are bucketed by host: external, none, internal", async () => {
  // `wrangler dev` presents requests to the Worker under the host of the route in
  // wrangler.jsonc, so the site's own hostname is the real one even locally.
  for (const referrer of ["t.co", "t.co", "www.google.com", "", "robbiewmthompson.com"]) {
    assert.equal((await post("/api/hit", { path: "/", referrer })).status, 204);
  }
  assert.deepEqual(db("SELECT referrer, count FROM views WHERE path = '/' ORDER BY referrer"), [
    { referrer: "", count: 1 },
    { referrer: "google.com", count: 1 },
    { referrer: "internal", count: 1 },
    { referrer: "t.co", count: 2 },
  ]);
});

test("a like is recorded once per visitor per day", async () => {
  const path = "/blog/a-touch-feral/";
  assert.equal((await post("/api/like", { path })).status, 204);
  assert.equal((await post("/api/like", { path })).status, 204);
  assert.equal(db(`SELECT COUNT(*) AS n FROM likes WHERE path = '${path}'`)[0].n, 1);

  await post("/api/like", { path }, { "User-Agent": OTHER_BROWSER });
  assert.equal(db(`SELECT COUNT(*) AS n FROM likes WHERE path = '${path}'`)[0].n, 2);
  assert.equal(
    db(`SELECT COUNT(*) AS n FROM views WHERE path = '${path}'`)[0].n,
    0,
    "a like is not a view",
  );
});

test("bad requests are rejected and write nothing", async () => {
  const ok = { path: "/projects/", referrer: "" }; // valid, so each case fails for its own reason only
  const cases = [
    ["cross-origin", 403, () => post("/api/hit", ok, { Origin: "https://evil.example" })],
    ["no Origin", 403, () => post("/api/hit", ok, { Origin: null })],
    ["cross-site fetch", 403, () => post("/api/hit", ok, { "Sec-Fetch-Site": "cross-site" })],
    ["cross-origin like", 403, () => post("/api/like", ok, { Origin: "https://evil.example" })],
    [
      "bot",
      403,
      () => post("/api/hit", ok, { "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1)" }),
    ],
    ["curl", 403, () => post("/api/hit", ok, { "User-Agent": "curl/8.7.1" })],
    ["oversized body", 413, () => post("/api/hit", { ...ok, pad: "x".repeat(5000) })],
    ["not JSON", 400, () => post("/api/hit", "path=/projects/")],
    ["JSON null", 400, () => post("/api/hit", "null")],
    ["junk referrer", 400, () => post("/api/hit", { path: "/projects/", referrer: "<script>" })],
    ["junk path", 400, () => post("/api/hit", { path: "/no-such-page/", referrer: "" })],
    ["junk like path", 400, () => post("/api/like", { path: "/no-such-page/" })],
    ["asset, not a page", 400, () => post("/api/hit", { path: "/blog.css", referrer: "" })],
    ["non-canonical page URL", 400, () => post("/api/hit", { path: "/projects", referrer: "" })],
    [
      "another origin's path",
      400,
      () => post("/api/hit", { path: "//evil.example/projects/", referrer: "" }),
    ],
    [
      "GET",
      405,
      () => fetch(base + "/api/hit", { headers: { Origin: base, "User-Agent": BROWSER } }),
    ],
    [
      "PUT",
      405,
      () => fetch(base + "/api/like", { method: "PUT", headers: { Origin: base }, body: "{}" }),
    ],
    ["unknown endpoint", 404, () => post("/api/stats", ok)],
    ["bare /api/", 404, () => fetch(base + "/api/")],
  ];
  for (const [name, status, send] of cases) assert.equal((await send()).status, status, name);

  const junk = "path LIKE '%projects%' OR path LIKE '%no-such-page%' OR path LIKE '%blog.css%'";
  for (const table of ["views", "visitors", "likes"]) {
    assert.equal(db(`SELECT COUNT(*) AS n FROM ${table} WHERE ${junk}`)[0].n, 0, table);
  }
});

test("visitors are stored as a daily salted hash, and old salts are deleted", async () => {
  const today = new Date().toISOString().slice(0, 10);
  assert.deepEqual(
    db("SELECT day FROM salts").map((r) => r.day),
    [today],
  );
  const before = db("SELECT visitor FROM visitors WHERE path = '/dateme/'")[0].visitor;
  assert.match(before, /^[0-9a-f]{32}$/);

  // Pretend a day went by: yesterday's salt is the only one left.
  db(`UPDATE salts SET day = '2000-01-01'`);
  await post("/api/hit", { path: "/dateme/", referrer: "" });
  assert.deepEqual(
    db("SELECT day FROM salts").map((r) => r.day),
    [today],
  );
  // Same browser, new salt: a different hash, so the two days cannot be linked.
  const hashes = db("SELECT visitor FROM visitors WHERE path = '/dateme/'").map((r) => r.visitor);
  assert.equal(hashes.length, 2);
});

const comments = (path) => fetch(`${base}/api/comments?path=${path}`).then((r) => r.json());

test("a comment is stored as plain text, listed oldest first, and emailed to Robbie", async () => {
  const path = "/blog/plastic-straws/";
  assert.deepEqual(await comments(path), []);

  const res = await post("/api/comment", {
    path,
    name: "  Ada   Lovelace ",
    body: "  <script>alert(1)</script>\r\n\r\n\r\n\r\nsecond paragraph  ",
  });
  assert.equal(res.status, 201);
  const made = await res.json();
  assert.match(made.created, /^\d{4}-\d\d-\d\dT[\d:.]+Z$/);
  assert.deepEqual(made, {
    id: made.id,
    name: "Ada Lovelace", // trimmed, inner whitespace collapsed
    body: "<script>alert(1)</script>\n\nsecond paragraph", // as typed: comments.js shows it as text
    created: made.created,
    author: 0,
  });

  await post("/api/comment", { path, name: "", body: "no name given" });
  const listed = await comments(path);
  assert.deepEqual(listed[0], made);
  assert.deepEqual(
    listed.map((c) => [c.name, c.body]),
    [
      ["Ada Lovelace", made.body],
      ["Anonymous", "no name given"],
    ],
  );
  assert.deepEqual(Object.keys(listed[0]), ["id", "name", "body", "created", "author"]); // no visitor hash
  assert.match(
    db(`SELECT visitor FROM comments WHERE id = ${made.id}`)[0].visitor,
    /^[0-9a-f]{32}$/,
  );

  // The email goes out after the response, so give it a moment to reach wrangler's log.
  const subject = `Subject: New comment on ${path}`;
  for (let i = 0; i < 50 && !log.includes(subject); i++)
    await new Promise((r) => setTimeout(r, 100));
  assert.ok(log.includes(subject), "no notification email");
  assert.ok(!log.includes("comment email failed"));
});

test("only Robbie's key can post under his name or as the author", async () => {
  const path = "/blog/serial/";
  for (const name of [
    "Robbie",
    "robbie thompson",
    " ROBBIE ",
    "Robbie W. M. Thompson",
    "Ｒｏｂｂｉｅ",
  ]) {
    assert.equal((await post("/api/comment", { path, name, body: "it's me" })).status, 403, name);
  }
  const wrongKey = await post("/api/comment", { path, name: "Ada", body: "hi", key: "guess" });
  assert.equal(wrongKey.status, 403);
  assert.deepEqual(await comments(path), []);

  // Other Robbies are fine, and the real one gets the author flag.
  assert.equal(
    (await post("/api/comment", { path, name: "Robbie K", body: "also me" })).status,
    201,
  );
  const res = await post("/api/comment", { path, name: "Robbie", body: "thanks", key: AUTHOR_KEY });
  assert.equal(res.status, 201);
  assert.deepEqual(
    (await comments(path)).map((c) => [c.name, c.author]),
    [
      ["Robbie K", 0],
      ["Robbie", 1],
    ],
  );
  await new Promise((r) => setTimeout(r, 500));
  assert.ok(!log.includes(`Subject: New comment on ${path}\n\nText: thanks`));
  assert.equal(
    log.split(`Subject: New comment on ${path}`).length - 1,
    1,
    "Robbie's own comment emailed him",
  );
});

test("a comment can be deleted with Robbie's key and not without", async () => {
  const path = "/blog/honesty/";
  const keep = await (await post("/api/comment", { path, name: "Ada", body: "keep" })).json();
  const spam = await (await post("/api/comment", { path, name: "Spam", body: "buy" })).json();

  assert.equal((await post("/api/comment/delete", { id: spam.id })).status, 403);
  assert.equal((await post("/api/comment/delete", { id: spam.id, key: "guess" })).status, 403);
  assert.equal(
    (await post("/api/comment/delete", { id: "1 OR 1=1", key: AUTHOR_KEY })).status,
    400,
  );
  assert.equal((await comments(path)).length, 2);

  assert.equal((await post("/api/comment/delete", { id: spam.id, key: AUTHOR_KEY })).status, 204);
  assert.deepEqual(await comments(path), [keep]);
});

test("bad comments are rejected and write nothing", async () => {
  const path = "/blog/miasma/";
  const ok = { path, name: "Ada", body: "hello" };
  const cases = [
    ["cross-origin", 403, () => post("/api/comment", ok, { Origin: "https://evil.example" })],
    ["curl", 403, () => post("/api/comment", ok, { "User-Agent": "curl/8.7.1" })],
    ["empty", 400, () => post("/api/comment", { ...ok, body: " \n " })],
    ["too long", 400, () => post("/api/comment", { ...ok, body: "x".repeat(5001) })],
    ["long name", 400, () => post("/api/comment", { ...ok, name: "x".repeat(41) })],
    ["huge", 413, () => post("/api/comment", { ...ok, body: "x".repeat(40000) })],
    ["no name field", 400, () => post("/api/comment", { path, body: "hello" })],
    ["body not a string", 400, () => post("/api/comment", { ...ok, body: { a: 1 } })],
    ["not JSON", 400, () => post("/api/comment", "hello")],
    ["not a post", 400, () => post("/api/comment", { ...ok, path: "/dateme/" })],
    ["no such post", 400, () => post("/api/comment", { ...ok, path: "/blog/no-such-post/" })],
    ["GET to post", 405, () => fetch(base + "/api/comment")],
    ["POST to list", 405, () => post(`/api/comments?path=${path}`, ok)],
    ["list without a path", 400, () => fetch(base + "/api/comments")],
    ["list a non-post", 400, () => fetch(base + "/api/comments?path=/dateme/")],
  ];
  for (const [name, status, send] of cases) assert.equal((await send()).status, status, name);
  assert.equal(
    db(
      "SELECT COUNT(*) AS n FROM comments WHERE path IN ('/blog/miasma/', '/dateme/', '/blog/no-such-post/')",
    )[0].n,
    0,
  );

  // The longest comment allowed does fit, even when every character needs JSON escaping.
  const longest = await post("/api/comment", { ...ok, body: '"'.repeat(5000) });
  assert.equal(longest.status, 201);
});

test("video Range requests still get 206", async () => {
  const res = await fetch(base + VIDEO, { headers: { Range: "bytes=0-99" } });
  assert.equal(res.status, 206);
  assert.match(res.headers.get("Content-Range"), /^bytes 0-99\/\d+$/);
  assert.equal((await res.arrayBuffer()).byteLength, 100);
});

test("pages are still served as static assets", async () => {
  const res = await fetch(base + "/dateme/");
  assert.equal(res.status, 200);
  const page = await res.text();
  assert.match(page, /<script src="\/hit\.js\?v=[0-9a-f]{8}" defer><\/script>/);
  assert.doesNotMatch(page, /comments/, "standalone pages have no comments");
});

test("a post carries the comments section and its script", async () => {
  const page = await (await fetch(base + "/blog/a-touch-feral/")).text();
  assert.match(page, /<section class="comments" id="comments" hidden>/);
  assert.match(page, /<script src="\/comments\.js\?v=[0-9a-f]{8}" defer><\/script>/);
});
