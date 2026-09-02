"""The paper's key chart, redrawn: safety-task awareness as EvalAwareBench factors stack.

Reproduces the safety-tasks panel of Figure 7 in arXiv:2605.23055 (2026). Numbers are hardcoded
from the paper (matched-type CoT awareness, 25 randomly sampled safety tasks, 10 random factor
combinations per task per count). The original is a low-res screenshot with no row labels; this
one has both.

Run from the post dir:  python3 charts/paper_figure7.py
"""

import altair as alt

from theme import BG, MUTED, fonts, save

# model -> awareness % with 0..8 factors varied (Figure 7, left panel)
ROWS = [
    ("Claude Sonnet 4.5", [1, 7, 11, 17, 14, 19, 22, 18, 11]),
    ("GPT-5", [0, 0, 1, 2, 2, 3, 2, 3, 7]),
    ("DeepSeek R1", [5, 4, 7, 11, 15, 14, 20, 19, 23]),
    ("Kimi K2.5", [13, 24, 30, 33, 31, 46, 47, 48, 44]),
    ("GLM-5", [0, 3, 5, 10, 8, 16, 19, 18, 17]),
    ("Qwen3 T-235B", [4, 14, 27, 33, 47, 38, 41, 39, 36]),
    ("Qwen3 T-30B", [4, 9, 13, 24, 27, 32, 36, 29, 35]),
    ("GPT-oss 120B", [0, 1, 1, 2, 1, 2, 4, 2, 3]),
    ("GPT-oss 20B", [0, 0, 0, 1, 0, 2, 1, 2, 3]),
]
N_FACTORS = 9
CELL = 56
ROW_H = CELL * 0.72

data = [
    {"model": model, "n": n, "rate": rate, "txt": f"{rate}%"}
    for model, rates in ROWS
    for n, rate in enumerate(rates)
]
width = CELL * N_FACTORS
f = fonts(width)
models = [m for m, _ in ROWS]

base = alt.Chart(alt.Data(values=data)).encode(
    x=alt.X("n:O", title="Number of Factors Varied", axis=alt.Axis(labelAngle=0)),
    y=alt.Y("model:N", sort=models, title=None, axis=alt.Axis(labelLimit=320)),
)
cells = base.mark_rect(stroke=BG, strokeWidth=1.5).encode(
    color=alt.Color("rate:Q",
                    scale=alt.Scale(domain=[0, max(max(r) for _, r in ROWS)],
                                    range=[BG, "#2e7dc1"]),
                    legend=None))
labels = base.mark_text(fontSize=f["label"] * 0.9, fontWeight="bold").encode(
    text="txt:N",
    color=alt.condition("datum.rate == 0", alt.value(MUTED), alt.value("#f2f3f5")))
# Dashed rule after the baseline column, as in the paper.
baseline_rule = alt.Chart(alt.Data(values=[{"x": CELL}])).mark_rule(
    stroke=MUTED, strokeDash=[4, 4], strokeWidth=1.5).encode(x=alt.value(CELL))

chart = (cells + labels + baseline_rule).properties(
    width=width, height=ROW_H * len(ROWS),
    title=alt.TitleParams(
        text="Safety Eval Awareness as Factors Stack",
        subtitle="Figure 7 of Decomposing and Measuring Evaluation Awareness (2026), safety tasks"))
save(chart, "paper-figure7-safety", width)
