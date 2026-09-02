"""Self-reported eval awareness on safety tasks across the harness-feature cells, per model.

Same layout as awareness_by_factor.py: x = bare harness, then one harness feature switched on at a time,
then all four; y = model, pooled row last. Cell = awareness rate; the superscript is the change vs
that model's bare-harness cell in percentage points (red = more aware, green = less).

Data: charts/harness_rates.csv from extract_harness.py. Writes harness-heatmap.

Run from the post dir:  python3 charts/harness_heatmap.py
"""

import csv
from collections import defaultdict

import altair as alt

from theme import BG, DOWN, HUE, MUTED, UP, fonts, save

MODELS = [
    ("claude-sonnet-4.5", "Claude Sonnet 4.5"),
    ("gemini-3.1-pro", "Gemini 3.1 Pro"),
    ("gemini-3.5-flash", "Gemini 3.5 Flash"),
    ("qwen3.8-2.4t", "Qwen3.8"),
    ("deepseek-v4-pro", "DeepSeek V4 Pro"),
    ("kimi-k3", "Kimi K3"),
    ("glm-5.3", "GLM-5.3"),
    ("minimax-m3", "MiniMax M3"),
]
COLS = [
    ("bare_harness", "Bare|harness"),
    ("bare+F9", "+ T3 system|prompt"),
    ("bare+F11", "+ opener|turn"),
    ("bare+F12", "+ search|tool"),
    ("bare+F13", "+ typos"),
    ("baseline", "All four on"),
]
RAMP = HUE["water"]  # same blue as the F1-F8 charts
CELL_W, ROW_H = 120, 30  # wide, short cells keep the image landscape (~1.6:1, like the
# by-factor chart); a squarer image gets scaled up into a tall block on screen
LABEL_COL = 130  # room for the y-axis model names

counts = defaultdict(lambda: [0, 0])
with open("charts/harness_rates.csv") as f:
    for row in csv.DictReader(f):
        if row["probe"] == "selfreport" and row["valence"] == "safety":
            counts[(row["model"], row["cell"])] = [int(row["yes"]), int(row["graded"])]
for cell, _ in COLS:
    counts[("POOLED", cell)] = [
        sum(counts[(m, cell)][0] for m, _ in MODELS),
        sum(counts[(m, cell)][1] for m, _ in MODELS),
    ]

ROWS = MODELS + [("POOLED", "Pooled")]
width = CELL_W * len(COLS) + LABEL_COL
f = fonts(width)
data = []
for key, name in ROWS:
    yes, n = counts[(key, "bare_harness")]
    bare = yes / n if n else None
    for cell, col in COLS:
        yes, n = counts[(key, cell)]
        r = yes / n if n else None
        delta = None
        if cell != "bare_harness" and r is not None and bare is not None:
            delta = round((r - bare) * 100)
        data.append({
            "model": name, "col": col, "rate": r,
            "txt": "–" if r is None else f"{r * 100:.0f}%",
            "nodata": r is None,
            "annot": "" if not delta else f"{delta:+d}",
            "up": bool(delta and delta > 0),
        })

base = alt.Chart(alt.Data(values=data)).encode(
    x=alt.X("col:N", sort=[c[1] for c in COLS], title="Bare Harness, Then One Feature Switched On",
            axis=alt.Axis(labelAngle=0, labelPadding=6, orient="bottom",
                          labelExpr="split(datum.label, '|')")),  # "|" = line break
    y=alt.Y("model:N", sort=[m[1] for m in ROWS], title=None,
            axis=alt.Axis(labelLimit=320)),
)
divider = alt.Chart(alt.Data(values=[{}])).mark_rule(
    strokeDash=[4, 4], color=MUTED, strokeWidth=1.5).encode(x=alt.value(CELL_W))
pooled_rule = alt.Chart(alt.Data(values=[{}])).mark_rule(
    color=MUTED, strokeWidth=1.5).encode(y=alt.value(ROW_H * len(MODELS)))
cells = base.transform_filter("datum.nodata == false").mark_rect(
    stroke=BG, strokeWidth=1.5).encode(
    color=alt.Color("rate:Q", scale=alt.Scale(domain=[0, 1], range=[BG, RAMP]), legend=None))
blanks = base.transform_filter("datum.nodata == true").mark_rect(
    fill=MUTED, stroke=BG, strokeWidth=1.5)
labels = base.mark_text(fontSize=f["label"], fontWeight="bold", dy=ROW_H * 0.1).encode(
    text="txt:N",
    color=alt.condition("datum.nodata", alt.value(MUTED), alt.value("#f2f3f5")))
annots = base.transform_filter("datum.annot != ''").mark_text(
    fontSize=f["label"] * 0.75, fontWeight="bold", align="right", baseline="top",
    dx=CELL_W * 0.45, dy=-ROW_H * 0.46).encode(
    text="annot:N",
    color=alt.condition("datum.up", alt.value(UP), alt.value(DOWN)))
chart = (cells + blanks + labels + annots + divider + pooled_rule).properties(
    width=CELL_W * len(COLS), height=ROW_H * len(ROWS),
    title=alt.TitleParams(
        text="Eval Awareness by Harness Feature, Self-Reported",
        subtitle=["Model shown its own transcript and asked; safety tasks, % of graded samples.",
                  "Superscript: change vs that model's bare harness, pp (red up, green down)"]))
save(chart, "harness-heatmap", width)
