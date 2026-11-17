# Cloudflare hosting

Since Nov 15, 2026 the site is served by a Cloudflare Worker named `personal-website`, not GitHub
Pages. The domain's DNS is a Cloudflare zone too (the registrar is still Hostinger; only its
nameservers point at Cloudflare). Everything is on the free plan.

## How a request is served

- `wrangler.jsonc` makes the repo root the asset directory. `.assetsignore` keeps dotfiles,
  `node_modules`, `export`, `worker` and `wrangler.jsonc` out of the upload. Everything else that is
  committed is public, as it was on GitHub Pages.
- Static files are answered by Cloudflare's asset store without running any code. Those requests are
  free and unmetered.
- Only the paths in `assets.run_worker_first` (`/*.mp4`, `/api/*`) run `worker/index.js`. See
  `worker/CLAUDE.md` for what they do. These count against the free plan's 100,000 Worker requests a
  day.
- `robbiewmthompson.com` is attached to the Worker as a custom domain (the `routes` entry in
  `wrangler.jsonc`). Cloudflare owns that DNS record and the certificate.
- `www.robbiewmthompson.com` never reaches the Worker. A zone redirect rule ("www to apex", under
  Rules → Redirect Rules) answers it with a 301 to the apex, keeping path and query. Its DNS record
  is a proxied `AAAA 100::` placeholder: a proxied record has to exist for the rule to run, and the
  address is never contacted.
- "Always Use HTTPS" is on for the zone, so `http://` redirects to `https://`.
- The `workers.dev` address is off (wrangler disables it when `routes` is set and `workers_dev`
  isn't).

## Deploying

Pushing to `main` deploys. The Worker is connected to the GitHub repo through Workers Builds (Worker
→ Settings → Builds), via Cloudflare's GitHub App installed on this one repo. The build runs no
build command, only `npx wrangler deploy`, so **it uploads the committed files as they are**. Run
`npm run build` and commit the output before pushing, as before. Preview builds for other branches
are off.

A failed build leaves the previous version live. Check builds in the dashboard under Worker →
Deployments, or `wrangler deployments list`.

To deploy by hand: `npm run build && wrangler deploy` (uploads the working tree, uncommitted changes
included). `wrangler` is a global install and needs `CLOUDFLARE_API_TOKEN`.

Database migrations are not part of a deploy. Apply them first:
`wrangler d1 migrations apply personal-website --remote`.

## Email

The Worker emails Robbie about each new comment (`worker/CLAUDE.md`). Three things outside the repo
make that work, all on the free plan:

- **The domain is onboarded for Email Sending** (dashboard: Compute → Email Service → Email Sending;
  it was done on Nov 16, 2026 with
  `POST /zones/<zone>/email/sending/subdomains {"name": "robbiewmthompson.com"}`). That created six
  DNS records: three MX and an SPF TXT on `cf-bounce.robbiewmthompson.com` (bounce handling), a DKIM
  TXT on `cf-bounce._domainkey`, and `_dmarc` with `p=reject`. Removing the domain there deletes
  them.
- **The recipient is a verified destination address** on the account (Email Service → Email Routing
  → Destination addresses). The free plan can only send to verified addresses, which is all this
  needs; sending to anyone else needs Workers Paid.
- **`wrangler.jsonc` has the `send_email` binding `EMAIL`** and the recipient in
  `vars.NOTIFY_EMAIL`.

The domain receives no mail: there are no MX records on the apex and Email Routing is off.
`_dmarc p=reject` tells receivers to refuse mail claiming to be from the domain that Cloudflare
didn't sign, so sending as `@robbiewmthompson.com` from any other provider needs that record changed
first.

## Gotchas

- **Range requests.** The asset store ignores `Range` and answers 200 with the whole file. iOS
  Safari won't play a `<video>` without a 206, which is why `.mp4` goes through the Worker. Any
  other file type that needs ranges (audio, large downloads) needs adding to `run_worker_first`.
- **Attaching a custom domain** fails with error 100117 while other DNS records exist for that
  hostname, and the API's `override_existing_dns_record` flag didn't help. The existing records have
  to be deleted first, then the domain attached.
- **Folder URLs.** `/dateme` redirects to `/dateme/` with a 307 (GitHub Pages used 301).
- **No 404 page.** An unknown path gets an empty 404. Adding a `404.html` at the root and
  `"not_found_handling": "404-page"` under `assets` would fix that.

## GitHub Pages

Pages was still enabled when this was written, building every push and serving the same files at
GitHub's IPs. That was deliberate for the changeover: the old Hostinger nameservers kept answering
with GitHub's addresses, and resolvers may cache the old nameserver delegation for up to 48 hours.
Visitors who land there see the site but aren't counted, because `/api/hit` doesn't exist on GitHub.
Once Pages is turned off (repo Settings → Pages), delete the `CNAME` file at the root, which only
GitHub reads.
