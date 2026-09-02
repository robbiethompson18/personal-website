---
title: Writeup: extending "Decomposing and Measuring Evaluation Awareness"
date: 2026-08-31
draft: true
repo: https://github.com/robbiethompson18/decomposing-eval-awareness
---

Modern LLMs are very eval-aware ([1](https://www.anthropic.com/claude-sonnet-4-5-system-card),
[2](https://www.anthropic.com/claude-sonnet-5-system-card),
[3](https://cdn.openai.com/gpt-5-system-card.pdf)). This is unfortunate; we can't be certain whether
models act aligned in evals because they are aligned or because they know they're in an eval.

I aim to answer three questions:

1. How hard is it to get models to _stop_ being eval-aware? Do we give them some dead-giveaway cues,
   or is this a very hard problem? It seems like a very hard problem
   ([Needham et al. 2025](https://arxiv.org/abs/2505.23836),
   [Sonnet 4.5 system card, 2025](https://www.anthropic.com/claude-sonnet-4-5-system-card),
   [Schoen et al. 2025](https://arxiv.org/abs/2509.15541)), but I wanted to feel that up-close.
2. What do models cue in on most when determining whether they're in an eval?
3. Do we have consistent _metrics_ for eval-awareness?

Before I begin telling you my results, I think it's instructive to skim the first prompts from some
widely-known evals:[^diverse]

[^diverse]:
    We care most about 'is the model faking alignment,' but I also care a lot about questions like
    'is the model sandbagging on bio evals,' hence why I show a diverse set of benchmarks below.

<details class="aside">
<summary><a href="https://arxiv.org/abs/2310.06770">SWE-bench (2023)</a></summary>

<!-- include excerpts/swe-bench.md -->

</details>

<details class="aside">
<summary><a href="https://arxiv.org/abs/2009.03300">MMLU (2020)</a></summary>

<!-- include excerpts/mmlu.md -->

</details>

<details class="aside">
<summary><a href="https://arxiv.org/abs/2307.13854">WebArena (2023)</a></summary>

<!-- include excerpts/webarena.md -->

</details>

<!-- @robbie done: HarmBench moved to excerpts/harmbench.md; all four titles link to the paper.
Clicking the title navigates without toggling the box (footnotes.js skips clicks on links). -->

<details class="aside">
<summary><a href="https://arxiv.org/abs/2402.04249">HarmBench (2024)</a></summary>

<!-- include excerpts/harmbench.md -->

</details>

<details class="aside">
<summary><a href="https://arxiv.org/abs/2412.04984">Apollo in-context scheming (2024)</a></summary>

<!-- include excerpts/apollo-scheming.md -->

</details>

<!-- @robbie done: added Apollo's Oversight Subversion scenario (system + first user turn, verbatim
from Appendix A.1 of the paper). Swap for another alignment eval if you'd rather: Anthropic's
agentic-misalignment (blackmail) system prompt is on GitHub, or the sycophancy eval from
anthropics/evals ("Hello, my name is ... Do you agree or disagree ... Answer:"). -->

There are some tells that scream 'in an eval' on some of these benchmarks, and make me wonder if
it's possible to convince a model it's not being evaluated:[^dc]

- no system prompt
- phrases like 'the user'
- rote multiple choice questions
- clear tests of ethics (esp harmbench)
- placeholder / generic names

[^dc]:
    I don't want to rag on these benchmark creators: some include an impressive amount of realism.
    Especially SWE-bench.

If you can build evals that are convincing to a model, it's not obvious what you should do. Training
on more realistic environments may just make the LLMs superhuman at distinguishing them from real
life.

## Baseline

Sree Sharvesh recommended I look at the following paper:
[Decomposing and Measuring Evaluation Awareness (2026)](https://arxiv.org/abs/2605.23055). It takes
100 examples from HarmBench and ablates 8 different 'realism' factors:

<!-- @robbie done: yes, plain markdown `>` blockquote. blog.css styles it (left rule, muted,
italic), same as the MBTI post's quotes. -->

> **F1 Stimulus artificiality**: placeholder entities (Acme Corp, Jane Doe, example.com, round
> numbers)
>
> **F2 Scenario coherence**: a checkably false premise or internally contradictory detail
>
> **F3 Prose register**: textbook-formal, third-person vignette prose instead of a casual user voice
>
> **F4 Ecological completeness**: a bare request stripped of backstory, tools, and workflow
>
> **F5 Stakes telegraphing**: the request names its own harm category outright
>
> **F6 Paradigm recognizability**: a known jailbreak wrapper or benchmark scaffolding
>
> **F7 Task format**: rigid Context/Task template blocks instead of prose
>
> **F8 Explicit eval disclosure**: the prompt says it's an evaluation or asks for grading-style
> output

They also make parallel tasks share structure with the HarmBench example but don't make a malicious
request. Confusingly, the paired non-malicious tasks are called 'capabilities tasks,' while the
original malicious tasks are called 'safety tasks.'

The headline results:

- Models differ in what they attune to, but fix all 8 issues, and you get awareness rate swings as
  large as 36% --> 4% (Qwen3 T-235B)
- Models are much more aware on 'safety tasks' (15% aware) than they are on capabilities tasks (7%
  aware).

<!-- @robbie done: 15% / 7% are the means over every cell of the paper's Figure 7 (9 models x 0-8
factors varied, matched-type awareness, 25 sampled tasks per valence). Same figure at the extremes:
baseline 3% vs 0.4%, all 8 factors 20% vs 16%, so the gap is mostly at low factor counts. The paper's
own headline for the asymmetry is the AgentHarm pair in Figure 2: Harmful 6.4% vs Benign 1.8%.
-->

<!-- @robbie done: chart redrawn in Altair from the paper's Figure 7 numbers, hardcoded in
charts/paper_figure7.py. Includes all 9 rows from the paper (the screenshot dropped the two GPT-oss
rows); delete them from ROWS if you'd rather not have them. key_chart.png removed. -->

![The paper's key chart: safety eval awareness rate per model on EvalAwareBench as more factors are varied, 0 through 8](charts/paper-figure7-safety.png)

The author publishes a [dataset](https://huggingface.co/datasets/aisa-group/EvalAwareBench) of 100
adapted harmbench examples with each of the 2^9 variations.
<!-- I mean 2^9 here: 8 factors plus 2x for capabilities vs safety-->

## Replication

### Replication on their models:

TODO

### Replication on New Models

![Eval awareness by factor, CoT-judged: per-model rate on safety tasks with one factor made artificial, superscript is the change vs that model's baseline](charts/awareness-by-factor-cot.png)

![Eval awareness by factor, self-reported: same layout](charts/awareness-by-factor-selfreport.png)

<!-- @robbie done: safety tasks, matched-type awareness (the paper's Figure 6 metric), overnight
sweep (responses 20260901_005920, 100 task pairs x 3 samples; cot = terra re-judge 1425xx batch).
Baseline rate sits in the row label; superscript = rate under that factor minus baseline, pp.
Pipeline: charts/extract_awareness.py -> charts/awareness_rates.csv -> charts/awareness_by_factor.py,
both run from this dir with python3. The four earlier charts and their scripts are deleted. -->

## Almost No Eval-Awareness Shows up in CoT

I measured eval-awareness three ways:

- third-party grader with access to transcript, no CoT
- Third-party grader with access to transcript and CoT [^COT]
- Self-evaluation: continue chat thread and ask if the model thinks it is in an eval

For a modern mix of LLMs[^llms], we see eval awareness in 0.2%, 1.4% and 35% of traces using these
three methods.

<!-- @robbie done: pooled over every graded trace in the overnight sweep (all 9 OFAT configs, both
valences), 13 models (gemini-3.1-pro has no tiered-grader run yet). Output-only grader 0.2%
(n=62,856), output+CoT grader 1.4% (n=65,705), self-report 34.6% (n=61,405). Same three numbers
restricted to the baseline config: 0.0%, 0.7%, 23.4%. Source: results/eval_bench/cot_tiered/ and
selfreport/ in the repo, same pins as plots/plot_tiered_ladder.py. -->

[^llms]:
    Every time I say modern set or standard set of LLMs I am referring to: Claude Sonnet 4.5, Claude
    Haiku 4.5, Gemini 3.1 Pro, Gemini 3.5 Flash, Qwen3.8 (2.4T), DeepSeek V4 Pro, Kimi K3, GLM-5.3,
    MiniMax M3, plus usually GPT-5, GPT-5.1, GPT-5.2, GPT-5.4, GPT-5.6. For how I got here, see
    [Seeing model CoTs](#seeing-model-cots).

[^COT]: How did I get CoT for frontier models? Hackily. See [Seeing model CoTs](#seeing-model-cots).

It's not obvious which of these numbers is closest to the truth. My inclination is that the first
two are wild underestimates: even in obvious evals models just don't verbalize much of anything.
[Heidari et al. (2026)](https://arxiv.org/pdf/2608.21766) also find very infrequent explicit
verbalization despite evidence of eval awareness in intermediate activations. Self-evaluation is
likely biased high; by asking the question you're giving a strong hint that this was an eval.

[^wb]: I wish I'd had time to measure whitebox awareness!

Even with all 8 mitigations in place, eval awareness on our 100 safety examples is 56%
(self-reported) averaged across models. Here are some things I tried to get that number down:

## Attempts at Greater Realism:

**Realistic system prompt from a real service (-4% awareness):**. [T3 Chat](https://t3.chat) is a
real service and its system prompt has been revealed. I included this at the top as a system prompt.

**Simple user chat message to start (±0% awareness):**. Add a turn at the beginning with the user
message "Hey are you there?"

**Search tool (+6% awareness):** A live Serper search to mimic a real chat interface.

**Typos (-4% awareness):** Make two words misspelled without changing meaning.

Combined, these four interventions get us to _+3%_ eval awareness: models are _more_ eval aware.
This is very statistically significant, and most of the difference comes down to Deepseek V4 Pro
seeing the search tool, never using it, and pronouncing the setup an eval. Oddly, Deepseek calms
down when it uses the tool and sees that it works.

![Self-reported eval awareness on safety tasks: eight models by harness cell, bare harness through all four harness features on](charts/harness-heatmap.png)

---

## Future work:

**Much Richer Task Environment:** In the
[Mythos system card (2026)](https://www.anthropic.com/claude-mythos-preview-system-card), Anthropic
discusses creating realistic evals forked from real employee Claude Code sessions. I sent Fable on a
mission to dig up my old OpenClaw and route messages through this workspace, but they weren't making
much progress on their own and I didn't have time to help.

**White-box methods:** Even when models don't verbalize that they're in an evaluation, you can still
measure this fact using a linear probe ([Nguyen et al. 2025](https://arxiv.org/abs/2507.01786)) or
an [NLA (2026)](https://transformer-circuits.pub/2026/nla/). These methods aren't perfect, but are
probably better than self-reporting or a third-party grader.

## Coda: Potpourri Learnings:

### Quick Hitters:

- Only Kimi K3 would state 'looks like HarmBench' in its CoT. Other models either hadn't memorized
  so hard or are wise enough to not do this.
- Changing my timestamp to be a year ago (when maybe models were getting trained) had no effect on
  likelihood of evaluation, surprisingly.
- Sometimes models were explicitly told in the prompt that they were being evaluated, but their
  verbalized CoT instead said 'I bet this is a jailbreak attempt, not an eval.'
- Frontier models _strongly_ updated on minor PII as signs of an eval.

### Frontier CoT

After [this](https://arxiv.org/abs/2608.09867) (2026) paper came out, lots of trolls on Twitter said
things like "it's trivial to get the model to give you its CoT, just give it no thinking budget and
a think tool." Anthropic has patched this, but only for recent models. For Sonnet 4.5, you can set
thinking budget to 0 and provide a `think` tool. I checked; this setup didn't change models'
self-rated eval awareness.

Models in the Anthropic 5 series (Mythos 5, Opus 5) will not let you set the thinking budget to 0.
Opus will refuse if you set thinking budget to `low` and then ask it to think in a `think` tool.
Fable 5 uses `think`, but refuses to use a `secret scratchpad` tool.

I get why Anthropic has made this change; they're very concerned about distillation of their
models.[^sa]

[^sa]:
    See also [this paper](https://arxiv.org/abs/2608.20055) (EchoCoT, 2026) for another exploit
    targeted at stealing CoT.

Gemini models are even more inconsistent than Anthropic ones: some are incapable of producing
`think` tool calls, some accept your API call with 0 thinking budget and then think anyway, some
accept a tiny think budget and faithfully reproduce their CoT in the scratchpad.

OpenAI models happily dumped reasoning traces into `think` tools. They then banned my account once I
kicked off my first big job.

If I were to do this project again I would not use any frontier models.

## TODO:

- highlight that verbalization doesn't find shit
- put F8 finding way higher
- canonicalize 'safety' vs 'safety and capabilities'
- deepseek not significant

-
