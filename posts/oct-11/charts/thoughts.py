"""Continuous-thoughts charts.

thoughts-prerl: before RL, sample accuracy on the 7-14 line RL targets (8 samples per target) by thoughts
per proof line, three-seed means of experiment 700's pretrained models. nd-rl branch autoresearch-thoughts,
code/experiments/current/autoresearch_thoughts/results/700-manual_baseline/results.json ("surprise").

thoughts-recipes: dev (1,108) solved with 64 samples at 8 thoughts per line, three-seed means, for the
feedback recipe (701), pause slots (704) and the loop's best (708), against the untied run-198 control
with the same harness (590, no thoughts). Same source, results/*/results.json; pretraining steps from
seed_pretrain, RL rounds from each surprise.

Run from the post dir:  python3 charts/thoughts.py
"""
import csv

import altair as alt

from theme import BG, FG, HUE, MUTED, fonts, save

# --- thoughts-prerl ----------------------------------------------------------
WIDTH, HEIGHT = 450, 280
rows = [{"thoughts": r["thoughts"], "acc": float(r["acc"])} for r in csv.DictReader(open("charts/thoughts_prerl.csv"))]
base = alt.Chart(alt.Data(values=rows)).encode(
    x=alt.X("thoughts:N", title="Thoughts per Proof Line", sort=None, axis=alt.Axis(labelAngle=0)),
    y=alt.Y("acc:Q", title="Valid Samples on RL Targets", scale=alt.Scale(domain=[0, 0.14]), axis=alt.Axis(format="%")),
)
bars = base.mark_bar(color=HUE["dollar"], size=60)
text = base.mark_text(dy=-8, color=FG, fontSize=fonts(WIDTH)["label"]).encode(text=alt.Text("acc:Q", format=".1%"))
chart = (bars + text).properties(width=WIDTH, height=HEIGHT, title="Before RL: Valid Samples by Thoughts")
save(chart, "thoughts-prerl", WIDTH)

# --- thoughts-recipes --------------------------------------------------------
WIDTH, HEIGHT = 560, 240
rows = [{**r, "solved": int(r["solved"]), "control": r["label"].startswith("Untied")}
        for r in csv.DictReader(open("charts/thoughts_recipes.csv"))]
f = fonts(WIDTH)
y = alt.Y("label:N", title=None, sort=None, axis=alt.Axis(labelLimit=0))
base = alt.Chart(alt.Data(values=rows)).encode(y=y)
bars = base.mark_bar(size=34).encode(
    x=alt.X("solved:Q", title="Dev Theorems Solved (of 1,108)", scale=alt.Scale(domain=[0, 800])),
    color=alt.Color("control:N", legend=None, scale=alt.Scale(domain=[False, True], range=[HUE["dollar"], MUTED])))
value = base.mark_text(align="left", dx=6, color=FG, fontSize=f["label"]).encode(x="solved:Q", text="solved:Q")
note = base.mark_text(align="left", dx=8, color=BG, fontSize=f["label"]).encode(x=alt.datum(0), text="note:N")
chart = (bars + value + note).properties(width=WIDTH, height=HEIGHT, title="After RL: Thoughts Models vs the Untied Control")
save(chart, "thoughts-recipes", WIDTH)
