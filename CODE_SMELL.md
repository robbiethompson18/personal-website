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
