"""Log-scale bars: US datacenter construction spending per year since 2020.

US Census Bureau, Value of Construction Put in Place, private "Data center"
line (2026 release). Buildings and installed structure in the US only: no
chips, servers or land. 2020 and 2021 are sums of the monthly figures. 2026 is
an estimate: $54.2B for January to September, plus three more months at
September's $8.5B.
https://www.census.gov/construction/c30/xlsx/private.xlsx

Values are rounded to about two significant figures.

Run from the post dir:  python3 charts/spend_bars.py
"""
import altair as alt

from theme import HUE, FG, fonts, save

ROWS = [
    # (year, billions of dollars)
    ("2020", 9), ("2021", 10), ("2022", 13), ("2023", 20),
    ("2024", 35), ("2025", 50), ("2026 (Est.)", 80),
]

WIDTH = 450
FLOOR = 1  # $1B; log axes have no zero, so bars rise from the bottom of the axis

data = [{"year": y, "usd": v, "floor": FLOOR, "label": f"{v:g}"} for y, v in ROWS]
f = fonts(WIDTH)

base = alt.Chart(alt.Data(values=data)).encode(
    x=alt.X("year:N", sort=[y for y, _ in ROWS], title=None, axis=alt.Axis(labelAngle=0)))
bar = base.mark_bar(color=HUE["dollar"], opacity=0.9).encode(
    y=alt.Y("usd:Q", title="Dollars (Log Scale)",
            scale=alt.Scale(type="log", domain=[FLOOR, 100], nice=False),
            axis=alt.Axis(values=[1, 10, 100], labelExpr="'$' + datum.value + 'B'")),
    y2="floor:Q")
labels = base.mark_text(dy=-6, fontSize=f["label"], color=FG).encode(y="usd:Q", text="label:N")

chart = (bar + labels).properties(width=WIDTH, height=200,
                                  title="US Datacenter Construction Spending")
save(chart, "spend_bars", WIDTH)
