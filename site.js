// Site-wide constants, plus the one URL policy shared by every surface that
// hotlinks a post's assets from the live site (feed.xml via build.js, the
// LessWrong exporter via export.js).

import { existsSync } from "node:fs";
import { join } from "node:path";

export const SITE = {
  title: "Robbie Thompson",
  url: "https://robbiewmthompson.com",
  description: "Essays by Robbie Thompson.",
};

// Absolute live URL for a post-relative asset like "charts/foo.png". Charts
// prefer the light-theme variant ("charts/light/foo.png") when it exists:
// feed, email, and cross-post surfaces are light backgrounds, unlike the dark
// on-site pages. See charts/theme.py (CHART_THEME=light).
export function liveAssetUrl(slug, rel) {
  const light = rel.replace(/^charts\//, "charts/light/");
  if (light !== rel && existsSync(join("posts", slug, light))) rel = light;
  return `${SITE.url}/blog/${slug}/${rel}`;
}
