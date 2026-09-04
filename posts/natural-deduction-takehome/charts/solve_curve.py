"""Held-out greedy solve rate over training, both positional schemes.

Same caveat as loss-curves: in these two runs the mid-training eval read the first 1,000 records of
the held-out file, which is ordered by length, so the curve covers lengths 2-4 only and reads a
little high. The final points (full 2,000, all lengths) are 99.6% NoPE / 99.8% RoPE. Whisker =
Wilson 95% CI.

Run from the post dir:  python3 charts/solve_curve.py
"""
import csv
import math

import altair as alt

from theme import HUE, fonts, save

WIDTH, HEIGHT = 560, 300
POS = {"nope": "NoPE", "rope": "RoPE"}
COLOR = {"NoPE": HUE["water"], "RoPE": HUE["carbon"]}


def wilson(k, n, z=1.96):
    p, d = k / n, 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return max(0.0, c - h), min(1.0, c + h)


rows = []
with open("charts/solve_curve.csv") as fh:
    for r in csv.DictReader(fh):
        k, n = int(r["solved"]), int(r["n"])
        lo, hi = wilson(k, n)
        rows.append({"model": POS[r["pos"]], "epoch": float(r["epoch"]),
                     "rate": 100 * k / n, "lo": 100 * lo, "hi": 100 * hi})

f = fonts(WIDTH)
color = alt.Color("model:N", title=None,
                  scale=alt.Scale(domain=list(COLOR), range=list(COLOR.values())),
                  legend=alt.Legend(orient="bottom-right", direction="vertical", offset=8))
base = alt.Chart(alt.Data(values=rows)).encode(
    x=alt.X("epoch:Q", title="Epochs Over the Training Set"),
    y=alt.Y("rate:Q", title="Held-Out Greedy Solve Rate (%)", scale=alt.Scale(domain=[80, 100])),
)
chart = (base.mark_line(strokeWidth=1.8).encode(color=color)
         + base.mark_rule(strokeWidth=1.5, opacity=0.8).encode(y="lo:Q", y2="hi:Q", color=color)
         + base.mark_point(filled=True, size=45).encode(color=color)).properties(
    width=WIDTH, height=HEIGHT,
    title=alt.TitleParams(
        text="Held-Out Solve Rate Over Training",
        subtitle="These mid-training evals covered lengths 2-4 only; the endpoint is the full set."),
)
save(chart, "solve-curve", WIDTH)
