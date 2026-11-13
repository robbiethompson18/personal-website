"""Teen behaviour vs parental surveillance, as four small panels (teens-panels).

Sources and caveats for every number are in POST_RESEARCH_KIDS.md; the short version:

- Licence at 16: share of 16-year-olds holding a licence, FHWA data via Sivak & Schoettle (2016).
- Ever had sex: US high schoolers, CDC YRBS. 1991-2011 from MMWR 61(29), 2012; 2013-2023 from the
  CDC "Data Summary & Trends Report: 2013-2023" (2024).
- Depression: past-year major depressive episode, ages 12-17, SAMHSA NSDUH 2019 report, Figure 48.
  Stops at 2019: 2020 was collected differently (COVID) and the survey method changed in 2021, so
  later figures (20.8% in 2021, 15.4% in 2024) aren't comparable.
- Read phone: parents of 13-17s who have looked through the teen's phone, Pew (2016, 2024).
- Track location: NOT one population. 2015 is Pew, parents of 13-17s; 2018 is one US state
  (Burnell et al.); 2023 is Pew, parents of 18-24s; 2026 is the Mott Poll, parents of 18-25s.

Run from the post dir:  python3 charts/teens.py
"""
import altair as alt

from theme import CAT, save

LIC, SEX, DEP = "Licensed at 16", "Had Sex (High Schoolers)", "Depressed (Ages 12-17)"
PHONE, LOC = "Parents Read Teen's Phone", "Parents Track Location"

DATA = {
    LIC: [(1983, 46.2), (2008, 31.1), (2011, 27.5), (2014, 24.5)],
    SEX: [(1991, 54.1), (1993, 53.0), (1995, 53.1), (1997, 48.4), (1999, 49.9), (2001, 45.6),
          (2003, 46.7), (2005, 46.8), (2007, 47.8), (2009, 46.0), (2011, 47.4), (2013, 47),
          (2015, 41), (2017, 40), (2019, 38), (2021, 30), (2023, 32)],
    DEP: list(zip(range(2004, 2020), [9.0, 8.8, 7.9, 8.2, 8.3, 8.1, 8.0, 8.2, 9.1, 10.7, 11.4,
                                      12.5, 12.8, 13.3, 14.4, 15.7])),
    PHONE: [(2015, 48), (2023, 50)],
    LOC: [(2015, 16), (2018, 51), (2023, 42), (2026, 52)],
}
rows = [{"series": series, "year": year, "pct": pct}
        for series, points in DATA.items() for year, pct in points]

COLOR = {LIC: CAT["travel"], SEX: CAT["food"], DEP: CAT["energy"],
         PHONE: CAT["goods"], LOC: CAT["digital"]}
X = alt.X("year:Q", title=None, axis=alt.Axis(format="d", tickCount=6),
          scale=alt.Scale(domain=[1980, 2027]))


def lines(series, width, height, y_title, legend):
    """Line + points for the given series, colored by series."""
    color = alt.Color("series:N", title=None, legend=legend,
                      scale=alt.Scale(domain=series, range=[COLOR[s] for s in series]))
    base = alt.Chart(alt.Data(values=[r for r in rows if r["series"] in series])).encode(
        x=X, y=alt.Y("pct:Q", title=y_title, scale=alt.Scale(domainMin=0)), color=color)
    return (base.mark_line(strokeWidth=2) + base.mark_point(filled=True, size=50)).properties(
        width=width, height=height)


PANEL = 310
panels = [
    lines([LIC], PANEL, 200, "Share (%)", None).properties(title=LIC),
    lines([SEX], PANEL, 200, "Share (%)", None).properties(title=SEX),
    lines([DEP], PANEL, 200, "Share (%)", None).properties(title=DEP),
    lines([PHONE, LOC], PANEL, 200, "Share (%)",
          alt.Legend(orient="bottom", columns=1, symbolType="stroke", labelLimit=0)).properties(
        title="Parental Surveillance"),
]
grid = alt.concat(*panels, columns=2).resolve_scale(color="independent")
# Fonts are sized for the whole two-column image, not one panel, so on-screen text matches.
save(grid, "teens-panels", 2 * PANEL + 80)
