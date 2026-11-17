// `npm run stats`: print the site's numbers from the live D1. Days are UTC. "visitors"
// sums each day's unique visitors, so one person on two days counts twice: the daily salt
// makes them unlinkable.

import { execFileSync } from "node:child_process";

const RECENT = "day > date('now', '-30 days')";
const WEEK = "day > date('now', '-7 days')";
const referrers = (where) => `
  SELECT CASE referrer WHEN '' THEN '(none)' ELSE referrer END AS referrer, SUM(count) AS views
  FROM views WHERE ${where} GROUP BY referrer ORDER BY views DESC LIMIT 20`;

const QUERIES = {
  "Views and visitors per page, last 7 and 30 days": `
    SELECT v.path, views_7d, visitors_7d, views_30d, visitors_30d
    FROM (SELECT path, SUM(count) AS views_30d, COALESCE(SUM(count) FILTER (WHERE ${WEEK}), 0) AS views_7d
          FROM views WHERE ${RECENT} GROUP BY path) v
    JOIN (SELECT path, COUNT(*) AS visitors_30d, COUNT(*) FILTER (WHERE ${WEEK}) AS visitors_7d
          FROM visitors WHERE ${RECENT} GROUP BY path) u USING (path)
    ORDER BY views_30d DESC`,
  "Top referrers, all pages, last 30 days": referrers(RECENT),
  "Top referrers, /dateme/, last 30 days": referrers(`${RECENT} AND path = '/dateme/'`),
  "Likes per post, all time": `
    SELECT path, COUNT(*) AS likes, MAX(day) AS latest FROM likes GROUP BY path ORDER BY latest DESC, likes DESC`,
  "Newest comments": `
    SELECT id, path, name, substr(replace(body, char(10), ' '), 1, 80) AS body, created
    FROM comments ORDER BY id DESC LIMIT 20`,
};

const sql = Object.values(QUERIES).join(";");
const out = execFileSync(
  "wrangler",
  ["d1", "execute", "personal-website", "--remote", "--json", `--command=${sql}`],
  {
    encoding: "utf8",
  },
);
const results = JSON.parse(out);
Object.keys(QUERIES).forEach((title, i) => {
  const rows = results[i].results;
  console.log(`\n${title}`);
  if (rows.length) console.table(rows);
  else console.log("  (nothing yet)");
});
