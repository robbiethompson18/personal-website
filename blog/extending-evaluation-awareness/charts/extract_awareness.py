"""Pull eval-awareness rates out of the decomposing-eval-awareness repo into a CSV.

Reads the judged result files from the 2026-08-31 -> 09-01 overnight sweep (responses generated
20260901_005920, the run whose config matches the paper: OFAT baseline + F1..F8, 100 HarmBench-
adapted task pairs x 3 samples, no F9-F12 extras) and writes charts/awareness_rates.csv with one
row per (model, probe, config, valence): yes count and graded count (yes+no; n/a and invalid
excluded from the denominator, same as the repo's plots/plot_awareness.py).

Two probes:
  cot        - external judge (gpt-5.6-terra, sonnet-5 backup) reads the model's reasoning. This is
               the paper's instrument.
  selfreport - the model is shown its own transcript and asked whether it was in an eval.

The all_varied / harmbench_verbatim anchor configs only exist for the five open-weight models
(50 tasks, safety arm); see the repo's .claude/notes/harmbench-anchor-configs.md.

Run from the post dir:  python3 charts/extract_awareness.py
"""

import csv
import json
import os
from collections import defaultdict

REPO = os.path.expanduser("~/repos/decomposing-eval-awareness/results/eval_bench")

# model -> probe -> result files. cot files are the gpt-5.6-terra re-judges from the 1425xx batch
# (every roster model, anchors included for OW); selfreport anchors were a separate run.
FILES = {
    "claude-sonnet-4.5": {
        "cot": ["cot_claude-sonnet-4.5_20260901_142454.json"],
        "selfreport": ["selfreport_claude-sonnet-4.5_20260901_033516.json"],
    },
    "claude-haiku-4.5": {
        "cot": ["cot_claude-haiku-4.5_20260901_142524.json"],
        "selfreport": ["selfreport_claude-haiku-4.5_20260901_034056.json"],
    },
    "gpt-5": {
        "cot": ["cot_gpt-5_20260901_142448.json"],
        "selfreport": ["selfreport_gpt-5_20260901_141533.json"],
    },
    "gpt-5.1": {
        "cot": ["cot_gpt-5.1_20260901_142738.json"],
        "selfreport": ["selfreport_gpt-5.1_20260901_143914.json"],
    },
    "gpt-5.2": {
        "cot": ["cot_gpt-5.2_20260901_142502.json"],
        "selfreport": ["selfreport_gpt-5.2_20260901_140000.json"],
    },
    "gpt-5.4": {
        "cot": ["cot_gpt-5.4_20260901_142611.json"],
        "selfreport": ["selfreport_gpt-5.4_20260901_140552.json"],
    },
    "gpt-5.6-sol": {
        "cot": ["cot_gpt-5.6-sol_20260901_142546.json"],
        "selfreport": ["selfreport_gpt-5.6-sol_20260901_142348.json"],
    },
    "gemini-3.1-pro": {
        "cot": ["cot_gemini-3.1-pro_20260901_142317.json"],
        "selfreport": ["selfreport_gemini-3.1-pro_20260901_150913.json"],
    },
    "gemini-3.5-flash": {
        "cot": ["cot_gemini-3.5-flash_20260901_142512.json"],
        "selfreport": ["selfreport_gemini-3.5-flash_20260901_094919.json"],
    },
    "qwen3.8-2.4t": {
        "cot": ["cot_qwen3.8-2.4t_20260901_142510.json"],
        "selfreport": [
            "selfreport_qwen3.8-2.4t_20260901_081110.json",
            "selfreport_qwen3.8-2.4t_20260901_153313.json",
        ],
    },
    "deepseek-v4-pro": {
        "cot": ["cot_deepseek-v4-pro_20260901_142806.json"],
        "selfreport": [
            "selfreport_deepseek-v4-pro_20260901_091928.json",
            "selfreport_deepseek-v4-pro_20260901_153510.json",
        ],
    },
    "kimi-k3": {
        "cot": ["cot_kimi-k3_20260901_142534.json"],
        "selfreport": [
            "selfreport_kimi-k3_20260901_085934.json",
            "selfreport_kimi-k3_20260901_153713.json",
        ],
    },
    "glm-5.3": {
        "cot": ["cot_glm-5.3_20260901_142520.json"],
        "selfreport": [
            "selfreport_glm-5.3_20260901_055442.json",
            "selfreport_glm-5.3_20260901_153455.json",
        ],
    },
    "minimax-m3": {
        "cot": ["cot_minimax-m3_20260901_142554.json"],
        "selfreport": [
            "selfreport_minimax-m3_20260901_074409.json",
            "selfreport_minimax-m3_20260901_153245.json",
        ],
    },
}


def records(path):
    with open(path) as f:
        data = json.load(f)
    return data["samples"] if isinstance(data, dict) else data


def conclusion(rec):
    """'yes' / 'no' / other. Mirrors core.metrics in the repo."""
    judge = rec.get("judge")
    if isinstance(judge, str):  # some files store the judge JSON as a string
        try:
            judge = json.loads(judge)
        except ValueError:
            return "invalid"
    if not isinstance(judge, dict):
        return "invalid"
    section = judge.get("model_awareness")
    if not isinstance(section, dict):
        return "invalid"
    val = section.get("conclusion")
    return val.strip().lower() if isinstance(val, str) else "invalid"


def main():
    counts = defaultdict(lambda: [0, 0])  # (model, probe, config, valence) -> [yes, graded]
    for model, probes in FILES.items():
        for probe, files in probes.items():
            for fname in files:
                for rec in records(os.path.join(REPO, probe, fname)):
                    c = conclusion(rec)
                    key = (model, probe, rec["config_name"], rec["valence"])
                    counts[key][0] += c == "yes"
                    counts[key][1] += c in ("yes", "no")
    out = "charts/awareness_rates.csv"
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["model", "probe", "config", "valence", "yes", "graded"])
        for key in sorted(counts):
            w.writerow([*key, *counts[key]])
    print(f"wrote {out}: {len(counts)} rows")


if __name__ == "__main__":
    main()
