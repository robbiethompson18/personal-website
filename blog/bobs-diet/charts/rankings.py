"""Horizontal log-scale bar charts for Bob's Diet rankings (Altair).

Two views of the same sheet
(docs.google.com/spreadsheets/d/1rI7JUUkDsFYI6SeeXpwu7DmEE8A8e12i8fNWkH2QNwo):

  1. suffering  = neurons * lifespan / calories  — only farmed animals (NA
     lifespan drops out). This is the post's main metric.
  2. neurons/cal = neurons / calories            — every animal + Human, the
     "if killing is the only evil" metric.

Values are copied verbatim from the sheet's computed columns (~1 sig fig). Both
metrics span ~4 orders of magnitude, so the value axis is log-scaled; each bar
is labelled with its value so tiny differences stay readable. Dark theme via
theme.save(). Run from posts/bobs-diet/:  python3 charts/rankings.py
"""
import altair as alt

from theme import HUE, FG, fonts, save


def si(v):
    """1-ish-sig-fig SI label: 600 / 5.5k / 91k / 1.2M."""
    if v >= 1e6:
        return f"{v / 1e6:.1f}M"
    if v >= 1e3:
        x = v / 1e3
        return f"{x:.0f}k" if x >= 10 else f"{x:.1f}k"
    return f"{v:.0f}"


def hbar(rows, unit, title, name, hue, domain):
    """rows: list of (animal, value); domain: [lo, hi] for the log x-axis."""
    # log-scale bars have no natural zero baseline, so give every bar an
    # explicit left edge at the domain floor via x2. Bar length then reads as
    # log(v / floor); the value label carries the exact number.
    data = [{"item": a, "v": float(v), "base": domain[0], "label": si(v)}
            for a, v in rows]
    order = [a for a, _ in sorted(rows, key=lambda r: r[1])]  # smallest at top
    n = len(data)
    width = 560
    height = 22 * n
    f = fonts(width)

    base = alt.Chart(alt.Data(values=data)).encode(
        y=alt.Y("item:N", sort=order, title=None,
                axis=alt.Axis(labelLimit=200)))
    bar = base.mark_bar(color=HUE[hue], opacity=0.9).encode(
        x=alt.X("v:Q", title=unit,
                scale=alt.Scale(type="log", domain=domain, nice=False),
                axis=alt.Axis(format="~s")),
        x2="base:Q")
    labels = base.mark_text(align="left", dx=4, fontSize=f["label"],
                            color=FG).encode(x="v:Q", text="label:N")

    chart = (bar + labels).properties(
        width=width, height=height, title=title)
    save(chart, name, width)


# 1. Suffering = neurons x lifespan / calories. Farmed animals only (animals
#    with NA lifespan compute to #VALUE! in the sheet and are excluded, per the
#    post). Human is not farmed, so it's excluded too.
#    Salmon overrides the sheet: 5000 cal (post's 5/17 update, not 2400) and
#    4e7 neurons (geometric midpoint of the ~1e7–1.3e8 estimate range, not the
#    sheet's high-end 1.3e8). 4e7 x 2.25 / 5000 = 18,000 (was 122k).
hbar([
    ("Scallop", 600), ("Oyster", 1250), ("Clam", 1430), ("Mussel", 1500),
    ("Snail", 2120), ("Prawn", 4000), ("Cow Milk", 5480), ("Shrimp", 5710),
    ("Chicken Eggs", 12700), ("Chicken", 16700), ("Salmon", 18000),
    ("Turkey", 26500), ("Pig", 28000), ("Horsefly", 33300), ("Cow", 78900),
], "neurons × lifespan / calorie  (log)", "Suffering per Calorie",
   "rankings-suffering", "carbon", domain=[200, 400000])

# 2. Neurons / calorie — every animal, including Human.
hbar([
    ("Scallop", 400), ("Lobster", 606), ("Clam", 714), ("Oyster", 833),
    ("Cow Milk", 913), ("Mussel", 1000), ("Crab", 1430), ("Snail", 3530),
    ("Chicken Eggs", 6350), ("Salmon", 8000), ("Prawn", 10000),
    ("Shrimp", 14300), ("Cow", 52600), ("Pig", 55900), ("Turkey", 75800),
    ("Tuna", 90900), ("Chicken", 111000), ("Mullet", 167000),
    ("Sea urchin", 167000), ("Horsefly", 333000), ("Cricket", 500000),
    ("Octopus", 625000), ("Human", 688000), ("Anchovy", 1000000),
    ("Squid", 1200000),
], "neurons / calorie  (log)", "Neurons per Calorie",
   "rankings-neurons-per-calorie", "dollar", domain=[200, 4000000])

print("done — 2 log bar charts (Altair)")
