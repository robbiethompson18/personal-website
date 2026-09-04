"""Training and held-out loss per step, both positional schemes.

Log y-axis: loss falls from ~1.0 to ~0.002, so a linear axis would show a cliff and then a flat
line. Solid = held-out, dashed = train. Writes loss-curves.

Caveat carried in the subtitle: in these two runs the held-out loss was measured on the first 1024
records of the held-out file, which is ordered by length, so it covers lengths 2-4 only. That is
why it sits below the train loss. Fixed after these runs (train.py now strides the subsample).

Run from the post dir:  python3 charts/loss_curves.py
"""
import csv

import altair as alt

from theme import HUE, fonts, save

WIDTH, HEIGHT = 560, 300
POS = {"nope": "NoPE", "rope": "RoPE"}
COLOR = {"NoPE": HUE["water"], "RoPE": HUE["carbon"]}

rows = []
with open("charts/loss_curves.csv") as fh:
    for r in csv.DictReader(fh):
        for key, split in (("train_loss", "Train"), ("val_loss", "Held-out")):
            rows.append({"epoch": float(r["epoch"]), "loss": float(r[key]),
                         "model": POS[r["pos"]], "split": split,
                         "series": f"{POS[r['pos']]} {split}"})

f = fonts(WIDTH)
chart = alt.Chart(alt.Data(values=rows)).mark_line(strokeWidth=1.8).encode(
    x=alt.X("epoch:Q", title="Epochs Over the Training Set", axis=alt.Axis(tickCount=8)),
    y=alt.Y("loss:Q", title="Cross-Entropy Loss (Proof Body Tokens)",
            scale=alt.Scale(type="log")),
    color=alt.Color("model:N", title=None,
                    scale=alt.Scale(domain=list(COLOR), range=list(COLOR.values())),
                    legend=alt.Legend(orient="top-right", direction="vertical", offset=4)),
    strokeDash=alt.StrokeDash("split:N", title=None,
                              scale=alt.Scale(domain=["Held-out", "Train"], range=[[1, 0], [4, 3]]),
                              legend=alt.Legend(orient="top-right", direction="vertical", offset=4)),
    detail="series:N",
).properties(
    width=WIDTH, height=HEIGHT,
    title=alt.TitleParams(
        text="Training and Held-Out Loss",
        subtitle="Held-out loss here covers lengths 2-4 only (subsample bug, fixed after these runs)."),
)
save(chart, "loss-curves", WIDTH)
