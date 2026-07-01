"""
Linear vertical bar charts for the post's 1-D tables.

Item on x-axis, metric on y-axis, LINEAR scale (Robbie's call). Caveat baked in:
on a linear axis anything ~>1 order of magnitude below the tallest bar is an
invisible sliver, so every bar gets a value label on top — the number survives
even when the bar doesn't. Sorted tallest-first. Ranges ("1-11 kg") draw the bar
at the geometric mean with an error whisker. Dark theme to match the blog.
Numbers copied verbatim from FINAL_POST.md tables.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("dark_background")
plt.rcParams.update({
    "figure.facecolor": "#0b0b0b",
    "axes.facecolor": "#0b0b0b",
    "savefig.facecolor": "#0b0b0b",
})

HUE = {"carbon": "#c1432e", "water": "#2e7dc1",
       "recycle": "#3f8f5b", "dollar": "#7a5fb0"}


def fmt(v):
    if v >= 100:
        return f"{v:,.0f}"
    if v >= 1:
        return f"{v:g}"
    return f"{v:.4g}"


def bars(rows, unit, title, fname, hue, note=None):
    """rows: list of (label, value) or (label, (lo, hi))."""
    labels, reps, ranges = [], [], []
    for label, v in rows:
        if isinstance(v, tuple):
            lo, hi = v
            reps.append((lo * hi) ** 0.5)
            ranges.append((lo, hi))
        else:
            reps.append(float(v))
            ranges.append(None)
        labels.append(label)
    order = np.argsort(reps)[::-1]            # tallest first
    labels = [labels[i] for i in order]
    reps = [reps[i] for i in order]
    ranges = [ranges[i] for i in order]
    color = HUE[hue]
    n = len(rows)

    fig, ax = plt.subplots(figsize=(max(6.5, 0.95 * n + 1.5), 5.6))
    x = np.arange(n)
    yerr = None
    if any(ranges):
        yerr = np.array([[v - (rg[0] if rg else v) for v, rg in zip(reps, ranges)],
                         [(rg[1] if rg else v) - v for v, rg in zip(reps, ranges)]])
    ax.bar(x, reps, width=0.72, color=color, alpha=0.9,
           edgecolor="#0b0b0b", linewidth=0.5, zorder=2,
           yerr=yerr, ecolor="#cccccc", capsize=3, error_kw={"lw": 1.2})

    top = max((rg[1] if rg else v) for v, rg in zip(reps, ranges))
    for xi, (v, rg) in enumerate(zip(reps, ranges)):
        txt = fmt(v) if not rg else f"{fmt(rg[0])}–{fmt(rg[1])}"
        yt = (rg[1] if rg else v) + top * 0.015
        ax.text(xi, yt, txt, ha="center", va="bottom", fontsize=8.5,
                color="#e8e8e8", zorder=4)

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=35, ha="right", fontsize=9)
    ax.set_ylabel(f"{unit}  (linear)", fontsize=11)
    ax.set_ylim(0, top * 1.16)
    ax.set_title(title, fontsize=13, fontweight="bold", pad=26 if note else 10)
    ax.grid(True, axis="y", ls="-", lw=0.5, alpha=0.18)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    if note:
        ax.text(0, 1.015, note, transform=ax.transAxes, fontsize=8,
                style="italic", color="#999", va="bottom", ha="left")
    fig.tight_layout()
    fig.savefig(f"charts/{fname}.png", dpi=150, bbox_inches="tight")
    fig.savefig(f"charts/{fname}.svg", bbox_inches="tight")
    plt.close(fig)
    print(f"wrote charts/{fname}.png  (n={n})")


# 1. Quotidian Power Use — CO2e (the row-comparable column), kg
bars([
    ("1 AI chat query", 0.0001), ("1 LED bulb-hour (9W)", 0.003),
    ("1 Tesla mile", 0.093), ("1 washer run (cold)", 0.2),
    ("5-min hot shower", 0.4), ("1 Ford F-150 mile", 0.44),
    ("daily household lighting", 0.65), ("1 dryer run", 1.1),
    ("month of Claude Max", (1, 11)), ("avg American daily food", 10),
    ("daily home use (excl. food/driving)", 11),
    ("avg American daily driving", 14),
], "kg CO₂e", "Quotidian power — carbon per action", "bar_power_co2e", "carbon",
   note="GWP20. Linear scale — sub-kg actions vanish next to driving; that's the point.")

# 2. Quotidian Water Use — per item, US gallons
bars([
    ("1 ChatGPT query", 0.0001), ("1 toilet flush (high-flush)", 3.5),
    ("$200/mo Claude plan, used fully", 8), ("5-min shower", 11),
    ("1 bowl of rice", 30), ("1 loaf of bread", 200),
    ("1 cotton t-shirt", 700), ("1 steak (1 lb beef)", 1800),
    ("1 lb almonds", 1900),
], "gallons", "Quotidian water — per item", "bar_water_item", "water",
   note="Food/textile = lifecycle (virtual) water; on a linear axis only they show.")

# 3. US freshwater withdrawals by sector, Bgal/day
bars([
    ("agriculture", 118), ("homes", 29), ("manufacturing", 15),
    ("landscaping", 9), ("golf courses", 2), ("software / datacenters", 0.1),
], "Bgal/day", "US freshwater withdrawals by sector", "bar_water_sector",
   "water", note="USGS Circular 1441, ~2015. Excludes thermoelectric cooling (~130 Bgal/day, mostly returned).")

# 4. Recycling — aggregate CO2e if all landfilled were recycled, MMT
bars([
    ("paper & cardboard", 60), ("plastics", 27), ("aluminum", 11),
    ("glass", 2.3),
], "MMT CO₂e", "Recycling — total carbon lever if all of it were recycled",
   "bar_recycle_total", "recycle",
   note="Plastics is an upper bound; most has no real recycling path.")

# 5. Recycling — CO2e saved per item, kg
bars([
    ("1 cardboard box (1 cu-ft)", 0.84), ("1 aluminum can (12 oz)", 0.13),
    ("1 glass bottle (12 oz)", 0.07), ("1 PET bottle (2 L)", 0.06),
], "kg CO₂e", "Recycling — carbon saved per item", "bar_recycle_item", "recycle")

# 6. Buying Fewer Things — lifetime CO2e per purchase, kg
bars([
    ("rubber ducky", 0.3), ("bowl of rice", 0.42), ("t-shirt", 5),
    ("steak", 30), ("new MacBook Air", 135),
    ("SF→NYC flight (1-way)", (500, 900)),
], "kg CO₂e", "Stuff you buy — total carbon per purchase", "bar_buy_absolute",
   "carbon")

# 7. CO2e per dollar (fills the [co2e per dollar] placeholder), kg/$
bars([
    ("SF→NYC flight (1-way)", 3), ("bowl of rice", 2.8), ("steak", 2.4),
    ("t-shirt", 0.3), ("new MacBook Air", 0.12), ("rubber ducky", 0.1),
], "kg CO₂e / $", "Carbon per dollar spent", "bar_co2e_per_dollar", "dollar",
   note="Absolute footprint and per-dollar intensity rank almost oppositely: "
        "the MacBook is the biggest single hit but the cheapest per dollar.")

print("done — 7 linear bar charts")
