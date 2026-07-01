# CLAUDE.md

## Linting

Run `./lint.sh` after editing HTML **or a post's Markdown** — Prettier reflows markdown prose + lists to 100 cols, so **don't hand-wrap markdown** (write long lines; lint rewraps them). Skips `POST_DRAFT.md` / `POST_RESEARCH.md`.

Agents underuse `CODE_SMELL.md`; when you notice or leave debt, add a dated note there instead of relying on memory.

## Blog

Robbie writes all the blog posts. Help him with coding,
but never with writing or research, unless he asks explicitly.
If he does ask you to research and fill in numbers, do so, 
but **do not** assume this gives you license to fix his typos or edit his prose.
And do not *hedge* so damn hard whenever you fill in a number.
Robbie will often be editing at the same time as you: try to edit a
file max five times before returning control to Robbie and asking him to stop editing.

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

Charts are Altair (Python) → static dark PNG + SVG at build time. **All the how-to — the pipeline,
the shared dark theme, agreed sizes (bars 200 / scatters 560), font-scaling rule, and title/subtitle
conventions — lives in the `/graph` skill (`.claude/skills/graph/SKILL.md`).** Read it before
authoring or editing a chart.