"""Eval awareness by what the monitor can see: output-only -> output + CoT -> self-report.

Slope chart, one line per model colored by lab, plus a thick dashed pooled line (the three numbers
quoted in the prose). Safety tasks, all OFAT configs pooled, 13 models.

Writes two charts:
  awareness-ladder        plain linear y axis
  awareness-ladder-inset  same, plus a zoomed 0-6% panel for the first two stages, drawn in the
                          empty upper-left of the main panel (the legend goes; labels are colored)
LADDER_SCALE=symlog writes a third, awareness-ladder-symlog (linear below ~5%, log above). It was
rejected for the post because it flattens the jump, kept for comparison.

Data: charts/ladder_rates.csv from extract_ladder.py.
Run from the post dir:  python3 charts/ladder.py
"""

import csv
import math
import os
from collections import defaultdict

import altair as alt

from theme import FG, GRID, MUTED, fonts, save

STAGES = ["Output only", "Output + CoT", "Self-report"]
STAGE_OF = {"output-only": STAGES[0], "output+cot": STAGES[1], "self-report": STAGES[2]}
MODELS = {  # key -> (display, lab)
    "claude-sonnet-4.5": ("Claude Sonnet 4.5", "Anthropic"),
    "claude-haiku-4.5": ("Claude Haiku 4.5", "Anthropic"),
    "gpt-5": ("GPT-5", "OpenAI"),
    "gpt-5.1": ("GPT-5.1", "OpenAI"),
    "gpt-5.2": ("GPT-5.2", "OpenAI"),
    "gpt-5.4": ("GPT-5.4", "OpenAI"),
    "gpt-5.6-sol": ("GPT-5.6", "OpenAI"),
    "gemini-3.5-flash": ("Gemini 3.5 Flash", "Google"),
    "qwen3.8-2.4t": ("Qwen3.8", "Alibaba"),
    "deepseek-v4-pro": ("DeepSeek V4 Pro", "DeepSeek"),
    "kimi-k3": ("Kimi K3", "Moonshot"),
    "glm-5.3": ("GLM-5.3", "Z.ai"),
    "minimax-m3": ("MiniMax M3", "MiniMax"),
}
# Lab brand hues (repo plots/style.py), with OpenAI's black lifted to a light grey for the dark
# background and Kimi's gold left at full brightness for the same reason.
LAB_COLOR = {
    "Anthropic": "#d97757", "OpenAI": "#c8ccd4", "Google": "#34a853", "Alibaba": "#c026d3",
    "DeepSeek": "#4d6bfe", "Moonshot": "#fec230", "Z.ai": "#dc2626", "MiniMax": "#22b8d8",
}
POOLED = "All 13 models pooled"
DOMAIN = list(LAB_COLOR) + [POOLED]
RANGE = list(LAB_COLOR.values()) + [FG]
COLOR = alt.Scale(domain=DOMAIN, range=RANGE)
WIDTH = 600
SYMLOG_C = 5  # symlog variant: trades room at the bottom (small) against room for labels (large)

# Inset geometry, in the main panel's data coordinates (x = stage index, y = % awareness).
INSET_BOX = {"x0": -0.08, "x1": 1.08, "y0": 10, "y1": 92}
INSET_X = [0.2, 0.68]  # where the two zoomed stages sit inside the box
INSET_Y = [18, 84]  # where 0% and INSET_MAX% sit inside the box
INSET_MAX = 6


def load():
    counts = defaultdict(lambda: [0, 0])  # (model, stage) -> [yes, graded]
    with open("charts/ladder_rates.csv") as fh:
        for row in csv.DictReader(fh):
            counts[(row["model"], STAGE_OF[row["stage"]])] = [int(row["yes"]), int(row["graded"])]
    points = []
    for key, (name, lab) in MODELS.items():
        for i, stage in enumerate(STAGES):
            yes, graded = counts[(key, stage)]
            points.append({"model": name, "lab": lab, "stage": stage, "x": i,
                           "rate": 100 * yes / graded, "pooled": False})
    for i, stage in enumerate(STAGES):
        yes = sum(counts[(k, stage)][0] for k in MODELS)
        graded = sum(counts[(k, stage)][1] for k in MODELS)
        points.append({"model": POOLED, "lab": POOLED, "stage": stage, "x": i,
                       "rate": 100 * yes / graded, "pooled": True})
    return points


def dodge(values, gap, lo=0.0, hi=1.0):
    """Spread label positions (in [0, 1] axis fractions) so none overlap, none leave [lo, hi].
    Push up past the neighbour below, then push back down from the top."""
    out = []
    for v in values:
        out.append(max(v, (out[-1] if out else -1e9) + gap, lo))
    cap = hi
    for i in range(len(out) - 1, -1, -1):
        out[i] = min(out[i], cap)
        cap = out[i] - gap
    return out


def render(name, symlog=False, inset=False):
    height = 800 if symlog else 440
    f = fonts(WIDTH)
    points = load()
    pooled_rate = {p["stage"]: p["rate"] for p in points if p["pooled"]}

    if symlog:  # Vega symlog: sign(x) * log1p(|x| / c), normalised to the [0, 100] domain
        def to_frac(r): return math.log1p(r / SYMLOG_C) / math.log1p(100 / SYMLOG_C)
        def from_frac(q): return SYMLOG_C * math.expm1(q * math.log1p(100 / SYMLOG_C))
        y_scale = alt.Scale(type="symlog", constant=SYMLOG_C, domain=[0, 100])
        y_ticks = [0, 0.5, 1, 2, 5, 10, 20, 50, 100]
    else:
        def to_frac(r): return r / 100
        def from_frac(q): return q * 100
        y_scale = alt.Scale(domain=[0, 100])
        y_ticks = [0, 20, 40, 60, 80, 100]

    # Right-edge labels: text is ~1.1 x font px tall; dodge in axis-fraction space.
    gap = 1.1 * f["label"] / height
    ends = sorted((p for p in points if p["x"] == 2), key=lambda p: p["rate"])
    fracs = dodge([to_frac(p["rate"]) for p in ends], gap)
    labels = [{**p, "y": from_frac(q), "txt": f'{p["model"]}  {p["rate"]:.0f}%'}
              for p, q in zip(ends, fracs)]

    label_expr = " : ".join(
        f"datum.value == {i} ? '{s} ({pooled_rate[s]:.1f}%)'" for i, s in enumerate(STAGES)
    ) + " : ''"
    legend = None if inset else alt.Legend(
        title=None, orient="top-left", offset=8, symbolType="stroke", symbolStrokeWidth=3,
        values=list(LAB_COLOR))
    base = alt.Chart(alt.Data(values=points)).encode(
        x=alt.X("x:Q", title="What the Monitor Can See (Pooled Rate)",
                scale=alt.Scale(domain=[-0.15, 2.15], nice=False),
                axis=alt.Axis(values=[0, 1, 2], labelExpr=label_expr, labelAngle=0,
                              labelPadding=8, grid=False)),
        y=alt.Y("rate:Q", title="Eval Awareness (% of Graded Samples)", scale=y_scale,
                axis=alt.Axis(values=y_ticks, format=".1~f")),
        color=alt.Color("lab:N", scale=COLOR, legend=legend),
        detail="model:N",
    )
    models = base.transform_filter("datum.pooled == false")
    pooled = base.transform_filter("datum.pooled == true")
    layers = [
        models.mark_line(strokeWidth=2, opacity=0.9),
        models.mark_point(filled=True, size=55, opacity=1),
        pooled.mark_line(strokeWidth=4, strokeDash=[7, 5]),
        pooled.mark_point(filled=True, size=110, opacity=1),
    ]
    label_base = alt.Chart(alt.Data(values=labels)).encode(
        x="x:Q", y="y:Q", text="txt:N", color=alt.Color("lab:N", scale=COLOR, legend=None))
    layers += [
        label_base.transform_filter("datum.pooled == false").mark_text(
            align="left", baseline="middle", dx=12, fontSize=f["label"]),
        label_base.transform_filter("datum.pooled == true").mark_text(
            align="left", baseline="middle", dx=12, fontSize=f["label"], fontWeight="bold"),
    ]
    if inset:
        layers += inset_layers(points, f, gap * 100 / (INSET_Y[1] - INSET_Y[0]))

    subtitle = ["Safety tasks, all factor configs pooled, 13 models. Stages 1-2: GPT-5.6 judge",
                "reads the transcript without / with CoT. Stage 3: the model is asked."
                + (" Log-ish y axis." if symlog else "")]
    chart = alt.layer(*layers).properties(
        width=WIDTH, height=height, padding={"left": 5, "top": 5, "bottom": 5, "right": 150},
        title=alt.TitleParams(text="Eval Awareness by What the Monitor Can See", subtitle=subtitle),
    ).configure_axisY(domain=False)
    save(chart, name, WIDTH)


def inset_layers(points, f, gap):
    """Zoomed panel for stages 1-2, drawn as marks in the main panel's coordinate system.
    `gap` is the label dodge gap in inset-fraction units."""
    b = INSET_BOX

    def ix(i): return INSET_X[i]
    def iy(rate): return INSET_Y[0] + rate / INSET_MAX * (INSET_Y[1] - INSET_Y[0])

    zoom = [{**p, "ix": ix(p["x"]), "iy": iy(p["rate"])} for p in points if p["x"] < 2]
    ticks = [{"iy": iy(t), "txt": f"{t}%"} for t in range(0, INSET_MAX + 1, 2)]
    heads = [{"ix": ix(i), "iy": INSET_Y[0] - 4, "txt": s} for i, s in enumerate(STAGES[:2])]
    # Value labels beside each column; models sharing a value (the 0% GPT-5.x pile) get one label.
    vals = []
    for i in (0, 1):
        col = {}
        for p in zoom:
            if p["x"] == i:
                col.setdefault((round(p["rate"], 1), p["lab"]), p)
        ordered = sorted(col.values(), key=lambda p: p["rate"])
        fr = dodge([p["rate"] / INSET_MAX for p in ordered], gap)
        for p, q in zip(ordered, fr):
            vals.append({**p, "ix": ix(i), "iy": iy(q * INSET_MAX), "txt": f'{p["rate"]:.1f}',
                         "side": i})

    box = alt.Chart(alt.Data(values=[b])).mark_rect(
        fill="#20242c", stroke=MUTED, strokeWidth=1, cornerRadius=4).encode(
        x="x0:Q", x2="x1:Q", y="y0:Q", y2="y1:Q")
    grid = alt.Chart(alt.Data(values=ticks)).mark_rule(color=GRID, strokeWidth=1).encode(
        x=alt.datum(b["x0"] + 0.02), x2=alt.datum(b["x1"] - 0.02), y="iy:Q")
    tick_txt = alt.Chart(alt.Data(values=ticks)).mark_text(
        align="left", baseline="bottom", dy=-2, fontSize=f["label"] * 0.85, color=MUTED).encode(
        x=alt.datum(b["x0"] + 0.03), y="iy:Q", text="txt:N")
    head_txt = alt.Chart(alt.Data(values=heads)).mark_text(
        align="center", baseline="top", fontSize=f["label"], color=FG).encode(
        x="ix:Q", y="iy:Q", text="txt:N")
    title = alt.Chart(alt.Data(values=[{"txt": "Stages 1-2, zoomed"}])).mark_text(
        align="left", baseline="top", fontSize=f["label"], fontWeight="bold", color=FG).encode(
        x=alt.datum(b["x0"] + 0.03), y=alt.datum(b["y1"] - 1.5), text="txt:N")
    zb = alt.Chart(alt.Data(values=zoom)).encode(
        x="ix:Q", y="iy:Q", color=alt.Color("lab:N", scale=COLOR, legend=None), detail="model:N")
    zm = zb.transform_filter("datum.pooled == false")
    zp = zb.transform_filter("datum.pooled == true")
    vb = alt.Chart(alt.Data(values=vals)).encode(
        x="ix:Q", y="iy:Q", text="txt:N", color=alt.Color("lab:N", scale=COLOR, legend=None))
    return [
        box, grid, tick_txt, head_txt, title,
        zm.mark_line(strokeWidth=2, opacity=0.9),
        zm.mark_point(filled=True, size=55, opacity=1),
        zp.mark_line(strokeWidth=4, strokeDash=[7, 5]),
        zp.mark_point(filled=True, size=110, opacity=1),
        vb.transform_filter("datum.side == 0").mark_text(
            align="right", baseline="middle", dx=-10, fontSize=f["label"] * 0.85),
        vb.transform_filter("datum.side == 1").mark_text(
            align="left", baseline="middle", dx=10, fontSize=f["label"] * 0.85),
    ]


if __name__ == "__main__":
    render("awareness-ladder")
    render("awareness-ladder-inset", inset=True)
    if os.environ.get("LADDER_SCALE") == "symlog":
        render("awareness-ladder-symlog", symlog=True)
