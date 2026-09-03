Metrics on ~5000 EvalAwareBench transcripts per model. Each cell is Pearson $r$ / AUROC. $r$ is
point-biserial for vector-vs-label pairs and $\phi$ for the two binary labels; AUROC is only defined
when exactly one side is a binary label.

Rows sorted by mean $r$.

| pair                       | Qwen3.8-27B  | GPT-OSS-20B  | Gemma 4 31B  | mean $r$ |
| -------------------------- | ------------ | ------------ | ------------ | -------- |
| PDV × self-reported        | +0.51 / 0.80 | +0.22 / 0.67 | +0.04 / 0.52 | +0.26    |
| BDV × self-reported        | +0.25 / 0.65 | −0.21 / 0.34 | +0.33 / 0.69 | +0.13    |
| verbalized × self-reported | +0.10 / NA   | +0.07 / NA   | +0.11 / NA   | +0.10    |
| PDV × verbalized           | +0.06 / 0.60 | +0.08 / 0.89 | −0.05 / 0.47 | +0.03    |
| BDV × PDV                  | +0.64 / NA   | −0.74 / NA   | +0.13 / NA   | +0.01    |
| BDV × verbalized           | −0.01 / 0.50 | −0.08 / 0.14 | +0.04 / 0.56 | −0.02    |

Verbalized awareness is rare (3 to 4% of transcripts), which caps $r$ near 0.3 for those rows even
for a perfect ranker; AUROC is base-rate free.
