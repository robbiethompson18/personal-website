"""Self-reported eval awareness per model, grouped by lab.

Horizontal bars, one per model, colored by lab (same hues and lab names as ladder.py). Models are
sorted by rate (highest first); the legend lists labs by their pooled rate and sits bottom-right,
next to the shortest bars. Whisker = Wilson 95% CI on the per-model rate. Safety tasks, baseline config
only (the as-shipped prompts, no factor made artificial). Value label at the whisker's end.

Data: charts/awareness_rates.csv from extract_awareness.py. Writes awareness-by-lab.

Run from the post dir:  python3 charts/awareness_by_lab.py
"""

import csv
import math
from collections import defaultdict

import altair as alt

from theme import BG, FG, LAB, WHISK, fonts, save

MODELS = {  # key -> (display, lab); same as ladder.py plus Gemini 3.1 Pro (no ladder tiers)
    "claude-sonnet-4.5": ("Claude Sonnet 4.5", "Anthropic"),
    "claude-haiku-4.5": ("Claude Haiku 4.5", "Anthropic"),
    "gpt-5": ("GPT-5", "OpenAI"),
    "gpt-5.1": ("GPT-5.1", "OpenAI"),
    "gpt-5.2": ("GPT-5.2", "OpenAI"),
    "gpt-5.4": ("GPT-5.4", "OpenAI"),
    "gpt-5.6-sol": ("GPT-5.6", "OpenAI"),
    "gemini-3.1-pro": ("Gemini 3.1 Pro", "Google"),
    "gemini-3.5-flash": ("Gemini 3.5 Flash", "Google"),
    "qwen3.8-2.4t": ("Qwen3.8", "Alibaba"),
    "deepseek-v4-pro": ("DeepSeek V4 Pro", "DeepSeek"),
    "kimi-k3": ("Kimi K3", "Moonshot"),
    "glm-5.3": ("GLM-5.3", "Z.ai"),
    "minimax-m3": ("MiniMax M3", "MiniMax"),
}
WIDTH, ROW_H = 600, 26


def wilson(k, n, z=1.96):
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h


counts = {}  # model -> [yes, graded]
with open("charts/awareness_rates.csv") as fh:
    for row in csv.DictReader(fh):
        if (row["probe"], row["config"], row["valence"]) == ("selfreport", "baseline", "safety"):
            counts[row["model"]] = [int(row["matched"]), int(row["graded"])]

lab_tot = defaultdict(lambda: [0, 0])
for key, (_, lab) in MODELS.items():
    lab_tot[lab][0] += counts[key][0]
    lab_tot[lab][1] += counts[key][1]
labs = sorted(LAB, key=lambda lab: -lab_tot[lab][0] / lab_tot[lab][1])

rows = []
for key, (name, lab) in MODELS.items():
    yes, graded = counts[key]
    lo, hi = wilson(yes, graded)
    rows.append({"model": name, "lab": lab, "rate": 100 * yes / graded,
                 "lo": 100 * lo, "hi": 100 * hi, "txt": f"{100 * yes / graded:.0f}%"})
rows.sort(key=lambda r: -r["rate"])
order = [r["model"] for r in rows]

f = fonts(WIDTH)
base = alt.Chart(alt.Data(values=rows)).encode(
    y=alt.Y("model:N", sort=order, title=None, axis=alt.Axis(labelLimit=320)))
bars = base.mark_bar(cornerRadiusTopRight=3, cornerRadiusBottomRight=3, stroke=BG,
                     strokeWidth=1).encode(
    x=alt.X("rate:Q", title="Self-Reported Eval Awareness (% of Graded Samples)",
            scale=alt.Scale(domain=[0, 100]), axis=alt.Axis(tickCount=5, grid=True)),
    color=alt.Color("lab:N", title=None,
                    scale=alt.Scale(domain=labs, range=[LAB[lab] for lab in labs]),
                    legend=alt.Legend(orient="bottom-right", direction="vertical",
                                      symbolType="square", offset=8)),
)
ci = base.mark_rule(color=WHISK, strokeWidth=1.5).encode(x="lo:Q", x2="hi:Q")
labels = base.mark_text(align="left", dx=6, fontSize=f["label"], fontWeight="bold",
                        color=FG).encode(x="hi:Q", text="txt:N")
chart = (bars + ci + labels).properties(
    width=WIDTH, height=ROW_H * len(rows),
    title=alt.TitleParams(
        text="Self-Reported Eval Awareness by Lab",
        subtitle=["Safety tasks, baseline config (nothing made artificial), ~300 samples per model.",
                  "Whisker: Wilson 95% CI."]),
).configure_axisY(domain=False, ticks=False)
save(chart, "awareness-by-lab", WIDTH)
