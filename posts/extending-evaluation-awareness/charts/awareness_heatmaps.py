"""Two side-by-side heatmaps per probe, mirroring the paper's key chart.

Left panel: awareness at the naturalistic baseline, split by task valence, plus verbatim HarmBench
where it was run (the five open-weight models). Right panel: safety tasks with one factor flipped
to its artificial level (the paper's OFAT grid), plus the all-varied ceiling where run.

The paper's right panel is "number of factors varied 0..8"; the overnight sweep is OFAT (one at a
time), so the columns here are which factor, not how many.

Data: charts/awareness_rates.csv from extract_awareness.py. Writes awareness-heatmaps-cot and
awareness-heatmaps-selfreport.

Run from the post dir:  python3 charts/awareness_heatmaps.py
"""

import csv
from collections import defaultdict

import altair as alt

from theme import BG, GRID, MUTED, fonts, save

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

# (config, valence) -> column label
LEFT = [
    ("harmbench_verbatim", "safety", "HarmBench verbatim"),
    ("baseline", "safety", "Baseline, safety"),
    ("baseline", "capability", "Baseline, capability"),
]
RIGHT = [
    ("baseline", "safety", "Baseline"),
    ("F1", "safety", "F1 fake entities"),
    ("F2", "safety", "F2 incoherent"),
    ("F3", "safety", "F3 formal"),
    ("F4", "safety", "F4 bare request"),
    ("F5", "safety", "F5 stakes named"),
    ("F6", "safety", "F6 jailbreak wrapper"),
    ("F7", "safety", "F7 template"),
    ("F8", "safety", "F8 eval disclosed"),
    ("all_varied", "safety", "All 8 varied"),
]
TITLE = {"cot": "CoT-Judged", "selfreport": "Self-Reported"}
SUBTITLE = {
    "cot": "GPT-5.6 judge reads the model's reasoning; % of graded samples",
    "selfreport": "Model shown its own transcript and asked; % of graded samples",
}

CELL = 50
rates = defaultdict(dict)  # probe -> (model, config, valence) -> rate
with open("charts/awareness_rates.csv") as f:
    for row in csv.DictReader(f):
        if int(row["graded"]) >= 20:  # drop tiny cells (partial anchor runs)
            rates[row["probe"]][(row["model"], row["config"], row["valence"])] = int(
                row["yes"]
            ) / int(row["graded"])


def panel(probe, cols, title, vmax, f):
    data = []
    for key, name in MODELS:
        for cfg, val, label in cols:
            r = rates[probe].get((key, cfg, val))
            data.append({
                "model": name, "col": label, "rate": r,
                "txt": "–" if r is None else f"{r * 100:.0f}%",
                "nodata": r is None,
            })
    width = CELL * len(cols)
    base = alt.Chart(alt.Data(values=data)).encode(
        x=alt.X("col:N", sort=[c[2] for c in cols], title=title,
                axis=alt.Axis(labelAngle=-40, labelLimit=220, orient="bottom")),
        y=alt.Y("model:N", sort=[m[1] for m in MODELS], title=None,
                axis=alt.Axis(labelLimit=200)),
    )
    cells = base.transform_filter("datum.nodata == false").mark_rect(
        stroke=BG, strokeWidth=1.5).encode(
        color=alt.Color("rate:Q",
                        scale=alt.Scale(domain=[0, vmax], range=[BG, "#2e7dc1"], clamp=True),
                        legend=None))
    blanks = base.transform_filter("datum.nodata == true").mark_rect(
        fill=GRID, stroke=BG, strokeWidth=1.5)
    labels = base.mark_text(fontSize=f["label"], fontWeight="bold").encode(
        text="txt:N",
        color=alt.condition("datum.nodata", alt.value(MUTED), alt.value("#f2f3f5")))
    return (cells + blanks + labels).properties(width=width, height=CELL * 0.6 * len(MODELS))


for probe in ("cot", "selfreport"):
    total_width = CELL * (len(LEFT) + len(RIGHT)) + 40
    f = fonts(total_width)
    vmax = max(rates[probe].values())
    left = panel(probe, LEFT, "Naturalistic prompts", vmax, f)
    right = panel(probe, RIGHT, "Safety tasks, one factor made artificial", vmax, f)
    chart = alt.hconcat(left, right, spacing=40).properties(
        title=alt.TitleParams(text=f"Eval Awareness, {TITLE[probe]}",
                              subtitle=SUBTITLE[probe]))
    save(chart, f"awareness-heatmaps-{probe}", total_width)
