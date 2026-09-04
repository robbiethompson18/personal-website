"""The robust frontier: verified proofs counted by the length actually written.

This is the metric that survives the generating-length labels being wrong. No denominator, so
nothing depends on how hard we thought a target was — just "the model wrote this many verified
proofs of this many lines". The README's frontier rule is the longest length with at least 5
distinct verified proofs; the dashed line is that threshold.

Attempts on the 7-16 line pools only (1,861 targets per model, greedy, one attempt each). The
held-out set is excluded because its targets are capped at 6 and would swamp the short bars.

Run from the post dir:  python3 charts/frontier.py
"""
import csv
from collections import defaultdict

import altair as alt

from theme import BG, FG, HUE, MUTED, fonts, save

WIDTH, HEIGHT = 560, 260
POS = {"nope": "NoPE", "rope": "RoPE"}
COLOR = {"NoPE": HUE["water"], "RoPE": HUE["carbon"]}

counts = defaultdict(int)
with open("charts/written_length.csv") as fh:
    for r in csv.DictReader(fh):
        if int(r["verified"]):
            counts[(POS[r["pos"]], int(r["written"]))] += int(r["count"])
rows = [{"model": m, "written": w, "count": c} for (m, w), c in sorted(counts.items())]

f = fonts(WIDTH)
bars = alt.Chart(alt.Data(values=rows)).mark_bar(stroke=BG, strokeWidth=0.5).encode(
    x=alt.X("written:O", title="Length of the Verified Proof (Lines)"),
    xOffset=alt.XOffset("model:N", sort=list(COLOR)),
    y=alt.Y("count:Q", title="Verified Proofs"),
    color=alt.Color("model:N", title=None,
                    scale=alt.Scale(domain=list(COLOR), range=list(COLOR.values())),
                    legend=alt.Legend(orient="top-right", direction="vertical", offset=4)),
)
thresh = alt.Chart(alt.Data(values=[{"y": 5}])).mark_rule(
    color=MUTED, strokeDash=[4, 4], strokeWidth=1).encode(y="y:Q")
thresh_label = alt.Chart(alt.Data(values=[{"y": 5, "t": "frontier threshold: 5 proofs"}])).mark_text(
    align="left", dx=4, dy=-6, color=MUTED, fontSize=f["label"]).encode(
    x=alt.value(4), y="y:Q", text="t:N")

chart = (bars + thresh + thresh_label).properties(
    width=WIDTH, height=HEIGHT,
    title=alt.TitleParams(
        text="Robust Frontier: 7 Lines",
        subtitle="Counts, not rates — this metric does not depend on how hard we labelled a target."),
)
save(chart, "frontier", WIDTH)
