"""Linear vertical bar charts for the post's 1-D tables (Altair).

Same data + design as before: linear y-axis, a value label on top of every bar
(so a sub-order-of-magnitude bar keeps its number even when the bar is an
invisible sliver), sorted tallest-first, ranges ("1-11 kg") drawn at the
geometric mean with a lo..hi whisker. Dark theme via theme.save().
Numbers copied verbatim from FINAL_POST.md tables.
"""
import textwrap

import altair as alt

from theme import HUE, FG, fmt, fonts, save


def _wrap(s, width=82):
    return textwrap.wrap(s, width) if s else ""


def bars(rows, unit, title, name, hue, note=None, height=200):
    """rows: list of (label, value) or (label, (lo, hi))."""
    data = []
    for label, v in rows:
        if isinstance(v, tuple):
            lo, hi = v
            rep = (lo * hi) ** 0.5
            data.append({"item": label, "v": rep, "lo": lo, "hi": hi,
                         "top": hi, "label": f"{fmt(lo)}–{fmt(hi)}"})
        else:
            v = float(v)
            data.append({"item": label, "v": v, "lo": None, "hi": None,
                         "top": v, "label": fmt(v)})
    n = len(data)
    order = [d["item"] for d in sorted(data, key=lambda d: -d["v"])]
    ymax = max(d["top"] for d in data) * 1.16
    width = max(360, min(720, 50 * n))
    f = fonts(width)

    base = alt.Chart(alt.Data(values=data)).encode(
        x=alt.X("item:N", sort=order, title=None,
                axis=alt.Axis(labelAngle=-35, labelLimit=220)))
    bar = base.mark_bar(color=HUE[hue], opacity=0.9).encode(
        y=alt.Y("v:Q", title=unit,
                scale=alt.Scale(domain=[0, ymax], nice=False)))
    whisker = base.transform_filter("datum.lo != null").mark_rule(
        color="#cccccc", strokeWidth=1.3).encode(y="lo:Q", y2="hi:Q")
    labels = base.mark_text(dy=-6, fontSize=f["label"], color=FG).encode(
        y="top:Q", text="label:N")

    chart = (bar + whisker + labels).properties(
        width=width, height=height,
        title=alt.TitleParams(text=title, subtitle=_wrap(note)))
    save(chart, name, width)


# 1. Quotidian Power Use — CO2e per day (the row-comparable column), kg.
# Everything is a day's worth. Driving is a day's driving, not one mile:
# ~37 mi/day (US avg per driver) × 0.093 kg/mi Tesla → 3.4, × 0.44 F-150 → 16.
# The AI bars are a day on a $200/mo Claude Max plan: light chat ~1 kg/mo and
# all-day agentic coding ~11 kg/mo (÷30 → 0.03 and 0.37 kg/day, ~1 kWh/day).
bars([
    ("AI chat, a day", 0.033), ("washer run", 0.2),
    ("AI coding, maxed", 0.37), ("hot shower", 0.4),
    ("lighting", 0.65), ("dryer run", 1.1),
    ("Tesla, a day", 3.4), ("food", 10),
    # "daily home (ex. food/car)" ~11 kg, split by end use. Carbon-weighted, NOT
    # energy-weighted: EIA RECS 2020 site-energy end-use shares (space heat ~42%,
    # water heat ~19%, AC ~9%, other ~30%) x delivered emission factors (gas ~0.18,
    # electricity ~0.38 kg CO2/kWh), renormalized. Lighting stays its own bar above,
    # so it's excluded from "home other"; the four pieces + lighting sum to ~11.
    ("home heating", 3.8), ("home other", 3.4),
    ("water heating", 1.9), ("cooling (AC)", 1.2),
    ("F-150, a day", 16),
], "kg CO₂e", "Quotidian Power — Carbon per Day", "bar_power_co2e", "carbon",
   note="A day's worth of each. Driving = ~37 mi/day (US avg per driver); "
        "\"AI coding, maxed\" = all-day agentic coding on a $200/mo Claude Max plan.")

# 2. Quotidian Water Use — per item, US gallons
bars([
    ("1 ChatGPT query", 0.0001), ("1 toilet flush (high-flush)", 3.5),
    ("$200/mo Claude plan, used fully", 8), ("5-min shower", 11),
    ("1 bowl of rice", 30), ("1 loaf of bread", 200),
    ("1 cotton t-shirt", 700), ("1 steak (1 lb beef)", 1800),
    ("1 lb almonds", 1900),
], "Gallons", "Quotidian Water Use", "bar_water_item", "water")

# 3. US freshwater withdrawals by sector, Bgal/day
bars([
    ("agriculture", 118), ("homes", 29), ("manufacturing", 15),
    ("landscaping", 9), ("golf courses", 2), ("software / datacenters", 0.1),
], "Bgal/day", "US Freshwater Withdrawals by Sector", "bar_water_sector",
   "water", note="USGS Circular 1441, ~2015. Excludes thermoelectric cooling (~130 Bgal/day, mostly returned).")

# 3b. US freshwater CONSUMPTION by sector, Bgal/day — water withdrawn but not
# returned to the source. Irrigation & thermoelectric are USGS Circular 1441
# (2015); the rest are estimated (withdrawal x typical return rate). The point:
# power drops from ~46% of withdrawals to ~4% of consumption (it returns ~97%).
bars([
    ("agriculture", 85), ("landscaping", 6), ("power (thermoelectric)", 4.3),
    ("homes", 3), ("manufacturing", 3), ("golf courses", 1),
    ("software / datacenters", 0.1),
], "Bgal/day", "US Freshwater Consumption by Sector", "bar_water_consumption",
   "water", note="Water withdrawn but not returned. Irrigation & power: USGS 2015; other sectors estimated. Power is ~46% of withdrawals but ~4% of consumption.")

# 4. Recycling — aggregate CO2e if all landfilled were recycled, MMT
bars([
    ("paper & cardboard", 60), ("plastics", 27), ("aluminum", 11),
    ("glass", 2.3),
], "MMT CO₂e", "Recycling — Carbon Lever if All Recycled",
   "bar_recycle_total", "recycle",
   note="Plastics is an upper bound; most has no real recycling path.")

# 5. Recycling — CO2e saved per item, kg
bars([
    ("1 cardboard box (1 cu-ft)", 0.84), ("1 aluminum can (12 oz)", 0.13),
    ("1 glass bottle (12 oz)", 0.07), ("1 PET bottle (12 oz)", 0.02),
], "kg CO₂e", "Recycling — Carbon Saved per Item", "bar_recycle_item", "recycle")

# 6. Buying Fewer Things — lifetime CO2e per purchase, kg
bars([
    ("rubber ducky", 0.3), ("bowl of rice", 0.42), ("t-shirt", 5),
    ("steak", 30), ("new MacBook Air", 135),
    ("SF→NYC flight (1-way)", (500, 900)),
], "kg CO₂e", "Stuff You Buy — Total Carbon per Purchase", "bar_buy_absolute",
   "carbon")

# 7. CO2e per dollar (fills the [co2e per dollar] placeholder), kg/$ (GWP20).
bars([
    ("cup of milk", 4.9), ("SF→NYC flight 1-way", 3), ("bowl of rice", 2.8),
    ("lamb chop", 2.8), ("cheese", 2.6), ("gallon of gas", 2.5), ("steak", 2.4),
    ("Tesla mile", 1.9), ("chicken breast", 1.3), ("40g chocolate", 0.93),
    ("cup of coffee", 0.67), ("t-shirt", 0.3), ("new MacBook Air", 0.12),
    ("rubber ducky", 0.1), ("oz almonds", 0.04),
], "kg CO₂e / $", "Carbon per Dollar Spent", "bar_co2e_per_dollar", "dollar")

print("done — 7 linear bar charts (Altair)")
