# CLAUDE.md

## Linting

Run `./lint.sh` after editing HTML files to format them with Prettier.

Agents underuse `CODE_SMELL.md`; when you notice or leave debt, add a dated note there instead of relying on memory.

## Blog

Robbie writes all the blog posts. Help him with coding,
but never with writing or research, unless he asks explicitly.
If he does ask you to research and fill in numbers, do so, 
but **do not** assume this gives you license to fix his typos or edit his prose.
And do not *hedge* so damn hard whenever you fill in a number.
Robbie will often be editing at the same time as you: try to edit a
file max five times before returning control to Robbie and asking him to stop editing.

## Blog Charts
* always dark mode
* make text bigger (14px for titles, 12px for axes, 10px for floating labels)
* Short titles plz

## Blog structure

Static site built by `build.js` (`npm run build`). Source lives in `posts/`, generated HTML lands
in `blog/` (committed — GitHub Pages serves the repo root). The landing page is `index.html` +
`style.css`; blog pages use `blog.css` + `footnotes.js`.

**One convention, no exceptions:** every post is a folder `posts/<slug>/` containing a
`FINAL_POST.md`. The builder renders that file to `/blog/<slug>/`. Everything else in the folder is
for Robbie, not the reader:

- `POST_DRAFT.md`, `POST_RESEARCH.md` — working files, ignored by the build.
- `charts/`, images, any non-`.md` asset — copied next to the post; reference with relative paths
  like `![](charts/foo.png)`.

**Frontmatter** at the top of `FINAL_POST.md`:

```
---
title:    Post Title        # required
subtitle: optional tagline  # optional
date:     2026-06-30        # required; sorts the index, sets the RSS pubDate
draft:    true              # optional; renders at its URL but stays out of index + feed
---
```

The blog index and `feed.xml` auto-source every non-draft post, newest first. To publish a draft,
set `draft: false` and fix the date.

**Why markdown?** It's the most portable form of the writing: editable in vim, easy to work on with
Claude, clean in git diffs, and the *same* file feeds the website, the RSS feed, a LessWrong
cross-post, and an email newsletter later. Static images/diagrams go in with `![]()`; because
markdown-it runs with `html: true`, interactive JS/SVG charts can be embedded inline when a flat
image isn't enough — so markdown doesn't cap what a post can hold.

### Charts

Interactive charts use **Observable Plot**, rendered client-side by `charts.js`. Add one to any post
with a fenced ` ```chart ` block whose body is JSON — the data lives in the post, no extra files:

    ```chart
    { "type": "dotplot", "scale": "log", "axisLabel": "gallons of water →",
      "caption": "…", "data": [ { "item": "one steak", "value": 1800 }, ... ] }
    ```

- `build.js` validates the JSON at build time (a bad block **fails the build**) and turns it into a
  `<figure class="chart" data-spec="…">`; `charts.js` is pulled in only on pages that have a chart.
- Chart types live in `charts.js` (`RENDERERS`). So far: **`dotplot`** — horizontal dot plot,
  auto-sorted largest→top, `scale: "log"` or `"linear"`. Add new types there.
- Charts theme themselves from `blog.css` CSS vars, and the plain markdown table stays as the
  no-JS fallback — so keep the table.
- Observable Plot is vendored (self-hosted) at `vendor/plot.umd.min.js`, loaded before `charts.js`; no external CDN.