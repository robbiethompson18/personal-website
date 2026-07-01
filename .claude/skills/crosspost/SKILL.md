---
name: crosspost
description:
  Cross-post one of Robbie's blog posts to Substack (the default target — NOT LessWrong unless he
  explicitly asks). Covers the Substack import, cleaning up the artifacts it leaves (heading "#"s,
  KaTeX→Unicode math, broken chart images), and publishing web-only. Never email subscribers. Use
  when Robbie says "crosspost <post>", "put <post> on Substack", or similar.
---

# Cross-posting a blog post

**Default target: Substack only** (publication "Bobstack" / robbiethompson.substack.com). Do **not**
crosspost to LessWrong unless Robbie explicitly asks — LW is an appendix at the bottom.

**Never email subscribers.** Substack's "Send to everyone" emails the list; always publish web-only
(Continue → Publish), never Send. The import itself does not email (it publishes backdated to the
web archive silently), which is fine.

You can't enter Robbie's passwords — he must already be logged in. Check with `tabs_context_mcp` + a
screenshot before assuming.

## Prereqs (usually already true)

- **The post must be live** on `https://robbiewmthompson.com/blog/<slug>/` — the importer fetches
  from the live site / RSS feed, not local files.
- **Light charts exist and are deployed.** Charts are dark on-site; cross-post surfaces are white.
  Generate light variants (`cd posts/<slug> && CHART_THEME=light python3 charts/<script>.py` →
  `charts/light/*.png`), copy into `blog/<slug>/charts/light/`, and ship so they're live (HTTP 200).
- **`build.js` emits absolute light chart URLs in the feed** (`feedHtml()`), so the importer now
  pulls the light charts automatically. If charts still import broken, use the image fix below.

## The flow (Substack)

1. **Import.** Substack → Settings → Import → **Import posts** → paste the single post URL
   (`https://robbiewmthompson.com/blog/<slug>/`) → Get started → tick "Yes, this is my publication"
   (a ToS/ownership checkbox — Robbie must approve this) → **Import**. It parses the RSS feed and
   creates a **published, backdated, web-only** post — **no email**. It may also pull 1 extra recent
   post; delete that stray draft.
2. **Unpublish to draft** while you clean: post "…" menu → **Unpublish** → confirm. Keeps the messy
   interim off the public archive. (Still no email either way.)
3. **Clean up the import artifacts** — see next section.
4. **No subtitle** — Robbie doesn't like them. Leave the "Add a subtitle…" field empty, and clear it
   if the import brought one in.
5. **Publish web-only** — Continue → Publish. Never "Send to everyone".

## Cleaning up import artifacts

Substack's editor is **TipTap**. Reach it from the page console (javascript_tool):
`const ed = document.querySelector('[contenteditable=true]').editor;` Edits via
`ed.view.dispatch(tr)` go through TipTap's normal pipeline, so Substack **autosaves** them — but
always **reload and re-verify**, because the browser tab group can reset mid-session.

### Broken chart images ("IMAGE NOT FOUND")

Failed images become `assetError` nodes whose `url` is the original (relative) path. Replace each
with a real `image2` node pointing at the **live light URL**; Substack re-hosts it to its own S3 on
save. The `assetError`s are in document order, matching the charts top-to-bottom.

```js
const ed = document.querySelector("[contenteditable=true]").editor,
  schema = ed.schema;
const base = "https://robbiewmthompson.com/blog/<slug>/charts/light/";
let guard = 0;
while (guard++ < 40) {
  const st = ed.state;
  let t = null;
  st.doc.descendants((n, pos) => {
    if (!t && n.type.name === "assetError")
      t = { pos, size: n.nodeSize, file: (n.attrs.url || "").split("/").pop() };
  });
  if (!t) break;
  const img = schema.nodes.image2.create({ src: base + t.file, alt: "" });
  const cap = schema.nodes.caption ? schema.nodes.caption.create() : null;
  const node = schema.nodes.captionedImage.create({}, cap ? [img, cap] : [img]);
  ed.view.dispatch(ed.state.tr.replaceWith(t.pos, t.pos + t.size, node));
}
```

Note: the browser `file_upload` tool refuses local files, so you **cannot** upload PNGs from disk —
this hotlink-then-Substack-rehosts trick is the way.

### Heading "#" artifacts

The site adds a hover anchor `<a href="#slug">#</a>` to every heading; it imports as a trailing "
#". Remove all of them (only matches text that is exactly `#` with a `#`-anchor link, so citations
and footnotes are untouched):

```js
const ed = document.querySelector("[contenteditable=true]").editor;
const st = ed.state,
  doc = st.doc,
  ranges = [];
doc.descendants((n, pos) => {
  if (
    n.isText &&
    n.text === "#" &&
    n.marks.some((m) => m.type.name === "link" && (m.attrs.href || "").startsWith("#"))
  ) {
    let from = pos,
      to = pos + n.nodeSize;
    if (doc.textBetween(Math.max(0, from - 1), from) === " ") from -= 1;
    ranges.push([from, to]);
  }
});
ranges.sort((a, b) => b[0] - a[0]);
let tr = st.tr;
for (const [f, t] of ranges) tr = tr.delete(f, t);
ed.view.dispatch(tr);
```

### Math (KaTeX → Unicode)

Substack has no inline KaTeX. Imported `$…$` flattens to raw LaTeX plus duplicated glyphs, e.g.
`CO2e\text{CO}_2\text{e}CO2​e` (with a zero-width space `​`). **First inspect the exact broken
strings**, then swap each blob for Unicode. Post-specific — build the map from what you find:

```js
// 1) inspect
ed.state.doc.descendants((n, pos) => {
  if (n.isText && /\\text|\\frac|\\times|\\approx|\^\{|\\%/.test(n.text || ""))
    console.log(pos, n.text);
});
// 2) fix: per text node, strip ​, .split(mangled).join(unicode), then
//    ed.view.dispatch(tr.replaceWith(pos, pos+node.nodeSize, ed.schema.text(newText, node.marks)));
```

Typical replacements: `CO₂e`, `CO₂`, `0.2 ft²`, `0.2/1590 × 100 ≈ 1/80`, `0.95¹⁰⁰ = 0.6%`. Where the
surrounding whitespace is a weird KaTeX space, anchor the regex on the neighbouring prose words
instead of the blob. After fixing, re-scan for the same LaTeX pattern → expect 0.

### Footnotes → native Substack footnotes

The import turns markdown footnotes into plain `[N]` links (`href="#fnN"`) plus an hr + "Notes"
heading + ordered list with `↩︎` backrefs. Substack has native footnote nodes — `footnoteAnchor`
(inline, `{number}`) and `footnote` (block, `{number}`, content `block+`) — so convert. This script
replaces each ref with a `footnoteAnchor`, rebuilds each list item as a `footnote` block appended at
doc end (Substack's native placement), strips the backrefs, and deletes the imported Notes section.
All edits use original-doc positions applied bottom-up in one transaction:

```js
const ed = document.querySelector("[contenteditable=true]").editor,
  schema = ed.schema;
const st = ed.state,
  doc = st.doc;
let hrStart = null,
  listEnd = null,
  listNode = null;
{
  const blocks = [];
  doc.forEach((n, offset) => blocks.push({ n, offset }));
  for (let i = 0; i < blocks.length; i++) {
    const b = blocks[i];
    if (b.n.type.name === "heading" && b.n.textContent.trim() === "Notes") {
      const prev = blocks[i - 1],
        next = blocks[i + 1];
      if (next && next.n.type.name === "orderedList") {
        hrStart = prev && prev.n.type.name === "horizontalRule" ? prev.offset : b.offset;
        listNode = next.n;
        listEnd = next.offset + next.n.nodeSize;
      }
    }
  }
}
const isBackref = (ch) =>
  ch.isText &&
  ch.marks.some((m) => m.type.name === "link" && (m.attrs.href || "").startsWith("#fnref"));
function cleanBlock(b) {
  if (b.isTextblock) {
    const inline = [];
    b.forEach((ch) => {
      if (!isBackref(ch)) inline.push(ch);
    });
    while (inline.length) {
      const last = inline[inline.length - 1];
      if (last.isText && /^\s+$/.test(last.text)) {
        inline.pop();
        continue;
      }
      if (last.isText && /\s+$/.test(last.text))
        inline[inline.length - 1] = schema.text(last.text.replace(/\s+$/, ""), last.marks);
      break;
    }
    return b.type.create(b.attrs, inline, b.marks);
  }
  const kids = [];
  b.forEach((ch) => kids.push(cleanBlock(ch)));
  return b.type.create(b.attrs, kids, b.marks);
}
const footnotes = [];
listNode.forEach((li) => {
  const blocks = [];
  li.forEach((ch) => blocks.push(cleanBlock(ch)));
  footnotes.push(schema.nodes.footnote.create({ number: footnotes.length + 1 }, blocks));
});
const refs = [];
doc.descendants((n, pos) => {
  if (!n.isText) return;
  const link = n.marks.find((m) => m.type.name === "link");
  if (link && /^#fn\d+$/.test(link.attrs.href || ""))
    refs.push({ pos, size: n.nodeSize, num: +link.attrs.href.slice(3) });
});
let tr = st.tr;
tr = tr.insert(doc.content.size, footnotes);
tr = tr.delete(hrStart, listEnd);
refs.sort((a, b) => b.pos - a.pos);
for (const r of refs)
  tr = tr.replaceWith(r.pos, r.pos + r.size, schema.nodes.footnoteAnchor.create({ number: r.num }));
ed.view.dispatch(tr);
```

Then verify: count `footnoteAnchor` == count `footnote` == the post's footnote count, 0 remaining
`#fn` links, no "Notes" heading. (A footnote cited twice on-site produces two anchors with the same
`number` — untested in Substack's renderer; check the preview if a post ever does that.)

### Citations / Sources — drop the section, keep the links

Don't include the Sources section on Substack. Delete it (the hr, the "Sources" heading, the intro
paragraph, and the ordered list — everything up to the first `footnote` block) and replace with an
hr plus a pointer paragraph: `Full source list on robbiewmthompson.com/blog/<slug>/#sources` (the
URL, anchor included, is the visible link text; href
`https://robbiewmthompson.com/blog/<slug>/#sources`).

Keep the in-body citation links, but make sure they're absolute. Recent feed builds emit absolute
`https://robbiewmthompson.com/blog/<slug>/#src-…` hrefs already; older imports have relative
`#src-…` links, which are dead on Substack. Repoint every relative one (they appear in body text AND
inside footnote blocks) by re-adding the link mark with the absolute href:

```js
const ed = document.querySelector("[contenteditable=true]").editor,
  schema = ed.schema;
const BASE = "https://robbiewmthompson.com/blog/<slug>/";
const cites = [];
ed.state.doc.descendants((n, pos) => {
  if (!n.isText) return;
  const link = n.marks.find((m) => m.type.name === "link");
  if (link && /^#src-/.test(link.attrs.href || ""))
    cites.push({ pos, size: n.nodeSize, href: link.attrs.href });
});
let tr = ed.state.tr;
for (const c of cites.sort((a, b) => b.pos - a.pos))
  tr = tr.addMark(c.pos, c.pos + c.size, schema.marks.link.create({ href: BASE + c.href }));
ed.view.dispatch(tr);
```

(The LW exporter still strips citations to plain text entirely — that asymmetry is intentional.)

## Verify before publishing

Reload the editor and confirm: 0 `assetError` nodes, 0 heading `#` links, 0 raw-LaTeX text nodes, 0
`#fn` links (footnotes converted to native nodes, no "Notes" heading), no "Sources" heading and 0
relative `#src-` links (section replaced by the pointer paragraph), all chart `<img>`s have
`naturalWidth > 0`, subtitle present. Then Continue → Publish (web-only).

## Appendix — LessWrong (ONLY if Robbie asks)

- **Export:** `npm run export -- <slug>` → `export/<slug>.lesswrong.md`. Strips citations to plain
  text, drops the Sources defs, flattens chart-src captions to italics, points images at the live
  `charts/light/` URLs, keeps footnotes and `$…$` math (LW renders MathJax). Prepend the subtitle as
  an italic first line (LW has no subtitle field).
- **Editor:** enable account setting **"Use Markdown editor"** (Account → Preferences → Save), then
  create a **new** post — editor type is fixed at creation, so pre-existing drafts stay rich-text.
- **Persistence:** LW's autosave does **not** catch programmatic edits. Persist via GraphQL (flat
  args, not wrapped in `input`):
  ```js
  await fetch("/graphql", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    credentials: "include",
    body: JSON.stringify({
      query: `mutation u($sel:SelectorInput!,$data:UpdatePostDataInput!){updatePost(selector:$sel,data:$data){data{_id draft}}}`,
      variables: {
        sel: { documentId: "<postId>" },
        data: {
          url: "<original blog url>",
          contents: { originalContents: { type: "markdown", data: "<full markdown>" } },
        },
      },
    }),
  }).then((r) => r.json());
  ```
  Read the textarea value straight from the DOM (`document.querySelector('textarea').value`) to
  avoid shuttling 15 KB through a tool call. Set `url` to make it a **linkpost** to the original
  (defuses LW's demand for sources, since citations are stripped). **Publish** with
  `data:{draft:false}` (`postedAt` is server-controlled — don't send it).
