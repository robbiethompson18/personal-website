// Moves note definitions in a post's source to where they are read. Source-only: the
// rendered page is identical, because the build collects definitions from anywhere.
//
//   [^id]: footnote  -> directly below the top-level block (paragraph, list, quote, ...)
//                       that first references it
//   {@id}: source    -> the end of the file, in order of first citation
//
// A definition nothing references stays where it is (build.js reports those). Posts with
// a `source:` frontmatter line are skipped: sync-post.js overwrites their body.
//
//   node place-notes.js            every posts/*/FINAL_POST.md and pages/*/index.md (lint.sh)
//   node place-notes.js <file...>  just those files
//   node place-notes.js --stdin    filter stdin to stdout (the save hook in ~/repos/dotfiles/.vimrc)

import { readFileSync, writeFileSync, readdirSync, existsSync } from "node:fs";
import { join } from "node:path";
import MarkdownIt from "markdown-it";
import footnote from "markdown-it-footnote";
import katex from "@vscode/markdown-it-katex";
import cite from "./cite.js";

// The same parser build.js renders with, so "which block is this reference in" and
// "where does this definition end" are answered the way the page will be.
const md = new MarkdownIt({ html: true, linkify: true, typographer: true })
  .use(footnote)
  .use(katex.default ?? katex)
  .use(cite);

const isBlank = (line) => line.trim() === "";
const footnoteRefs = (inline) =>
  inline.children.filter((c) => c.type === "footnote_ref" && c.meta.label).map((c) => c.meta.label);

function placeNotes(raw) {
  const split = raw.match(/^(---\n[\s\S]*?\n---\n)([\s\S]*)$/);
  const [front, body] = split ? [split[1], split[2]] : ["", raw];
  if (/^source:/m.test(front)) return raw;

  const lines = body.split("\n");
  const env = {};
  const tokens = md.parse(body, env);

  // The body's top-level blocks in reading order, each with the footnotes it references.
  // markdown-it-footnote has already lifted the definitions out into a tail section.
  const blocks = [];
  const sources = new Map(); // id -> [startLine, endLine)
  let i = 0;
  for (; i < tokens.length && tokens[i].type !== "footnote_block_open"; i++) {
    const t = tokens[i];
    if (t.level === 0 && t.type === "cite_definition") sources.set(t.meta.id, t.map);
    else if (t.level === 0 && t.map) blocks.push({ start: t.map[0], end: t.map[1], refs: [] });
    else if (t.type === "inline" && blocks.length) blocks.at(-1).refs.push(...footnoteRefs(t));
  }

  // That tail: each referenced definition's line range, and the footnotes it references.
  const defs = new Map(); // label -> { start, end, refs }
  let def = null;
  for (; i < tokens.length; i++) {
    const t = tokens[i];
    if (t.type === "footnote_open") def = { label: t.meta.label, start: Infinity, end: -1, refs: [] };
    else if (t.type === "footnote_close") {
      if (def.label && def.end > 0) defs.set(def.label, def);
      def = null;
    } else if (def) {
      if (t.map) [def.start, def.end] = [Math.min(def.start, t.map[0]), Math.max(def.end, t.map[1])];
      if (t.type === "inline") def.refs.push(...footnoteRefs(t));
    }
  }

  const gone = new Set(); // lines leaving their current position
  // Lift lines [start, end) out, plus the blank lines after them, and return the text.
  // `indent` strips a definition's nesting (one written under a list item) back to column 0.
  const lift = (start, end, indent = 0) => {
    for (let l = start; l < end; l++) gone.add(l);
    for (let l = end; l < lines.length && isBlank(lines[l]); l++) gone.add(l);
    const text = lines.slice(start, end).map((line) => line.replace(new RegExp(`^\\s{0,${indent}}`), ""));
    while (text.length && isBlank(text.at(-1))) text.pop();
    return text;
  };

  // A definition's ranges come from its content, which starts on the `[^id]:` line or,
  // once Prettier has wrapped it, the line after.
  const liftDef = (d) => {
    for (const start of [d.start, d.start - 1]) {
      const m = /^(\s*)\[\^([^\]\s]+)\]:/.exec(lines[start] ?? "");
      if (m && m[2] === d.label) return lift(start, d.end, m[1].length);
    }
    return null; // e.g. inside a blockquote: leave it alone
  };

  const placed = new Set();
  const place = (label, group) => {
    const d = defs.get(label);
    if (!d || placed.has(label)) return;
    placed.add(label);
    const text = liftDef(d);
    if (text) group.push(text);
    for (const ref of d.refs) place(ref, group); // a footnote's own footnotes follow it
  };
  for (const b of blocks) {
    b.group = [];
    for (const ref of b.refs) place(ref, b.group);
  }

  const after = new Map(); // line index -> definitions to write below it
  for (const b of blocks) {
    if (!b.group.length) continue;
    let anchor = b.end - 1; // the block's last line that is staying
    while (anchor > b.start && (gone.has(anchor) || isBlank(lines[anchor]))) anchor--;
    after.set(anchor, b.group);
  }

  const tail = (env.cites?.order ?? []).filter((id) => sources.has(id)).map((id) => lift(...sources.get(id)));
  if (!gone.size) return raw;

  const out = [];
  const write = (group) => {
    for (const text of group) {
      if (out.length && !isBlank(out.at(-1))) out.push("");
      out.push(...text);
    }
  };
  let justWrote = false;
  for (let l = 0; l < lines.length; l++) {
    if (gone.has(l)) continue;
    if (justWrote && !isBlank(lines[l])) out.push("");
    out.push(lines[l]);
    justWrote = after.has(l);
    if (justWrote) write(after.get(l));
  }
  while (out.length && isBlank(out.at(-1))) out.pop();
  write(tail);
  return front + out.join("\n") + "\n";
}

function allPosts() {
  const files = [];
  for (const [dir, name] of [
    ["posts", "FINAL_POST.md"],
    ["pages", "index.md"],
  ])
    for (const slug of existsSync(dir) ? readdirSync(dir) : [])
      if (existsSync(join(dir, slug, name))) files.push(join(dir, slug, name));
  return files;
}

const args = process.argv.slice(2);
if (args[0] === "--stdin") {
  const raw = readFileSync(0, "utf8");
  let out = raw;
  try {
    out = placeNotes(raw);
  } catch {
    // A save must never eat the buffer: on any failure, hand the text back untouched.
  }
  process.stdout.write(out);
} else {
  for (const file of args.length ? args : allPosts()) {
    const raw = readFileSync(file, "utf8");
    const out = placeNotes(raw);
    if (out === raw) continue;
    writeFileSync(file, out);
    console.log(`place-notes: ${file}`);
  }
}
