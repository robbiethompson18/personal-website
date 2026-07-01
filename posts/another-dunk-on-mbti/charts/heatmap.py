"""Predictor x outcome correlation heatmap (Altair, dark theme).

Replaces the old hand-made white-background matplotlib PNG. Cells are absolute
correlations |r|. Rows are sorted by each predictor's mean |r| across the
outcomes it has data for. Color ramps BG -> carbon-red, clamped at 0.6 (so the
one huge cell, race->spouse .90, saturates instead of blowing out the scale) —
same convention as the original legend that topped out at 0.6.

Numbers are approximate effect sizes pulled from meta-analyses; see FINAL_POST.md
footnote [^1] for the per-predictor sources. A few cells were corrected after a
sourcing pass (marked ADJ below): the post-Sackett IQ->job-performance value, the
politics->mortality cell (the county-level gap is not an individual r), the
internally-inconsistent openness->job-performance cell, three income cells snapped
to Ng et al. 2005, and the Big Five marriage-rate cells reordered so extraversion
leads (Stern et al. 2024). Cells with no meta-analytic r are None -> rendered "—".
"""
import altair as alt

from theme import BG, FG, MUTED, GRID, fonts, save

# Outcomes = columns, in display order.
OUTCOMES = ["Spouse Similarity", "Education", "Job Type", "Job Performance",
            "Income", "Divorce", "Mortality", "Marriage Rate"]

# predictor -> |r| per outcome (None = no meta-analytic estimate). ADJ = changed
# from the original chart during the sourcing pass.
ROWS = {
    "IQ":               [.42, .56, .45, .31, .23, .10, .12, .07],  # ADJ jobperf .40->.31 (Sackett 2022)
    "Race":             [.90, .22, .17, .13, .24, .12, .12, .22],
    "Parental SES":     [.30, .28, .30, None, .34, .15, .20, .15],
    "Politics":         [.58, .20, .30, .08, .20, .10, .08, .22],  # ADJ mortality .25->.08 (ecological); spouse .60->.58 (Alford party r, matches [^1])
    "Big Five (all)":   [.13, .22, .35, .28, .20, .27, .12, .15],
    "Conscientiousness":[.16, .25, .13, .20, .12, .13, .09, .06],  # ADJ marriage .08->.06
    "Openness":         [.21, .14, .48, .13, .01, .05, .00, None], # ADJ jobperf .06->.13 (Zell 2022)
    "Agreeableness":    [.11, .07, .19, .10, .10, .18, .04, .05],  # ADJ income .07->.10, marriage .10->.05
    "Extraversion":     [.08, .00, .41, .10, .10, .05, .03, .12],  # ADJ income .04->.10, marriage .05->.12
    "MBTI":             [.05, .15, .15, .05, .07, None, None, None],
    "Neuroticism":      [.11, .03, .00, .12, .12, .17, .05, .06],  # ADJ income .10->.12, marriage .05->.06
    "Zodiac":           [.00, .00, .00, .00, .00, .00, .02, .00],
}


def _mean(vals):
    seen = [v for v in vals if v is not None]
    return sum(seen) / len(seen) if seen else 0.0


# Both sorted strongest-first by mean |r|: rows highest on top, columns highest
# on the left.
order = sorted(ROWS, key=lambda k: -_mean(ROWS[k]))
col_mean = {o: _mean([ROWS[p][i] for p in ROWS]) for i, o in enumerate(OUTCOMES)}
col_order = sorted(OUTCOMES, key=lambda c: -col_mean[c])

data = []
for pred in order:
    for out, r in zip(OUTCOMES, ROWS[pred]):
        data.append({
            "pred": pred, "out": out,
            "r": r,
            "txt": "—" if r is None else f"{r:.2f}".lstrip("0"),
            "nodata": r is None,
        })

width, height = 520, 470
f = fonts(width)

base = alt.Chart(alt.Data(values=data)).encode(
    x=alt.X("out:N", sort=col_order, title="Life Outcome  (sorted by avg |r|)",
            axis=alt.Axis(labelAngle=-30, labelLimit=200, orient="bottom")),
    y=alt.Y("pred:N", sort=order, title="Predictor  (sorted by avg |r|)",
            axis=alt.Axis(labelLimit=200)),
)

# Valued cells: red ramp. No-data cells: flat muted fill.
cells = base.transform_filter("datum.nodata == false").mark_rect(stroke=BG, strokeWidth=1.5).encode(
    color=alt.Color("r:Q",
                    scale=alt.Scale(domain=[0, 0.6], range=[BG, "#c1432e"], clamp=True),
                    legend=alt.Legend(title="|r|", gradientLength=180)))
blanks = base.transform_filter("datum.nodata == true").mark_rect(
    fill=GRID, stroke=BG, strokeWidth=1.5)
labels = base.mark_text(fontSize=f["label"], fontWeight="bold").encode(
    text="txt:N",
    color=alt.condition("datum.nodata", alt.value(MUTED), alt.value("#f2f3f5")))

chart = (cells + blanks + labels).properties(
    width=width, height=height,
    title=alt.TitleParams(text="What Predicts Life Outcomes?"))

save(chart, "heatmap", width)
