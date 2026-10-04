"""Two-stir brew accuracy per open-weights model, no chain of thought (OpenRouter, 20 items each)."""

import json

import altair as alt
import pandas as pd
from theme import FG, MUTED, fonts, save

WIDTH = 450
f = fonts(WIDTH)

rows = pd.DataFrame(json.load(open("charts/data/brew_accuracy.json")))
rows = rows[rows.stirs == 2].assign(percent=lambda d: 100 * d.correct / d.n, gemma=lambda d: d.model == "gemma-4-31b-it")

base = alt.Chart(rows).encode(
    y=alt.Y("model:N", sort="-x", title=None),
    x=alt.X("percent:Q", title="Two-Stir Items Correct (%)", scale=alt.Scale(domain=[0, 100])),
)
bars = base.mark_bar().encode(color=alt.condition("datum.gemma", alt.value("#d98a1f"), alt.value(MUTED)))
labels = base.mark_text(align="left", dx=4, fontSize=f["label"], color=FG).encode(text=alt.Text("percent:Q", format=".0f"))
save((bars + labels).properties(width=WIDTH, height=200, title="Brew, Two Stirs, No Chain of Thought"), "brew_accuracy", WIDTH)
