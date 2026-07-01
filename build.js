// Static blog builder: posts/*.md -> blog/<slug>/index.html + blog/index.html + feed.xml
// Run with: npm run build  (or: node build.js)
//
// Each post is a markdown file with a tiny frontmatter block:
//   ---
//   title: How to Make People Feel Smart
//   subtitle: (And thus ask more questions and learn quickly)
//   date: 2025-01-25
//   ---
//   <markdown body, with [^1] style footnotes>

import { readFileSync, writeFileSync, readdirSync, mkdirSync, copyFileSync, existsSync } from "node:fs";
import { join } from "node:path";
import MarkdownIt from "markdown-it";
import footnote from "markdown-it-footnote";
import katex from "@vscode/markdown-it-katex";

const SITE = {
  title: "Robbie Thompson",
  url: "https://robbiewmthompson.com",
  description: "Essays by Robbie Thompson.",
};

const md = new MarkdownIt({ html: true, linkify: true, typographer: true })
  .use(footnote)
  .use(katex.default ?? katex);

// Show a reused footnote as [1] [1] instead of [1] [1:1]. Only the visible
// caption changes; the anchor IDs (fnref1 vs fnref1:1) stay unique, so each
// citation's back-link still returns to the right spot.
md.renderer.rules.footnote_caption = (tokens, idx) => `[${tokens[idx].meta.id + 1}]`;

// A ```chart fenced block (JSON body) becomes a <figure> that charts.js renders
// with Observable Plot in the browser. We validate the JSON at build time, and
// flag the post so its page pulls in charts.js only when it actually has a chart.
let renderHasChart = false;
const defaultFence = md.renderer.rules.fence;
md.renderer.rules.fence = (tokens, idx, options, env, self) => {
  const token = tokens[idx];
  if (token.info.trim() === "chart") {
    let spec;
    try {
      spec = JSON.parse(token.content);
    } catch (e) {
      throw new Error(`Invalid \`\`\`chart JSON: ${e.message}`);
    }
    renderHasChart = true;
    const json = JSON.stringify(spec)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/'/g, "&#39;");
    return `<figure class="chart" data-spec='${json}'><noscript>(interactive chart — enable JavaScript)</noscript></figure>\n`;
  }
  return defaultFence(tokens, idx, options, env, self);
};

// A reused footnote otherwise gets one bare ↩︎ per citation (↩︎ ↩︎), which are
// indistinguishable. Emit a single back-arrow that returns to the first citation.
md.renderer.rules.footnote_anchor = (tokens, idx, options, env, slf) => {
  if (tokens[idx].meta.subId > 0) return "";
  const id = slf.rules.footnote_anchor_name(tokens, idx, options, env, slf);
  return ` <a href="#fnref${id}" class="footnote-backref">↩︎</a>`;
};

const MONTHS = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];

// --- helpers -------------------------------------------------------------

// Parse a YYYY-MM-DD date string into display + RFC-822 forms without relying
// on the local timezone (date-only strings would otherwise shift a day).
function fmtDate(iso) {
  const [y, m, d] = iso.split("-").map(Number);
  return `${MONTHS[m - 1]} ${d}, ${y}`;
}
function rfc822(iso) {
  // Anchor at noon UTC so the weekday/day are stable regardless of TZ.
  return new Date(`${iso}T12:00:00Z`).toUTCString();
}
function esc(s = "") {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

// Minimal frontmatter parser: a leading ---\n...\n--- block of key: value lines.
function parse(raw) {
  const m = raw.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
  if (!m) return { meta: {}, body: raw };
  const meta = {};
  for (const line of m[1].split("\n")) {
    const i = line.indexOf(":");
    if (i === -1) continue;
    meta[line.slice(0, i).trim()] = line.slice(i + 1).trim();
  }
  return { meta, body: m[2] };
}

// --- templates -----------------------------------------------------------

function layout({ title, description, canonical, body, hasChart, hasMath }) {
  return `<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>${esc(title)}</title>
    <meta name="description" content="${esc(description)}" />
    <link rel="canonical" href="${canonical}" />
    <meta property="og:title" content="${esc(title)}" />
    <meta property="og:description" content="${esc(description)}" />
    <meta property="og:type" content="article" />
    <meta property="og:url" content="${canonical}" />
    <link rel="alternate" type="application/rss+xml" title="${esc(SITE.title)}" href="/feed.xml" />
    <link rel="stylesheet" href="/blog.css" />${hasMath ? '\n    <link rel="stylesheet" href="/vendor/katex/katex.min.css" />' : ""}
  </head>
  <body>
${body}
    <script src="/footnotes.js" defer></script>${hasChart ? '\n    <script defer src="/vendor/d3.min.js"></script>\n    <script defer src="/vendor/plot.umd.min.js"></script>\n    <script type="module" src="/charts.js"></script>' : ""}
  </body>
</html>
`;
}

function postPage(p) {
  const draftBanner = p.draft
    ? `<p class="draft-banner">Draft — not in the index or feed</p>\n          `
    : "";
  const body = `    <main class="post">
      <article>
        <header class="post-header">
          ${draftBanner}<p class="post-meta"><a href="/blog/">&larr; Writing</a> &middot; <time datetime="${p.meta.date}">${fmtDate(p.meta.date)}</time></p>
          <h1>${esc(p.meta.title)}</h1>
          ${p.meta.subtitle ? `<p class="subtitle">${esc(p.meta.subtitle)}</p>` : ""}
        </header>
        ${p.html}
      </article>
      <footer class="post-footer">
        <p><a href="/blog/">&larr; More writing</a></p>
      </footer>
    </main>`;
  return layout({
    title: p.meta.title,
    description: p.meta.subtitle || SITE.description,
    canonical: `${SITE.url}/blog/${p.slug}/`,
    body,
    hasChart: p.hasChart,
    hasMath: p.hasMath,
  });
}

function indexPage(posts) {
  const items = posts
    .map(
      (p) => `        <li>
          <a class="post-link" href="/blog/${p.slug}/">${esc(p.meta.title)}</a>
          <span class="post-date"><time datetime="${p.meta.date}">${fmtDate(p.meta.date)}</time></span>
          ${p.meta.subtitle ? `<p class="post-sub">${esc(p.meta.subtitle)}</p>` : ""}
        </li>`,
    )
    .join("\n");
  const body = `    <main class="index">
      <header class="index-header">
        <h1>Writing</h1>
        <p class="index-sub"><a href="/">robbiewmthompson.com</a> &middot; <a href="/feed.xml">RSS</a></p>
      </header>
      <ul class="post-list">
${items}
      </ul>
    </main>`;
  return layout({
    title: `Writing — ${SITE.title}`,
    description: SITE.description,
    canonical: `${SITE.url}/blog/`,
    body,
  });
}

function feed(posts) {
  const items = posts
    .map(
      (p) => `    <item>
      <title>${esc(p.meta.title)}</title>
      <link>${SITE.url}/blog/${p.slug}/</link>
      <guid isPermaLink="true">${SITE.url}/blog/${p.slug}/</guid>
      <pubDate>${rfc822(p.meta.date)}</pubDate>
      <description>${esc(p.meta.subtitle || "")}</description>
      <content:encoded><![CDATA[${p.html}]]></content:encoded>
    </item>`,
    )
    .join("\n");
  return `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>${esc(SITE.title)}</title>
    <link>${SITE.url}/blog/</link>
    <atom:link href="${SITE.url}/feed.xml" rel="self" type="application/rss+xml" />
    <description>${esc(SITE.description)}</description>
    <language>en</language>
${items}
  </channel>
</rss>
`;
}

// --- build ---------------------------------------------------------------

// Recursively copy a post folder's assets (anything that isn't markdown) into
// its output dir, e.g. posts/<slug>/charts/foo.png -> blog/<slug>/charts/foo.png.
function copyAssets(srcDir, destDir) {
  for (const e of readdirSync(srcDir, { withFileTypes: true })) {
    const src = join(srcDir, e.name);
    const dest = join(destDir, e.name);
    if (e.isDirectory()) {
      mkdirSync(dest, { recursive: true });
      copyAssets(src, dest);
    } else if (!e.name.endsWith(".md")) {
      copyFileSync(src, dest);
    }
  }
}

// Every post is a folder: posts/<slug>/FINAL_POST.md is the published body,
// with co-located assets (charts/, images) copied to the output. Other .md
// files in the folder (POST_DRAFT.md, POST_RESEARCH.md) are ignored by the build.
function loadPost(slug, mdPath, assetDir) {
  const { meta, body } = parse(readFileSync(mdPath, "utf8"));
  if (!meta.title || !meta.date) throw new Error(`${mdPath}: frontmatter needs title and date`);
  renderHasChart = false;
  const html = md.render(body);
  // KaTeX always emits <span class="katex">; use that to pull in its stylesheet
  // only on pages that actually render math (same lazy-load spirit as charts).
  const hasMath = html.includes('class="katex"');
  return { slug, meta, html, draft: meta.draft === "true", hasChart: renderHasChart, hasMath, assetDir };
}

const posts = [];
for (const e of readdirSync("posts", { withFileTypes: true })) {
  if (!e.isDirectory()) continue;
  const mdPath = join("posts", e.name, "FINAL_POST.md");
  if (existsSync(mdPath)) posts.push(loadPost(e.name, mdPath, join("posts", e.name)));
}
posts.sort((a, b) => b.meta.date.localeCompare(a.meta.date));

for (const p of posts) {
  const dir = join("blog", p.slug);
  mkdirSync(dir, { recursive: true });
  writeFileSync(join(dir, "index.html"), postPage(p));
  if (p.assetDir) copyAssets(p.assetDir, dir);
}

// Drafts render at their own URL but stay out of the index and the feed.
const published = posts.filter((p) => !p.draft);
mkdirSync("blog", { recursive: true });
writeFileSync(join("blog", "index.html"), indexPage(published));
writeFileSync("feed.xml", feed(published));

const draftCount = posts.length - published.length;
console.log(
  `Built ${posts.length} post(s) -> blog/, feed.xml` +
    (draftCount ? ` (${draftCount} draft excluded from index/feed)` : ""),
);
