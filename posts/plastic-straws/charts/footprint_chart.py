"""
Footprint scatter for the "green virtue actions" post.

Log-log: x = carbon footprint (kg CO2e), y = water footprint (litres).
Carbon is the universal "energy/impact" axis (Robbie's fungible Tesla-mile =
0.093 kg CO2e is marked as a gridline); a second top axis reads x in Tesla-miles.
Marker SIZE ~ land use (m2) where known.

NUMBERS are from POST_RESEARCH.md (each verified by an adversarial fact-checker).
Sources inline. Two honest caveats baked into the labels:
  - WATER for food/textiles is *virtual* (lifecycle green+blue+grey) water;
    for energy/transport items it is small *operational* water (cooling), so the
    two conventions aren't identical. Energy items sit low on water by construction.
  - CARBON for energy items uses US grid 0.373 kg CO2e/kWh (battery-to-wheel for EV).
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, FuncFormatter

# Dark theme to match the blog (blog.css --bg is #0b0b0b).
plt.style.use("dark_background")
plt.rcParams.update({
    "figure.facecolor": "#0b0b0b",
    "axes.facecolor": "#0b0b0b",
    "savefig.facecolor": "#0b0b0b",
})

TESLA_MILE_KG = 0.093  # 0.25 kWh * 0.373 kg CO2e/kWh (EPA eGRID2022)

# name: (carbon kg CO2e, water L, land m2 or None, category, label dx/dy align)
items = {
    "1 AI chat query":            (0.00011, 0.0003, None, "digital",  "left"),
    "1 LED bulb-day (9W·24h)":    (0.081,   0.4,    None, "energy",   "right"),
    "1 Tesla-mile":               (0.093,   0.5,    None, "energy",   "left"),
    "1 oz almonds":               (0.012,   454,    0.36, "food",     "left"),
    "cup of coffee":              (0.20,    132,    0.15, "food",     "left"),
    "10-min hot shower":          (0.82,    40,     None, "energy",   "right"),
    "40g dark-chocolate bar":     (1.87,    688,    2.8,  "food",     "left"),
    "cotton t-shirt":             (4.0,     2700,   None, "goods",    "left"),
    "month of heavy AI coding":   (11.2,    90,     None, "digital",  "left"),
    "1 lb beef (a steak)":        (27.0,    6800,   148,  "food",     "left"),
    "SF<->NYC round-trip flight": (1000.0,  50,     None, "travel",   "right"),
}

colors = {"food": "#c1432e", "energy": "#2e7dc1", "goods": "#7a5fb0",
          "digital": "#3f8f5b", "travel": "#d98a1f"}

fig, ax = plt.subplots(figsize=(12, 8))

for name, (c, w, land, cat, align) in items.items():
    size = 90 if land is None else 90 + land * 12
    ax.scatter(c, w, s=size, color=colors[cat], alpha=0.78,
               edgecolor="white", linewidth=1.1, zorder=3)
    dx = 1.18 if align == "left" else 0.85
    ha = "left" if align == "left" else "right"
    ax.annotate(name, (c * dx, w), fontsize=9.5, ha=ha, va="center",
                color="#e8e8e8", zorder=4)

ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(5e-5, 5e3)
ax.set_ylim(1e-4, 3e4)

ax.set_xlabel("Carbon footprint  (kg CO₂e, log scale)", fontsize=12)
ax.set_ylabel("Water footprint  (litres, log scale)", fontsize=12)
ax.set_title("One chart, two footprints: what actually moves the needle",
             fontsize=15, fontweight="bold", pad=34)

# Tesla-mile reference line + secondary top axis in Tesla-miles
ax.axvline(TESLA_MILE_KG, color="#2e7dc1", ls=":", lw=1, alpha=0.5, zorder=1)
secax = ax.secondary_xaxis(
    "top", functions=(lambda x: x / TESLA_MILE_KG, lambda t: t * TESLA_MILE_KG))
secax.set_xlabel("Carbon, read as Tesla-miles  (1 Tesla-mile = 0.093 kg CO₂e)",
                 fontsize=11, color="#2e7dc1")
secax.xaxis.set_major_formatter(FuncFormatter(
    lambda v, _: f"{v:,.0f}" if v >= 1 else f"{v:g}"))

ax.grid(True, which="major", ls="-", lw=0.5, alpha=0.25)
ax.grid(True, which="minor", ls=":", lw=0.4, alpha=0.12)
ax.xaxis.set_minor_locator(LogLocator(base=10, subs="auto", numticks=20))

handles = [plt.Line2D([0], [0], marker="o", ls="", mfc=colors[k], mec="white",
                      ms=10, label=k.capitalize()) for k in colors]
ax.legend(handles=handles, loc="lower right", frameon=True, framealpha=0.9,
          title="category", fontsize=9.5)

ax.text(0.33, 0.035,
        "marker size ∝ land use   ·   food/textile water is virtual (lifecycle) water;\n"
        "energy/transport water is small operational/cooling water (so they sit low by construction)",
        transform=ax.transAxes, fontsize=8, color="#9a9a9a", va="bottom")

# orientation arrows
ax.text(0.985, 0.5, "more water →", transform=ax.transAxes, rotation=90,
        ha="left", va="center", fontsize=8.5, color="#999")

fig.tight_layout()
fig.savefig("charts/footprint_energy_water.png", dpi=150, bbox_inches="tight")
fig.savefig("charts/footprint_energy_water.svg", bbox_inches="tight")
print("wrote charts/footprint_energy_water.png and .svg")
