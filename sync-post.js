// Pull a post's body from a markdown file in another repo. Manual, not part of
// the build: run it when the upstream writeup changes.
//
//   node sync-post.js <slug>
//
// The post's frontmatter carries the pointer and survives the copy:
//
//   ---
//   title:  Natural Deduction Takehome
//   date:   2026-09-03
//   source: ../nd-takehome/writeup.md
//   ---
//
// Everything below the frontmatter is overwritten with the source file's body.
// That's fine — git is the undo. Run `git diff` after to see what you'd lose,
// and `git checkout` the file if the blog version had drifted on purpose.

import { readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";

const slug = process.argv[2];
if (!slug) throw new Error("usage: node sync-post.js <slug>");

const postPath = `posts/${slug}/FINAL_POST.md`;
const raw = readFileSync(postPath, "utf8");
const m = raw.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
if (!m) throw new Error(`${postPath}: no frontmatter (create it first, with a source: line)`);

const source = m[1].match(/^source:\s*(.+)$/m)?.[1].trim();
if (!source) throw new Error(`${postPath}: frontmatter needs a source: path`);

// Strip frontmatter from the source too, in case it ever grows one.
const upstream = readFileSync(resolve(source), "utf8");
const body = upstream.match(/^---\n[\s\S]*?\n---\n?([\s\S]*)$/)?.[1] ?? upstream;

writeFileSync(postPath, `---\n${m[1]}\n---\n\n${body.replace(/^\n+/, "")}`);
const lines = (s) => s.split("\n").length;
console.log(`${postPath}: ${lines(m[2])} -> ${lines(body)} lines from ${source}`);
