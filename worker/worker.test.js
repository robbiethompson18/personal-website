// Integration tests for the Worker (`npm test`). They boot `wrangler dev` on a spare port
// against a throwaway local D1, so nothing here touches the deployed Worker or its data.
// Each test owns a page path, which keeps the tests independent without wiping tables.

import { test, before, after } from "node:test";
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
let base, wrangler;

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
    ],
    { stdio: "ignore", detached: true }, // detached: its own process group, so after() can kill workerd too
  );
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
  for (const referrer of ["t.co", "t.co", "www.google.com", "", "127.0.0.1"]) {
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

test("video Range requests still get 206", async () => {
  const res = await fetch(base + VIDEO, { headers: { Range: "bytes=0-99" } });
  assert.equal(res.status, 206);
  assert.match(res.headers.get("Content-Range"), /^bytes 0-99\/\d+$/);
  assert.equal((await res.arrayBuffer()).byteLength, 100);
});

test("pages are still served as static assets", async () => {
  const res = await fetch(base + "/dateme/");
  assert.equal(res.status, 200);
  assert.match(await res.text(), /<script src="\/hit\.js\?v=[0-9a-f]{8}" defer><\/script>/);
});
