"""Cumulative RL targets solved (of 18,439) by every GRPO run on the fixed recipe (nd-rl
long_rl_20261014, runs v3 and v4, two seeds each, 3 h RL budget). v3 seed 0 is the one that jumps;
the other three flatten near 2,500. v2's GRPO (the collapsed recipe, stopped early) is left out.

Data: grpo_solved.csv, exported from nd-rl code/experiments/current/long_rl_20261014/report/data.json.
Run from the post dir:  python3 charts/grpo_solved.py
"""
import csv

import altair as alt

from theme import HUE, MUTED, save

WIDTH, HEIGHT = 560, 300
JUMP = "v3/untied-grpo_s0"
LABEL = {JUMP: "Run with the Jump", "other": "Other Three Runs"}

rows = [{"run": r["run"], "group": LABEL[JUMP if r["run"] == JUMP else "other"],
         "clock": float(r["clock"]), "solved": int(r["solved"])}
        for r in csv.DictReader(open("charts/grpo_solved.csv")) if not r["run"].startswith("v2/")]

chart = alt.Chart(alt.Data(values=rows)).mark_line(strokeWidth=2).encode(
    x=alt.X("clock:Q", title="RL Time (Hours)", scale=alt.Scale(domain=[0, 3]),
            axis=alt.Axis(values=[0, 0.5, 1, 1.5, 2, 2.5, 3])),
    y=alt.Y("solved:Q", title="RL Targets Solved", axis=alt.Axis(format=",.0f")),
    color=alt.Color("group:N", title=None, scale=alt.Scale(domain=list(LABEL.values()), range=[HUE["carbon"], MUTED]),
                    legend=alt.Legend(orient="top-left", offset=8)),
    detail="run:N",
).properties(width=WIDTH, height=HEIGHT, title="RL Targets Solved, GRPO")
save(chart, "grpo-solved", WIDTH)
