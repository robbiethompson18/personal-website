"""The expert-iteration loop, counted in proofs the model actually wrote.

Each round samples k=32 against the RL targets, keeps every verified proof, and re-fine-tunes
from the frozen Stage-1 base. Bars are verified proofs by the length written *after pruning dead
lines*, greedy, one attempt per theorem — no denominator, so nothing depends on how hard the
generator thought a target was.

The two panels are the whole argument: RL targets are the theorems the loop trained against,
Transfer is the pool it never sampled. Transfer rising is what rules out memorisation.

The bar that never appears is length 9. Every round tops out at 8.

Run from the post dir:  python3 charts/harvest_loop.py
"""
import csv

import altair as alt

from theme import BG, FG, HUE, fonts, save

WIDTH, HEIGHT = 300, 260
STAGES = ["Pretrain only", "1 round", "2 rounds", "3 rounds"]
COLOR = {"7 lines": HUE["water"], "8 lines": HUE["carbon"]}

rows = []
with open("charts/harvest_loop.csv") as fh:
    for r in csv.DictReader(fh):
        rows.append({"stage": r["stage"], "pool": r["pool"],
                     "len": f'{r["length"]} lines', "count": int(r["count"])})

f = fonts(WIDTH)
base = alt.Chart(alt.Data(values=rows)).encode(
    x=alt.X("stage:N", sort=STAGES, title=None,
            axis=alt.Axis(labelAngle=-30, labelLimit=90)),
    xOffset=alt.XOffset("len:N", sort=list(COLOR)),
)
bars = base.mark_bar(cornerRadiusTopLeft=3, cornerRadiusTopRight=3,
                     stroke=BG, strokeWidth=1).encode(
    y=alt.Y("count:Q", title="Verified Proofs Written",
            scale=alt.Scale(domain=[0, 82])),
    color=alt.Color("len:N", title=None,
                    scale=alt.Scale(domain=list(COLOR), range=list(COLOR.values())),
                    legend=alt.Legend(orient="top-left", direction="vertical",
                                      symbolType="square", offset=4)),
)
# direct labels as well as the legend: identity is never carried by colour alone
labels = base.mark_text(dy=-6, fontSize=f["label"], color=FG).encode(
    y="count:Q", text="count:Q")

chart = (bars + labels).properties(width=WIDTH, height=HEIGHT).facet(
    column=alt.Column("pool:N", title=None, sort=["RL targets", "Transfer"],
                      header=alt.Header(labelFontSize=f["axis_title"], labelColor=FG)),
).properties(
    title=alt.TitleParams(
        text="Expert Iteration Adds Proofs at 7 and 8 Lines, Then Stops",
        subtitle="Verified proofs by the length written (dead lines pruned). "
                 "No 9-line proof in any round, on either pool.",
    ),
)
save(chart, "harvest-loop", WIDTH)
