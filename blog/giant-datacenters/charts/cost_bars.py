"""Paired bars, linear scale: what was spent on each part of the two sites.

Dollars, to about one significant figure. Full sourcing, ranges and arithmetic
are in POST_RESEARCH.md, part "Cost Breakdown for the Chart". Most bars are
estimates; the comments say which rest on a filing.

Servers  = accelerators in whole servers and racks. Abilene: Epoch AI's $21.2B
           per GW x 0.824 GW of IT power (SemiAnalysis's per-rack price agrees;
           the FT's reported $40B is the outlier). New Carlisle: about 1.04M
           Trainium2 x ~$7,000 installed + 104k Trainium3 x ~$10,000, capped by
           Amazon's reported $8.9B total. Soft.
Buildings = shells plus cooling, switchgear and generators. Shells are from
           filings (Texas TDLR: $292M each; St. Joseph County assessments), the
           fit-out is modelled.
Networking = switches, optics and fiber between racks: 13% of capital cost
           (Epoch AI), applied to each site. Overstates New Carlisle, where
           AWS uses its own gear.
New Power = generation and grid equipment built or bought for the site.
           Abilene: the on-site gas plant (reported at up to $500M) plus
           substations. New Carlisle: $185M of substations (PJM filing) plus a
           54% share of Indiana Michigan Power's gas plant purchases; the
           utility paid, not Amazon.
Power per Year = today's load x 8,760 h x the tariff (I&M large-load rate,
           6.1 cents/kWh) or the ERCOT West price ($46-53/MWh).
Storage  = 1 to 1.5% of capital cost (Bernstein). No site figure exists.
Land     = acreage x comparable local prices per acre. No deed price found.

Run from the post dir:  python3 charts/cost_bars.py
"""
import altair as alt

from theme import CAT, FG, fonts, save

ABILENE, CARLISLE = "Abilene", "New Carlisle"
ROWS = [
    # (category, Abilene $B, New Carlisle $B), biggest first
    ("Servers", 18, 8),
    ("Buildings", 9, 5),
    ("Networking", 4, 1.4),
    ("New Power", 0.7, 0.8),
    ("Power per Year", 0.4, 0.6),
    ("Storage", 0.4, 0.3),
    ("Land", 0.007, 0.07),
]

WIDTH = 50 * 2 * len(ROWS)
# Linear axis (Robbie's call): the small categories shrink to slivers, which is
# the point, and every bar keeps its value label.
YMAX = max(max(ab, nc) for _, ab, nc in ROWS) * 1.16


def dollars(billions):
    # no "$" on the bar labels: the axis carries it, and "$700M" is wider than a bar
    # "0.7B", not "700M": the narrower label fits beside its neighbour
    return f"{billions:g}B" if billions >= 0.1 else f"{billions * 1000:g}M"


data = [{"item": cat, "site": site, "usd": v, "label": dollars(v)}
        for cat, ab, nc in ROWS for site, v in ((ABILENE, ab), (CARLISLE, nc))]
f = fonts(WIDTH)

base = alt.Chart(alt.Data(values=data)).encode(
    x=alt.X("item:N", sort=[cat for cat, _, _ in ROWS], title=None,
            scale=alt.Scale(paddingInner=0.22),
            axis=alt.Axis(labelAngle=-35, labelLimit=220)),
    xOffset=alt.XOffset("site:N", sort=[ABILENE, CARLISLE]))
bar = base.mark_bar(opacity=0.9).encode(
    y=alt.Y("usd:Q", title="Billions of Dollars",
            scale=alt.Scale(domain=[0, YMAX], nice=False),
            axis=alt.Axis(values=[0, 5, 10, 15, 20], labelExpr="datum.value == 0 ? '$0' : '$' + datum.value + 'B'")),
    color=alt.Color("site:N", title=None, sort=[ABILENE, CARLISLE],
                    scale=alt.Scale(domain=[ABILENE, CARLISLE], range=[CAT["energy"], CAT["travel"]]),
                    legend=alt.Legend(orient="top")))
# A label is wider than its bar, so where a pair is close in height the two labels
# collide. Nudge each one outward from the pair's centre.
NUDGE = 4
labels = alt.layer(*[
    base.transform_filter(alt.datum.site == site)
    .mark_text(dy=-6, dx=dx, fontSize=f["label"], color=FG)
    .encode(y="usd:Q", text="label:N")
    for site, dx in ((ABILENE, -NUDGE), (CARLISLE, NUDGE))])

chart = (bar + labels).properties(width=WIDTH, height=200, title="Spending by Category")
save(chart, "cost_bars", WIDTH)
