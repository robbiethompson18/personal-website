---
name: blog-review
description:
  Editorial pass over one of Robbie's blog posts — typos, em dashes, hedges, "I think/believe",
  chart rules, uncited numbers, awkward phrasing, superfluous sections, missing KaTeX. Fixes typos,
  casing and footnote placement itself; leaves everything else as inline `<!-- @claude … -->`
  comments in the post, never editing the prose. Use on /blog-review or "review this post".
---

# Blog review

**Two kinds of finding.** Edit the post for the mechanical ones under "Should fix yourself" (typos,
casing, `@claudereview` comments, footnote placement) and list what you changed. Everything under
"Report Only, No Fixing" becomes an inline comment in the post (below): Robbie fixes his own prose,
and he reads the comments in VS Code, where HTML comments show up highlighted next to the text.

**Which post:** review `posts/<slug>/FINAL_POST.md` for the named slug/path. If none given, list
`posts/` and ask.

Read the whole post first, then run the checks below.

## Inline comments

Put each report-only finding in an HTML comment glued to the end of the text it's about, with no
space before `<!--`:

```
I also suspect<!-- @claude hedge --> that dry air causes dry airways.
It’s no coincidence these illnesses peak in the winter.<!-- @claude uncited, and it carries the argument -->
```

- **Format:** `<!-- @claude <check>: <note> -->`, one finding per comment. When the check's name
  says it all, write just that (`hedge`, `filler`, `em dash`, `I think`). Keep notes to a line;
  never write a rewrite of Robbie's sentence.
- **Anchor:** after the word or phrase for small findings, after the sentence for sentence-level
  ones. A superfluous paragraph or section gets one comment after its last sentence or its heading.
  A chart gets one after its `![](charts/…)` line: pass, or which graph-skill rules it fails.
- **Where not to put one:** inside link text, inline code, KaTeX, fenced blocks (` ```prompt `,
  ` ```claude `: they'd render literally) or a table (a `|` breaks the row). Put it after the link
  or span; for a fence or table, on its own line after it.
- **Threads:** Robbie replies inside the same comment: `<!-- @claude … | @robbie keep it -->`. On a
  re-review, answer a reply by appending `| @claude …`, don't duplicate a comment that's already
  there, and don't re-raise one he dismissed. Never delete comments; Robbie removes them as he
  fixes.
- **Writing them:** re-read the file right before writing and insert every comment in one write,
  since Robbie may be editing live. Run `./lint.sh` after. Prettier never wraps inside an inline
  comment, so a long one lands on its own line and the prose rewraps around it. That's expected. A
  few seconds later, check the comments are still in the file and re-insert them if his save
  clobbered them.

**Reply in chat** with: the "Should fix yourself" changes, a count of inline comments per check, and
only the findings that can't be anchored to text (e.g. a missing chart script). Don't re-list the
inline comments. No summary verdict.

## Should fix yourself

1. **Typos** — real misspellings, doubled words, wrong homophones, broken markdown/links. Obvious
   only; never flag style or US/UK spelling.
2. **Casing** - Title Case on the post title, headings and graphs (rule in `CLAUDE.md`, "Title
   Case").
3. Any @claudereview comment: those are specifically left for the reviewer to handle.
4. A footnote before closing punctuation, eg (BAD:) `...end of sentence[^EPGY].` instead of (GOOD:)
   `..end of sentence.[^EPGY]`

## Report Only, No Fixing

1. **Filler Words** pretty (eg "pretty small"), just ("just doesn't count"), actually (eg "actually
   good"), really ("doesn't really matter")
2. **Em dashes** — comment every `—` (`em dash`). No verdict.
3. **Hedges** — seems, roughly, probably, maybe, might, I suspect, fairly, somewhat, basically, etc.
   Don't flag approximate numbers (eg "about 1 ton").
4. **"I think" / "I believe"** — and kin (I feel, I'd argue). Enumerate.
5. **Charts** — check each embedded `charts/*.png` against the **graph** skill (invoke it / read
   `.claude/skills/graph/SKILL.md`): dark theme via `save()`, `fonts(width)` not hardcoded sizes,
   short Title-Case titles, informative-only subtitles, HUE/CAT colors, ~1 sig fig. Confirm each
   PNG + its script exist. Per-chart pass/fail.
6. **Uncited numbers** — every stat/count/$ lacking a nearby link, footnote, or stated source. A
   number framed as Robbie's own estimate counts as cited.
7. **Awkward phrasing** — comment after the sentence, name why in a few words. Don't rewrite.
8. **Superfluous sections** — paragraphs/sections cuttable without losing the argument; one line
   why.
9. **Missing KaTeX** — math/formulae/units written as plain text that should be `$…$` (or `$$…$$`).
