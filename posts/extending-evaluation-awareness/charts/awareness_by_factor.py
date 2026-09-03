"""Eval awareness on safety tasks with one factor made artificial, per model. One image, two
panels side by side (CoT-judged | self-reported) sharing the model column.

x = baseline then F1..F8 (one factor flipped at a time, no stacking; codes only, the post defines
them just above the chart), y = model. Cell = matched-type awareness rate under that factor (no %
sign; the panels are in %); the superscript is the change vs that model's baseline in percentage
points (red = more aware, green = less). Each panel has its own color scale: CoT-judged rates top
out around 10%, self-reported around 100%.

Data: charts/awareness_rates.csv from extract_awareness.py. Writes awareness-by-factor.

Run from the post dir:  python3 charts/awareness_by_factor.py
"""

import csv
from collections import defaultdict

import altair as alt

from theme import BG, DOWN, HUE, MUTED, UP, fonts, save

MODELS = [  # display order, grouped by provider
    ("claude-sonnet-4.5", "Claude Sonnet 4.5"),
    ("claude-haiku-4.5", "Claude Haiku 4.5"),
    ("gpt-5", "GPT-5"),
    ("gpt-5.1", "GPT-5.1"),
    ("gpt-5.2", "GPT-5.2"),
    ("gpt-5.4", "GPT-5.4"),
    ("gpt-5.6-sol", "GPT-5.6"),
    ("gemini-3.1-pro", "Gemini 3.1 Pro"),
    ("gemini-3.5-flash", "Gemini 3.5 Flash"),
    ("qwen3.8-2.4t", "Qwen3.8"),
    ("deepseek-v4-pro", "DeepSeek V4 Pro"),
    ("kimi-k3", "Kimi K3"),
    ("glm-5.3", "GLM-5.3"),
    ("minimax-m3", "MiniMax M3"),
]
# Column codes only: the post defines F1..F8 in the list right above the chart.
COLS = [("baseline", "Base")] + [(f"F{i}", f"F{i}") for i in range(1, 9)]
PANELS = [("cot", "Verbalized"), ("selfreport", "Self-Reported")]

CELL = 40
ROW_H = CELL * 0.72
LABEL_COL = 130  # room for the model names on the left panel
SPACING = 12
WIDTH = 2 * CELL * len(COLS) + LABEL_COL + SPACING  # total image width, for font scaling
POOLED = "Pooled"
ROWS = MODELS + [(POOLED, POOLED)]

counts = defaultdict(dict)  # probe -> (model, config) -> [matched, graded], safety tasks only
with open("charts/awareness_rates.csv") as f:
    for row in csv.DictReader(f):
        if row["valence"] == "safety" and int(row["graded"]) >= 20:
            counts[row["probe"]][(row["model"], row["config"])] = [
                int(row["matched"]), int(row["graded"])
            ]


def panel(probe, title, f, show_models):
    rates = {k: m / g for k, (m, g) in counts[probe].items()}
    # Pooled row: every model's samples together, so it weights models by graded n.
    for cfg, _ in COLS:
        m = sum(counts[probe][(k, cfg)][0] for k, _ in MODELS if (k, cfg) in counts[probe])
        g = sum(counts[probe][(k, cfg)][1] for k, _ in MODELS if (k, cfg) in counts[probe])
        if g:
            rates[(POOLED, cfg)] = m / g
    data = []
    for key, name in ROWS:
        bl = rates.get((key, "baseline"))
        for cfg, col in COLS:
            r = rates.get((key, cfg))
            delta = None
            if cfg != "baseline" and r is not None and bl is not None:
                delta = round((r - bl) * 100)
            data.append({
                "model": name, "col": col, "rate": r,
                "txt": "–" if r is None else f"{r * 100:.0f}",
                "nodata": r is None,
                "annot": "" if not delta else f"{delta:+d}",
                "up": bool(delta and delta > 0),
            })
    vmax = max(rates.values())
    base = alt.Chart(alt.Data(values=data)).encode(
        x=alt.X("col:N", sort=[c[1] for c in COLS], title=None,
                axis=alt.Axis(labelAngle=0, labelPadding=6, orient="bottom",
                              labelFontSize=f["axis_label"] * 0.8)),  # "Base" must fit a cell
        y=alt.Y("model:N", sort=[m[1] for m in ROWS], title=None,
                axis=alt.Axis(labelLimit=320) if show_models else None),
    )
    # Dashed rule after the baseline column (as in the paper's figure); solid rule above Pooled.
    rule = alt.Chart(alt.Data(values=[{}]))
    divider = (
        rule.mark_rule(strokeDash=[4, 4], color=MUTED, strokeWidth=1.5).encode(x=alt.value(CELL))
        + rule.mark_rule(color=MUTED, strokeWidth=1.5).encode(y=alt.value(ROW_H * len(MODELS)))
    )
    cells = base.transform_filter("datum.nodata == false").mark_rect(
        stroke=BG, strokeWidth=1.5).encode(
        color=alt.Color("rate:Q",
                        scale=alt.Scale(domain=[0, vmax], range=[BG, HUE["water"]], clamp=True),
                        legend=None))
    blanks = base.transform_filter("datum.nodata == true").mark_rect(
        fill=MUTED, stroke=BG, strokeWidth=1.5)
    # Value sits a touch below center so the top-right superscript has its own band. The cells
    # are narrow (two panels share the column), so the in-cell text runs below the theme size.
    labels = base.mark_text(fontSize=f["label"] * 0.7, fontWeight="bold",
                            dy=ROW_H * 0.12).encode(
        text="txt:N",
        color=alt.condition("datum.nodata", alt.value(MUTED), alt.value("#f2f3f5")))
    annots = base.transform_filter("datum.annot != ''").mark_text(
        fontSize=f["label"] * 0.5, fontWeight="bold", align="right", baseline="top",
        dx=CELL * 0.46, dy=-ROW_H * 0.48).encode(
        text="annot:N",
        color=alt.condition("datum.up", alt.value(UP), alt.value(DOWN)))
    return (cells + blanks + labels + annots + divider).properties(
        width=CELL * len(COLS), height=ROW_H * len(ROWS),
        title=alt.TitleParams(text=title, anchor="middle", fontSize=f["subtitle"] * 1.1,
                              fontWeight="bold"))


f = fonts(WIDTH)
chart = alt.hconcat(
    *[panel(probe, title, f, show_models=i == 0) for i, (probe, title) in enumerate(PANELS)],
    spacing=SPACING,
).resolve_scale(color="independent").properties(
    title=alt.TitleParams(
        text="Eval Awareness by Factor, Verbalized vs Self-Reported",
        subtitle="Superscript: change vs that model's baseline, pp (red up, green down)."))
save(chart, "awareness-by-factor", WIDTH)
