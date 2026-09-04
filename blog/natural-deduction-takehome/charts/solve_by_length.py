"""Greedy solve rate by the length of the proof the theorem was generated with.

The headline Stage-1 figure: ~99% inside the training cap, then a cliff. Lengths 2-6 are the
held-out split (400 each, from the checkpoints' own recorded final eval); 7-16 are the RL-target
and transfer pools pooled (200 each, 61 at length 16). Whisker = Wilson 95% CI. The dashed rule
marks the cap of 6 lines, which is the longest proof anything was trained on.

Run from the post dir:  python3 charts/solve_by_length.py
"""
import csv
import math

import altair as alt

from theme import FG, HUE, MUTED, fonts, save

WIDTH, HEIGHT = 560, 300
POS = {"nope": "NoPE", "rope": "RoPE"}
COLOR = {"NoPE": HUE["water"], "RoPE": HUE["carbon"]}


def wilson(k, n, z=1.96):
    p, d = k / n, 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return max(0.0, c - h), min(1.0, c + h)


rows = []
with open("charts/solve_by_length.csv") as fh:
    for r in csv.DictReader(fh):
        k, n = int(r["solved"]), int(r["n"])
        lo, hi = wilson(k, n)
        rows.append({"model": POS[r["pos"]], "len": int(r["gen_lines"]),
                     "rate": 100 * k / n, "lo": 100 * lo, "hi": 100 * hi})

f = fonts(WIDTH)
color = alt.Color("model:N", title=None,
                  scale=alt.Scale(domain=list(COLOR), range=list(COLOR.values())),
                  legend=alt.Legend(orient="top-right", direction="vertical", offset=4))
base = alt.Chart(alt.Data(values=rows)).encode(
    x=alt.X("len:Q", title="Proof Length, min(Generated, Written) (Lines)",
            scale=alt.Scale(domain=[1.5, 16.5]), axis=alt.Axis(tickCount=8, values=list(range(2, 17, 2)))),
    y=alt.Y("rate:Q", title="Greedy Solve Rate (%)", scale=alt.Scale(domain=[0, 100])),
)
cap = alt.Chart(alt.Data(values=[{"x": 6.5}])).mark_rule(
    color=MUTED, strokeDash=[4, 4], strokeWidth=1).encode(x="x:Q")
cap_label = alt.Chart(alt.Data(values=[{"x": 6.5, "y": 92, "t": "training cap"}])).mark_text(
    align="left", dx=6, color=MUTED, fontSize=f["label"]).encode(x="x:Q", y="y:Q", text="t:N")
ci = base.mark_rule(strokeWidth=1.5, opacity=0.8).encode(y="lo:Q", y2="hi:Q", color=color)
line = base.mark_line(strokeWidth=1.8, opacity=0.9).encode(color=color)
pts = base.mark_point(filled=True, size=45).encode(color=color)

chart = (cap + cap_label + line + ci + pts).properties(
    width=WIDTH, height=HEIGHT,
    title=alt.TitleParams(
        text="Solve Rate Collapses at the Training Cap",
        subtitle="A solved theorem is filed under the proof length the model actually wrote."),
)
save(chart, "solve-by-length", WIDTH)
