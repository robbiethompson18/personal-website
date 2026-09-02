"""Safety eval awareness as EvalAwareBench factors stack: the paper's Figure 7 next to our replication.

One image, two panels sharing the model column. Left: the safety-tasks panel of Figure 7 in
arXiv:2605.23055 (2026), numbers hardcoded from the paper (matched-type CoT awareness, 25 randomly
sampled safety tasks, 10 random factor combinations per task per count). Right: our run of the same
design (F9-F13 pinned to the paper's harness, 1 sample per cell, claude-sonnet-5 judge), yes / graded
from decomposing-eval-awareness results/eval_bench/plots/stacking_summary_matched.json (run
2026-09-01, pins in plots/plot_stacking.py). In ours, cells at 0 and 8 factors have one combination
per task (n = 20-25); the rest have n = 150-250. One color scale across both panels, cell values in %.

GPT-5: the OpenAI account was terminated ~700 calls into our run, so 2,701 of its 3,400 cells are
API errors; its row has n = 4-57 per cell and is drawn muted on the right.

Pooled row: the paper's design gives every model the same cells per count, so its pooled rate is
the unweighted mean of the model rates; ours pools graded samples (weights models by n) and leaves
out the GPT-5 stub so its handful of cells doesn't pretend to be a ninth model.

Run from the post dir:  python3 charts/figure7_stacking.py
"""

import altair as alt

from theme import BG, MUTED, fonts, save

MODELS = ["Claude Sonnet 4.5", "GPT-5", "DeepSeek R1", "Kimi K2.5", "GLM-5",
          "Qwen3 T-235B", "Qwen3 T-30B", "GPT-oss 120B", "GPT-oss 20B"]
# model -> awareness % with 0..8 factors varied (Figure 7, left panel)
PAPER = {
    "Claude Sonnet 4.5": [1, 7, 11, 17, 14, 19, 22, 18, 11],
    "GPT-5": [0, 0, 1, 2, 2, 3, 2, 3, 7],
    "DeepSeek R1": [5, 4, 7, 11, 15, 14, 20, 19, 23],
    "Kimi K2.5": [13, 24, 30, 33, 31, 46, 47, 48, 44],
    "GLM-5": [0, 3, 5, 10, 8, 16, 19, 18, 17],
    "Qwen3 T-235B": [4, 14, 27, 33, 47, 38, 41, 39, 36],
    "Qwen3 T-30B": [4, 9, 13, 24, 27, 32, 36, 29, 35],
    "GPT-oss 120B": [0, 1, 1, 2, 1, 2, 4, 2, 3],
    "GPT-oss 20B": [0, 0, 0, 1, 0, 2, 1, 2, 3],
}
# model -> (aware, graded) with 0..8 factors varied, safety tasks
OURS = {
    "Claude Sonnet 4.5": [(0, 20), (8, 177), (13, 216), (19, 210), (12, 207), (8, 201), (17, 207), (8, 153), (1, 20)],
    "GPT-5": [(0, 5), (0, 34), (1, 33), (1, 37), (0, 36), (0, 33), (0, 39), (0, 29), (0, 4)],
    "DeepSeek R1": [(0, 22), (4, 182), (5, 221), (11, 219), (12, 219), (20, 217), (29, 217), (27, 179), (4, 22)],
    "Kimi K2.5": [(3, 22), (29, 179), (37, 221), (37, 222), (59, 235), (57, 228), (54, 233), (35, 182), (2, 22)],
    "GLM-5": [(0, 25), (3, 191), (8, 239), (7, 237), (11, 239), (7, 237), (14, 238), (8, 191), (1, 24)],
    "Qwen3 T-235B": [(1, 23), (19, 181), (35, 225), (66, 229), (100, 228), (114, 226), (135, 222), (120, 183), (15, 23)],
    "Qwen3 T-30B": [(0, 23), (8, 181), (21, 227), (28, 229), (43, 231), (47, 235), (58, 233), (51, 187), (6, 24)],
    "GPT-oss 120B": [(0, 25), (0, 193), (0, 235), (1, 234), (1, 240), (1, 240), (2, 237), (2, 192), (0, 24)],
    "GPT-oss 20B": [(0, 25), (0, 195), (1, 243), (0, 241), (0, 243), (1, 240), (2, 242), (0, 193), (0, 24)],
}
STUB = {"GPT-5"}  # muted in our panel only
N_FACTORS = 9
CELL = 40
ROW_H = CELL * 0.72
LABEL_COL = 130
SPACING = 12
WIDTH = 2 * CELL * N_FACTORS + LABEL_COL + SPACING
POOLED = "Pooled"
ROWS = MODELS + [POOLED]

paper = {m: [{"rate": r, "stub": False} for r in rs] for m, rs in PAPER.items()}
paper[POOLED] = [{"rate": round(sum(PAPER[m][n] for m in MODELS) / len(MODELS)), "stub": False}
                 for n in range(N_FACTORS)]
ours = {m: [{"rate": round(100 * y / g), "stub": m in STUB} for y, g in cs] for m, cs in OURS.items()}
ours[POOLED] = [{"rate": round(100 * sum(OURS[m][n][0] for m in MODELS if m not in STUB)
                               / sum(OURS[m][n][1] for m in MODELS if m not in STUB)),
                 "stub": False} for n in range(N_FACTORS)]
VMAX = max(c["rate"] for panel in (paper, ours) for cells in panel.values() for c in cells)


def panel(grid, title, f, show_models):
    data = [{"model": m, "n": n, "txt": str(c["rate"]), **c}
            for m in ROWS for n, c in enumerate(grid[m])]
    base = alt.Chart(alt.Data(values=data)).encode(
        x=alt.X("n:O", title="Factors Varied", axis=alt.Axis(labelAngle=0, labelPadding=6)),
        y=alt.Y("model:N", sort=ROWS, title=None,
                axis=alt.Axis(labelLimit=320) if show_models else None),
    )
    cells = base.mark_rect(stroke=BG, strokeWidth=1.5).encode(
        color=alt.Color("rate:Q", scale=alt.Scale(domain=[0, VMAX], range=[BG, "#2e7dc1"]),
                        legend=None))
    labels = base.mark_text(fontSize=f["label"] * 0.7, fontWeight="bold").encode(
        text="txt:N",
        color=alt.condition("datum.rate == 0 || datum.stub", alt.value(MUTED),
                            alt.value("#f2f3f5")))
    # Dashed rule after the baseline column, as in the paper; solid rule above Pooled.
    rule = alt.Chart(alt.Data(values=[{}]))
    rules = (
        rule.mark_rule(stroke=MUTED, strokeDash=[4, 4], strokeWidth=1.5).encode(x=alt.value(CELL))
        + rule.mark_rule(stroke=MUTED, strokeWidth=1.5).encode(y=alt.value(ROW_H * len(MODELS)))
    )
    return (cells + labels + rules).properties(
        width=CELL * N_FACTORS, height=ROW_H * len(ROWS),
        title=alt.TitleParams(text=title, anchor="middle", fontSize=f["subtitle"] * 1.1,
                              fontWeight="bold"))


f = fonts(WIDTH)
chart = alt.hconcat(
    panel(paper, "Paper (Figure 7)", f, show_models=True),
    panel(ours, "Our Replication", f, show_models=False),
    spacing=SPACING,
).properties(
    title=alt.TitleParams(
        text="Safety Eval Awareness as Factors Stack",
        subtitle=["CoT-judged, % of graded samples, one color scale. Left: Figure 7 of Decomposing and",
                  "Measuring Evaluation Awareness (2026). Right: same design, Sonnet 5 judge, 1 sample",
                  "per cell; GPT-5 (muted) cut short by an account ban, n = 4-57 per cell."]))
save(chart, "figure7-stacking", WIDTH)
