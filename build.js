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
import cite from "./cite.js";
import { SITE, liveAssetUrl } from "./site.js";

const md = new MarkdownIt({ html: true, linkify: true, typographer: true })
  .use(footnote)
  .use(katex.default ?? katex)
  .use(cite);

// Only autolink explicit URLs (https://...), not bare domains — otherwise
// filenames like skill.md linkify (.md is Moldova's TLD).
md.linkify.set({ fuzzyLink: false });

// Title the footnote section "Notes" (the commentary/aside stream), to sit
// alongside the "Sources" section cite.js appends. Mirrors the default
// markdown-it-footnote block markup, plus the heading.
md.renderer.rules.footnote_block_open = () =>
  '<hr class="footnotes-sep">\n<section class="footnotes">\n' +
  '<h2 class="footnotes-title" id="notes">Notes <a class="heading-anchor" href="#notes" aria-label="Link to this section">#</a></h2>\n<ol class="footnotes-list">\n';

// Give every markdown heading a stable id + a hover-visible "#" anchor, so
// sections are linkable (like Substack). The slug is derived from the heading
// text; duplicate slugs get -2, -3, … suffixes so ids stay unique per page.
function slugify(text) {
  return text
    .toLowerCase()
    .replace(/[^\w\s-]/g, "") // drop punctuation
    .trim()
    .replace(/\s+/g, "-");
}
md.core.ruler.push("heading_anchors", (state) => {
  const seen = new Map();
  const tokens = state.tokens;
  for (let i = 0; i < tokens.length; i++) {
    if (tokens[i].type !== "heading_open") continue;
    const inline = tokens[i + 1]; // heading_open, inline, heading_close
    let slug = slugify(inline.content);
    if (!slug) continue;
    const n = (seen.get(slug) ?? 0) + 1;
    seen.set(slug, n);
    if (n > 1) slug = `${slug}-${n}`;
    tokens[i].attrSet("id", slug);
    // Append a "#" link as the last child of the heading's inline content.
    const link = new state.Token("html_inline", "", 0);
    link.content = ` <a class="heading-anchor" href="#${slug}" aria-label="Link to this section">#</a>`;
    inline.children.push(link);
  }
});

// Show a reused footnote as [1] [1] instead of [1] [1:1]. Only the visible
// caption changes; the anchor IDs (fnref1 vs fnref1:1) stay unique, so each
// citation's back-link still returns to the right spot.
md.renderer.rules.footnote_caption = (tokens, idx) => `[${tokens[idx].meta.id + 1}]`;

// A reused footnote otherwise gets one bare ↩︎ per citation (↩︎ ↩︎), which are
// indistinguishable. Emit a single back-arrow that returns to the first citation.
md.renderer.rules.footnote_anchor = (tokens, idx, options, env, slf) => {
  if (tokens[idx].meta.subId > 0) return "";
  const id = slf.rules.footnote_anchor_name(tokens, idx, options, env, slf);
  return ` <a href="#fnref${id}" class="footnote-backref">↩︎</a>`;
};

// Glue every footnote marker to the word before it: strip any space in
// "land. [5]" so the superscript hugs the word directly and can never wrap to
// the next line on its own. Token-level (not a regex on source) so it only ever
// touches real footnote refs, never a "[^...]" inside code or prose.
md.core.ruler.after("inline", "footnote_nbsp", (state) => {
  for (const blk of state.tokens) {
    if (blk.type !== "inline") continue;
    const kids = blk.children;
    for (let i = 1; i < kids.length; i++) {
      if (kids[i].type !== "footnote_ref") continue;
      const prev = kids[i - 1];
      if (prev.type === "text") prev.content = prev.content.replace(/\s+$/, "");
    }
  }
});

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

function layout({ title, description, canonical, body, hasMath }) {
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
    <link rel="icon" href="/favicon.ico" sizes="any" />
    <link rel="icon" type="image/png" href="/favicon-32.png" sizes="32x32" />
    <link rel="apple-touch-icon" href="/apple-touch-icon.png" />
    <link rel="stylesheet" href="/blog.css" />${hasMath ? '\n    <link rel="stylesheet" href="/vendor/katex/katex.min.css" />' : ""}
  </head>
  <body>
${body}
    <script src="/footnotes.js" defer></script>
  </body>
</html>
`;
}

function postPage(p) {
  const draftBanner = p.draft
    ? `<p class="draft-banner">Draft — not in the index or feed</p>\n          `
    : p.archive
      ? `<p class="draft-banner">Archived — not in the index or feed</p>\n          `
      : "";
  const body = `    <main class="post">
      <article>
        <header class="post-header">
          ${draftBanner}<p class="post-meta"><a href="/blog/">&larr; Blog</a></p>
          <h1>${esc(p.meta.title)}</h1>
          ${p.meta.subtitle ? `<p class="subtitle">${esc(p.meta.subtitle)}</p>` : ""}
          <p class="post-dates"><span>Published <time datetime="${p.meta.date}">${fmtDate(p.meta.date)}</time></span><span>Last edited <time datetime="${p.updated}">${fmtDate(p.updated)}</time></span></p>
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
    hasMath: p.hasMath,
  });
}

function indexPage(posts, { heading = "Blog", subpath = "" } = {}) {
  const items = posts
    .map((p) => {
      const tags =
        (p.draft ? ' <span class="draft-tag">draft</span>' : "") +
        (p.archive ? ' <span class="draft-tag archive-tag">archive</span>' : "");
      return `        <li>
          <a class="post-link" href="/blog/${p.slug}/">${esc(p.meta.title)}${tags}</a>
          <span class="post-date"><time datetime="${p.meta.date}">${fmtDate(p.meta.date)}</time></span>
          ${p.meta.subtitle ? `<p class="post-sub">${esc(p.meta.subtitle)}</p>` : ""}
        </li>`;
    })
    .join("\n");
  const body = `    <main class="index">
      <header class="index-header">
        <h1>${esc(heading)}</h1>
        <p class="index-sub"><a href="/">robbiewmthompson.com</a></p>
      </header>
      <ul class="post-list">
${items}
      </ul>
    </main>`;
  return layout({
    title: `${heading} — ${SITE.title}`,
    description: SITE.description,
    canonical: `${SITE.url}/blog/${subpath}`,
    body,
  });
}

// The feed's <content:encoded> is consumed out of context — RSS readers, email,
// and cross-post importers (e.g. Substack) have no base URL, so a relative image
// src like "charts/foo.png" resolves to nothing, and an in-page anchor like
// href="#fn1" (footnotes, heading "#" links, backrefs) goes nowhere. Absolute-ize
// both against the post's live URL. Image URLs go through liveAssetUrl (site.js),
// which prefers the light-theme chart variant for these light-background surfaces.
function feedHtml(p) {
  return p.html
    .replace(/\bsrc="(?!https?:|\/)([^"]+)"/g, (_m, rel) => `src="${liveAssetUrl(p.slug, rel)}"`)
    .replace(/\bhref="#/g, `href="${SITE.url}/blog/${p.slug}/#`);
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
      <content:encoded><![CDATA[${feedHtml(p).replace(/\]\]>/g, "]]]]><![CDATA[>")}]]></content:encoded>
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
// Chart .py sources are published on purpose (the chart-source captions link to
// them); interpreter/editor junk like __pycache__ and dotfiles is not.
function copyAssets(srcDir, destDir) {
  for (const e of readdirSync(srcDir, { withFileTypes: true })) {
    if (e.name === "__pycache__" || e.name.startsWith(".")) continue;
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

// markdown-it renders broken footnotes and unclosed math as *literal text*
// without ever throwing, so a typo'd `[^foo]` or a stray `$` would otherwise
// sail through as a "successful" build with mangled output. These checks catch
// the common silent degradations and surface them as build warnings. (Named
// "check", not "lint", to avoid colliding with lint.sh — the Prettier formatter.)
function checkContent(body) {
  const issues = [];

  // Strip the zones where `$` and `[^...]` are legitimately literal, so we don't
  // false-alarm on code samples, editor notes, etc.
  const prose = body
    .replace(/```[\s\S]*?```/g, "") // fenced code blocks
    .replace(/`[^`]*`/g, "") // inline code spans
    .replace(/<!--[\s\S]*?-->/g, ""); // HTML comments (@claude/@robbie notes)

  // Footnotes: every `[^id]` reference needs a matching `[^id]:` definition, and
  // an unreferenced definition is silently dropped from the output entirely.
  const defs = new Set();
  const refs = new Set();
  for (const m of prose.matchAll(/^\[\^([^\]]+)\]:/gm)) defs.add(m[1]);
  for (const m of prose.matchAll(/\[\^([^\]]+)\](?!:)/g)) refs.add(m[1]);
  for (const id of refs)
    if (!defs.has(id)) issues.push(`footnote [^${id}] is referenced but never defined (renders as literal text)`);
  for (const id of defs)
    if (!refs.has(id)) issues.push(`footnote [^${id}] is defined but never referenced (silently dropped)`);

  // Source citations (cite.js): every `[phrase](@id)` reference needs a matching
  // `{@id}:` definition, and an unreferenced definition renders nothing.
  const citeDefs = new Set();
  const citeRefs = new Set();
  for (const m of prose.matchAll(/^\{@([\w-]+)\}:/gm)) citeDefs.add(m[1]);
  for (const m of prose.matchAll(/\]\(@([\w-]+)\)/g)) citeRefs.add(m[1]);
  for (const id of citeRefs)
    if (!citeDefs.has(id)) issues.push(`source (@${id}) is cited but never defined ({@${id}}: … is missing)`);
  for (const id of citeDefs)
    if (!citeRefs.has(id)) issues.push(`source {@${id}} is defined but never cited (renders nothing)`);

  // Math: with the dollar-sign delimiter, currency `$` is escaped as `\$`. Once
  // those are removed, every remaining `$` should pair up into a `$…$` / `$$…$$`
  // span — an odd count means an unclosed span or a currency `$` missing its `\`.
  const dollars = prose.replace(/\\\$/g, "").match(/\$/g)?.length ?? 0;
  if (dollars % 2 !== 0)
    issues.push(
      `odd number of unescaped '$' (${dollars}) — an unclosed $…$ math span, or a currency $ that needs escaping as \\$`,
    );

  return issues;
}

// Every post is a folder: posts/<slug>/FINAL_POST.md is the published body,
// with co-located assets (charts/, images) copied to the output. Other .md
// files in the folder (POST_DRAFT.md, POST_RESEARCH.md) are ignored by the build.
function loadPost(slug, mdPath, assetDir) {
  const { meta, body } = parse(readFileSync(mdPath, "utf8"));
  if (!meta.title || !meta.date) throw new Error(`${mdPath}: frontmatter needs title and date`);
  const html = md.render(body);
  // KaTeX always emits <span class="katex">; use that to pull in its stylesheet
  // only on pages that actually render math (same lazy-load spirit as charts).
  const hasMath = html.includes('class="katex"');
  // "Last edited" is an editorial statement, not a file-touch: it mirrors the
  // published date until you opt in with an `updated: YYYY-MM-DD` frontmatter field.
  const updated = meta.updated || meta.date;
  return {
    slug,
    meta,
    html,
    updated,
    draft: meta.draft === "true",
    archive: meta.archive === "true",
    hasMath,
    assetDir,
    issues: checkContent(body),
  };
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

// Drafts and archived posts render at their own URL but stay out of the public
// index and the feed.
const published = posts.filter((p) => !p.draft && !p.archive);
mkdirSync("blog", { recursive: true });
writeFileSync(join("blog", "index.html"), indexPage(published));
writeFileSync("feed.xml", feed(published));

// Two private-ish indexes, unlinked from anywhere and kept out of feed.xml:
//   /blog/drafts/  — every post (drafts + archive included), for eyeballing.
//   /blog/archive/ — just the archived (retired) posts.
mkdirSync(join("blog", "drafts"), { recursive: true });
writeFileSync(
  join("blog", "drafts", "index.html"),
  indexPage(posts, { heading: "Blog (incl. drafts)", subpath: "drafts/" }),
);
mkdirSync(join("blog", "archive"), { recursive: true });
writeFileSync(
  join("blog", "archive", "index.html"),
  indexPage(
    posts.filter((p) => p.archive),
    { heading: "Archive", subpath: "archive/" },
  ),
);

const excluded = posts.length - published.length;
console.log(
  `Built ${posts.length} post(s) -> blog/, feed.xml` +
    (excluded ? ` (${excluded} draft/archived excluded from index/feed)` : ""),
);

// Content warnings are non-fatal: the HTML is already written (so previews still
// work), but we flag the silent degradations and exit non-zero so `npm run build`
// in CI / a `&&` chain — and the watch terminal — visibly fail.
const warnings = posts.flatMap((p) => p.issues.map((i) => `  ⚠️  ${p.slug}: ${i}`));
if (warnings.length) {
  console.error(`\n${warnings.length} content warning(s):\n${warnings.join("\n")}`);
  process.exitCode = 1;
}
