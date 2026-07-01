// Render every post's Altair chart scripts to PNG/SVG.
//
// The markdown build (build.js) only *copies* existing chart images into blog/;
// it never runs Python. This is that missing Python step:
//
//   node render-charts.js            render every chart once (npm run charts)
//   node render-charts.js --watch    re-render a chart when its .py changes
//                                    (wired into npm run dev)
//
// Each script's theme.save() writes to charts/<name>.{svg,png} *relative to the
// current dir*, so we spawn python with cwd = the post folder (not charts/).
// Writing the fresh PNG into posts/<slug>/charts/ then trips build.js's own
// posts/ watcher, which copies it into blog/<slug>/charts/ for serving. There's
// no live-reload, so we log "done → refresh" to say when it's safe to reload.

import { readdirSync, existsSync, watch } from "node:fs";
import { join } from "node:path";
import { spawn } from "node:child_process";

const POSTS = "posts";

// theme.py is an imported library (the shared dark theme), not a runnable chart
// — running it produces no output. Everything else in charts/ is a chart script.
const isChart = (f) => f.endsWith(".py") && f !== "theme.py";

// [slug, file] for every chart script under posts/*/charts/.
function allCharts() {
  const out = [];
  for (const e of readdirSync(POSTS, { withFileTypes: true })) {
    if (!e.isDirectory()) continue;
    const dir = join(POSTS, e.name, "charts");
    if (!existsSync(dir)) continue;
    for (const f of readdirSync(dir)) if (isChart(f)) out.push([e.name, f]);
  }
  return out;
}

// Spawn `python3 charts/<file>` from posts/<slug>/, logging start + done so you
// know when the fresh image has landed and it's safe to refresh the browser.
function render(slug, file) {
  return new Promise((resolve) => {
    process.stdout.write(`⟳ ${slug}/${file} …`);
    const t = Date.now();
    const p = spawn("python3", [join("charts", file)], {
      cwd: join(POSTS, slug),
      stdio: ["ignore", "ignore", "inherit"], // let Python errors through to stderr
    });
    p.on("close", (code) => {
      console.log(code === 0 ? ` done in ${Date.now() - t}ms → refresh` : ` FAILED (exit ${code})`);
      resolve(code);
    });
  });
}

// One-shot: render sequentially (vl-convert is memory-heavy; keeps logs readable).
async function renderAll() {
  const charts = allCharts();
  for (const [slug, file] of charts) await render(slug, file);
  console.log(`rendered ${charts.length} chart script(s)`);
}

// Watch mode: re-render a chart when its .py is saved. A change to theme.py
// re-renders every chart in that post, since they all import the shared theme.
function watchCharts() {
  console.log("watching posts/*/charts/*.py …");
  const timers = new Map();
  watch(POSTS, { recursive: true }, (_event, rel) => {
    if (!rel) return;
    const parts = rel.split(/[/\\]/); // e.g. plastic-straws/charts/table_bars.py
    if (parts.length !== 3 || parts[1] !== "charts" || !parts[2].endsWith(".py")) return;
    const [slug, , file] = parts;
    const targets =
      file === "theme.py"
        ? readdirSync(join(POSTS, slug, "charts"))
            .filter(isChart)
            .map((f) => [slug, f])
        : [[slug, file]];
    for (const [s, f] of targets) {
      const key = `${s}/${f}`;
      clearTimeout(timers.get(key));
      // Debounce: a single save fires several write events.
      timers.set(key, setTimeout(() => render(s, f), 150));
    }
  });
}

if (process.argv.includes("--watch")) watchCharts();
else renderAll();
