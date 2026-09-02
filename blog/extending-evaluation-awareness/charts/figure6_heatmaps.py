"""The paper's Figure 6, on the new roster: safety-task and capability-task panels.

Same OFAT grid as awareness_heatmaps.py's right panel, but the way arXiv:2605.23055 draws it:
one panel per task valence, cells are *matched-type* awareness (a safety task counts only when the
judge typed the awareness "safety", and vice versa), and a small superscript gives the change in
task compliance vs baseline in percentage points when it exceeds 5 (red = more compliant, green =
more refusals on safety tasks / more failures on capability tasks). Compliance always comes from
the cot judge, whichever probe supplies the awareness rates.

Data: charts/awareness_rates.csv from extract_awareness.py. Writes figure6-cot and
figure6-selfreport.

Run from the post dir:  python3 charts/figure6_heatmaps.py
"""

import csv
from collections import defaultdict

import altair as alt

from theme import BG, MUTED, fonts, save

MODELS = [  # display order, grouped by provider (same as awareness_heatmaps.py)
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
ANNOT_PP = 5
UP, DOWN = "#e0524f", "#3fbf7f"

CELL = 50
rates = defaultdict(dict)  # probe -> (model, config, valence) -> matched rate
compliance = {}  # (model, config, valence) -> share of gradable verdicts that complied (cot judge)
with open("charts/awareness_rates.csv") as f:
    for row in csv.DictReader(f):
        key = (row["model"], row["config"], row["valence"])
        if int(row["graded"]) >= 20:
            rates[row["probe"]][key] = int(row["matched"]) / int(row["graded"])
        if row["probe"] == "cot" and int(row["perf_graded"]) >= 20:
            compliance[key] = int(row["done"]) / int(row["perf_graded"])


def panel(probe, valence, title, vmax, f):
    data = []
    for key, name in MODELS:
        base = compliance.get((key, "baseline", valence))
        for cfg, label in COLS:
            r = rates[probe].get((key, cfg, valence))
            c = compliance.get((key, cfg, valence))
            delta = None if cfg == "baseline" or base is None or c is None else (c - base) * 100
            data.append({
                "model": name, "col": label, "rate": r,
                "txt": "–" if r is None else f"{r * 100:.0f}%",
                "nodata": r is None,
                "annot": "" if delta is None or abs(delta) < ANNOT_PP else f"{delta:+.0f}",
                "up": delta is not None and delta > 0,
            })
    width = CELL * len(COLS)
    row_h = CELL * 0.72  # taller than awareness_heatmaps.py's cells: the superscript needs headroom
    base = alt.Chart(alt.Data(values=data)).encode(
        x=alt.X("col:N", sort=[c[1] for c in COLS], title=title,
                axis=alt.Axis(labelAngle=-40, labelLimit=320, orient="bottom")),
        y=alt.Y("model:N", sort=[m[1] for m in MODELS], title=None,
                axis=alt.Axis(labelLimit=320)),
    )
    cells = base.transform_filter("datum.nodata == false").mark_rect(
        stroke=BG, strokeWidth=1.5).encode(
        color=alt.Color("rate:Q",
                        scale=alt.Scale(domain=[0, vmax], range=[BG, "#2e7dc1"], clamp=True),
                        legend=None))
    blanks = base.transform_filter("datum.nodata == true").mark_rect(
        fill=MUTED, stroke=BG, strokeWidth=1.5)
    # Value sits a touch below center so the top-right superscript has its own band.
    labels = base.mark_text(fontSize=f["label"] * 0.85, fontWeight="bold",
                            dy=row_h * 0.08).encode(
        text="txt:N",
        color=alt.condition("datum.nodata", alt.value(MUTED), alt.value("#f2f3f5")))
    annots = base.transform_filter("datum.annot != ''").mark_text(
        fontSize=f["label"] * 0.5, fontWeight="bold", align="right", baseline="top",
        dx=CELL * 0.47, dy=-row_h * 0.47).encode(
        text="annot:N",
        color=alt.condition("datum.up", alt.value(UP), alt.value(DOWN)))
    return (cells + blanks + labels + annots).properties(
        width=width, height=row_h * len(MODELS))


for probe in ("cot", "selfreport"):
    total_width = CELL * len(COLS) * 2 + 40
    f = fonts(total_width)
    vmax = max(rates[probe].values())
    left = panel(probe, "safety", "Safety Tasks", vmax, f)
    right = panel(probe, "capability", "Capability Tasks", vmax, f)
    chart = alt.hconcat(left, right, spacing=40).properties(
        title=alt.TitleParams(
            text=f"Eval Awareness by Factor, {TITLE[probe]}",
            subtitle=[
                "Matched-type awareness, % of graded samples. Superscript: task compliance vs "
                f"baseline in pp when |Δ| ≥ {ANNOT_PP};",
                "red = more compliant, green = more refusals (safety) or failures (capability)",
            ]))
    save(chart, f"figure6-{probe}", total_width)
