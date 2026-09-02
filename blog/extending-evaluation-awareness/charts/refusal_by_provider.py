"""Refusal + classifier-block rate by lab, safety tasks vs capability tasks.

Grouped bars: x = task valence, one bar per lab (brand colors and lab order as in ladder.py), label
on each bar. Rate = samples the judge graded "refused" plus API-level blocks (classifier stops,
prompt filters, empty returns) over every graded sample; the blocks alone are tabulated in the post.
All nine OFAT configs pooled per lab.

Data: charts/refusal_rates.csv from extract_refusals.py. Writes refusal-by-provider.

Run from the post dir:  python3 charts/refusal_by_provider.py
"""

import csv
from collections import defaultdict

import altair as alt

from theme import BG, FG, fonts, save

# Same domain order and hues as ladder.py so the two legends read alike.
LAB_COLOR = {
    "Anthropic": "#d97757", "OpenAI": "#c8ccd4", "Google": "#34a853", "Alibaba": "#c026d3",
    "DeepSeek": "#4d6bfe", "Moonshot": "#fec230", "Z.ai": "#dc2626", "MiniMax": "#22b8d8",
}
LABS = list(LAB_COLOR)
VALENCE = [("safety", "Safety tasks"), ("capability", "Capability tasks")]

tot = defaultdict(lambda: [0, 0])  # (lab, valence) -> [refused + blocked, all samples]
with open("charts/refusal_rates.csv") as f:
    for row in csv.DictReader(f):
        t = tot[(row["lab"], row["valence"])]
        t[0] += int(row["model_refused"]) + int(row["api_blocked"])
        t[1] += int(row["model_refused"]) + int(row["api_blocked"]) + int(row["answered"])

data = [
    {"lab": lab, "valence": label, "rate": tot[(lab, v)][0] / tot[(lab, v)][1],
     "txt": f"{100 * tot[(lab, v)][0] / tot[(lab, v)][1]:.0f}"}
    for v, label in VALENCE
    for lab in LABS
]

width = 640
f = fonts(width)
base = alt.Chart(alt.Data(values=data)).encode(
    x=alt.X("valence:N", sort=[v[1] for v in VALENCE], title=None,
            axis=alt.Axis(labelAngle=0, labelPadding=8, labelLimit=0)),
    xOffset=alt.XOffset("lab:N", sort=LABS),
)
bars = base.mark_bar(cornerRadiusTopLeft=3, cornerRadiusTopRight=3, stroke=BG, strokeWidth=2).encode(
    y=alt.Y("rate:Q", title=None, scale=alt.Scale(domain=[0, 1]),
            axis=alt.Axis(format="%", tickCount=5)),
    color=alt.Color("lab:N", sort=LABS, title=None,
                    scale=alt.Scale(domain=LABS, range=list(LAB_COLOR.values())),
                    legend=alt.Legend(orient="top-right", direction="vertical", symbolType="square")),
)
labels = base.mark_text(dy=-6, fontSize=f["label"] * 0.85, fontWeight="bold", color=FG).encode(
    y="rate:Q", text="txt:N")
chart = (bars + labels).properties(
    width=width, height=200,
    title=alt.TitleParams(text="Refusal + Classifier Block Rate by Lab"))
save(chart, "refusal-by-provider", width)
