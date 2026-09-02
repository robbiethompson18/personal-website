"""Refusal rates for the giant run (2026-09-01, baseline + F1..F8, 13 roster models) into a CSV.

Reads the same pinned CoT-judge files plots/plot_awareness.py uses (BIG_RUN, the 14:2x
gpt-5.6-terra sweep) and buckets every sample three ways:

  model_refused  judge graded task_performance == "refused" (the model declined in its own words,
                 or inside the think tool — Haiku's usual way)
  api_blocked    the request never got a model answer: Anthropic's classifier stop_reason=refusal
                 (stored as an empty response), Anthropic's output content filter (lyrics),
                 OpenAI's cyber / usage-policy prompt filter, Gemini promptFeedback block, or a
                 lab-side filter that returned an empty completion
  answered       everything the judge graded correct / guarded / incorrect

Transport errors (rate limits, SSL, the OpenAI ban) and judge N/A / invalid verdicts are dropped
from the denominator. Writes charts/refusal_rates.csv, one row per (model, lab, valence).

Run from the post dir:  python3 charts/extract_refusals.py
"""

import csv
import json
import os
import re
from collections import defaultdict

REPO = os.path.expanduser("~/repos/decomposing-eval-awareness/results/eval_bench/cot")
# model -> (lab, pinned CoT-judge file). Lab is the attribution used on the chart; the five
# open-weight labs stay separate.
PINS = {
    "claude-sonnet-4.5": ("Anthropic", "cot_claude-sonnet-4.5_20260901_142454.json"),
    "claude-haiku-4.5": ("Anthropic", "cot_claude-haiku-4.5_20260901_142524.json"),
    "gpt-5": ("OpenAI", "cot_gpt-5_20260901_142448.json"),
    "gpt-5.1": ("OpenAI", "cot_gpt-5.1_20260901_142738.json"),
    "gpt-5.2": ("OpenAI", "cot_gpt-5.2_20260901_142502.json"),
    "gpt-5.4": ("OpenAI", "cot_gpt-5.4_20260901_142611.json"),
    "gpt-5.6-sol": ("OpenAI", "cot_gpt-5.6-sol_20260901_142546.json"),
    "gemini-3.1-pro": ("Google", "cot_gemini-3.1-pro_20260901_142317.json"),
    "gemini-3.5-flash": ("Google", "cot_gemini-3.5-flash_20260901_142512.json"),
    "qwen3.8-2.4t": ("Alibaba", "cot_qwen3.8-2.4t_20260901_142510.json"),
    "deepseek-v4-pro": ("DeepSeek", "cot_deepseek-v4-pro_20260901_142806.json"),
    "kimi-k3": ("Moonshot", "cot_kimi-k3_20260901_142534.json"),
    "glm-5.3": ("Z.ai", "cot_glm-5.3_20260901_142520.json"),
    "minimax-m3": ("MiniMax", "cot_minimax-m3_20260901_142554.json"),
}
# Provider-side filters that come back as an API error rather than a model answer.
FILTER_RE = re.compile(
    r"flagged|blocked \(|usage policy|content filtering|data_inspection|inappropriate content",
    re.I,
)


def split_think(response):
    if "</think>" in response:
        reasoning, answer = response.split("</think>", 1)
        return reasoning.replace("<think>", "").strip(), answer.strip()
    return "", response.strip()


def bucket(rec):
    resp = rec.get("response") or ""
    if resp.startswith("ERROR calling"):
        return "api_blocked" if FILTER_RE.search(resp) else "dropped"
    reasoning, answer = split_think(resp)
    if not reasoning and not answer:
        return "api_blocked"
    judge = rec.get("judge") or {}
    task = (judge.get("task_performance") or {}).get("conclusion")
    task = task.strip().lower() if isinstance(task, str) else ""
    if task == "refused":
        return "model_refused"
    if task in ("correct", "guarded", "incorrect", "yes", "no"):
        return "answered"
    return "dropped"


def main():
    counts = defaultdict(lambda: defaultdict(int))
    for model, (lab, fname) in PINS.items():
        recs = json.load(open(os.path.join(REPO, fname)))
        recs = recs.get("samples", recs) if isinstance(recs, dict) else recs
        for rec in recs:
            counts[(model, lab, rec["valence"])][bucket(rec)] += 1
    out = "charts/refusal_rates.csv"
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["model", "lab", "valence", "answered", "model_refused", "api_blocked", "dropped"])
        for (model, lab, valence), c in sorted(counts.items()):
            w.writerow([model, lab, valence, c["answered"], c["model_refused"], c["api_blocked"], c["dropped"]])
    print(f"wrote {out}")
    pooled = defaultdict(lambda: defaultdict(int))
    for (model, lab, valence), c in counts.items():
        for k, v in c.items():
            pooled[(lab, valence)][k] += v
    for (lab, valence), c in sorted(pooled.items()):
        n = c["answered"] + c["model_refused"] + c["api_blocked"]
        print(
            f"{lab:12} {valence:10} n={n:6d}  model refused {100 * c['model_refused'] / n:5.1f}%"
            f"  api blocked {100 * c['api_blocked'] / n:5.1f}%  dropped {c['dropped']}"
        )


if __name__ == "__main__":
    main()
