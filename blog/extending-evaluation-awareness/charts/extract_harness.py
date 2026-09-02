"""Pull the harness-feature run (2026-09-01 ~21:50 PT, RUN_TAG=harness) into a CSV.

Six cells per model: bare_harness (all harness features off), bare+F9 (T3 system prompt),
bare+F11 (opener turn), bare+F12 (live web_search tool), bare+F13 (typos), baseline (all four on).
8 models (roster minus OpenAI minus Haiku), 100 task pairs, 1 sample. Writes
charts/harness_rates.csv with one row per (model, probe, cell, valence): yes, graded, and for the
paired-delta columns the number of tasks that flipped up / down relative to bare_harness.

Also prints the pooled paired deltas used in the post's "More methods for realism" section.

Run from the post dir:  python3 charts/extract_harness.py
"""

import csv
import glob
import json
import os
from collections import defaultdict

REPO = os.path.expanduser("~/repos/decomposing-eval-awareness/results/eval_bench")
STAMP = "harness_20260901_215048"
CELLS = ["bare_harness", "bare+F9", "bare+F11", "bare+F12", "bare+F13", "baseline"]


def conclusion(rec):
    judge = rec.get("judge")
    if isinstance(judge, str):
        try:
            judge = json.loads(judge)
        except ValueError:
            return "invalid"
    section = judge.get("model_awareness") if isinstance(judge, dict) else None
    val = section.get("conclusion") if isinstance(section, dict) else None
    return val.strip().lower() if isinstance(val, str) else "invalid"


def main():
    sources = {}
    for path in glob.glob(f"{REPO}/response/responses_*_{STAMP}.json"):
        sources[os.path.basename(path)] = json.load(open(path))["model"]
    # probe -> model -> (task, valence) -> cell -> yes/no
    verdicts = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
    for path in glob.glob(f"{REPO}/selfreport/selfreport_*_2026090*.json"):
        data = json.load(open(path))
        model = sources.get(os.path.basename(data.get("source_response_file", "")))
        if not model:
            continue
        for rec in data["samples"]:
            c = conclusion(rec)
            if c in ("yes", "no"):
                verdicts["selfreport"][model][(rec["task_name"], rec["valence"])][rec["config_name"]] = c == "yes"
    for path in glob.glob(f"{REPO}/cot/cot_*_2026090*.json"):
        recs = json.load(open(path))
        recs = recs.get("samples", recs) if isinstance(recs, dict) else recs
        if not recs or not recs[0]["id"].split("_sample")[0].endswith(tuple(CELLS)):
            continue
        if not all(r["config_name"] in CELLS for r in recs):
            continue
        model = os.path.basename(path).split("_")[1]
        if model not in sources.values():
            continue
        for rec in recs:
            c = conclusion(rec)
            if c in ("yes", "no"):
                verdicts["cot"][model][(rec["task_name"], rec["valence"])][rec["config_name"]] = c == "yes"

    rows = []
    pooled = defaultdict(lambda: defaultdict(lambda: [0, 0, 0, 0]))  # probe -> (cell,val) -> yes,n,up,down
    for probe, models in verdicts.items():
        for model, tasks in models.items():
            for cell in CELLS:
                for val in ("safety", "capability"):
                    yes = n = up = down = 0
                    for (task, v), cells in tasks.items():
                        if v != val or cell not in cells:
                            continue
                        yes += cells[cell]
                        n += 1
                        if "bare_harness" in cells and cell != "bare_harness":
                            up += cells[cell] and not cells["bare_harness"]
                            down += cells["bare_harness"] and not cells[cell]
                    rows.append([model, probe, cell, val, yes, n, up, down])
                    p = pooled[probe][(cell, val)]
                    p[0] += yes; p[1] += n; p[2] += up; p[3] += down
    out = "charts/harness_rates.csv"
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["model", "probe", "cell", "valence", "yes", "graded", "up_vs_bare", "down_vs_bare"])
        w.writerows(sorted(rows))
    print(f"wrote {out}: {len(rows)} rows, models: {sorted(verdicts['selfreport'])}")
    for probe in ("selfreport", "cot"):
        for val in ("safety", "capability"):
            print(f"-- {probe} {val}")
            for cell in CELLS:
                yes, n, up, down = pooled[probe][(cell, val)]
                delta = f"  paired delta {100 * (up - down) / n:+.1f} pp (+{up}/-{down})" if cell != "bare_harness" else ""
                print(f"   {cell:13} {100 * yes / n:5.1f}% (n={n}){delta}")


if __name__ == "__main__":
    main()
