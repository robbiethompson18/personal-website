---
title: Pretraining ablations, week of September 21, 2026
date: 2026-09-27
draft: true
project: true
source: ../nd-rl/experiment-summaries/2026-09-21-pretrain-ablations/README.md
---

<!-- HUMAN-ONLY: agents must not edit this file. Robbie writes it by hand. -->

## Open questions:

1. when does held-out score peak? Will probably take what we got there.

## Summary

The only things that I really trust working here are:

1. Lean
2. Muon

Everything else could just be noise.

Leon's new RL recipe does _much_ better on the recipe 39 I sent him than on recipe 1 (~2x more
proofs) which is nice.

## Methodology:

1. Freeze training data to Dan's set (500k pertrain examples, 1.5k RL proofs for expert iteration,
   1.5k proofs not trained on and used to decide whether run is kept, 1k proofs held out until after
   runs finish)
2. Advance based on pass@16? on the eval set.
3. Free RL methodology (very vanilla expert iteration)
4. Freeze GPU budget: 300s of pretrain, __ seconds of RL
5. Parameter cap of 10m. Didn't get hit because pretrain time was the limiting factor

## Findings

### Does pretrain loss correlate with RL theorems learned?

A: Not much. R = ?

@claude insert simple scatter chart here.

### Pretrain loss, RL theorems

x: run # y: pretrain loss, RL theorems in val set proved, RL theorems in heldout set

## Mistakes made:

1. even tiny prompts get amplified if you don't notice. Took me far too long to realize that the
   agents thought speedups were out of bounds (and thus they were training tiny models).
2. I think I spent way too many tokens letting autoresearch spin and didn't think hard eonugh about
   validation

## Summary of results (Claude written)

Top 10 single-change jumps. Metric: dev theorems solved at length >= 7, mean of seeds 0/1/2. Delta
is vs the incumbent the run was compared against. Protocol changes are excluded.

| #   | Run | Δ       | Score   | What changed                                          | Notes                                                                        |
| --- | --- | ------- | ------- | ----------------------------------------------------- | ---------------------------------------------------------------------------- |
| 1   | 030 | **+65** | 148→213 | **Muon** for hidden matrices (was AdamW)              | Every seed up (+117/+21/+57); val loss ~flat. The one clearly real jump.     |
| 2   | 081 | **+48** | 356→404 | **Polar Express** Newton-Schulz coefficients in Muon  | Pretraining indistinguishable; RL went further. Every seed up.               |
| 3   | 115 | +26     | 606→631 | Hybrid heads: ALiBi on 4 heads, NoPE on 4             | Fixed 113's bad RL start (round-1 parse failures 30–64% → 18–25%).           |
| 4   | 070 | +25     | 327→353 | Muon weight decay 3× → 10×                            | RL better from round 1; no sharpness failure.                                |
| 5   | 066 | +23     | 293→316 | Batch 256 → 128 (2× optimizer steps, same wall-clock) | Val loss didn't drop. "Steps turn into score."                               |
| 6   | 032 | +19     | 213→233 | AdamW finish for last 20% of pretraining              | **Later removed (040) at an exact tie.**                                     |
| 7   | 113 | +19     | 587→606 | ALiBi replaces RoPE                                   | ~+30% pretraining steps; own mechanism refuted. Probably partly a speed win. |
| 8   | 038 | +17     | 237→254 | AdamW finish shortened to 10%                         | Same AdamW-finish line.                                                      |
| 9   | 101 | +16     | 563→580 | 5 → 6 layers (Lean protocol)                          | −17% steps, still up on every seed.                                          |
| 10  | 039 | +16     | 254→270 | AdamW finish shortened to 5%                          | Same AdamW-finish line.                                                      |

Just below the cutoff: 129 (LR floor 0.1 → 0.3, +15), 153 (width 384, +15), 150 (bigram table, +14),
151 (width 320, +14).

Protocol jumps (not comparable, not ideas): 000 → 012 (56 → 148, 600 s → 1200 s harness and 3-seed
bar); 081 → 100 (404 → 563, Lean tokenizer + Lean ∧ nd_verify reward + 2400 s).

Noise: pooled one-seed sd is 41.6 (token era) and 44.7 (Lean era), so the SE of a difference of two
3-seed means is ~36. Only Muon (~1.8 SE) and Polar Express (~1.3 SE) clear it. Ranks 6, 8 and 10
(+52 combined) came from the AdamW finish, which 040 then deleted at a tie. Keeps are selected for
being high, so kept deltas overstate true effects. 153 (687) has held for 30+ runs (154–184), many
of which scored 670–685.

By era: token era 148 → 404 (2.7×), almost all from the Muon family. Lean era 563 → 687 (+22%), from
architecture and position encoding, plus spending 148's token-batching speed on width.
