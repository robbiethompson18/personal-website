"""Retry-EI charts (retrying with Lean errors in context). Base recipe: run 590 (untied run 198 with the
autoresearch-loops RL recipe), three seeds per arm. nd-rl branch robbie-experiments,
experiment-summaries/2026-10-08-retry-ei/README.md (tables) and code/experiments/current/retry_ei_20261008/.

retry-arms: dev (1,108) solved with 64 independent samples, per seed and mean, per arm.
retry-repeat: share of second attempts token-identical to the first (after renumbering names), against
the share of two independent failed samples that are identical. Three-seed means, from diversity.py on
the rerun retry/blank arms.
retry-distinct: distinct proofs among 8 attempts of one episode vs among 8 independent samples.

Run from the post dir:  python3 charts/retry.py
"""
import csv

import altair as alt

from theme import FG, HUE, MUTED, fonts, save

# --- retry-arms --------------------------------------------------------------
WIDTH, HEIGHT = 560, 260
arms = list(csv.DictReader(open("charts/retry_arms.csv")))
order = [a["arm"] for a in arms]
seeds = [{"arm": a["arm"], "solved": int(a[f"s{s}"])} for a in arms for s in range(3)]
means = [{"arm": a["arm"], "mean": round(sum(int(a[f"s{s}"]) for s in range(3)) / 3)} for a in arms]
y = alt.Y("arm:N", title=None, sort=order)
x = alt.X("solved:Q", title="Dev Theorems Solved (of 1,108)", scale=alt.Scale(domain=[650, 800]))
dots = alt.Chart(alt.Data(values=seeds)).mark_point(filled=True, size=60, color=MUTED, opacity=0.9).encode(y=y, x=x)
mean = alt.Chart(alt.Data(values=means)).encode(y=y, x=alt.X("mean:Q"))
ticks = mean.mark_tick(color=HUE["carbon"], thickness=3, size=26)
text = mean.mark_text(dy=-17, color=FG, fontSize=fonts(WIDTH)["label"]).encode(text="mean:Q")
chart = (dots + ticks + text).properties(width=WIDTH, height=HEIGHT,
                                         title="Dev Solved by Arm (Dots: Seeds, Bar: Mean)")
save(chart, "retry-arms", WIDTH)


def paired(name, title, xtitle, fmt, domain):
    """Grouped horizontal bars: with the failed attempt in context vs independent samples."""
    rows = [{"arm": r["arm"], "kind": kind, "value": float(r[col])}
            for r in csv.DictReader(open(f"charts/{name.replace('-', '_')}.csv"))
            for col, kind in (("in_episode", "Failed Attempt in Context"), ("independent", "Independent Samples"))]
    kinds = ["Failed Attempt in Context", "Independent Samples"]
    base = alt.Chart(alt.Data(values=rows)).encode(
        y=alt.Y("arm:N", title=None, sort=None), yOffset=alt.YOffset("kind:N", sort=kinds))
    bars = base.mark_bar(size=16).encode(
        x=alt.X("value:Q", title=xtitle, scale=alt.Scale(domain=domain), axis=alt.Axis(format=fmt)),
        color=alt.Color("kind:N", title=None, sort=kinds, scale=alt.Scale(domain=kinds, range=[HUE["carbon"], MUTED]),
                        legend=alt.Legend(orient="top", direction="horizontal", labelLimit=0)))
    text = base.mark_text(align="left", dx=5, color=FG, fontSize=fonts(WIDTH)["label"]).encode(
        x="value:Q", text=alt.Text("value:Q", format=fmt))
    save((bars + text).properties(width=WIDTH, height=280, title=title), name, WIDTH)


paired("retry-repeat", "Second Attempt Identical to the First", "Share Identical", ".0%", [0, 0.85])
paired("retry-distinct", "Distinct Proofs in 8 Attempts", "Distinct Proofs", ".1f", [0, 7])
