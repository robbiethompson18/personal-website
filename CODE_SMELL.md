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

Sep 3, 2026: `npm run dev` sets DEV=true, which makes build.js emit `/blog/drafts/` instead of
`/blog/` for every post's back-link (build.js `blogHref`). Since blog/ is committed build output,
any commit taken while the dev server has rebuilt will silently repoint all ~36 published posts' "←
Blog" links at the drafts index on the live site. Caught once during a ship (36 dirty index.html,
each a one-line back-link change) and fixed by running `npm run build` before committing. Either
make ship always prod-build first, have lint.sh fail when a committed blog/*.html contains
`/blog/drafts/` in a post back-link, or stop letting DEV touch committed output.

Sep 3, 2026 (same day, fixed): it recurred twice more in one session — including on a `sync-post.js`
write, which counts as a `posts/` change and so retriggers the watcher after a prod build. Took the
third option: `DEV=1` now builds into `.dev/` (gitignored), which the build fills out with symlinks
to the root's static files so `http.server --directory .dev` still serves a whole site. A DEV build
now touches zero tracked files. `hooks/pre-commit` is the backstop, refusing any staged
`blog/**/index.html` that contains `/blog/drafts/` (the drafts index itself is exempt); enable it
per clone with `git config core.hooksPath hooks`.

Nov 13, 2026: `![alt](clip.mp4)` → `<video>` (build.js image renderer) left three rough edges. (1)
The tag has no `width`/`height`, because the build doesn't probe the file, so the page below a video
shifts when the poster or metadata loads. (2) `export.js` (LessWrong) only absolutizes `charts/…`
image paths, so a video, like any other non-chart image such as
`posts/bobs-feet-much-more-than-you-wanted-to-know/your-speed-sign.jpg`, exports as a relative path
that LessWrong can't load; the image half of that predates the video rule. (3) A video inside a
` ```claude ` fence gets no poster, because that fence renders with a fresh env and the poster
lookup needs the post's folder.

Nov 15, 2026: standalone pages (`pages/<slug>/index.md` → `/<slug>/`, added for `/dateme/`) make
build.js write generated output outside `blog/`: a tracked `dateme/` at the repo root. Four rough
edges. (1) `npm run build && git add blog feed.xml` (the habit, and what `hooks/pre-commit` prints)
misses it. (2) Nothing checks the slug, so `pages/assets/` would write an `index.html` into the real
`assets/`. (3) Deleting a page's source leaves its generated folder behind; that was already true of
posts. (4) A standalone page reuses the post template, so it gets the shared layout's
`og:type: article` and RSS `<link>`; split the template if a page ever needs to look less like a
post.

Nov 15, 2026: first-party analytics (`hit.js`, `worker/api.js`, D1) left six rough edges. (1)
Nothing rate-limits `/api/hit` and `/api/like`: the Origin and User-Agent checks stop browsers on
other sites and lazy bots, but anyone with curl can forge both, inflate counts, and burn the free
plan's 100k D1 row writes a day (a hit is about 2). Add a Cloudflare rate-limiting rule if it ever
happens. (2) `visitors` and `likes` keep one row per visitor per page per day forever. The hashes
are meaningless once their salt is deleted, but the rows pile up; roll old days up into counts if
the tables get big. (3) `calendar/index.html` loads `hit.js` as a blocking script, so the redirect
waits on one small fetch. A deferred one never ran before the redirect (0 of 5 views counted in
headless Chrome). (4) `index.html` and `calendar/index.html` are hand-written, so they load an
unversioned `/hit.js` and lean on the host's revalidation rather than `versioned()`. (5) The
hostname `robbiewmthompson.com` is hard-coded in `hit.js` as well as `site.js`. (6)
`worker/worker.test.js` shells out to a globally installed `wrangler` and depends on real content
(`/dateme/`, `/blog/a-touch-feral/` and its video); renaming those breaks the tests, not the site.

Nov 15, 2026: the move to Cloudflare (`docs/cloudflare-hosting.md`) left four loose ends. (1) GitHub
Pages is still enabled and builds every push; it was left on so resolvers with the old nameservers
cached still reach a working site. Turn it off after Nov 18, 2026 and delete the root `CNAME` file.
(2) The www redirect rule, the "Always Use HTTPS" setting and the DNS records live only in the
Cloudflare dashboard, not in the repo. (3) Deploys upload committed build output and run no build,
so a push without `npm run build` publishes stale HTML; `hooks/pre-commit` is the only backstop. (4)
There is no `404.html`, so an unknown path returns an empty 404.
