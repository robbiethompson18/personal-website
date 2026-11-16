# worker/

The site's Cloudflare Worker (`personal-website`, config in `/wrangler.jsonc`). Static files are
served straight from the asset store without running it; only paths in `assets.run_worker_first`
reach `index.js`. Everything in this folder is kept out of the public upload by `/.assetsignore`.

- `/*.mp4` → `serveWithRanges` in `index.js`: answers Range requests with 206, which the asset store
  doesn't do and iOS Safari needs to play a video.
- `/api/*` → `api.js`: first-party analytics, written to the D1 database `personal-website` (binding
  `DB`).

## Analytics

`/hit.js` (repo root, loaded by every page) is the only caller. It sends only when
`location.hostname` is `robbiewmthompson.com`, so local dev never counts. No cookies, and counts are
private to Robbie: never display them on the site.

- `POST /api/hit` with `{"path": "/dateme/", "referrer": "t.co"}` counts a page view. `referrer` is
  the hostname of `document.referrer`, `""` for none.
- `POST /api/like` with `{"path": "/blog/<slug>/"}` records a like. A post has two like buttons, a
  bare heart beside the title and a labelled one centred at the end of the text above Notes and
  Sources (`likeButton` and `withLikeRow` in `build.js`, `.like` in `blog.css`). Clicking either
  fills both. Like only, no unlike; the browser remembers it in localStorage under `liked:<path>`.

Both answer 204. Rejections: 403 for a request that isn't same-origin (`Origin`, `Sec-Fetch-Site`)
or has a bot User-Agent, 413 for a body over 512 bytes, 400 for bad JSON, a referrer that isn't a
hostname, or a `path` the asset store doesn't serve as a 200 HTML page, 405 for a method other than
POST, 404 for any other `/api/` path. A page path must look like `/`, `/a/`, `/a/b/` (letters,
digits, `-`, `_`), so a slug with a dot in it would go uncounted.

## Schema

`migrations/0001_analytics.sql`. Days are UTC `YYYY-MM-DD`.

- `views (day, path, referrer, count)`: referrer is a hostname without `www.`, `''` for none,
  `internal` for the site itself.
- `visitors (day, path, visitor)`: one row per visitor per page per day, so unique visitors is
  `COUNT(*)`.
- `likes (day, path, visitor)`: the key caps likes at one per visitor per page per day.
- `salts (day, salt)`: `visitor` is the first 16 bytes of SHA-256 over that day's random salt + IP +
  User-Agent. The first request of a UTC day creates the salt and deletes older ones, so a hash
  can't be recomputed later or matched across days. Raw IPs and user agents are never stored.

## Commands

Run from the repo root. `wrangler` is a global install (not in `package.json`) and needs
`CLOUDFLARE_API_TOKEN` for anything remote.

- `npm test`: `hit.test.js` runs `/hit.js` against fake browser globals; `worker.test.js` boots
  `wrangler dev` on a spare port with a throwaway local D1 and checks counting, validation and the
  video 206. It uses real pages (`/dateme/`, `/blog/a-touch-feral/` and its video), so run
  `npm run build` first.
- `npm run stats`: views and visitors per page for the last 7 and 30 days, top referrers overall and
  for `/dateme/`, likes per post, read from the remote D1 (`stats.js`).
- New migration: add `migrations/000N_name.sql`, then
  `wrangler d1 migrations apply personal-website --remote` before deploying code that needs it.
- Deploy: pushing to `main` deploys the committed files (see `/docs/cloudflare-hosting.md`). By
  hand: `npm run build && wrangler deploy`, which uploads the working tree as it is, uncommitted
  changes included.
- Ad-hoc query:
  `wrangler d1 execute personal-website --remote --command="SELECT * FROM views ORDER BY day DESC LIMIT 20"`.
