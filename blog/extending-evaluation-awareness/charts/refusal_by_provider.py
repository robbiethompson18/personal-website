"""Refusal + classifier-block rate by lab, safety tasks vs capability tasks.

Grouped bars: x = task valence, one bar per lab (brand colors as in ladder.py), bars sorted by
rate within each group, legend ordered by safety-task rate, label on each bar. Rate = samples the judge graded "refused" plus API-level blocks (classifier stops,
prompt filters, empty returns) over every graded sample; the blocks alone are tabulated in the post.
All nine OFAT configs pooled per lab.

Data: charts/refusal_rates.csv from extract_refusals.py. Writes refusal-by-provider.

Run from the post dir:  python3 charts/refusal_by_provider.py
"""

import csv
from collections import defaultdict

import altair as alt

from theme import BG, FG, LAB, fonts, save

VALENCE = [("safety", "Safety tasks"), ("capability", "Capability tasks")]

tot = defaultdict(lambda: [0, 0])  # (lab, valence) -> [refused + blocked, all samples]
with open("charts/refusal_rates.csv") as f:
    for row in csv.DictReader(f):
        t = tot[(row["lab"], row["valence"])]
        t[0] += int(row["model_refused"]) + int(row["api_blocked"])
        t[1] += int(row["model_refused"]) + int(row["api_blocked"]) + int(row["answered"])

rate = {(lab, v): tot[(lab, v)][0] / tot[(lab, v)][1] for lab in LAB for v, _ in VALENCE}
LABS = sorted(LAB, key=lambda lab: -rate[(lab, "safety")])  # legend order
data = []
for v, label in VALENCE:
    for rank, lab in enumerate(sorted(LAB, key=lambda lab: -rate[(lab, v)])):
        data.append({"lab": lab, "valence": label, "rate": rate[(lab, v)], "rank": rank,
                     "txt": f"{100 * rate[(lab, v)]:.0f}%"})

width = 640
f = fonts(width)
base = alt.Chart(alt.Data(values=data)).encode(
    x=alt.X("valence:N", sort=[v[1] for v in VALENCE], title=None,
            axis=alt.Axis(labelAngle=0, labelPadding=8, labelLimit=0)),
    xOffset=alt.XOffset("rank:O"),
)
bars = base.mark_bar(cornerRadiusTopLeft=3, cornerRadiusTopRight=3, stroke=BG, strokeWidth=2).encode(
    y=alt.Y("rate:Q", title=None, scale=alt.Scale(domain=[0, 1]),
            axis=alt.Axis(format="%", tickCount=5)),
    color=alt.Color("lab:N", sort=LABS, title=None,
                    scale=alt.Scale(domain=LABS, range=[LAB[lab] for lab in LABS]),
                    legend=alt.Legend(orient="top-right", direction="vertical", symbolType="square")),
)
labels = base.mark_text(dy=-6, fontSize=f["label"] * 0.85, fontWeight="bold", color=FG).encode(
    y="rate:Q", text="txt:N")
chart = (bars + labels).properties(
    width=width, height=200,
    title=alt.TitleParams(text="Refusal + Classifier Block Rate by Lab"))
save(chart, "refusal-by-provider", width)
