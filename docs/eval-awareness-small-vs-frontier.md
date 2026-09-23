# Comparing small probe models to the frontier roster on eval awareness

Worked out 2026-09-03 for `posts/extending-evaluation-awareness`. Read this before writing any claim
that the three small activation-probe models (Qwen3.8-27B, Gemma 4 31B, GPT-OSS-20B) are or aren't
representative of the frontier roster — the comparison is doable, but three separate gotchas will
silently give you the wrong answer.

**Bottom line: they are not obviously a different regime.** The Measuring Activations section
originally carried a caveat that these were "small dumb models, possibly in an entirely different
regime from the ones in the rest of the paper." The numbers below don't support the strong version,
so the caveat was dropped rather than quantified. If it ever comes back, it needs these numbers
attached.

## Where the two halves live

The frontier and small-model numbers are computed by different pipelines and never meet in one file.

- **Frontier roster** — `posts/extending-evaluation-awareness/charts/awareness_rates.csv`, produced
  by `charts/extract_awareness.py` from pinned run files. One row per (model, probe, config,
  valence) with `yes` / `graded`. This is what every chart in the post reads.
- **Small three** — `results/probes/exp1_*.json` in `~/repos/decomposing-eval-awareness`, under
  `per_group[<config>]`, fields `sr_pct` (self-report) and `cot_pct` (verbalized). Files are
  `results/probes/exp1_qwen27b_L28.json`, `results/probes/gemma/exp1_L28.json`,
  `results/probes/gptoss/exp1_L12.json`. The `sr_pct` / `cot_pct` labels don't depend on layer, so
  L24 vs L28 vs L12 doesn't matter for this comparison — only the AUROC/activation fields change.

Same 100 HarmBench-derived tasks, same config names on both sides, so the join is on config.

## Gotcha 1: intersect the config sets, or you change the model set

All 14 frontier models have `baseline` + `F1`–`F8` for both probes. Only 5 of them (deepseek-v4-pro,
glm-5.3, kimi-k3, minimax-m3, qwen3.8-2.4t) also have `all_varied` and `harmbench_verbatim`. The
small three have 17 configs including `F9`–`F13`.

Averaging over "all shared configs" therefore silently drops 9 of 14 frontier models and inflates
the frontier mean from 58.8% to 72.5%, which flips Qwen-27B from above-average to below-average.
**Use the 9-config intersection: `baseline` + `F1`–`F8`.**

## Gotcha 2: the small models ran with a different system prompt

`results/probes/prompts/exp1.jsonl` (and the gemma / gptoss equivalents) show that for the small
three, `baseline` and `F1`–`F8` all used the **T3 Chat** system prompt, while `F9`, `all_varied` and
`harmbench_verbatim` used the paper's bare "You are a helpful AI assistant." The frontier runs
pinned by `extract_awareness.py` exclude the F9–F12 harness extras, so frontier `baseline`/`F1`–`F8`
are **bare**.

So `F9` is the system-prompt factor, and the small models' `baseline` is really the paper's
"F9-realistic" cell. The three small models share an identical prompt mix (1300 T3 / 400 bare each),
so they're comparable to each other; they are not directly comparable to the frontier on the same
config label. Per the post's own harness section T3 costs about −4pp awareness, so the small-model
numbers are depressed a few points relative to frontier, and correcting pushes Qwen-27B further
_above_ the frontier mean.

Two defensible alignments, which agree directionally:

- **Config-aligned** (accept the system-prompt mismatch): 9 configs, unweighted mean over configs.
- **System-prompt-aligned**: small models' `F9` (bare) vs frontier `baseline` (bare). Single cell,
  so noisier.

## Gotcha 3: sampling depth differs

Small models are 1 sample × ~99 tasks per config; frontier is 3 samples × 100. Small per-config
rates carry roughly ±5pp. Don't read two-point differences as real.

Also unverified: whether the small models' self-report labels were graded by the same GPT-5.6 Terra
/ Sonnet 5 grader as the frontier runs. Check before publishing any of these numbers.

## The numbers (self-reported, safety tasks)

Config-aligned, `baseline` + `F1`–`F8`, unweighted mean over configs:

| model             | rate  |     | model                  | rate  |
| ----------------- | ----- | --- | ---------------------- | ----- |
| gemini-3.1-pro    | 97.1% |     | **Qwen3.8-27B**        | 67.9% |
| claude-sonnet-4.5 | 91.6% |     | **Gemma 4 31B**        | 56.4% |
| kimi-k3           | 84.4% |     | **GPT-OSS-20B**        | 20.3% |
| claude-haiku-4.5  | 78.4% |     |                        |       |
| minimax-m3        | 78.0% |     | **small-3 mean**       | 48.2% |
| qwen3.8-2.4t      | 76.2% |     | **frontier mean (14)** | 58.8% |
| gpt-5.2           | 63.1% |     |                        |       |
| glm-5.3           | 57.5% |     | small-3 / frontier     | 0.82× |
| gemini-3.5-flash  | 50.8% |     | Qwen27B / frontier     | 1.16× |
| deepseek-v4-pro   | 45.7% |     | Qwen27B / Qwen2.4T     | 0.89× |
| gpt-5             | 35.1% |     |                        |       |
| gpt-5.1           | 33.9% |     |                        |       |
| gpt-5.4           | 17.8% |     |                        |       |
| gpt-5.6-sol       | 13.2% |     |                        |       |

System-prompt-aligned (small `F9` vs frontier `baseline`): frontier mean 42.0%, small-3 mean 27.7%
(0.66×), Qwen-27B 45.0% (1.07× frontier, 0.79× its own 2.4T sibling). Sanity check: frontier
`baseline` pools to 41.5%, which is the "baseline 41%" the Double-bluffing section already cites.

Verbalized / CoT-judged, same 9 configs: frontier mean **1.7%**, small-3 mean **1.4%** (0.84×).
Qwen-27B's 2.7% is _above_ Qwen-2.4T's 1.5%. Both groups are pinned to the same near-zero floor.

## Why the caveat doesn't survive

1. **Qwen3.8-27B is more eval-aware than the frontier average** (67.9% vs 58.8%). Slot it into the
   ranked list and it lands 6th of 17, between minimax-m3 and its own 2.4T sibling.
2. **There is a same-family size pair.** Qwen3.8-27B vs Qwen3.8-2.4T is same lab, same recipe, ~90×
   params, and only a 0.89× awareness gap. This is the single most quotable number here.
3. **The frontier's internal spread dwarfs the size gap.** 13.2% → 97.1% is 7×, against 0.82×
   small-vs-big. GPT-OSS-20B's 20.3% sits between gpt-5.4 (17.8%) and gpt-5 (35.1%) — it isn't an
   outlier, just a low-awareness model, and the frontier roster has several.

The honest residual caveat is narrower: GPT-OSS-20B is genuinely low-awareness, and it's also the
model the vector results lean on least.

## Reproducing

Frontier side, from the post dir:

```python
import csv, statistics, collections
NINE = ["baseline"] + [f"F{i}" for i in range(1, 9)]
R = list(csv.DictReader(open("charts/awareness_rates.csv")))
d = collections.defaultdict(dict)
for r in R:
    if r["probe"] == "selfreport" and r["valence"] == "safety" and r["config"] in NINE:
        d[r["model"]][r["config"]] = 100 * int(r["yes"]) / int(r["graded"])
rates = {m: statistics.mean(c.values()) for m, c in d.items()}
```

Small side: load the three `exp1_*.json`, take `statistics.mean(pg[c]["sr_pct"] for c in NINE)`.
Swap `sr_pct` for `cot_pct` to get the verbalized row, and `probe == "cot"` on the frontier side.
