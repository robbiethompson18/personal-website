"""Textbook72 pass@k out to 10,240 attempts: the pretrained model vs the same model after ~5.4 h of
expert-iteration RL (nd-rl long_rl_20261014, untied-ei seed 1, v5 round 25). Bands are 95%
theorem-bootstrap intervals.

Data: passk.csv, exported from nd-rl code/experiments/current/long_rl_20261014/passk/export_10k.py.
Run from the post dir:  python3 charts/passk.py
"""
import csv

import altair as alt

from theme import HUE, save

WIDTH, HEIGHT = 560, 400
LABEL = {"pretrain": "Pretrain", "v5_round025": "Pretrain + 5.4 h RL"}
COLOR = {LABEL["pretrain"]: HUE["water"], LABEL["v5_round025"]: HUE["recycle"]}

rows = [{**r, "model": LABEL[r["model"]]} for r in csv.DictReader(open("charts/passk.csv"))]
for r in rows:
    for key in ("k", "mean", "lo", "hi"):
        r[key] = float(r[key])

base = alt.Chart(alt.Data(values=rows)).encode(
    x=alt.X("k:Q", scale=alt.Scale(type="log", domain=[1, 10240], nice=False), title="Attempts per Problem (k)",
            axis=alt.Axis(values=[1, 10, 100, 1000, 10000], format="~s")),
)
scale = alt.Scale(domain=list(COLOR), range=list(COLOR.values()))
band = base.mark_area(fillOpacity=0.18).encode(y=alt.Y("lo:Q"), y2="hi:Q", color=alt.Color("model:N", scale=scale))
line = base.mark_line(strokeWidth=2.5).encode(
    y=alt.Y("mean:Q", title="Share of Textbook Problems Solved", scale=alt.Scale(domain=[0, 1]),
            axis=alt.Axis(format="%")),
    color=alt.Color("model:N", title=None, scale=scale, legend=alt.Legend(orient="top-left", offset=8, symbolType="stroke",
                                                                      symbolOpacity=1, symbolStrokeWidth=3)))
chart = (band + line).properties(width=WIDTH, height=HEIGHT, title="Textbook Problems Solved by Pass@k")
save(chart, "passk", WIDTH)
