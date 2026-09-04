"""Why the solve-rate curve is non-zero out at 14 lines: the labels are wrong, not the model.

Every solved target in the 7-16 line pools, plotted as the length it was *generated* with against
the length the model actually *wrote*. The dashed diagonal is where a solve would have to sit for
the label to mean what it looks like it means. Nothing sits near it past 8 — the model wrote 5-7
lines for every theorem labelled 11 or more, because those theorems have short proofs that the
generator's padded derivation missed.

Run from the post dir:  python3 charts/label_inflation.py
"""
import csv

import altair as alt

from theme import FG, HUE, MUTED, fonts, save

WIDTH, HEIGHT = 560, 300

rows = []
with open("charts/solved_lengths.csv") as fh:
    for r in csv.DictReader(fh):
        rows.append({"gen": int(r["gen_lines"]), "written": int(r["written"]),
                     "count": int(r["count"])})

f = fonts(WIDTH)
diag = alt.Chart(alt.Data(values=[{"x": 2, "y": 2}, {"x": 17, "y": 17}])).mark_line(
    color=MUTED, strokeDash=[4, 4], strokeWidth=1).encode(x="x:Q", y="y:Q")
diag_label = alt.Chart(alt.Data(values=[{"x": 10.2, "y": 11.4, "t": "wrote what the label claims"}])
                       ).mark_text(align="left", angle=360 - 34, color=MUTED,
                                   fontSize=f["label"]).encode(x="x:Q", y="y:Q", text="t:N")
pts = alt.Chart(alt.Data(values=rows)).mark_circle(color=HUE["recycle"], opacity=0.85).encode(
    x=alt.X("gen:Q", title="Length of the Generating Proof (Lines)",
            scale=alt.Scale(domain=[6, 17], nice=False), axis=alt.Axis(tickCount=6)),
    y=alt.Y("written:Q", title="Length the Model Wrote (Lines)",
            scale=alt.Scale(domain=[3, 17], nice=False), axis=alt.Axis(tickCount=5)),
    size=alt.Size("count:Q", title="Solves",
                  scale=alt.Scale(range=[30, 400]),
                  legend=alt.Legend(orient="bottom-right", offset=8, values=[1, 10, 30, 60])),
)
chart = (diag + diag_label + pts).properties(
    width=WIDTH, height=HEIGHT,
    title=alt.TitleParams(text="The Long Targets Have Short Proofs"),
)
save(chart, "label-inflation", WIDTH)
