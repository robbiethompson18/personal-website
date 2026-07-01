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
4. **Re-add the subtitle** — the import drops it (there's an "Add a subtitle…" field).
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
this hotlink-then-Substack-rehosts trick is the way. (Alternatively Robbie can drag PNGs in by
hand.)

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

### Citations / Sources — leave them

The import keeps the `[phrase](@id)` links and the "Sources" section as a complete, working sourced
version (the links jump to the section). Keep it — stripping ~40 links by hand isn't worth it, and
it reads fine. (The LW exporter strips them; Substack keeps them. This asymmetry is intentional.)

## Verify before publishing

Reload the editor and confirm: 0 `assetError` nodes, 0 heading `#` links, 0 raw-LaTeX text nodes,
all chart `<img>`s have `naturalWidth > 0`, subtitle present. Then Continue → Publish (web-only).

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
