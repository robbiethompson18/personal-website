"""Two charts for the "dollars as a proxy for externalities" section (Altair).

FIG 1  dollar_vs_carbon  — headline log-log scatter, $ price vs carbon, OLS fit.
FIG 2  dollar_vs_food_externalities — 21 groceries, three STACKED log-log panels
       ($ vs carbon / water / land), each with its own OLS fit. Vertical stack,
       each panel big — the post's "food section".

NUMBERS: carbon & land per-kg = Poore & Nemecek 2018 (OWID); water per-kg =
Mekonnen & Hoekstra total water footprints; prices = US consumer, ~1 sig fig.
GWP20 basis: carbon_gwp20 = carbon_gwp100 * (1 + 2*f), f = methane share
(only ruminants + rice carry meaningful f). Approximate by design.
"""
import numpy as np
import altair as alt

from theme import CAT, FG, fonts, save

# --- GWP20 methane rescale + log-log OLS -----------------------------------
F_CH4 = {
    # FIG 1 per-item labels
    "bowl of rice": 0.55, "1 lb beef (a steak)": 0.49,
    # FIG 2 per-lb food names (ruminants + rice carry the methane rescale)
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


DOLLAR = alt.Axis(format="$~r", grid=True)          # $0.0001 ... $1,000, no SI
PLAIN = alt.Axis(format="~r", grid=True)            # plain decimals on log y

# ---------------------------------------------------------------- FIG 1
# name: ($ price, carbon kg CO2e GWP100, category, label-side)
broad = {
    "1 LED bulb-day":         (0.035,  0.081,   "energy",  "left"),
    "1 Tesla-mile":           (0.05,   0.093,   "energy",  "right"),
    "bowl of rice":           (0.15,   0.225,   "food",    "left"),
    "oz of almonds":          (0.30,   0.012,   "food",    "left"),
    "cup of coffee":          (0.30,   0.20,    "food",    "right"),
    "10-min hot shower":      (0.50,   0.82,    "energy",  "right"),
    "chocolate bar":          (2.0,    1.87,    "food",    "left"),
    "rubber ducky":           (3.0,    0.30,    "goods",   "right"),
    "gallon of gas (burned)": (3.5,    8.9,     "energy",  "left"),
    "1 lb beef (a steak)":    (10.0,   27.0,    "food",    "left"),
    "cotton t-shirt":         (15.0,   4.0,     "goods",   "right"),
    "new iPhone":             (800.0,  65.0,    "goods",   "right"),
    "month heavy AI coding":  (200.0,  11.0,    "digital", "left"),
    "SF->NYC flight (1-way)": (200.0,  500.0,   "travel",  "left"),
    "MacBook Air":            (1100.0, 135.0,   "goods",   "left"),
}
rows = [{"name": n, "price": x, "carbon": gwp20(n, y0), "cat": cat, "side": side}
        for n, (x, y0, cat, side) in broad.items()]
bx = np.array([r["price"] for r in rows])
by = np.array([r["carbon"] for r in rows])
line, m, r2 = fit_line(bx, by, 0.5, 2)
f = fonts(720)

# One gridline per order of magnitude (decades only, no 2-3-4×10ⁿ minor ticks),
# and all FIG-1 text +2px over the shared theme (local props override save()'s
# global configure_* — so only this chart grows, the others are untouched).
DECADES = [1e-2, 1e-1, 1, 10, 100, 1000]
color = alt.Color("cat:N", scale=alt.Scale(domain=list(CAT), range=list(CAT.values())),
                  legend=alt.Legend(title="category"))
base = alt.Chart(alt.Data(values=rows))
ex = alt.X("price:Q", scale=alt.Scale(type="log", domain=[1e-2, 3e3]),
           axis=alt.Axis(format="$~r", grid=True, values=DECADES),
           title="What you pay  (US$, log)")
ey = alt.Y("carbon:Q", scale=alt.Scale(type="log", domain=[5e-3, 2e3]),
           axis=alt.Axis(format="~r", grid=True, values=DECADES),
           title="Carbon footprint  (kg CO₂e GWP20, log)")
pts = base.mark_circle(size=190, opacity=0.85, stroke="white", strokeWidth=1).encode(ex, ey, color=color)
lab_l = base.transform_filter("datum.side == 'left'").mark_text(
    align="left", dx=9, fontSize=f["label"], color=FG).encode(ex, ey, text="name:N")
lab_r = base.transform_filter("datum.side == 'right'").mark_text(
    align="right", dx=-9, fontSize=f["label"], color=FG).encode(ex, ey, text="name:N")
trend = alt.Chart(alt.Data(values=line)).mark_line(
    strokeDash=[6, 4], color="#888", strokeWidth=1.5).encode(x="x:Q", y="y:Q")
fig1 = (trend + pts + lab_l + lab_r).properties(
    width=720, height=560,
    # autosize=fit -> the 720x560 is the TOTAL image (chrome shrinks the plot to
    # fit inside), so this and the two food scatters end up identical pixel sizes
    # and therefore the same on-screen height in the column.
    autosize=alt.AutoSizeParams(type="fit", contains="padding"),
    title=alt.TitleParams(
        text="Dollar Cost vs Carbon Footprint: Log-Log",
        subtitle=[f"r = {r2**0.5:.2f}  ·  log-log OLS slope {m:.2f}"]))
save(fig1, "dollar_vs_carbon", 720)

# ---------------------------------------------------------------- FIG 2
G = {"staple": "#b5893b", "produce": "#6aa84f", "plant": "#3f8f5b",
     "indulge": "#7a5fb0", "dairy": "#d98a1f", "meat": "#c1432e"}
# Everything here is normalized to ONE POUND of food, so the groceries compare
# apples-to-apples with no portion-size artifact. portion_kg survives only to turn
# the surveyed per-portion price into a price-per-lb; it no longer touches the y axes.
LB = 0.453592  # kg per pound
# name: ($ price for the portion, portion_kg, carbon/kg, water L/kg, land m2/kg, group)
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
fp = np.array([v[0] / v[1] * LB for v in foods.values()])   # price per pound ($/lb)
anchor = {"beef", "almonds", "coffee", "chocolate", "potato", "rice"}
metrics = [
    ("Carbon", "carbon per pound (kg CO₂e GWP20, log)",
     {n: gwp20(n, v[2] * LB) for n, v in foods.items()}),
    ("Water", "water per pound (litres, log)",
     {n: v[3] * LB for n, v in foods.items()}),
    ("Land", "land per pound (m², log)",
     {n: v[4] * LB for n, v in foods.items()}),
]

f2 = fonts(660)

# Decade-only ticks for the standalone panels, matching the headline
# dollar_vs_carbon chart (one gridline per order of magnitude). Broad lists;
# Vega clips each to the chart's auto domain.
DEC_X = [0.01, 0.1, 1, 10, 100]
DEC_Y = [0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000]


def food_panel(label, ytitle, vals, legend, height=300, decades=False, width=660):
    """One $-vs-externality scatter over the 21 groceries, with its OLS fit.
    Returns (chart-without-title, r, slope). decades=True gives decade-only
    gridlines (the headline-chart style) instead of Vega's minor log ticks."""
    rows = [{"name": n, "price": foods[n][0], "y": float(vals[n]),
             "grp": foods[n][5], "anchor": n in anchor} for n in foods]
    yv = np.array([vals[n] for n in foods])
    line, m, r2 = fit_line(fp, yv, 0.7, 1.4)
    xaxis = alt.Axis(format="$~r", grid=True, values=DEC_X) if decades else DOLLAR
    yaxis = alt.Axis(format="~r", grid=True, values=DEC_Y) if decades else PLAIN
    base = alt.Chart(alt.Data(values=rows))
    ex = alt.X("price:Q", scale=alt.Scale(type="log"), axis=xaxis,
               title="price per pound  (US$, log)")
    ey = alt.Y("y:Q", scale=alt.Scale(type="log"), axis=yaxis, title=ytitle)
    leg = alt.Legend(title="food group") if legend else None
    pts = base.mark_circle(size=120, opacity=0.85, stroke="white", strokeWidth=0.8).encode(
        ex, ey, color=alt.Color("grp:N", scale=alt.Scale(domain=list(G), range=list(G.values())),
                                legend=leg))
    lab = base.transform_filter("datum.anchor").mark_text(
        align="left", dx=7, fontSize=f2["label"], color=FG).encode(ex, ey, text="name:N")
    trend = alt.Chart(alt.Data(values=line)).mark_line(
        strokeDash=[6, 4], color="#888").encode(x="x:Q", y="y:Q")
    return (trend + pts + lab).properties(width=width, height=height), r2 ** 0.5, m


# Stacked triptych — legend only on the last panel to avoid three copies.
panels = []
for i, (label, ytitle, vals) in enumerate(metrics):
    ch, r, _ = food_panel(label, ytitle, vals, legend=(i == len(metrics) - 1))
    panels.append(ch.properties(title=alt.TitleParams(text=f"{label}   (r = {r:.2f})")))
fig2 = alt.vconcat(*panels, spacing=44).properties(
    title=alt.TitleParams(
        text="Inside the grocery basket, price tracks carbon, water AND land about equally",
        subtitle=["21 groceries; no clean water/land break inside food — the "
                  "\"dollars don't proxy water\" intuition is a cross-category effect"]))
save(fig2, "dollar_vs_food_externalities", 660)

# Standalone water + land panels styled like the headline dollar_vs_carbon chart:
# decade-only gridlines, "Dollar Cost vs X: Log-Log" title, r/slope subtitle.
M = {label: (ytitle, vals) for label, ytitle, vals in metrics}
# 720x560 matches the headline dollar_vs_carbon chart, so all three scatters render
# at the same on-screen height (and share its font scaling).
for key, fname in [("Water", "dollar_vs_food_water"), ("Land", "dollar_vs_food_land")]:
    ytitle, vals = M[key]
    ch, r, m = food_panel(key, ytitle, vals, legend=True, height=560, decades=True, width=720)
    ch = ch.properties(
        title=alt.TitleParams(
            text=f"Dollar Cost vs {key} Use: Log-Log",
            subtitle=[f"r = {r:.2f}  ·  log-log OLS slope {m:.2f}"]),
        autosize=alt.AutoSizeParams(type="fit", contains="padding"))
    save(ch, fname, 720)

print("wrote dollar_vs_carbon.*, dollar_vs_food_externalities.*, "
      "dollar_vs_food_water.*, dollar_vs_food_land.*")
