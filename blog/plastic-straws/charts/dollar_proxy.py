"""Three log-log scatters for the "dollars as a proxy for externalities" section.

All three go through ONE code path (scatter() below), styled like the headline
chart: colored points, an OLS trend line, an r/slope subtitle, and a hand-placed
text label on EVERY point (Altair has no auto label de-clutter, so each label's
offset is picked by hand via a `place` key — see PLACE).

  dollar_vs_carbon      — 15 everyday purchases, $ vs carbon, colored by category.
  dollar_vs_food_water  — 21 groceries, $/lb vs water/lb, colored by food group.
  dollar_vs_food_land   — 21 groceries, $/lb vs land/lb,  colored by food group.

NUMBERS: carbon & land per-kg = Poore & Nemecek 2018 (OWID); water per-kg =
Mekonnen & Hoekstra total water footprints; prices = US consumer, ~1 sig fig.
GWP20 basis: carbon_gwp20 = carbon_gwp100 * (1 + 2*f), f = methane share
(only ruminants + rice carry meaningful f). Approximate by design.
"""
import numpy as np
import altair as alt

from theme import CAT, FG, fonts, save

# --- GWP20 methane rescale + log-log OLS ------------------------------------
F_CH4 = {
    # per-item labels (FIG 1)
    "bowl of rice": 0.55, "1 lb beef (a steak)": 0.49,
    # per-lb food names (ruminants + rice carry the methane rescale)
    "rice": 0.55, "beef": 0.49, "lamb": 0.50, "milk": 0.45,
    "cheese": 0.40, "pork": 0.13, "chicken": 0.06, "eggs": 0.06,
}


def gwp20(name, carbon100):
    return carbon100 * (1 + 2 * F_CH4.get(name, 0.0))


def ols_loglog(x, y):
    lx, ly = np.log10(x), np.log10(y)
    m, b = np.polyfit(lx, ly, 1)
    r2 = 1 - np.sum((ly - (m * lx + b)) ** 2) / np.sum((ly - ly.mean()) ** 2)
    return float(m), float(b), float(r2)


def fit_line(x, y, lo_mult, hi_mult):
    m, b, r2 = ols_loglog(x, y)
    x0, x1 = float(x.min() * lo_mult), float(x.max() * hi_mult)
    pts = [{"x": x0, "y": float(10 ** (m * np.log10(x0) + b))},
           {"x": x1, "y": float(10 ** (m * np.log10(x1) + b))}]
    return pts, m, r2


# --- the one shared scatter -------------------------------------------------
# Per-point label placement. Vega-Lite can't vary a text mark's dx/dy by
# encoding, so we emit one text layer per distinct placement key (cheap: a
# handful of offsets cover all points). Keys: r/l = right/left of the point;
# a/b (alone) = above/below; the a/b *suffix* on r/l nudges up/down to dodge a
# neighbor.
PLACE = {
    "r":  ("left",    9,   0, "middle"),   # right of point
    "l":  ("right",  -9,   0, "middle"),   # left of point
    "ra": ("left",    9, -11, "middle"),   # right + raised
    "rb": ("left",    9,  12, "middle"),   # right + lowered
    "la": ("right",  -9, -12, "middle"),   # left + raised
    "lb": ("right",  -9,  12, "middle"),   # left + lowered
    "a":  ("center",  0, -10, "bottom"),   # above
    "b":  ("center",  0,  11, "top"),      # below
}
# Broad decade gridlines; Vega clips each list to the chart's own domain.
DECADES = [1e-3, 1e-2, 1e-1, 1, 10, 100, 1000, 1e4]


def scatter(rows, *, title, xtitle, ytitle, palette, color_field, legend_title,
            x_domain, y_domain, fname, lo_mult, hi_mult, width=720, height=560):
    """One log-log $-vs-externality scatter. Each row is
    {name, x, y, <color_field>, place}. Draws the OLS trend, the colored points,
    and a hand-placed label on every point; titles carry the r / slope. All three
    of the section's scatters call this, so they render identically-sized and
    identically-styled. Returns (r, slope)."""
    x = np.array([r["x"] for r in rows])
    y = np.array([r["y"] for r in rows])
    line, m, r2 = fit_line(x, y, lo_mult, hi_mult)
    f = fonts(width)

    color = alt.Color(f"{color_field}:N",
                      scale=alt.Scale(domain=list(palette), range=list(palette.values())),
                      legend=alt.Legend(title=legend_title))
    base = alt.Chart(alt.Data(values=rows))
    ex = alt.X("x:Q", scale=alt.Scale(type="log", domain=x_domain),
               axis=alt.Axis(format="$~r", grid=True, values=DECADES), title=xtitle)
    ey = alt.Y("y:Q", scale=alt.Scale(type="log", domain=y_domain),
               axis=alt.Axis(format="~r", grid=True, values=DECADES), title=ytitle)
    pts = base.mark_circle(size=190, opacity=0.85, stroke="white", strokeWidth=1).encode(
        ex, ey, color=color)
    labels = [
        alt.Chart(alt.Data(values=[r for r in rows if r["place"] == key])).mark_text(
            align=align, dx=dx, dy=dy, baseline=baseline,
            fontSize=f["label"], color=FG).encode(ex, ey, text="name:N")
        for key, (align, dx, dy, baseline) in PLACE.items()
        if any(r["place"] == key for r in rows)
    ]
    trend = alt.Chart(alt.Data(values=line)).mark_line(
        strokeDash=[6, 4], color="#888", strokeWidth=1.5).encode(x="x:Q", y="y:Q")
    chart = alt.layer(trend, pts, *labels).properties(
        width=width, height=height,
        # autosize=fit -> width/height are the TOTAL image (chrome shrinks the
        # plot to fit), so all three scatters end up the same on-screen height.
        autosize=alt.AutoSizeParams(type="fit", contains="padding"),
        title=alt.TitleParams(text=title,
                              subtitle=[f"r = {r2**0.5:.2f}  ·  log-log OLS slope {m:.2f}"]))
    save(chart, fname, width)
    return r2 ** 0.5, m


# ---------------------------------------------------------------- CARBON
# name: ($ price, carbon kg CO2e GWP100, category, place-key).
broad = {
    "1 LED bulb-day":         (0.035,  0.081,   "energy",  "ra"),
    "1 Tesla-mile":           (0.05,   0.093,   "energy",  "rb"),
    "bowl of rice":           (0.15,   0.225,   "food",    "l"),
    "oz of almonds":          (0.30,   0.012,   "food",    "r"),
    "cup of coffee":          (0.30,   0.20,    "food",    "l"),
    "10-min hot shower":      (0.50,   0.82,    "energy",  "r"),
    "chocolate bar":          (2.0,    1.87,    "food",    "r"),
    "rubber ducky":           (3.0,    0.30,    "goods",   "r"),
    "gallon of gas (burned)": (3.5,    8.9,     "energy",  "l"),
    "1 lb beef (a steak)":    (10.0,   27.0,    "food",    "l"),
    "cotton t-shirt":         (15.0,   4.0,     "goods",   "l"),
    "new iPhone":             (800.0,  65.0,    "goods",   "l"),
    "month heavy AI coding":  (200.0,  11.0,    "digital", "la"),
    "SF→NYC flight (1-way)": (200.0,  500.0,   "travel",  "l"),
    "MacBook Air":            (1100.0, 135.0,   "goods",   "l"),
}
carbon_rows = [{"name": n, "x": x, "y": gwp20(n, y0), "cat": cat, "place": place}
               for n, (x, y0, cat, place) in broad.items()]
scatter(carbon_rows,
        title="Dollar Cost vs Carbon Footprint: Log-Log",
        xtitle="What You Pay  (US$, log)",
        ytitle="Carbon Footprint  (kg CO₂e GWP20, log)",
        palette=CAT, color_field="cat", legend_title="category",
        x_domain=[1e-2, 3e3], y_domain=[5e-3, 2e3],
        fname="dollar_vs_carbon", lo_mult=0.5, hi_mult=2.0)

# ---------------------------------------------------------------- FOOD (water, land)
# Six well-separated hues (staple/produce/plant/indulge/dairy/meat).
G = {"staple": "#d9a441", "produce": "#6aa84f", "plant": "#3aa6a0",
     "indulge": "#7a5fb0", "dairy": "#2e7dc1", "meat": "#c1432e"}
LB = 0.453592  # kg per pound
# name: ($ portion price, portion_kg, carbon/kg, water L/kg, land m2/kg, group).
# Everything is normalized to ONE POUND so the groceries compare apples-to-apples.
foods = {
    "potato":        (0.30, 0.170, 0.46,  287,   0.9,  "staple"),
    "rice":          (0.15, 0.050, 4.5,   2497,  2.8,  "staple"),
    "bread":         (0.30, 0.060, 1.6,   1608,  2.7,  "staple"),
    "lettuce":       (0.50, 0.085, 0.5,   237,   0.4,  "produce"),
    "banana":        (0.25, 0.120, 0.86,  790,   1.9,  "produce"),
    "apple":         (0.50, 0.150, 0.43,  822,   0.63, "produce"),
    "tomato":        (0.50, 0.120, 1.4,   214,   0.8,  "produce"),
    "avocado":       (1.50, 0.150, 2.5,   2000,  2.0,  "produce"),
    "tofu":          (0.50, 0.100, 3.2,   2000,  2.2,  "plant"),
    "peanut butter": (0.20, 0.030, 2.5,   2782,  3.0,  "plant"),
    "almonds":       (0.30, 0.028, 0.43,  16000, 13.0, "plant"),
    "olive oil":     (0.25, 0.014, 6.0,   14400, 26.0, "plant"),
    "coffee":        (0.30, 0.007, 28.5,  18900, 21.0, "indulge"),
    "chocolate":     (2.00, 0.040, 46.7,  17200, 70.0, "indulge"),
    "milk":          (0.30, 0.240, 3.2,   1020,  8.9,  "dairy"),
    "eggs":          (0.50, 0.100, 4.7,   3265,  6.3,  "dairy"),
    "cheese":        (0.50, 0.030, 23.9,  5060,  87.8, "dairy"),
    "chicken":       (1.50, 0.170, 9.9,   4325,  12.2, "meat"),
    "pork":          (1.75, 0.140, 12.3,  5988,  17.4, "meat"),
    "lamb":          (4.00, 0.140, 39.7,  10412, 369.0,"meat"),
    "beef":          (10.0, 0.454, 60.0,  15000, 326.0,"meat"),
}


def price_per_lb(n):
    return foods[n][0] / foods[n][1] * LB


# Per-point label placement, hand-tuned separately for each metric's y-spread.
PLACE_FOOD = {
    "water": {
        "milk": "l", "potato": "b", "banana": "a", "rice": "l", "apple": "r",
        "tomato": "b", "bread": "l", "tofu": "r", "eggs": "a", "lettuce": "r",
        "peanut butter": "r", "chicken": "r", "avocado": "b", "almonds": "a",
        "pork": "a", "cheese": "r", "olive oil": "a", "beef": "r", "lamb": "r",
        "coffee": "a", "chocolate": "r",
    },
    "land": {
        "milk": "l", "potato": "l", "banana": "b", "rice": "l", "apple": "b",
        "tomato": "r", "bread": "a", "tofu": "b", "eggs": "a", "lettuce": "b",
        "peanut butter": "r", "chicken": "a", "avocado": "b", "almonds": "r",
        "pork": "a", "cheese": "l", "olive oil": "a", "beef": "l", "lamb": "r",
        "coffee": "b", "chocolate": "r",
    },
}
# metric: (foods-tuple index, title, y-axis title, filename, y-domain).
FOOD_META = [
    ("water", 3, "Dollar Cost vs Water Use: Log-Log",
     "Water per Pound  (Litres, log)", "dollar_vs_food_water", [70, 1.2e4]),
    ("land", 4, "Dollar Cost vs Land Use: Log-Log",
     "Land per Pound  (m², log)", "dollar_vs_food_land", [0.15, 500]),
]
for metric, idx, title, ytitle, fname, y_domain in FOOD_META:
    rows = [{"name": n, "x": price_per_lb(n), "y": foods[n][idx] * LB,
             "grp": foods[n][5], "place": PLACE_FOOD[metric][n]} for n in foods]
    scatter(rows, title=title, xtitle="Price per Pound  (US$, log)", ytitle=ytitle,
            palette=G, color_field="grp", legend_title="food group",
            x_domain=[0.4, 40], y_domain=y_domain, fname=fname,
            lo_mult=0.7, hi_mult=1.4)

print("wrote dollar_vs_carbon.*, dollar_vs_food_water.*, dollar_vs_food_land.*")
