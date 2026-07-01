"""Footprint scatter for the "green virtue actions" post (Altair).

Log-log: x = carbon footprint (kg CO2e), y = water footprint (litres).
Marker SIZE ~ land use (m2) where known. A dotted rule marks Robbie's fungible
"1 Tesla-mile" = 0.093 kg CO2e. Numbers from POST_RESEARCH.md.

Two honest caveats baked into the subtitle:
  - Food/textile water is *virtual* (lifecycle) water; energy/transport water is
    small *operational* (cooling) water, so the two conventions differ.
  - Carbon for energy items uses US grid 0.373 kg CO2e/kWh.
"""
import altair as alt

from theme import CAT, FG, fonts, save

TESLA = 0.093  # 0.25 kWh * 0.373 kg CO2e/kWh (EPA eGRID2022)
WIDTH = 720
f = fonts(WIDTH)

# name: (carbon kg CO2e, water L, land m2 or None, category, label side)
items = {
    "1 AI chat query":            (0.00011, 0.0003, None, "digital", "left"),
    "1 LED bulb-day (9W·24h)":    (0.081,   0.4,    None, "energy",  "right"),
    "1 Tesla-mile":               (0.093,   0.5,    None, "energy",  "left"),
    "1 oz almonds":               (0.012,   454,    0.36, "food",    "left"),
    "cup of coffee":              (0.20,    132,    0.15, "food",    "left"),
    "10-min hot shower":          (0.82,    40,     None, "energy",  "right"),
    "40g dark-chocolate bar":     (1.87,    688,    2.8,  "food",    "left"),
    "cotton t-shirt":             (4.0,     2700,   None, "goods",   "left"),
    "month of heavy AI coding":   (11.2,    90,     None, "digital", "left"),
    "1 lb beef (a steak)":        (27.0,    6800,   148,  "food",    "left"),
    "SF<->NYC round-trip flight": (1000.0,  50,     None, "travel",  "right"),
}
rows = [{"name": n, "carbon": c, "water": w, "cat": cat, "side": side,
         "size": 120 if land is None else 120 + land * 14}
        for n, (c, w, land, cat, side) in items.items()]

base = alt.Chart(alt.Data(values=rows))
ex = alt.X("carbon:Q", scale=alt.Scale(type="log", domain=[5e-5, 5e3]),
           axis=alt.Axis(format="~r", grid=True), title="Carbon footprint  (kg CO₂e, log)")
ey = alt.Y("water:Q", scale=alt.Scale(type="log", domain=[1e-4, 3e4]),
           axis=alt.Axis(format="~r", grid=True), title="Water footprint  (litres, log)")
color = alt.Color("cat:N", scale=alt.Scale(domain=list(CAT), range=list(CAT.values())),
                  legend=alt.Legend(title="category"))
pts = base.mark_circle(opacity=0.8, stroke="white", strokeWidth=1).encode(
    ex, ey, color=color, size=alt.Size("size:Q", scale=None, legend=None))
lab_l = base.transform_filter("datum.side == 'left'").mark_text(
    align="left", dx=11, fontSize=f["label"], color=FG).encode(ex, ey, text="name:N")
lab_r = base.transform_filter("datum.side == 'right'").mark_text(
    align="right", dx=-11, fontSize=f["label"], color=FG).encode(ex, ey, text="name:N")
rule = alt.Chart(alt.Data(values=[{"x": TESLA}])).mark_rule(
    color="#2e7dc1", strokeDash=[2, 3], opacity=0.6).encode(x="x:Q")
ruletext = alt.Chart(alt.Data(values=[{"x": TESLA, "y": 2.2e4, "t": "1 Tesla-mile"}])).mark_text(
    color="#2e7dc1", align="left", dx=4, fontSize=f["label"]).encode(x="x:Q", y="y:Q", text="t:N")

chart = (rule + ruletext + pts + lab_l + lab_r).properties(
    width=WIDTH, height=520,
    title=alt.TitleParams(
        text="One chart, two footprints: what actually moves the needle",
        subtitle=["marker size ∝ land use  ·  food/textile water is lifecycle (virtual); "
                  "energy/transport water is small operational (cooling) water"]))
save(chart, "footprint_energy_water", WIDTH)
print("wrote footprint_energy_water.*")
