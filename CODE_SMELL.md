Agents: write down any times you ran into code smell, or left some code smell to preserve backwards
compatibility, or just couldn't think of a clean way to do something, or left code smell because you
wanted to keep your changes targeted.

Use Pacific time for timestamps.

May 28 12:06pm PDT: EXAMPLE ENTRY. Left an example in CODE_SMELL.md so that other agents know what
format to follow.

Jun 29, 2026: build.js has a hand-rolled frontmatter parser (split each line on first colon) instead
of pulling in a YAML dep like gray-matter. Fine for title/subtitle/date, but it can't do multi-line
values, quoted strings, or escaping. Upgrade to gray-matter if frontmatter ever needs to get fancy.

Jul 1, 2026: blog/ + feed.xml are committed build output (GitHub Pages serves the repo root), so one
prose edit dirties the source md, the post HTML, both indexes, and feed.xml — and every regenerated
chart PNG lands as a new git blob twice (posts/ + blog/), growing history monotonically. Considered
moving the build to CI (Actions → gh-pages branch); decided against for now: it adds a deploy moving
part and breaks "what's committed is what's live". Revisit if repo size or multi-agent
ship-only-my-code conflicts get painful.

Jul 27, 2026: lint.sh claims to format HTML but its `*.html` glob only reaches root-level files, so
nested standalone pages such as tutoring/index.html are skipped. Expand the Prettier inputs if more
nested HTML pages are added.

Aug 11, 2026: build.js's footnote-definition checker (`/^\[\^([^\]]+)\]:/gm`) requires the `[^id]:`
line to start at column 0, so a footnote defined under an indented list item (e.g.
`posts/bobs-diet/FINAL_POST.md`'s `[^CFF]`, nested two spaces under a bullet) gets flagged as
"referenced but never defined" even though markdown-it-footnote renders it correctly. False
positive, not a real bug — the regex just doesn't account for list-item indentation. Fix by
stripping leading whitespace before matching, or documenting that footnote defs should stay
flush-left.

Sep 3, 2026: the `/graph` skill fixes agreed heights for bar charts (200) and scatterplots (560) but
says nothing about line charts, which have neither's shape — a 15-point series at 560 is mostly
whitespace, at 200 it's a squashed ribbon. `posts/natural-deduction-takehome/charts/` picked 300 for
both of its line charts, unblessed. Add a line-chart height to the skill so the next agent doesn't
re-invent one.
