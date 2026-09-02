---
title: Getting an LLM to Run Really Fast on My Machine
date: 2026-07-23
draft: true
---

After finishing [The Scaling Book](https://jax-ml.github.io/scaling-book/) I set up a final exam for
myself: find whatever the SOTA <45B Open-weights LLM is, predict how fast it will run on my MAC
using and on a pod of eight v5es. Then run it both places and see how close I can get.

## Model: Qwen 3.6B

https://huggingface.co/Qwen/Qwen3.6-35B-A3B

## BOTEC: How Fast Will This Run on TPU?

My 8x v5e pod does 8 _ 2e14 = 1.6e15 flops/s in bf16. Qwen 3.6 35B is sparse, meaning that only 3B
params are active each forward pass. We two two flops per param per forward pass, so I expect a
minimum time of 2 \* 3e9 / 1.6e15 = 4e-6 = 4us per forward pass per token on flops.

My 8x v5e pod has 8 \* 8.2e11 of HBM bandwidth. At 16 bit quantization Qwen 35B is ~70GB, again only
6GB of which are active. So we should expect a minimum of 6e9 / 8.2e11 = 8e-3 = 8ms per forward pass
on memory, if we're generating only a single token.

Given that this all fits on one TPU, I will run just run it there for now.

TODO: pick a B to run this at, probably 2k? And decide what throughput there will be.

## BOTEC: How Fast Will \_ Run on Mac?

My mac is an M4 with 48GB of RAM and _ of memory bandwidth. It can do _ flops.

On flops, for a single token, I expect to spend 6e9 / _ = xus on flops, and 6e9 / _ on memory.

----- must get to here by 10am morning of July 24 -----

## Increasing Batch Size

...

## 0: Benchmarking

- benchmark written: xyz
- benchmark code: xyz
- written text: xyz
- code: xyz

## Improvement I: Analyzing the Kernels

## Improvement II: Speculative Decoding

## Improvement III: Predicting The Expert

## Improvement IV:
