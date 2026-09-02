"""Our replication of the paper's Figure 7 (safety panel), same layout as paper_figure7.py.

Design matches the paper: 25 randomly sampled tasks, 10 random factor combinations per task per
count (every combination where fewer exist), F9-F13 pinned to the paper's harness, 1 sample per
cell, matched-type CoT awareness (safety awareness on safety tasks), claude-sonnet-5 judge. Numbers
are yes / graded from decomposing-eval-awareness results/eval_bench/plots/stacking_summary_matched.json
(run 2026-09-01, pins in plots/plot_stacking.py). Cells at 0 and 8 factors have one combination per
task (n = 20-25); the rest have n = 150-250.

GPT-5: the OpenAI account was terminated ~700 calls into the run, so 2,701 of its 3,400 cells are
API errors; its row has n = 4-57 per cell and is drawn muted.

Run from the post dir:  python3 charts/replication_figure7.py
"""

import altair as alt

from theme import BG, MUTED, fonts, save

# model -> (aware, graded) with 0..8 factors varied, safety tasks
ROWS = [
    ("Claude Sonnet 4.5", [(0, 20), (8, 177), (13, 216), (19, 210), (12, 207), (8, 201), (17, 207), (8, 153), (1, 20)]),
    ("GPT-5*", [(0, 5), (0, 34), (1, 33), (1, 37), (0, 36), (0, 33), (0, 39), (0, 29), (0, 4)]),
    ("DeepSeek R1", [(0, 22), (4, 182), (5, 221), (11, 219), (12, 219), (20, 217), (29, 217), (27, 179), (4, 22)]),
    ("Kimi K2.5", [(3, 22), (29, 179), (37, 221), (37, 222), (59, 235), (57, 228), (54, 233), (35, 182), (2, 22)]),
    ("GLM-5", [(0, 25), (3, 191), (8, 239), (7, 237), (11, 239), (7, 237), (14, 238), (8, 191), (1, 24)]),
    ("Qwen3 T-235B", [(1, 23), (19, 181), (35, 225), (66, 229), (100, 228), (114, 226), (135, 222), (120, 183), (15, 23)]),
    ("Qwen3 T-30B", [(0, 23), (8, 181), (21, 227), (28, 229), (43, 231), (47, 235), (58, 233), (51, 187), (6, 24)]),
    ("GPT-oss 120B", [(0, 25), (0, 193), (0, 235), (1, 234), (1, 240), (1, 240), (2, 237), (2, 192), (0, 24)]),
    ("GPT-oss 20B", [(0, 25), (0, 195), (1, 243), (0, 241), (0, 243), (1, 240), (2, 242), (0, 193), (0, 24)]),
]
STUB = {"GPT-5*"}
N_FACTORS = 9
CELL = 56
ROW_H = CELL * 0.72
POOLED = "Pooled"

# Pooled row: every model's graded samples together (weights models by n); the GPT-5
# stub is left out so its handful of cells doesn't pretend to be a ninth model.
pooled = [
    (sum(c[n][0] for m, c in ROWS if m not in STUB), sum(c[n][1] for m, c in ROWS if m not in STUB))
    for n in range(N_FACTORS)
]
rows = ROWS + [(POOLED, pooled)]
data = [
    {
        "model": model,
        "n": n,
        "rate": round(100 * yes / graded),
        "txt": f"{round(100 * yes / graded)}%",
        "stub": model in STUB,
    }
    for model, cells in rows
    for n, (yes, graded) in enumerate(cells)
]
width = CELL * N_FACTORS
f = fonts(width)
models = [m for m, _ in rows]

base = alt.Chart(alt.Data(values=data)).encode(
    x=alt.X("n:O", title="Number of Factors Varied", axis=alt.Axis(labelAngle=0)),
    y=alt.Y("model:N", sort=models, title=None, axis=alt.Axis(labelLimit=320)),
)
cells = base.mark_rect(stroke=BG, strokeWidth=1.5).encode(
    color=alt.Color("rate:Q",
                    scale=alt.Scale(domain=[0, max(d["rate"] for d in data)],
                                    range=[BG, "#2e7dc1"]),
                    legend=None))
labels = base.mark_text(fontSize=f["label"] * 0.9, fontWeight="bold").encode(
    text="txt:N",
    color=alt.condition("datum.rate == 0 || datum.stub", alt.value(MUTED), alt.value("#f2f3f5")))
# Dashed rule after the baseline column, as in the paper; solid rule above Pooled.
rule = alt.Chart(alt.Data(values=[{}]))
rules = (
    rule.mark_rule(stroke=MUTED, strokeDash=[4, 4], strokeWidth=1.5).encode(x=alt.value(CELL))
    + rule.mark_rule(stroke=MUTED, strokeWidth=1.5).encode(y=alt.value(ROW_H * len(ROWS)))
)

chart = (cells + labels + rules).properties(
    width=width, height=ROW_H * len(rows),
    title=alt.TitleParams(
        text="Our Replication: Safety Eval Awareness as Factors Stack",
        subtitle="Same design as Figure 7, Sonnet 5 judge, 1 sample per cell. *GPT-5 cut short by an account ban"))
save(chart, "replication-figure7-safety", width)
