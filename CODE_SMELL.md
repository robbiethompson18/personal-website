Agents: write down any times you ran into code smell, or left some code smell to preserve backwards
compatibility, or just couldn't think of a clean way to do something, or left code smell because you
wanted to keep your changes targeted.

Use Pacific time for timestamps.

May 28 12:06pm PDT: EXAMPLE ENTRY. Left an example in CODE_SMELL.md so that other agents know what
format to follow.

Jun 29, 2026: build.js has a hand-rolled frontmatter parser (split each line on first colon) instead
of pulling in a YAML dep like gray-matter. Fine for title/subtitle/date, but it can't do multi-line
values, quoted strings, or escaping. Upgrade to gray-matter if frontmatter ever needs to get fancy.
