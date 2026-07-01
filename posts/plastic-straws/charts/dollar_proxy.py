"""
Two charts for the "dollars as a proxy for externalities" section.

FIG 1  dollar_vs_carbon.png   — the headline.
  Log-log scatter, x = consumer $ price, y = carbon (kg CO2e), across the whole
  economy (food / energy / goods / travel / digital). OLS fit in log space.
  Punchline: across ~4 orders of magnitude of spending, $ predicts carbon well
  (r ~ 0.9). A budget is already a carbon budget.

FIG 2  dollar_vs_food_externalities.png — the honest caveat.
  Same 21 groceries, three panels: $ vs carbon / water / land. The surprise
  (see POST_RESEARCH.md discussion): WITHIN a grocery basket, $ predicts water
  and land about as well as it predicts carbon (all r ~ 0.8). The "dollars don't
  proxy water/land" intuition is a *cross-category* composition effect (most
  spending isn't food; nearly all water/land impact lives in food), NOT a
  per-item one. There is no clean break inside the basket.

NUMBERS: carbon & land per-kg = Poore & Nemecek 2018 (OWID); water per-kg =
Mekonnen & Hoekstra total (green+blue+grey) water footprints. Prices = US
consumer, ~1 sig fig. Beef row matches the verified datapoint in FINAL_POST.md
(1 lb = 27 kg CO2e, 6800 L, 148 m2). Approximate by design (see the post's
"Probably Approximately Correct" note); the axes span orders of magnitude, so
+/-30% on any input does not move the story.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, FuncFormatter

# Dark theme to match the blog (blog.css --bg is #0b0b0b).
plt.style.use("dark_background")
plt.rcParams.update({
    "figure.facecolor": "#0b0b0b",
    "axes.facecolor": "#0b0b0b",
    "savefig.facecolor": "#0b0b0b",
})

CAT = {"food": "#c1432e", "energy": "#2e7dc1", "goods": "#7a5fb0",
       "digital": "#3f8f5b", "travel": "#d98a1f"}

# GWP20 basis. Shortening the horizon 100->20 yr only rescales METHANE
# (CH4: GWP100~28 -> GWP20~84, ratio 3x). CO2 = 1 on any horizon; N2O lives
# ~116 yr so GWP20~=GWP100 (fertilizer-heavy plants don't move). So the source
# GWP100 footprints convert as:  carbon_gwp20 = carbon_gwp100 * (1 + 2*f),
# where f = methane share of the item's GWP100 footprint. Only ruminants + rice
# carry meaningful f here; everything else is pure CO2 (f=0, unchanged).
# f sources: OWID "carbon-footprint-food-methane" (beef 49%); livestock/rice LCAs.
F_CH4 = {
    "1 lb beef": 0.49, "1 lb beef (a steak)": 0.49, "lamb chop": 0.50,
    "cup of milk": 0.45, "cheese (30g)": 0.40, "bowl of rice": 0.55,
    "pork chop": 0.13, "chicken breast": 0.06, "2 eggs": 0.06,
}


def gwp20(name, carbon100):
    return carbon100 * (1 + 2 * F_CH4.get(name, 0.0))


def ols_loglog(x, y):
    lx, ly = np.log10(x), np.log10(y)
    m, b = np.polyfit(lx, ly, 1)
    r2 = 1 - np.sum((ly - (m * lx + b)) ** 2) / np.sum((ly - ly.mean()) ** 2)
    return m, b, r2


def money_fmt(v, _):
    if v < 0.01:
        return f"${v:.4f}".rstrip("0")
    if v < 1:
        return f"${v:.2f}"
    return f"${v:,.0f}"


# ---------------------------------------------------------------- FIG 1
# name: ($ price, carbon kg CO2e, category, label-side)
broad = {
    "1 AI chat query":        (0.0002, 0.00011, "digital", "left"),
    "1 LED bulb-day":         (0.035,  0.081,   "energy",  "left"),
    "1 Tesla-mile":           (0.05,   0.093,   "energy",  "right"),
    "bowl of rice":           (0.15,   0.225,   "food",    "left"),
    "oz of almonds":          (0.30,   0.012,   "food",    "left"),
    "cup of coffee":          (0.30,   0.20,    "food",    "right"),
    "10-min hot shower":      (0.50,   0.82,    "energy",  "right"),
    "40g chocolate bar":      (2.0,    1.87,    "food",    "left"),
    "rubber ducky":           (3.0,    0.30,    "goods",   "right"),
    "gallon of gas (burned)": (3.5,    8.9,     "energy",  "left"),
    "1 lb beef (a steak)":    (10.0,   27.0,    "food",    "left"),
    "cotton t-shirt":         (15.0,   4.0,     "goods",   "right"),
    "new iPhone":             (800.0,  65.0,    "goods",   "right"),
    "month heavy AI coding":  (200.0,  11.0,    "digital", "left"),
    "SF->NYC flight (1-way)": (200.0,  500.0,   "travel",  "left"),
    "MacBook Air":            (1100.0, 135.0,   "goods",   "left"),
}

bx = np.array([v[0] for v in broad.values()])
by = np.array([gwp20(n, v[1]) for n, v in broad.items()])
m, b, r2 = ols_loglog(bx, by)

fig, ax = plt.subplots(figsize=(12, 8))
for name, (x, y0, cat, side) in broad.items():
    y = gwp20(name, y0)
    ax.scatter(x, y, s=130, color=CAT[cat], alpha=0.82,
               edgecolor="white", linewidth=1.2, zorder=3)
    dx = 1.15 if side == "left" else 0.86
    ha = "left" if side == "left" else "right"
    ax.annotate(name, (x * dx, y), fontsize=9.5, ha=ha, va="center",
                color="#e8e8e8", zorder=4)

xs = np.array([bx.min() * 0.5, bx.max() * 2])
ax.plot(xs, 10 ** (m * np.log10(xs) + b), ls="--", lw=1.6, color="#888",
        alpha=0.8, zorder=2)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1e-4, 3e3)
ax.set_ylim(5e-5, 2e3)
ax.xaxis.set_major_formatter(FuncFormatter(money_fmt))
ax.set_xlabel("What you pay  (US$, log scale)", fontsize=12)
ax.set_ylabel("Carbon footprint  (kg CO₂e GWP20, log scale)", fontsize=12)
ax.set_title("Spend more, emit more: dollars are a decent carbon proxy",
             fontsize=15, fontweight="bold", pad=14)
ax.text(0.03, 0.94,
        f"r = {r2**0.5:.2f}   (log-log OLS, slope {m:.2f})\n"
        f"across ~7 orders of magnitude of price",
        transform=ax.transAxes, fontsize=11, va="top",
        bbox=dict(boxstyle="round,pad=0.4", fc="#161616", ec="#333", alpha=0.95))
ax.grid(True, which="major", ls="-", lw=0.5, alpha=0.25)
ax.grid(True, which="minor", ls=":", lw=0.4, alpha=0.12)
handles = [plt.Line2D([0], [0], marker="o", ls="", mfc=CAT[k], mec="white",
                      ms=10, label=k.capitalize()) for k in CAT]
ax.legend(handles=handles, loc="lower right", frameon=True, framealpha=0.9,
          title="category", fontsize=9.5)
fig.tight_layout()
fig.savefig("charts/dollar_vs_carbon.png", dpi=150, bbox_inches="tight")
fig.savefig("charts/dollar_vs_carbon.svg", bbox_inches="tight")
print(f"FIG1 $ vs carbon (n={len(broad)}): r={r2**0.5:.2f} r2={r2:.2f} slope={m:.2f}")

# ---------------------------------------------------------------- FIG 2
# name: ($ price, portion_kg, carbon/kg, water L/kg, land m2/kg, group)
G = {"staple": "#b5893b", "produce": "#6aa84f", "plant": "#3f8f5b",
     "indulge": "#7a5fb0", "dairy": "#d98a1f", "meat": "#c1432e"}
foods = {
    "potato":          (0.30, 0.170, 0.46,  287,   0.9,  "staple"),
    "bowl of rice":    (0.15, 0.050, 4.5,   2497,  2.8,  "staple"),
    "2 slices bread":  (0.30, 0.060, 1.6,   1608,  2.7,  "staple"),
    "side salad":      (0.50, 0.085, 0.5,   237,   0.4,  "produce"),
    "banana":          (0.25, 0.120, 0.86,  790,   1.9,  "produce"),
    "apple":           (0.50, 0.150, 0.43,  822,   0.63, "produce"),
    "tomato":          (0.50, 0.120, 1.4,   214,   0.8,  "produce"),
    "avocado":         (1.50, 0.150, 2.5,   2000,  2.0,  "produce"),
    "tofu":            (0.50, 0.100, 3.2,   2000,  2.2,  "plant"),
    "peanut butter":   (0.20, 0.030, 2.5,   2782,  3.0,  "plant"),
    "oz almonds":      (0.30, 0.028, 0.43,  16000, 13.0, "plant"),
    "olive oil (Tbsp)":(0.25, 0.014, 6.0,   14400, 26.0, "plant"),
    "cup of coffee":   (0.30, 0.007, 28.5,  18900, 21.0, "indulge"),
    "40g chocolate":   (2.00, 0.040, 46.7,  17200, 70.0, "indulge"),
    "cup of milk":     (0.30, 0.240, 3.2,   1020,  8.9,  "dairy"),
    "2 eggs":          (0.50, 0.100, 4.7,   3265,  6.3,  "dairy"),
    "cheese (30g)":    (0.50, 0.030, 23.9,  5060,  87.8, "dairy"),
    "chicken breast":  (1.50, 0.170, 9.9,   4325,  12.2, "meat"),
    "pork chop":       (1.75, 0.140, 12.3,  5988,  17.4, "meat"),
    "lamb chop":       (4.00, 0.140, 39.7,  10412, 369.0,"meat"),
    "1 lb beef":       (10.0, 0.454, 60.0,  15000, 326.0,"meat"),
}
fp = np.array([v[0] for v in foods.values()])
fg = [v[5] for v in foods.values()]
carbon = np.array([gwp20(n, v[1] * v[2]) for n, v in foods.items()])
water = np.array([v[1] * v[3] for v in foods.values()])
land = np.array([v[1] * v[4] for v in foods.values()])

# label only a few anchors per panel to avoid clutter
anchor = {"1 lb beef", "oz almonds", "cup of coffee", "40g chocolate",
          "potato", "bowl of rice"}

fig, axes = plt.subplots(3, 1, figsize=(11, 21), sharex=True)
panels = [("Carbon", carbon, "kg CO₂e GWP20"),
          ("Water", water, "litres"),
          ("Land", land, "m²")]
for ax, (title, y, unit) in zip(axes, panels):
    m, b, r2 = ols_loglog(fp, y)
    for (name, v), yi in zip(foods.items(), y):
        ax.scatter(v[0], yi, s=95, color=G[v[5]], alpha=0.82,
                   edgecolor="white", linewidth=1.0, zorder=3)
        if name in anchor:
            ax.annotate(name, (v[0] * 1.12, yi), fontsize=8, ha="left",
                        va="center", color="#e8e8e8", zorder=4)
    xs = np.array([fp.min() * 0.7, fp.max() * 1.4])
    ax.plot(xs, 10 ** (m * np.log10(xs) + b), ls="--", lw=1.5,
            color="#888", alpha=0.8, zorder=2)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.xaxis.set_major_formatter(FuncFormatter(money_fmt))
    ax.set_title(f"{title}   (r = {r2**0.5:.2f})", fontsize=13,
                 fontweight="bold")
    ax.set_xlabel("grocery price (US$, log)", fontsize=10)
    ax.set_ylabel(f"{title.lower()} per serving  ({unit}, log)", fontsize=10)
    ax.grid(True, which="major", ls="-", lw=0.5, alpha=0.22)
    ax.grid(True, which="minor", ls=":", lw=0.4, alpha=0.10)

handles = [plt.Line2D([0], [0], marker="o", ls="", mfc=G[k], mec="white",
                      ms=9, label=k.capitalize()) for k in G]
axes[2].legend(handles=handles, loc="lower right", frameon=True,
               framealpha=0.9, fontsize=8, title="food group")
fig.suptitle("Inside the grocery basket, price tracks carbon, water AND land "
             "about equally — no clean water/land break",
             fontsize=14.5, fontweight="bold")
fig.tight_layout(rect=(0, 0, 1, 0.96))
fig.savefig("charts/dollar_vs_food_externalities.png", dpi=150,
            bbox_inches="tight")
fig.savefig("charts/dollar_vs_food_externalities.svg", bbox_inches="tight")
for title, y, _ in panels:
    m, b, r2 = ols_loglog(fp, y)
    print(f"FIG2 food $ vs {title:6s} (n={len(foods)}): "
          f"r={r2**0.5:.2f} r2={r2:.2f} slope={m:.2f}")
print("wrote charts/dollar_vs_carbon.* and charts/dollar_vs_food_externalities.*")
