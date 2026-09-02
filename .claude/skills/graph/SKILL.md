---
name: graph
description:
  How to author charts for Robbie's blog posts — the Altair pipeline, the shared dark theme, agreed
  sizes, and the title/subtitle rules. Use whenever creating or editing a chart in a post's
  `charts/` folder, or when Robbie asks for a graph/chart/figure.
---

# Blog graphs

**One system: Altair (Python) → static dark PNG + SVG at build time via `vl-convert`.** No
interactivity, no client JS. Vega-Lite sizes in CSS pixels, so text sizes are honest at the ~720px
column — **never use matplotlib/seaborn** (inches→raster→squished-to-column is why the old charts
had tiny text).

## The five rules we agreed on

1. **Dark background, always.** Don't set colors by hand — end every chart with
   `save(chart, name, width)` (in `charts/theme.py`), which applies the dark theme (`BG #1a1d24`,
   `FG #ccd0d8`) and writes `<name>.svg` + `<name>.png` @2x.

2. **Consistent sizes = consistent on-screen text.** A chart authored `width` px wide is scaled to
   fit the content column, so on-screen text = `font × column/width` — a _narrower_ chart's text
   looks _bigger_. So **never hardcode font sizes.** In every chart do `f = fonts(width)`, use
   `f["label"]` for any in-chart `mark_text`, and pass the **same `width`** to `save()` (it sizes
   the axis/title/legend chrome). Result: every chart's text is identical on screen, matched to the
   reference (`_REF_WIDTH` in `theme.py`).

3. **Agreed heights** (the `height=` on `.properties(...)`):
   - **Bar / column charts → `height=200`.** Values are short; a taller plot is just wasted
     whitespace above the tallest bar. `table_bars.py`'s `bars()` defaults to this — don't add
     per-chart overrides.
   - **Scatterplots → `height=560`.** They need vertical range, and keeping them all at one height
     means adjacent scatters (e.g. the dollars-vs-carbon / water / land trio) line up on screen.
     Pair with `autosize=alt.AutoSizeParams(type="fit", contains="padding")` so the total image is a
     fixed size and the chrome shrinks the plot to fit — that's what makes multiple scatters render
     at identical on-screen heights.

4. **Short titles, Title Case** — and Title-Case axis titles too ("Price per Pound", not "price per
   pound"). "US Freshwater Withdrawals by Sector", not a sentence.

5. **No subtitle by default.** The default is _none_ — agents reach for a subtitle on nearly every
   chart and Robbie finds it infuriating. Only add one when it carries real information a reader
   needs and the prose doesn't already say: a source (`USGS Circular 1441, ~2015`), a unit caveat,
   or a "what this omits" note. Never filler that restates the title, and never a two-line methods
   paragraph — that belongs in the post.

## Consistent colors

The theme also owns the palettes, so charts share a language:

- `HUE` — one color per metric for bars: `carbon` (red), `water` (blue), `recycle` (green), `dollar`
  (purple).
- `CAT` — one color per category for scatters: `food`, `energy`, `goods`, `digital`, `travel`.

Reuse these; don't invent new colors per chart. If a chart needs its own categorical palette, keep
the hues well-separated (no two greens / two golds — they're indistinguishable in the legend).

## Mechanics

- **Scripts** live in the post's `charts/` folder (e.g. `posts/plastic-straws/charts/*.py`). Run
  them **from the post dir** so the `charts/<name>` output paths and the `from theme import …`
  sibling import both resolve:
  ```
  cd posts/plastic-straws && python3 charts/table_bars.py
  ```
- **`theme.py`** exports what you need: `HUE`, `CAT`, `FG`, `fonts(width)`, `fmt(v)` (compact number
  labels), and `save(chart, name, width)`. Every chart ends in `save(...)`.
- **Embed** as a normal image: `![alt](charts/<name>.png)`. The build copies `charts/` to the
  output, so re-rendering needs **no `FINAL_POST.md` change**. When you re-render, also copy the
  changed `.png`/`.svg` into the built `blog/<slug>/charts/` so the committed site matches (or run
  `npm run build`).
- **Deps:** `altair` + `vl-convert-python` (`pip install --break-system-packages …`, same env as
  matplotlib).
- **Numbers:** keep to ~1 sig fig / order of magnitude (see the post's "Probably Approximately
  Correct" note).
