"""Proof length (body lines: proof lines after the premise block) of Dan's old training data vs
Robbie's new long-proofs set, on the same x axis so the difference in reach shows.

- dan: Dan's cap-6 pretraining file (154,990) plus cap-horizon train_k12 (155,000); written lengths.
- new: nd-rl long_proofs_20261013, selected as long_rl_20261014/make_data.py does (body >= 7, plus
  a 3+-premise bridge below 7), before its group-overlap drop and Lean gate. Exact minimal length
  where known, else the written length of a proof certified to need >= 20.

Data: proof_lengths.csv. Run from the post dir:  python3 charts/proof_lengths.py
"""
import csv

import altair as alt

from theme import HUE, save

WIDTH, HEIGHT = 560, 200

rows = [{"dataset": r["dataset"], "body": int(r["body"]), "count": int(r["count"])}
        for r in csv.DictReader(open("charts/proof_lengths.csv"))]


def hist(dataset, name, title, color):
    data = [r for r in rows if r["dataset"] == dataset]
    chart = alt.Chart(alt.Data(values=data)).mark_bar(color=color, width=4).encode(
        x=alt.X("body:Q", title="Proof Length (Body Lines)", scale=alt.Scale(domain=[0, 80])),
        y=alt.Y("count:Q", title="Proofs", axis=alt.Axis(format="~s")),
    ).properties(width=WIDTH, height=HEIGHT, title=title)
    save(chart, name, WIDTH)


hist("dan", "lengths-dan", "Dan's Proofs by Length", HUE["water"])
hist("new", "lengths-new", "New Proofs by Length", HUE["recycle"])
