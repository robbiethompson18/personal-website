# worker/

The site's Cloudflare Worker (`personal-website`, config in `/wrangler.jsonc`). Static files are
served straight from the asset store without running it; only paths in `assets.run_worker_first`
reach `index.js`. Everything in this folder is kept out of the public upload by `/.assetsignore`.

- `/*.mp4` → `serveWithRanges` in `index.js`: answers Range requests with 206, which the asset store
  doesn't do and iOS Safari needs to play a video.
- `/api/*` → `api.js`: first-party analytics and post comments, written to the D1 database
  `personal-website` (binding `DB`).

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

## Comments

Every post (not standalone pages) ends with a comments section below Notes and Sources. `build.js`
renders it empty and hidden (`COMMENTS`), and `/comments.js` (repo root, loaded on posts only) fills
it and unhides it. No accounts, no moderation queue, no rate limit, no count shown: a comment is a
name plus plain text, and it is public the moment it is posted.

- `GET /api/comments?path=/blog/<slug>/` answers a JSON array of
  `{id, name, body, created, author}`, oldest first.
- `POST /api/comment` with `{"path", "name", "body"}` (and `"key"` for Robbie) answers 201 with the
  stored comment. The name is trimmed to one line and capped at 40 characters, empty becomes
  `Anonymous`. The body is capped at 5,000 characters and keeps its line breaks. The request body is
  capped at 32 KB.
- `POST /api/comment/delete` with `{"id", "key"}` answers 204. Robbie's key only.

**Plain text is the whole safety model.** The Worker stores what was typed, and `comments.js` puts
it on the page with `textContent`, never `innerHTML`. So a comment can't carry markup or a clickable
link, which is also what makes it worthless to link spammers. Keep it that way: don't add markdown,
auto-linking or `innerHTML`.

**Robbie's name and key.** A name that reads as Robbie's (`RESERVED_NAME` in `api.js`: "Robbie",
"Robbie Thompson", "Robbie W. M. Thompson", any case or punctuation) is refused with 403 unless the
request carries the Worker secret `AUTHOR_KEY`. A comment posted with the key is stored with
`author = 1` and shown with an "author" badge; the badge, not the name, is what can't be faked. A
browser gets the key by opening any post once with `#author-key=<key>` on the URL: `comments.js`
stores it in localStorage and takes it off the URL. That browser then posts as the author and sees a
delete button on every comment. To rotate the key: `wrangler secret put AUTHOR_KEY`, then open the
link with the new key on each device.

**Email.** Each new comment that isn't Robbie's emails him through the `EMAIL` binding (`notify` in
`api.js`, sent after the response so the commenter doesn't wait). It is sent from
`comments@robbiewmthompson.com` to `NOTIFY_EMAIL` in `wrangler.jsonc`. A failed send is logged with
`console.error` and the comment still posts. The account-side setup is in
`/docs/cloudflare-hosting.md`.

Rejections are the same as analytics', plus 400 for an empty or over-long comment, a missing `name`
or `body`, or a path that isn't a post, and 403 for a reserved name or a wrong key.

## Schema

`migrations/0001_analytics.sql` and `migrations/0002_comments.sql`. Days are UTC `YYYY-MM-DD`.

- `views (day, path, referrer, count)`: referrer is a hostname without `www.`, `''` for none,
  `internal` for the site itself.
- `visitors (day, path, visitor)`: one row per visitor per page per day, so unique visitors is
  `COUNT(*)`.
- `likes (day, path, visitor)`: the key caps likes at one per visitor per page per day.
- `salts (day, salt)`: `visitor` is the first 16 bytes of SHA-256 over that day's random salt + IP +
  User-Agent. The first request of a UTC day creates the salt and deletes older ones, so a hash
  can't be recomputed later or matched across days. Raw IPs and user agents are never stored.
- `comments (id, path, name, body, created, author, visitor)`: `created` is a UTC ISO 8601
  timestamp. `visitor` is the same daily hash, never sent to a browser; it is there so one spammer's
  comments from one day can be deleted together.

## Commands

Run from the repo root. `wrangler` is a global install (not in `package.json`) and needs
`CLOUDFLARE_API_TOKEN` for anything remote.

- `npm test`: `hit.test.js` and `comments.test.js` run `/hit.js` and `/comments.js` against fake
  browser globals; `worker.test.js` boots `wrangler dev` on a spare port with a throwaway local D1
  and checks counting, comments, validation and the video 206. It uses real pages (`/dateme/`,
  `/blog/a-touch-feral/` and its video, and four more posts for comments), so run `npm run build`
  first. Locally the `EMAIL` binding sends nothing: wrangler prints each email to its log, which is
  what the test reads.
- `npm run stats`: views and visitors per page for the last 7 and 30 days, top referrers overall and
  for `/dateme/`, likes per post, and the 20 newest comments, read from the remote D1 (`stats.js`).
- Delete a comment without a browser:
  `wrangler d1 execute personal-website --remote --command="DELETE FROM comments WHERE id = 12"`.
  Everything one visitor posted that day:
  `DELETE FROM comments WHERE visitor = (SELECT visitor FROM comments WHERE id = 12)`.
- New migration: add `migrations/000N_name.sql`, then
  `wrangler d1 migrations apply personal-website --remote` before deploying code that needs it.
- Deploy: pushing to `main` deploys the committed files (see `/docs/cloudflare-hosting.md`). By
  hand: `npm run build && wrangler deploy`, which uploads the working tree as it is, uncommitted
  changes included.
- Ad-hoc query:
  `wrangler d1 execute personal-website --remote --command="SELECT * FROM views ORDER BY day DESC LIMIT 20"`.
