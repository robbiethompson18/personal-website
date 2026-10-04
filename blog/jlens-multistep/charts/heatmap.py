"""Gemma 4 31B on the two-stir brew items it gets right: median J-lens rank of each colour, by layer and token."""

import json

import altair as alt
import pandas as pd
from theme import BG, fonts, save

WIDTH = 700
f = fonts(WIDTH)

data = json.load(open("charts/data/heatmap_mean.json"))
titles = {"start": "Start Colour", "after stir 1": "Colour After Stir 1", "answer": "Colour After Stir 2 (the Answer)"}
cells = pd.DataFrame(
    [
        {"role": role, "layer": layer, "token": f"{position:02d}|{token or '⏎'}", "rank": ranks[position]}
        for role, by_layer in data["rank"].items()
        for layer, ranks in zip(data["layers"], by_layer)
        for position, token in enumerate(data["tokens"])
    ]
)


def panel(role: str, show_tokens: bool) -> alt.Chart:
    return (
        alt.Chart(cells[cells.role == role])
        .mark_rect()
        .encode(
            x=alt.X(
                "token:O",
                title=None,
                axis=alt.Axis(labels=show_tokens, ticks=False, labelAngle=-60, labelExpr="split(datum.label, '|')[1]"),
            ),
            y=alt.Y("layer:O", title="Layer", sort="descending", axis=alt.Axis(values=list(range(0, 60, 10)))),
            color=alt.Color(
                "rank:Q",
                title="Rank of 10",
                scale=alt.Scale(domain=[1, 5.5], range=["#f5b041", BG], interpolate="rgb", clamp=True),  # 5.5 = chance
                legend=alt.Legend(values=[1, 2, 3, 4, 5.5]) if show_tokens else None,
            ),
        )
        .properties(width=WIDTH, height=120, title=titles[role])
    )


save(alt.vconcat(*(panel(role, role == "answer") for role in titles)), "heatmap", WIDTH)
