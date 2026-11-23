"""Log-scale bar chart: the two datacenter sites against familiar power uses.

Gigawatts, to about one significant figure. Sources and quotes are in
POST_RESEARCH.md (the Abilene part and "Power Comparisons for the Chart").
Everything except the two sites and the forecast is annual energy / 8,760 h.

- All US Cars (Fuel): 124.8 bn gallons burned by light-duty vehicles in 2024
  (FHWA VM-1) x 120,214 Btu/gal = 4,397 TWh of fuel heat = 500 GW. This is heat,
  not electricity: the same miles in EVs would take about 100 GW.
- All US Homes: 1,519 TWh of residential sales in 2025 (EIA) = 173 GW.
- Aschenbrenner's 2030 Cluster: ~100 GW, the "trillion-dollar cluster" row of
  the table in Situational Awareness (2024). A forecast.
- All Datacenters Globally: 485 TWh in 2025 (IEA estimate) = 55 GW. The Energy
  Institute's count is 788 TWh, 90 GW.
- All US Datacenters: 192 TWh in 2024 (LBNL estimate, excludes crypto) = 22 GW.
- New York City: 50.1 TWh in 2025 (NYISO Zone J) = 5.7 GW.
- New Carlisle: 1,244 MW total facility power for the 18 buildings running in
  Oct 2026 (Epoch AI estimate from air permits). Full buildout is 2.2 GW.
- Abilene: 1.2 GW grid connection (Crusoe); Epoch AI estimates 1,154 MW total
  facility power with all eight buildings on, Nov 2026.
- A Nuclear Reactor: 784.8 TWh from 94 US reactors in 2025 (EIA) = 0.95 GW each.
- San Francisco: 5.1 TWh in 2022 (California Energy Commission) = 0.58 GW.
- Hoover Dam: 3.26 TWh a year averaged over FY2016-25 (Reclamation) = 0.37 GW.
  Nameplate is 2.08 GW, but Lake Mead's level keeps output far below that.

The two site bars are facility power at full load, which a training cluster
sits close to around the clock.

Run from the post dir:  python3 charts/power_bars.py
"""
import altair as alt

from theme import CAT, FG, fonts, save

SITE, OTHER = "site", "other"
ROWS = [
    # (label, gigawatts, kind), tallest first
    ("All US Cars (Fuel)", 500, OTHER),
    ("All US Homes", 170, OTHER),
    ("Aschenbrenner's 2030 Cluster", 100, OTHER),
    ("All Datacenters Globally", 55, OTHER),
    ("All US Datacenters", 22, OTHER),
    ("New York City", 6, OTHER),
    ("New Carlisle Site", 1.2, SITE),
    ("Abilene Site", 1.2, SITE),
    ("A Nuclear Reactor", 1, OTHER),
    ("San Francisco", 0.6, OTHER),
    ("Hoover Dam", 0.4, OTHER),
]

WIDTH = 50 * len(ROWS)
FLOOR = 0.1  # log axes have no zero, so bars rise from the bottom of the axis

data = [{"item": name, "gw": gw, "floor": FLOOR, "kind": kind, "label": f"{gw:g}"}
        for name, gw, kind in ROWS]
f = fonts(WIDTH)

base = alt.Chart(alt.Data(values=data)).encode(
    x=alt.X("item:N", sort=[name for name, _, _ in ROWS], title=None,
            axis=alt.Axis(labelAngle=-35, labelLimit=260)))
bar = base.mark_bar(opacity=0.9).encode(
    y=alt.Y("gw:Q", title="Gigawatts (Log Scale)",
            scale=alt.Scale(type="log", domain=[FLOOR, 1000], nice=False),
            axis=alt.Axis(values=[0.1, 1, 10, 100, 1000], format="~g")),
    y2="floor:Q",
    # the two sites the post is about get their own color; everything else is context
    color=alt.Color("kind:N", legend=None,
                    scale=alt.Scale(domain=[SITE, OTHER], range=[CAT["travel"], CAT["energy"]])))
labels = base.mark_text(dy=-6, fontSize=f["label"], color=FG).encode(
    y="gw:Q", text="label:N")

chart = (bar + labels).properties(width=WIDTH, height=200, title="Average Power")
save(chart, "power_bars", WIDTH)
