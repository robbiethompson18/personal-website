"""Test-time loops charts.

loops-spike: long dev (329 theorems of 10+ lines) solved with 64 samples, by test-time loop count, for
looped models trained on random 1-4, 1-8 and 1-16 loops (4 RL rounds), plus the 1-4 model after 12 RL
rounds. One seed each. nd-rl looped_spike_20261006/results_table.md, "solved at k" column.

loops-gap: dev (1,108) solved with 64 samples at 2 and 8 test-time loops, three-seed means, for the kept
experiments of the autoresearch-loops loop and the untied run-198 control (590, no loops, so both
points coincide). nd-rl branch autoresearch-loops, code/experiments/current/autoresearch_loops/results/*/results.json
(metric = 8 loops, metric_diag = 2 loops).

retry-depth: of the RL targets that failed 8 tries at 1 loop, the share solved on retry at 2, 4 and 8
loops (experiment 502, pooled over seeds and rounds, about 4,100 targets per arm). Same source, 502's results.json.

Run from the post dir:  python3 charts/loops.py
"""
import csv

import altair as alt

from theme import FG, HUE, MUTED, fonts, save

# --- loops-spike -------------------------------------------------------------
WIDTH, HEIGHT = 560, 340
rows = [{**r, "loops": int(r["loops"]), "solved": int(r["solved"])} for r in csv.DictReader(open("charts/loops_spike.csv"))]
models = list(dict.fromkeys(r["model"] for r in rows))
for r in rows:
    r["more_rl"] = "12 RL Rounds" in r["model"]
color = alt.Color("model:N", title=None, sort=models,
                  scale=alt.Scale(domain=models, range=[HUE["water"], HUE["recycle"], HUE["dollar"], HUE["carbon"]]),
                  legend=alt.Legend(orient="bottom-right", offset=8, labelLimit=0))
base = alt.Chart(alt.Data(values=rows)).encode(
    x=alt.X("loops:Q", title="Test-Time Loops", scale=alt.Scale(type="log", base=2, domain=[1, 24], nice=False),
            axis=alt.Axis(values=[1, 2, 4, 8, 16, 24])),
    y=alt.Y("solved:Q", title="Long Dev Theorems Solved (of 329)", scale=alt.Scale(domain=[60, 125])),
    color=color,
)
line = base.mark_line(strokeWidth=2.5).encode(strokeDash=alt.StrokeDash("more_rl:N", legend=None,
                                                                         scale=alt.Scale(domain=[False, True], range=[[1, 0], [6, 4]])))
chart = (line + base.mark_point(filled=True, size=50)).properties(
    width=WIDTH, height=HEIGHT, title="Long Dev Solved by Test-Time Loops")
save(chart, "loops-spike", WIDTH)

# --- loops-gap ---------------------------------------------------------------
WIDTH, HEIGHT = 560, 300
rows = [{**r, "loops2": int(r["loops2"]), "loops8": int(r["loops8"])} for r in csv.DictReader(open("charts/loops_gap.csv"))]
order = [r["label"] for r in rows]
points = [{"label": r["label"], "loops": f"{n} Loops", "solved": r[f"loops{n}"]} for r in rows for n in (2, 8)]
y = alt.Y("label:N", title=None, sort=order, axis=alt.Axis(labelLimit=0))
rule = alt.Chart(alt.Data(values=rows)).mark_rule(color=MUTED, strokeWidth=2).encode(
    y=y, x=alt.X("loops2:Q", title="Dev Theorems Solved (of 1,108)", scale=alt.Scale(domain=[640, 800])), x2="loops8:Q")
dots = alt.Chart(alt.Data(values=points)).mark_point(filled=True, size=110, opacity=1).encode(
    y=y, x="solved:Q",
    color=alt.Color("loops:N", title=None, scale=alt.Scale(domain=["2 Loops", "8 Loops"], range=[MUTED, HUE["water"]]),
                    legend=alt.Legend(orient="top", direction="horizontal")))
chart = (rule + dots).properties(width=WIDTH, height=HEIGHT, title="Dev Solved at 2 vs 8 Test-Time Loops")
save(chart, "loops-gap", WIDTH)

# --- retry-depth -------------------------------------------------------------
WIDTH, HEIGHT = 450, 280
rows = [{"loops": f"{r['loops']} Loops", "cracked": float(r["cracked"])} for r in csv.DictReader(open("charts/retry_depth.csv"))]
base = alt.Chart(alt.Data(values=rows)).encode(
    x=alt.X("loops:N", title="Loops on Retry", sort=None, axis=alt.Axis(labelAngle=0)),
    y=alt.Y("cracked:Q", title="Share of Failed Targets Solved", scale=alt.Scale(domain=[0, 0.2]), axis=alt.Axis(format="%")),
)
bars = base.mark_bar(color=HUE["water"], size=60)
text = base.mark_text(dy=-8, color=FG, fontSize=fonts(WIDTH)["label"]).encode(text=alt.Text("cracked:Q", format=".1%"))
chart = (bars + text).properties(width=WIDTH, height=HEIGHT, title="Retrying Targets That Failed at 1 Loop")
save(chart, "retry-depth", WIDTH)
