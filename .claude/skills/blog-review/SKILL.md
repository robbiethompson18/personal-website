---
name: blog-review
description:
  Read-only editorial pass over one of Robbie's blog posts — typos, em dashes, hedges, "I
  think/believe", chart rules, uncited numbers, awkward phrasing, superfluous sections, missing
  KaTeX. Reports only, never edits. Use on /blog-review or "review this post".
---

# Blog review

**Read-only.** Report findings; never edit any file (except for the two exceptions mentioned).
Robbie fixes his own prose.

**Which post:** review `posts/<slug>/FINAL_POST.md` for the named slug/path. If none given, list
`posts/` and ask.

Read the whole post first. Then output the nine checks below, each as a `##` section, in order.
Quote every finding with a `line:` ref. Zero findings → "None found" (no padding). No summary
verdict.

## Can Fix Yourself

1. **Typos** — real misspellings, doubled words, wrong homophones, broken markdown/links. Obvious
   only; never flag style or US/UK spelling.
2. **Casing** - Title Case on graphs and headings.

## Report Only, No Fixing

1. **Filler Words** pretty (eg "pretty small") and actually (eg "actually good")
2. **Em dashes** — list every `—` with its line. Count + locations only, no verdict.
3. **Hedges** — seems, roughly, probably, maybe, might, I suspect, fairly, somewhat, basically, etc.
   Don't flag approximate numbers (eg "about 1 ton").
4. **"I think" / "I believe"** — and kin (I feel, I'd argue). Enumerate.
5. **Charts** — check each embedded `charts/*.png` against the **graph** skill (invoke it / read
   `.claude/skills/graph/SKILL.md`): dark theme via `save()`, `fonts(width)` not hardcoded sizes,
   short Title-Case titles, informative-only subtitles, HUE/CAT colors, ~1 sig fig. Confirm each
   PNG + its script exist. Per-chart pass/fail.
6. **Uncited numbers** — every stat/count/$ lacking a nearby link, footnote, or stated source. A
   number framed as Robbie's own estimate counts as cited.
7. **Awkward phrasing** — quote the sentence, name why in a few words. Don't rewrite.
8. **Superfluous sections** — paragraphs/sections cuttable without losing the argument; one line
   why.
9. **Missing KaTeX** — math/formulae/units written as plain text that should be `$…$` (or `$$…$$`).
