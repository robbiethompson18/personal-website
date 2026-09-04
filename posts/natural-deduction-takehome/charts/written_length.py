"""How long a proof the model writes when the target needs 7-16 lines.

The stopping-prior figure. Every one of these targets needs more than 6 lines, so a model that had
simply learned "stop at 6" would show nothing to the right of the cap. It does write 7s, and a few
8s-10s — they are almost all rejected. Stacked by whether the verifier accepted the proof.

Both positional schemes are pooled (1,861 targets each, 3,722 attempts): they differ by less than
the bar widths here, and solve-by-length already carries that comparison. Unparseable outputs are
excluded (NoPE 68, RoPE 130).

Run from the post dir:  python3 charts/written_length.py
"""
import csv
from collections import defaultdict

import altair as alt

from theme import BG, HUE, MUTED, fonts, save

WIDTH, HEIGHT = 560, 200
STATUS = {1: "Verified", 0: "Rejected"}
COLOR = {"Verified": HUE["recycle"], "Rejected": MUTED}

counts = defaultdict(int)
with open("charts/written_length.csv") as fh:
    for r in csv.DictReader(fh):
        counts[(int(r["written"]), STATUS[int(r["verified"])])] += int(r["count"])
rows = [{"written": w, "status": s, "count": c} for (w, s), c in sorted(counts.items())]

f = fonts(WIDTH)
# size, not a band scale: the x axis stays quantitative so the cap rule can sit at 6.5
bars = alt.Chart(alt.Data(values=rows)).mark_bar(size=44, stroke=BG, strokeWidth=0.5).encode(
    x=alt.X("written:Q", title="Proof Length the Model Wrote (Lines)",
            scale=alt.Scale(domain=[2.5, 10.5]), axis=alt.Axis(tickCount=8, grid=False)),
    y=alt.Y("count:Q", title="Attempts", stack=True),
    color=alt.Color("status:N", title=None,
                    scale=alt.Scale(domain=list(COLOR), range=list(COLOR.values())),
                    legend=alt.Legend(orient="top-right", direction="vertical", offset=4)),
)
cap = alt.Chart(alt.Data(values=[{"x": 6.5}])).mark_rule(
    color=MUTED, strokeDash=[4, 4], strokeWidth=1).encode(x="x:Q")
cap_label = alt.Chart(alt.Data(values=[{"x": 6.5, "y": 1500, "t": "training cap"}])).mark_text(
    align="left", dx=6, color=MUTED, fontSize=f["label"]).encode(x="x:Q", y="y:Q", text="t:N")

chart = (bars + cap + cap_label).properties(
    width=WIDTH, height=HEIGHT,
    title=alt.TitleParams(text="Every Target Here Needs 7+ Lines. The Model Writes 6."),
)
save(chart, "written-length", WIDTH)
