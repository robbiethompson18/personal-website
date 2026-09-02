"""Eval awareness on safety tasks with one factor made artificial, per model. Two charts, one per probe.

x = F1..F8 (one factor flipped at a time, no stacking), y = model. Cell = matched-type awareness
rate under that factor; the superscript is the change vs that model's baseline in percentage
points (red = more aware, green = less). The baseline rate is shown next to the model name.

Data: charts/awareness_rates.csv from extract_awareness.py. Writes awareness-by-factor-cot and
awareness-by-factor-selfreport.

Run from the post dir:  python3 charts/awareness_by_factor.py
"""

import csv
from collections import defaultdict

import altair as alt

from theme import BG, MUTED, fonts, save

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
COLS = [
    ("baseline", "Baseline"),
    ("F1", "F1 fake entities"),
    ("F2", "F2 incoherent"),
    ("F3", "F3 formal"),
    ("F4", "F4 bare request"),
    ("F5", "F5 stakes named"),
    ("F6", "F6 jailbreak wrapper"),
    ("F7", "F7 template"),
    ("F8", "F8 eval disclosed"),
]
TITLE = {"cot": "CoT-Judged", "selfreport": "Self-Reported"}
SUBTITLE = {
    "cot": "GPT-5.6 judge reads the model's reasoning; safety tasks, % of graded samples.",
    "selfreport": "Model shown its own transcript and asked; safety tasks, % of graded samples.",
}
UP, DOWN = "#e0524f", "#3fbf7f"

CELL = 50
POOLED = "Pooled"
counts = defaultdict(dict)  # probe -> (model, config) -> [matched, graded], safety tasks only
with open("charts/awareness_rates.csv") as f:
    for row in csv.DictReader(f):
        if row["valence"] == "safety" and int(row["graded"]) >= 20:
            counts[row["probe"]][(row["model"], row["config"])] = [
                int(row["matched"]), int(row["graded"])
            ]

for probe in ("cot", "selfreport"):
    width = CELL * len(COLS) + 40
    f = fonts(width)
    row_h = CELL * 0.72
    rates = {k: m / g for k, (m, g) in counts[probe].items()}
    # Pooled row: every model's samples together, so it weights models by graded n.
    for cfg, _ in COLS:
        m = sum(counts[probe][(k, cfg)][0] for k, _ in MODELS if (k, cfg) in counts[probe])
        g = sum(counts[probe][(k, cfg)][1] for k, _ in MODELS if (k, cfg) in counts[probe])
        if g:
            rates[(POOLED, cfg)] = m / g
    rows = MODELS + [(POOLED, POOLED)]
    data = []
    for key, name in rows:
        bl = rates.get((key, "baseline"))
        for cfg, col in COLS:
            r = rates.get((key, cfg))
            delta = None
            if cfg != "baseline" and r is not None and bl is not None:
                delta = round((r - bl) * 100)
            data.append({
                "model": name, "col": col, "rate": r,
                "txt": "–" if r is None else f"{r * 100:.0f}%",
                "nodata": r is None,
                "annot": "" if not delta else f"{delta:+d}",
                "up": bool(delta and delta > 0),
            })
    vmax = max(rates.values())
    base = alt.Chart(alt.Data(values=data)).encode(
        x=alt.X("col:N", sort=[c[1] for c in COLS], title="Baseline, Then One Factor Made Artificial",
                axis=alt.Axis(labelAngle=-40, labelLimit=320, orient="bottom")),
        y=alt.Y("model:N", sort=[m[1] for m in rows], title=None,
                axis=alt.Axis(labelLimit=320)),
    )
    # Dashed rule after the baseline column (as in the paper's figure); solid rule above Pooled.
    rule = alt.Chart(alt.Data(values=[{}]))
    divider = (
        rule.mark_rule(strokeDash=[4, 4], color=MUTED, strokeWidth=1.5).encode(x=alt.value(CELL))
        + rule.mark_rule(color=MUTED, strokeWidth=1.5).encode(y=alt.value(row_h * len(MODELS)))
    )
    cells = base.transform_filter("datum.nodata == false").mark_rect(
        stroke=BG, strokeWidth=1.5).encode(
        color=alt.Color("rate:Q",
                        scale=alt.Scale(domain=[0, vmax], range=[BG, "#2e7dc1"], clamp=True),
                        legend=None))
    blanks = base.transform_filter("datum.nodata == true").mark_rect(
        fill=MUTED, stroke=BG, strokeWidth=1.5)
    # Value sits a touch below center so the top-right superscript has its own band.
    labels = base.mark_text(fontSize=f["label"], fontWeight="bold",
                            dy=row_h * 0.1).encode(
        text="txt:N",
        color=alt.condition("datum.nodata", alt.value(MUTED), alt.value("#f2f3f5")))
    annots = base.transform_filter("datum.annot != ''").mark_text(
        fontSize=f["label"] * 0.75, fontWeight="bold", align="right", baseline="top",
        dx=CELL * 0.45, dy=-row_h * 0.46).encode(
        text="annot:N",
        color=alt.condition("datum.up", alt.value(UP), alt.value(DOWN)))
    chart = (cells + blanks + labels + annots + divider).properties(
        width=CELL * len(COLS), height=row_h * len(rows),
        title=alt.TitleParams(
            text=f"Eval Awareness by Factor, {TITLE[probe]}",
            subtitle=[SUBTITLE[probe],
                      "Superscript: change vs that model's baseline, pp (red up, green down)"]))
    save(chart, f"awareness-by-factor-{probe}", width)
