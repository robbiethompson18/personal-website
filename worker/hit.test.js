// Tests for the browser script hit.js (`npm test`). No browser: the script only touches
// a handful of globals, so it runs in a node:vm context with fakes for them.

import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import vm from "node:vm";

const SCRIPT = readFileSync(new URL("../hit.js", import.meta.url), "utf8");

// Load hit.js as a page would. Returns what it sent, both like buttons, and localStorage.
function load({
  hostname = "robbiewmthompson.com",
  referrer = "",
  liked = false,
  button = true,
  beacon = true,
} = {}) {
  const sent = [];
  const store = new Map(liked ? [["liked:/blog/some-post/", "1"]] : []);
  // A post has two like buttons (beside the title, and at the end of the text).
  const makeButton = () => ({
    attrs: { "aria-pressed": "false" },
    setAttribute(name, value) {
      this.attrs[name] = value;
    },
    addEventListener(type, fn) {
      this[type] = fn;
    },
  });
  const like = makeButton();
  const other = makeButton();
  vm.runInNewContext(SCRIPT, {
    URL,
    location: { hostname, pathname: "/blog/some-post/" },
    document: {
      referrer,
      querySelectorAll: (sel) => (button && sel === ".like" ? [like, other] : []),
    },
    navigator: beacon
      ? { sendBeacon: (url, body) => sent.push({ via: "beacon", url, body: JSON.parse(body) }) }
      : {},
    fetch: (url, opts) => {
      sent.push({
        via: "fetch",
        url,
        body: JSON.parse(opts.body),
        method: opts.method,
        keepalive: opts.keepalive,
      });
      return Promise.reject(new Error("offline")); // a failed request must not surface anywhere
    },
    localStorage: { getItem: (k) => store.get(k) ?? null, setItem: (k, v) => store.set(k, v) },
  });
  return { sent, like, other, store };
}

test("sends one hit with the path and the referrer's hostname", () => {
  const { sent } = load({ referrer: "https://t.co/AbC123?utm=x" });
  assert.deepEqual(sent, [
    { via: "beacon", url: "/api/hit", body: { path: "/blog/some-post/", referrer: "t.co" } },
  ]);
});

test("no referrer is an empty string", () => {
  assert.equal(load().sent[0].body.referrer, "");
});

test("sends nothing anywhere but the real site", () => {
  for (const hostname of [
    "robbiewmthompson.localhost",
    "localhost",
    "personal-website.robbiethompson2018.workers.dev",
  ]) {
    const { sent, like } = load({ hostname });
    like.click();
    assert.deepEqual(sent, [], hostname);
    assert.equal(like.attrs["aria-pressed"], "true", "the button still works locally");
  }
});

test("falls back to fetch with keepalive when sendBeacon is missing", () => {
  const { sent } = load({ beacon: false });
  assert.deepEqual(sent, [
    {
      via: "fetch",
      url: "/api/hit",
      body: { path: "/blog/some-post/", referrer: "" },
      method: "POST",
      keepalive: true,
    },
  ]);
});

test("pages without a like button just send the hit", () => {
  assert.equal(load({ button: false }).sent.length, 1);
});

test("clicking like fills both hearts, remembers it, and sends one like", () => {
  const { sent, like, other, store } = load();
  assert.equal(like.attrs["aria-pressed"], "false");
  like.click();
  like.click(); // like only: a second click neither unlikes nor re-sends
  other.click(); // nor does the page's other button
  assert.equal(like.attrs["aria-pressed"], "true");
  assert.equal(other.attrs["aria-pressed"], "true");
  assert.equal(store.get("liked:/blog/some-post/"), "1");
  assert.deepEqual(sent.slice(1), [
    { via: "beacon", url: "/api/like", body: { path: "/blog/some-post/" } },
  ]);
});

test("a post liked on an earlier visit loads filled and cannot be liked again", () => {
  const { sent, like, other } = load({ liked: true });
  assert.equal(like.attrs["aria-pressed"], "true");
  assert.equal(other.attrs["aria-pressed"], "true");
  other.click();
  assert.equal(sent.length, 1, "only the hit");
});
