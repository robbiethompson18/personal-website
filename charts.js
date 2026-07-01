// Renders <figure class="chart" data-spec="..."> blocks with Observable Plot.
// build.js turns a ```chart fenced block into that figure and only loads this
// module on pages that have one. Data lives in the post; this is pure display.
//
// Observable Plot is vendored at /vendor/plot.umd.min.js (loaded before this
// module by build.js) and exposes the global `Plot`. Self-hosted so a post has
// zero external dependencies.
const Plot = window.Plot;

// Pull colors from blog.css so charts match the theme (light on dark).
const css = getComputedStyle(document.documentElement);
const theme = {
  bg: css.getPropertyValue("--bg").trim() || "#0b0b0b",
  text: css.getPropertyValue("--text").trim() || "#e8e8e8",
  accent: css.getPropertyValue("--link").trim() || "#8ab4f8",
};

// Horizontal dot plot: one dot per item, value on a (usually log) x-axis, items
// sorted largest-at-top. Reads an "item | value" table straight across.
function dotplot(spec, width) {
  const data = [...spec.data].sort((a, b) => b.value - a.value);
  return Plot.plot({
    width,
    height: 34 + data.length * 40,
    marginLeft: spec.marginLeft ?? 184,
    marginRight: 28,
    style: { background: theme.bg, color: theme.text, fontSize: "15px" },
    x: {
      type: spec.scale === "log" ? "log" : "linear",
      grid: true,
      label: spec.axisLabel ?? null,
      // Plain decimals ("0.001", "1,000") instead of SI ("1m", "1k") — SI's
      // milli/mega collision is a readability trap on these charts.
      tickFormat: (d) => d.toLocaleString("en-US", { maximumSignificantDigits: 4 }),
    },
    y: { label: null, domain: data.map((d) => d.item) },
    marks: [
      Plot.dot(data, {
        x: "value",
        y: "item",
        r: 7,
        fill: theme.accent,
        stroke: theme.accent,
        tip: true,
      }),
    ],
  });
}

const RENDERERS = { dotplot };

function render(figure) {
  let spec;
  try {
    spec = JSON.parse(figure.dataset.spec);
  } catch {
    return;
  }
  const build = RENDERERS[spec.type];
  if (!build) {
    figure.textContent = `[unknown chart type: ${spec.type}]`;
    return;
  }
  const width = figure.clientWidth || 720;
  figure.replaceChildren(build(spec, width));
  if (spec.caption) {
    const cap = document.createElement("figcaption");
    cap.textContent = spec.caption;
    figure.appendChild(cap);
  }
}

const init = () => {
  if (!window.Plot) return; // vendored Plot failed to load
  document.querySelectorAll("figure.chart[data-spec]").forEach(render);
};

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}
