---
title: Can reasoning models keep Codenames words out of their CoT?
date: 2026-09-28
draft: true
source: ../cot-codenames/writeup.md
---

1. By default, models can't keep themselves from writing the board words in their CoT, even when
   told an adversary reads it: 30/30 told spymasters wrote essentially all 25 words. They even
   notice as it happens, e.g. DeepSeek V4.1 Flash: "Since I've already written them, let me at least
   minimize further exposure and produce a clean final answer."
2. The models have memorized every word in the standard Codenames word list, so a monitor that
   guesses from that list barely needs the CoT. I had to expand the noun set.
3. Adding few-shot examples of how to keep thoughts secret (label the words T1–T9 / N1–N16, then
   reason only through labels) didn't work: still 30/30 leaked, usually by writing out the label
   table with the words themselves ("T1 = LIGHT").
4. Adding a pre-labeled board, so the model never has to write the word-to-label mapping itself,
   might help.
5. Why are open models _so janky_ about obeying rules? Kimi K3's endpoint ignores
   `tool_choice="required"` and DeepSeek Flash narrates its reasoning in the reply when thinking is
   off, while GLM-5.3 and Qwen3.8 can't turn thinking off at all.
