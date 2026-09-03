"""Distribution of the PDV projection, split by self-reported awareness, one panel per model.

Every unsteered EvalAwareBench transcript per model (~5-6k), read at the model's readout layer,
projected onto PDV and expressed in d-units: (projection - mean over real chat prompts) / pooled SD
of the chat and benchmark training prompts. Two density curves per panel: transcripts where the
model later self-reported being evaluated vs not. Overlap is the story.

Data: charts/pdv_distribution_bins.csv (per-model, per-label histogram of pdv_d in 0.25-unit
bins, as fractions), built from charts/pdv_distribution.csv which was exported from the
decomposing-eval-awareness repo (results/probes/*). Writes pdv-distribution.

Run from the post dir:  python3 charts/pdv_distribution.py
"""

import csv

import altair as alt

from theme import FG, fonts, save

WIDTH = 620
MODELS = ["Qwen3.8-27B", "GPT-OSS-20B", "Gemma 4 31B"]
COLORS = {"aware": "#c1432e", "not aware": "#2e7dc1"}


def main() -> None:
    f = fonts(WIDTH)
    with open("charts/pdv_distribution_bins.csv") as fh:
        rows = [
            {
                **r,
                "bin_lo": float(r["bin_lo"]),
                "bin_hi": float(r["bin_hi"]),
                "frac": float(r["frac"]),
                "zero": 0.0,
            }
            for r in csv.DictReader(fh)
        ]
    base = alt.Chart(alt.Data(values=rows))
    hist = base.mark_bar(opacity=0.6).encode(
        x=alt.X(
            "bin_lo:Q",
            title="PDV Projection (d-units)",
            scale=alt.Scale(domain=[-4, 4]),
            axis=alt.Axis(values=[-4, -2, 0, 2, 4]),
        ),
        x2="bin_hi:Q",
        y=alt.Y("frac:Q", title=None, axis=None, stack=None, scale=alt.Scale(nice=False)),
        y2="zero:Q",
        color=alt.Color(
            "self_reported:N",
            title="Self-Reported",
            scale=alt.Scale(domain=list(COLORS), range=list(COLORS.values())),
            legend=alt.Legend(orient="top"),
        ),
    )
    chart = (
        hist.properties(width=WIDTH, height=110)
        .facet(
            row=alt.Row(
                "model:N",
                title=None,
                sort=MODELS,
                header=alt.Header(
                    labelColor=FG, labelFontSize=f["label"], labelAngle=0, labelAlign="left"
                ),
            )
        )
        .properties(title="PDV Projection by Self-Reported Awareness")
        .resolve_scale(y="independent")
    )
    save(chart, "pdv-distribution", WIDTH)


if __name__ == "__main__":
    main()
