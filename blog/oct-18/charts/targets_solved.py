"""Cumulative RL targets solved (of 18,439) by one expert-iteration run: nd-rl long_rl_20261014,
untied-ei seed 1, run v2 (0-3 h) resumed as v5 (3-7 h). The x axis is RL GPU time, Lean-gate time
excluded.

Data: targets_solved.csv, exported from nd-rl code/experiments/current/long_rl_20261014/report/data.json.
Run from the post dir:  python3 charts/targets_solved.py
"""
import csv

import altair as alt

from theme import HUE, save

WIDTH, HEIGHT = 560, 300

rows = [{"clock": float(r["clock"]), "solved": int(r["solved"])} for r in csv.DictReader(open("charts/targets_solved.csv"))]

chart = alt.Chart(alt.Data(values=rows)).mark_line(strokeWidth=2.5, color=HUE["water"]).encode(
    x=alt.X("clock:Q", title="RL Time (Hours)", scale=alt.Scale(domain=[0, 7]), axis=alt.Axis(values=list(range(8)))),
    y=alt.Y("solved:Q", title="RL Targets Solved", scale=alt.Scale(domain=[0, 18439], nice=False),
            axis=alt.Axis(values=[0, 5000, 10000, 15000, 18439], format=",.0f")),
).properties(width=WIDTH, height=HEIGHT, title="RL Targets Solved, One Expert-Iteration Run")
save(chart, "targets-solved", WIDTH)
