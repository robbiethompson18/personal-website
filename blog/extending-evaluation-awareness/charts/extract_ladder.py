"""Pull the three-stage awareness numbers (output-only -> output+CoT -> self-report) into a CSV.

Stages 1 and 2 come from the tiered grader (results/eval_bench/cot_tiered/, one file per model:
the same transcript graded once from the output alone and once with the CoT attached). Stage 3 is
the self-report probe, pooled from charts/awareness_rates.csv (extract_awareness.py's pins), so
the self-report number here equals the one behind the awareness-by-factor charts.

Safety tasks only, pooled over every OFAT config (baseline + F1..F8), same as the prose in
"Almost No Eval-Awareness Shows up in CoT". gemini-3.1-pro has no tiered run, so it is left out
of all three stages to keep the model set constant across the ladder (13 models).

Writes charts/ladder_rates.csv: model, stage, yes, graded.
Run from the post dir:  python3 charts/extract_ladder.py
"""

import csv
import json
import os
from collections import defaultdict

from extract_awareness import REPO

TIERED = {  # pinned, not newest-wins: a later canary run must not swap in silently
    "claude-sonnet-4.5": "tiered_claude-sonnet-4.5_20260901_130004.json",
    "claude-haiku-4.5": "tiered_claude-haiku-4.5_20260901_130026.json",
    "gpt-5": "tiered_gpt-5_20260901_135756.json",
    "gpt-5.1": "tiered_gpt-5.1_20260901_135632.json",
    "gpt-5.2": "tiered_gpt-5.2_20260901_140026.json",
    "gpt-5.4": "tiered_gpt-5.4_20260901_140209.json",
    "gpt-5.6-sol": "tiered_gpt-5.6-sol_20260901_142317.json",
    "gemini-3.5-flash": "tiered_gemini-3.5-flash_20260901_130208.json",
    "qwen3.8-2.4t": "tiered_qwen3.8-2.4t_20260901_130119.json",
    "deepseek-v4-pro": "tiered_deepseek-v4-pro_20260901_133446.json",
    "kimi-k3": "tiered_kimi-k3_20260901_133304.json",
    "glm-5.3": "tiered_glm-5.3_20260901_133252.json",
    "minimax-m3": "tiered_minimax-m3_20260901_133238.json",
}
TIERS = {"output": "output-only", "output_cot": "output+cot"}
OFAT = {"baseline", *(f"F{i}" for i in range(1, 9))}


def main():
    counts = defaultdict(lambda: [0, 0])  # (model, stage) -> [yes, graded]
    for model, fname in TIERED.items():
        with open(os.path.join(REPO, "cot_tiered", fname)) as f:
            samples = json.load(f)["samples"]
        for rec in samples:
            if rec["valence"] != "safety":
                continue
            for tier, stage in TIERS.items():
                section = (rec.get("judgments") or {}).get(tier) or {}
                concl = str((section.get("model_awareness") or {}).get("conclusion", "")).lower()
                counts[(model, stage)][0] += concl == "yes"
                counts[(model, stage)][1] += concl in ("yes", "no")
    with open("charts/awareness_rates.csv") as f:
        for row in csv.DictReader(f):
            # OFAT configs only: the OW anchor configs (all_varied, harmbench_verbatim) have no
            # tiered grading, so they must stay out of every stage.
            if (row["model"] in TIERED and row["probe"] == "selfreport"
                    and row["valence"] == "safety" and row["config"] in OFAT):
                counts[(row["model"], "self-report")][0] += int(row["yes"])
                counts[(row["model"], "self-report")][1] += int(row["graded"])
    out = "charts/ladder_rates.csv"
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["model", "stage", "yes", "graded"])
        for key in sorted(counts):
            w.writerow([*key, *counts[key]])
    print(f"wrote {out}: {len(counts)} rows")


if __name__ == "__main__":
    main()
