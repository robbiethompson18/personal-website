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

**One system: Altair (Python), rendered to static dark PNG + SVG at build time via `vl-convert`.**
No interactivity, no client JS. Vega-Lite sizes in CSS pixels, so label sizes are honest at the
~720px column — matplotlib's inches→raster→squished-to-column is why the old charts had tiny text,
so **don't use matplotlib/seaborn** for post charts.

- Chart scripts live in the post's `charts/` folder (e.g. `posts/plastic-straws/charts/*.py`). Run
  them **from the post dir** so the `charts/<name>` output paths and the `from theme import …`
  sibling import both resolve: `cd posts/plastic-straws && python3 charts/table_bars.py`.
- `charts/theme.py` holds the shared dark theme, the color palettes, `fonts(width)`, and
  `save(chart, name, width)` (writes `charts/<name>.svg` + `.png` @2x). Every chart ends with `save(...)`.
- Embed as a normal image: `![alt](charts/<name>.png)`. The build copies `charts/` to the output, so
  re-rendering needs **no `FINAL_POST.md` change**.
- **Text-size rule (important) — never hardcode font sizes.** A chart authored `width` px wide is
  scaled to fit the content column, so on-screen text = `font × column/width`: a *narrow* chart's
  text looks *bigger*. So fonts scale with width. In every chart: `f = fonts(width)`, use
  `f["label"]` for any in-chart `mark_text`, and pass the same `width` to `save()` (it sizes the
  axis/title/legend chrome). Result: every chart's text is identical on screen, matched to the
  Quotidian-water bar chart (the reference in `theme.py`).
- Deps: `altair` + `vl-convert-python` (`pip install --break-system-packages …`, same env as
  matplotlib). Keep numbers ~1 sig fig / OOM (see the post's "Probably Approximately Correct" note).