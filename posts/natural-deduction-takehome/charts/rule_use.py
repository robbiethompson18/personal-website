"""How often each inference rule shows up in the training set.

Share of proofs using the rule at least once, rather than raw counts: the counts span IMPE's 82k
down to NEGI's 300 and a bar chart on a log axis lies about length. The three rules that open a
subproof — IMPI, ORE, NEGI — are shaded apart, because they are the ones long proofs are built
from and the ones the generator almost never produces.

Run from the post dir:  python3 charts/rule_use.py
"""
import csv

import altair as alt

from theme import BG, FG, HUE, MUTED, fonts, save

WIDTH, ROW_H = 500, 24
BOXY = {"IMPI", "ORE", "NEGI"}          # the discharging rules: these open a box

rows = []
with open("charts/rule_use.csv") as fh:
    for r in csv.DictReader(fh):
        share = 100 * int(r["proofs"]) / int(r["total"])
        rows.append({"rule": r["rule"], "share": share,
                     "kind": "Opens a subproof" if r["rule"] in BOXY else "Local",
                     "txt": f"{share:.1f}%" if share >= 0.1 else f"{share:.2f}%"})
rows.sort(key=lambda r: -r["share"])
order = [r["rule"] for r in rows]

f = fonts(WIDTH)
base = alt.Chart(alt.Data(values=rows)).encode(y=alt.Y("rule:N", sort=order, title=None))
bars = base.mark_bar(cornerRadiusTopRight=3, cornerRadiusBottomRight=3,
                     stroke=BG, strokeWidth=1).encode(
    x=alt.X("share:Q", title="Share of Training Proofs Using the Rule (%)",
            scale=alt.Scale(domain=[0, 60])),
    color=alt.Color("kind:N", title=None,
                    scale=alt.Scale(domain=["Local", "Opens a subproof"],
                                    range=[MUTED, HUE["carbon"]]),
                    legend=alt.Legend(orient="bottom-right", direction="vertical",
                                      symbolType="square", offset=8)),
)
labels = base.mark_text(align="left", dx=6, fontSize=f["label"], color=FG).encode(
    x="share:Q", text="txt:N")
chart = (bars + labels).properties(
    width=WIDTH, height=ROW_H * len(rows),
    title=alt.TitleParams(text="The Rules That Open a Subproof Are the Rare Ones"),
).configure_axisY(domain=False, ticks=False)
save(chart, "rule-use", WIDTH)
