"""Is the colour after stir k readable at stir k's ingredient token? Median J-lens rank among the 10 colours."""

import json

import altair as alt
import pandas as pd
from theme import MUTED, fonts, save

PANEL = 330
TOTAL = 2 * PANEL + 80  # two panels side by side plus axis chrome: size fonts for the whole image
f = fonts(TOTAL)
RANK = alt.Scale(domain=[1, 10], reverse=True, zero=False)
NAMES = {"gemma-4-31b-it": "Gemma 4 31B", "qwen3.6-27b": "Qwen 3.6 27B"}

rows = pd.DataFrame(json.load(open("charts/data/stir_states.json")))
rows["step"] = rows.apply(lambda r: f"{r.stir}/{r.stirs}", axis=1)
long = rows.melt(id_vars=["model", "step", "correct"], value_vars=["produced", "control"], var_name="series", value_name="rank")
long["series"] = long.series.map({"produced": "Colour after this stir", "control": "Other colours (control)"})
order = [f"{stir}/{stirs}" for stirs in (1, 2, 3) for stir in range(1, stirs + 1)]


def panel(model: str) -> alt.Chart:
    data = long[long.model == model]
    dots = (
        alt.Chart(data)
        .mark_circle(size=140, opacity=1)
        .encode(
            x=alt.X("step:N", sort=order, title="Stir / Total Stirs", axis=alt.Axis(labelAngle=0)),
            y=alt.Y("rank:Q", title="Rank Among 10 Colours", scale=RANK, axis=alt.Axis(values=list(range(1, 11)))),
            color=alt.Color(
                "series:N",
                title=None,
                scale=alt.Scale(domain=["Colour after this stir", "Other colours (control)"], range=["#d98a1f", MUTED]),
                legend=alt.Legend(orient="bottom", labelLimit=0),
            ),
        )
    )
    chance = alt.Chart(pd.DataFrame({"rank": [5.5]})).mark_rule(strokeDash=[4, 4], color=MUTED).encode(y=alt.Y("rank:Q", scale=RANK))
    return (chance + dots).properties(width=PANEL, height=260, title=NAMES[model])


chart = alt.hconcat(panel("gemma-4-31b-it"), panel("qwen3.6-27b")).resolve_scale(y="shared")
save(chart, "stir_states", TOTAL)
