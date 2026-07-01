// Cross-post exporter: posts/<slug>/FINAL_POST.md -> export/<slug>.lesswrong.md
// Run with: npm run export -- <slug>   (e.g. npm run export -- plastic-straws)
//
// LessWrong's markdown editor keeps our math ($...$) and footnotes ([^id]) as-is,
// and can hotlink images straight from the live site — so the export is nearly
// lossless. The only things that don't travel are our custom citation system
// (cite.js's [phrase](@id) / {@id}: / <span class="chart-src">), which we flatten
// to plain text, since LessWrong has no equivalent and Robbie wants sources dropped.
//
// What this does NOT touch: real markdown links ([x](https://…)), math, footnotes.

import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const SITE_URL = "https://robbiewmthompson.com";

const slug = process.argv[2];
if (!slug) {
  console.error("usage: npm run export -- <slug>");
  process.exit(1);
}

const raw = readFileSync(join("posts", slug, "FINAL_POST.md"), "utf8");

// --- split frontmatter from body -----------------------------------------
const fm = raw.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
if (!fm) throw new Error(`${slug}: no frontmatter block found`);
const meta = {};
for (const line of fm[1].split("\n")) {
  const i = line.indexOf(":");
  if (i !== -1) meta[line.slice(0, i).trim()] = line.slice(i + 1).trim();
}
let body = fm[2];

// --- strip our custom citation system ------------------------------------
// 1. Drop the `{@id}: …` source definitions. Each is one or more physical lines
//    (Prettier wraps prose) terminated by a blank line or the next definition.
body = body.replace(/^\{@[\w-]+\}:[\s\S]*?(?=\n\n|\n*$)/gm, "");

// 2. Flatten `<span class="chart-src">…</span>` captions to a plain italic line.
//    (Spans can wrap across lines.) The citation links inside are handled by step 3.
body = body.replace(/<span class="chart-src">([\s\S]*?)<\/span>/g, (_, inner) => `*${inner.replace(/\s+/g, " ").trim()}*`);

// 3. Turn citation links `[phrase](@id)` into just `phrase`. Real links whose
//    href doesn't start with `@` are left alone. Phrases never contain a `]`.
body = body.replace(/\[([^\]]+)\]\(@[\w-]+\)/g, "$1");

// --- make images hotlinkable from the live site --------------------------
// `![alt](charts/foo.png)` -> `![alt](https://robbiewmthompson.com/blog/<slug>/charts/foo.png)`
const assetBase = `${SITE_URL}/blog/${slug}`;
body = body.replace(/\]\((charts\/[^)]+)\)/g, `](${assetBase}/$1)`);

// --- drop editor-only HTML comments (@claude/@robbie notes, section markers) --
body = body.replace(/<!--[\s\S]*?-->/g, "");

// Collapse the runs of blank lines the deletions leave behind.
body = body.replace(/\n{3,}/g, "\n\n").trim() + "\n";

mkdirSync("export", { recursive: true });
const outPath = join("export", `${slug}.lesswrong.md`);
writeFileSync(outPath, body);

console.log(`Wrote ${outPath}`);
console.log(`\nPaste the body into LessWrong's *Markdown* editor (Account → Settings → Markdown).`);
console.log(`Fill the LessWrong form fields separately:`);
console.log(`  Title:    ${meta.title ?? "(none)"}`);
if (meta.subtitle) console.log(`  Subtitle: ${meta.subtitle}`);
console.log(`\nImages hotlink from ${assetBase}/charts/ — they'll still be dark until you re-render light.`);
