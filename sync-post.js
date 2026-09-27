// Pull a post's body from a markdown file in another repo. Manual, not part of
// the build: run it when the upstream writeup changes.
//
//   node sync-post.js <slug>
//
// The post's frontmatter carries the pointer:
//
//   ---
//   title:  Natural Deduction Takehome
//   date:   2026-09-03
//   source: ../nd-takehome/writeup.md
//   ---
//
// The header lives upstream when the source has one: each key in the source's
// frontmatter overwrites ours (title, date, draft, project, …), and we keep only
// the keys it doesn't set (source:, or the whole header if it has no frontmatter).
// A source's `written_on:` fills `date:` and its leading `# ` heading fills
// `title:`, unless it sets those keys itself. Deleting a key upstream does NOT
// delete ours — set `draft: false` to publish rather than removing `draft: true`.
//
// Everything below the frontmatter is overwritten with the source file's body.
// That's fine — git is the undo. Run `git diff` after to see what you'd lose,
// and `git checkout` the file if the blog version had drifted on purpose.

import { copyFileSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, resolve } from "node:path";

const slug = process.argv[2];
if (!slug) throw new Error("usage: node sync-post.js <slug>");

const postPath = `posts/${slug}/FINAL_POST.md`;
const raw = readFileSync(postPath, "utf8");
const m = raw.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
if (!m) throw new Error(`${postPath}: no frontmatter (create it first, with a source: line)`);

const source = m[1].match(/^source:\s*(.+)$/m)?.[1].trim();
if (!source) throw new Error(`${postPath}: frontmatter needs a source: path`);

// Flat `key: value` lines only, like build.js reads them; a YAML list (e.g. nd-rl's
// `papers:`) is skipped.
const fields = (fm) =>
  new Map([...fm.matchAll(/^([\w-]+):[ \t]*(\S.*)$/gm)].map(([, k, v]) => [k, v.trim()]));

const upstream = readFileSync(resolve(source), "utf8");
const up = upstream.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
const upFields = fields(up?.[1] ?? "");
// Move a leading `# ` title (only blank lines / HTML comments may precede it) into title:, since
// build.js renders the frontmatter title as the h1 and leaving it in would show it twice.
const body = (up?.[2] ?? upstream).replace(
  /^((?:\s*<!--[\s\S]*?-->)*\s*)# (.*)\n/,
  (_, pre, h1) => {
    if (!upFields.has("title")) upFields.set("title", h1.trim());
    return pre;
  },
);
if (upFields.has("written_on") && !upFields.has("date"))
  upFields.set("date", upFields.get("written_on"));

const header = new Map([...fields(m[1]), ...upFields]);
const frontmatter = [...header].map(([k, v]) => `${k}: ${v}`).join("\n");
writeFileSync(postPath, `---\n${frontmatter}\n---\n\n${body.replace(/^\n+/, "")}`);
const lines = (s) => s.split("\n").length;
console.log(`${postPath}: ${lines(m[2])} -> ${lines(body)} lines from ${source}`);

// Copy the images the body references by relative path (e.g. charts/foo.png) from next to the
// source into the post folder, where build.js picks them up as assets.
for (const [, rel] of body.matchAll(/!\[[^\]]*\]\(([^)\s]+)\)/g)) {
  if (/^([a-z]+:|\/)/.test(rel)) continue; // URLs and site-absolute paths
  mkdirSync(dirname(`posts/${slug}/${rel}`), { recursive: true });
  copyFileSync(resolve(dirname(source), rel), `posts/${slug}/${rel}`);
  console.log(`  copied ${rel}`);
}
