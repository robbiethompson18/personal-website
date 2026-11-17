// Tests for the browser script comments.js (`npm test`). No browser: it runs in a node:vm
// context against a small fake DOM. The fake has no innerHTML at all, so a test fails if
// the script ever tries to put a comment on the page as markup.

import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import vm from "node:vm";

const SCRIPT = readFileSync(new URL("../comments.js", import.meta.url), "utf8");
const PATH = "/blog/some-post/";

function element(tag) {
  return {
    tag,
    children: [],
    listeners: {},
    textContent: "",
    set innerHTML(_) {
      throw new Error("comments.js must never set innerHTML");
    },
    append(...nodes) {
      for (const node of nodes) node.parent = this;
      this.children.push(...nodes);
    },
    remove() {
      this.parent.children.splice(this.parent.children.indexOf(this), 1);
    },
    addEventListener(type, fn) {
      this.listeners[type] = fn;
    },
    find(className) {
      return this.children.find((c) => c.className === className);
    },
  };
}

// Load comments.js as a post page would. `responses` maps "METHOD url" to a status or a
// [status, json] pair; anything unlisted fails like a dropped connection.
async function load({
  existing = [],
  stored = {},
  hash = "",
  responses = {},
  section = true,
} = {}) {
  const page = {
    section: Object.assign(element("section"), { hidden: true, scrolled: false }),
    list: element("ol"),
    form: element("form"),
    note: element("p"),
    button: element("button"),
    name: { value: "" },
    body: { value: "" },
  };
  page.section.scrollIntoView = () => (page.section.scrolled = true);
  page.form.elements = { name: page.name, body: page.body };
  page.form.querySelector = () => page.button;
  page.section.querySelector = (sel) =>
    ({ ".comment-list": page.list, ".comment-form": page.form, ".comment-status": page.note })[sel];

  const store = new Map(Object.entries(stored));
  const sent = [];
  const location = { pathname: PATH, search: "", hash };
  const replaced = [];
  vm.runInNewContext(SCRIPT, {
    location,
    history: { replaceState: (_state, _title, url) => replaced.push(url) },
    localStorage: { getItem: (k) => store.get(k) ?? null, setItem: (k, v) => store.set(k, v) },
    document: {
      querySelector: (sel) => (section && sel === ".comments" ? page.section : null),
      createElement: element,
    },
    fetch: async (url, opts = {}) => {
      const method = opts.method || "GET";
      if (method === "GET") return { ok: true, status: 200, json: async () => existing };
      sent.push({ url, body: JSON.parse(opts.body) });
      const answer = responses[`${method} ${url}`];
      if (answer === undefined) throw new Error("offline");
      const [status, data] = [].concat(answer);
      return { ok: status < 300, status, json: async () => data };
    },
  });
  await settle();
  const submit = async () => {
    await page.form.listeners.submit({ preventDefault() {} });
  };
  return { ...page, sent, store, replaced, submit };
}

const settle = () => new Promise((resolve) => setTimeout(resolve, 0));

const ADA = {
  id: 1,
  name: "Ada",
  body: "<img src=x onerror=alert(1)>",
  created: "2026-11-16T20:00:00.000Z",
  author: 0,
};
const ROBBIE = {
  id: 2,
  name: "Robbie",
  body: "thanks",
  created: "2026-11-17T01:00:00.000Z",
  author: 1,
};

test("does nothing on a page without a comments section", async () => {
  const { sent } = await load({ section: false });
  assert.deepEqual(sent, []);
});

test("lists comments as text, oldest first, and unhides the section", async () => {
  const { section, list } = await load({ existing: [ADA, ROBBIE] });
  assert.equal(section.hidden, false);
  assert.equal(section.scrolled, false);
  assert.deepEqual(
    list.children.map((item) => item.find("comment-body").textContent),
    ["<img src=x onerror=alert(1)>", "thanks"],
  );
  const [ada, robbie] = list.children.map((item) => item.find("comment-meta"));
  assert.equal(ada.find("comment-name").textContent, "Ada");
  assert.equal(ada.find("comment-date").dateTime, ADA.created);
  assert.match(ada.find("comment-date").textContent, /^Nov 1[67], 2026$/); // the reader's time zone
  assert.equal(ada.find("comment-author"), undefined);
  assert.equal(robbie.find("comment-author").textContent, "author");
  assert.equal(ada.find("comment-delete"), undefined, "no delete button without Robbie's key");
});

test("a link to #comments scrolls there once the section is shown", async () => {
  assert.equal((await load({ hash: "#comments" })).section.scrolled, true);
});

test("posting appends the comment, clears the box, and remembers the name", async () => {
  const made = { ...ADA, id: 3, body: "hello" };
  const page = await load({ existing: [ADA], responses: { "POST /api/comment": [201, made] } });
  page.name.value = "Ada";
  page.body.value = "hello";
  await page.submit();
  assert.deepEqual(page.sent, [
    { url: "/api/comment", body: { path: PATH, name: "Ada", body: "hello" } },
  ]);
  assert.deepEqual(
    page.list.children.map((item) => item.find("comment-body").textContent),
    [ADA.body, "hello"],
  );
  assert.equal(page.body.value, "");
  assert.equal(page.store.get("comment-name"), "Ada");
  assert.equal(page.note.textContent, "");
  assert.equal(page.button.disabled, false);

  assert.equal((await load({ stored: { "comment-name": "Ada" } })).name.value, "Ada");
});

test("a refused or failed post keeps what was typed and says so", async () => {
  const reserved = await load({ responses: { "POST /api/comment": 403 } });
  reserved.name.value = "Robbie";
  reserved.body.value = "it's me";
  await reserved.submit();
  assert.equal(reserved.note.textContent, "That name is reserved. Pick another.");
  assert.equal(reserved.body.value, "it's me");
  assert.equal(reserved.list.children.length, 0);
  assert.equal(reserved.store.has("comment-name"), false);

  const offline = await load();
  offline.body.value = "hello";
  await offline.submit();
  assert.equal(offline.note.textContent, "That didn't post. Try again in a moment.");
  assert.equal(offline.body.value, "hello");
  assert.equal(offline.button.disabled, false);
});

test("Robbie's key is taken from the URL once, then sent with his comments", async () => {
  const page = await load({
    hash: "#author-key=s3cret",
    responses: { "POST /api/comment": [201, ROBBIE] },
  });
  assert.equal(page.store.get("author-key"), "s3cret");
  assert.deepEqual(page.replaced, [PATH], "the key is taken off the URL");
  assert.equal(page.name.value, "Robbie");
  page.body.value = "thanks";
  await page.submit();
  assert.equal(page.sent[0].body.key, "s3cret");
});

test("with Robbie's key each comment has a delete button that removes it", async () => {
  const page = await load({
    existing: [ADA, ROBBIE],
    stored: { "author-key": "s3cret" },
    responses: { "POST /api/comment/delete": 204 },
  });
  const del = page.list.children[0].find("comment-meta").find("comment-delete");
  await del.listeners.click();
  assert.deepEqual(page.sent, [{ url: "/api/comment/delete", body: { id: 1, key: "s3cret" } }]);
  assert.deepEqual(
    page.list.children.map((item) => item.find("comment-body").textContent),
    ["thanks"],
  );

  // A delete the server refuses leaves the comment on the page.
  const refused = await load({ existing: [ADA], stored: { "author-key": "old" } });
  await refused.list.children[0].find("comment-meta").find("comment-delete").listeners.click();
  assert.equal(refused.list.children.length, 1);
});
