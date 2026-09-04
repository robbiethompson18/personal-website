"""Why the verifier rejected the model's attempts on the 7-16 line pools.

3,722 attempts, 3,554 of them rejected. One failure dominates: `bad line cite`, which is specific
to the content-addressed citation format — the model writes a witness formula that is not actually
in scope, the decoder cannot resolve it to a line, and it fills the citation with the line's own
index, which the verifier refuses. So most failures are the model naming a premise it does not have,
not the model breaking a rule.

Run from the post dir:  python3 charts/error_breakdown.py
"""
import csv
from collections import defaultdict

import altair as alt

from theme import BG, FG, HUE, fonts, save

WIDTH, ROW_H = 500, 30
POS = {"nope": "NoPE", "rope": "RoPE"}
COLOR = {"NoPE": HUE["water"], "RoPE": HUE["carbon"]}

counts = defaultdict(int)
with open("charts/error_breakdown.csv") as fh:
    for r in csv.DictReader(fh):
        counts[(r["reason"], POS[r["pos"]])] += int(r["count"])
totals = defaultdict(int)
for (reason, _), c in counts.items():
    totals[reason] += c
order = sorted(totals, key=lambda r: -totals[r])
rows = [{"reason": reason, "model": m, "count": c} for (reason, m), c in counts.items()]

f = fonts(WIDTH)
chart = alt.Chart(alt.Data(values=rows)).mark_bar(
    cornerRadiusTopRight=2, cornerRadiusBottomRight=2, stroke=BG, strokeWidth=0.5).encode(
    y=alt.Y("reason:N", sort=order, title=None, axis=alt.Axis(labelLimit=220)),
    yOffset=alt.YOffset("model:N", sort=list(COLOR)),
    x=alt.X("count:Q", title="Rejected Attempts (of 1,861 per Model)"),
    color=alt.Color("model:N", title=None,
                    scale=alt.Scale(domain=list(COLOR), range=list(COLOR.values())),
                    legend=alt.Legend(orient="bottom-right", direction="vertical",
                                      symbolType="square", offset=8)),
).properties(
    width=WIDTH, height=ROW_H * len(order),
    title=alt.TitleParams(
        text="Failures Past the Cap Are Almost All Bad Citations",
        subtitle="`bad line cite` = the model named a formula that is not in scope to cite."),
).configure_axisY(domain=False, ticks=False)
save(chart, "error-breakdown", WIDTH)
