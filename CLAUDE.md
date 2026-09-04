# CLAUDE.md

## Linting

Run `./lint.sh` after editing HTML **or any Markdown** (posts, skills, `CLAUDE.md`, notes) —
Prettier reflows markdown prose + lists to 100 cols, so **don't hand-wrap markdown** (write long
lines; lint rewraps them).

Agents underuse `CODE_SMELL.md`; when you notice or leave debt, add a dated note there instead of
relying on memory.

## Blog

Robbie writes all the blog posts. Help him with coding, but never with writing or research, unless
he asks explicitly. If he does ask you to research and fill in numbers, do so, but **do not** assume
this gives you license to fix his typos or edit his prose. And do not _hedge_ so damn hard whenever
you fill in a number. Robbie will often be editing at the same time as you: try to edit a file max
five times before returning control to Robbie and asking him to stop editing.

**Cross-posting** a published post to Substack (the default; not LessWrong unless asked, and never
email subscribers) lives in the `/crosspost` skill — the import, the cleanup of its artifacts, and
web-only publishing.

## Blog structure

Static site built by `build.js` (`npm run build`). Source lives in `posts/`, generated HTML lands in
`blog/` (committed — GitHub Pages serves the repo root). The landing page is `index.html` +
`style.css`; blog pages use `blog.css` + `footnotes.js`.

**Local dev:** `npm run dev` watches `posts/` (rebuild on save) and serves `.dev/` on port 7000.
Caddy proxies it at http://robbiewmthompson.localhost/. Ctrl-C stops both. `DEV=1` builds into
`.dev/` (gitignored) rather than the committed `blog/`, because DEV rewrites every post's back-link
to `/blog/drafts/` and the watcher rebuilds all posts on any `posts/` change — see CODE_SMELL.
Run `git config core.hooksPath hooks` once per clone to enable the pre-commit backstop.

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
date:     2026-06-30        # required; sorts the index, sets the RSS pubDate
draft:    true              # optional; renders at its URL but stays out of index + feed
rating:   5                 # optional; 1-5, shown as stars next to the date on the index (default 3)
repo:     https://…         # optional; renders a GitHub link inline with the dates
source:   ../other/x.md     # optional; upstream file for `node sync-post.js <slug>` (see below)
---
```

**Posts sourced from another repo.** A post whose text lives in another repo (e.g.
`natural-deduction-takehome` ← `../nd-takehome/writeup.md`) gets a `source:` frontmatter line, and
`node sync-post.js <slug>` copies that file's body in, preserving the frontmatter. It is **not**
part of the build — run it by hand when upstream changes. It overwrites the body, so any blog-side
edits are lost; `git diff` afterwards is the safety net. Prettier adds a blank line before headings,
so the synced copy differs from upstream by whitespace only — that's stable, not churn.

**No subtitles.** The builder doesn't support them and Robbie doesn't like them — don't add a
subtitle anywhere (posts, Substack drafts).

The blog index and `feed.xml` auto-source every non-draft post, newest first. To publish a draft,
set `draft: false` and fix the date.

**Everything committed is public, and that's fine.** The repo is public and GitHub Pages serves the
repo root, so drafts, `/blog/drafts/`, `POST_DRAFT.md` / `POST_RESEARCH.md`, and chart `.py` source
are all reachable at robbiewmthompson.com (and on GitHub). This is intentional: "draft" means
unlisted (out of index + feed), not secret. Don't flag it or try to fix it.

**Why markdown?** It's the most portable form of the writing: editable in vim, easy to work on with
Claude, clean in git diffs, and the _same_ file feeds the website, the RSS feed, a LessWrong
cross-post, and an email newsletter later. Static images/diagrams go in with `![]()`; because
markdown-it runs with `html: true`, interactive JS/SVG charts can be embedded inline when a flat
image isn't enough — so markdown doesn't cap what a post can hold.

**Asides, verbatim prompts, includes** Collapsible `<details class="aside">` boxes, ` ```prompt `
fences for pasted eval prompts (never paste them bare: markdown and Prettier both mangle them), and
`<!-- include excerpts/foo.md -->` to keep long excerpts out of `FINAL_POST.md`. The mechanics and
gotchas are in the note below; read it before using any of the three.

**Sources** If you're just adding a source, use that syntax for the nice purple underline, instead
of creating a footnote. For example: `[40,000 Americans](@nhtsa)`

### Charts

Charts are Altair (Python) → static dark PNG + SVG at build time. **All the how-to — the pipeline,
the shared dark theme, agreed sizes (bars 200 / scatters 560), font-scaling rule, and title/subtitle
conventions — lives in the `/graph` skill (`.claude/skills/graph/SKILL.md`).** Read it before
authoring or editing a chart.

## Notes

- [Asides, verbatim prompts, and includes — read before adding a collapsible box, pasting an eval prompt/transcript, or splitting an excerpt out of a post](.claude/notes/asides-prompts-includes.md)
  — the blank-line rule, why bare pasted text breaks, the `prompt` fence, prettier-ignore ranges,
  the include directive, cache-busting
- [Small probe models vs the frontier roster on eval awareness — read before claiming Qwen3.8-27B / Gemma 4 31B / GPT-OSS-20B are or aren't representative](.claude/notes/eval-awareness-small-vs-frontier.md)
  — where each half's numbers live, the config-intersection and system-prompt gotchas, the
  apples-to-apples table, why the "different regime" caveat was dropped
