# Submitting a post to Inkhaven (IH)

Robbie is a resident at Inkhaven #3 (fall 2026), a daily-writing residency. Each day he submits one
post from this blog to the Inkhaven portal. "Submit to IH" means this.

**One post per day, never two.** The portal shows a "Submit another piece" box after the day's
submission. Never use it. Before submitting, check that today has no submission yet; if it does,
stop and tell Robbie.

## Before submitting

- The post is published: `draft: false`, `date:` today, built and pushed to `main`, and the URL
  returns 200 (`curl -s -o /dev/null -w "%{http_code}" <url>`). The portal fetches the page for the
  title and word count.
- Today has no submission. In the portal, the "Daily Post Publication" box shows a green "Published"
  badge once the day's piece is in. Clicking Robbie's name in "Inkhaven Participants" lists his
  posts with dates.
- The deadline is midnight (Pacific). The box shows a countdown.

## Submitting

1. Use Robbie's personal ("purple") Chrome profile, which is signed into the portal. See
   `~/.claude/docs/chrome-profiles.md`.
2. Open https://www.inkhaven.blog/portal (`/dashboard` is a 404).
3. Paste the post URL into "Paste the link to today's piece". It has to be a real paste: put the URL
   on the clipboard with `pbcopy` and press cmd+v in the field. Typing it (or `form_input`) doesn't
   fire the paste handler, so the title never loads and Submit fails with "URL and title are
   required."
4. After the paste, the portal shows a preview card, a prefilled **Title**, an optional "Time spent
   writing (HH:mm)", a content preview with word count, and an AI-detection check ("AI analysis ran
   and did not flag this post"). Leave the time blank unless Robbie gave one.
5. Click **Submit**. Success: the badge reads "Published" and the post appears at the top of
   Robbie's list with today's date.

First done 2026-11-27 (Movie Review: You Can See Everything).
