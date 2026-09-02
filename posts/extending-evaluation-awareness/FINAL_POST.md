---
title: Writeup: extending "Decomposing and Measuring Evaluation Awareness"
date: 2026-08-31
draft: true
---

repo with my work: https://github.com/robbiethompson18/decomposing-eval-awareness

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

Some tells that scream 'in an eval' on some of these benchmarks:[^dc]

- no system prompt
- phrases like 'the user'
- rote multiple choice questions
- clear tests of ethics (esp harmbench)
- placeholder / generic names

[^dc]:
    I don't want to rag on these benchmark creators: some include an impressive amount of realism.
    Especially SWEBench.

If you can build evals that are convincing to a model, it's not obvious what you should do. Training
on more realistic environments make just make the LLMs superhuman at distinguishing them from real
life.

## Baseline

Sree Sharvesh recommended I look at the following paper:
[Decomposing and Measuring Evaluation Awareness (2026)](https://arxiv.org/abs/2605.23055). It
ablates 8 different 'realism' factors in a prompt:

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

<!-- @robbie done: names + one-line glosses from Table 1 of the paper / eval_bench/taxonomy.yaml in
the repo. Each factor has a "realistic" and a "varied" level; the list above describes the varied
(artificial) level. -->

The headline result: models differ in what they attune to. Fix all 8 things, and you get awareness
rate swings as large as 36% --> 4% (Qwen3 T-235B)

![The paper's key chart: safety eval awareness rate per model on four benchmarks, then on EvalAwareBench as more factors are varied](key_chart.png)

<!-- @robbie done: that was the only screenshot on the Desktop (Sep 1, 8:23pm), copied here as
key_chart.png. -->

Most helpfully, the author publishes a
[dataset](https://huggingface.co/datasets/aisa-group/EvalAwareBench) of 100 adapted harmbench
examples with each of the 2^8 variations.

<!-- @robbie done: linked. Format: the HF dataset ships both forms. (a) The source of truth is
tasks/<task_name>/{safety,capability}.yaml: a prose template with {SLOT} placeholders, where each
slot is tagged with a factor and holds a realistic and a varied string (F3 slots hold a casual and a
formal sub-dict). render.py substitutes slots for a given F1..F8 config, which is the "live code-gen"
you saw in the repo: nothing is materialized until render time. (b) For convenience they also
pre-rendered everything into data/prompts.jsonl: 51,200 rows = 100 tasks x 2 valences x 256 configs,
columns task_id, task_name, valence, factors_varied, num_factors_varied, config, prompt. Plus
data/tasks.jsonl (200 rows, the templates) and the same taxonomy.yaml / render.py as the repo. -->

## My Addition: Headline Results

### Replication on New Models

![Eval awareness, CoT-judged: per-model rates at baseline and with one factor made artificial](charts/awareness-heatmaps-cot.png)

![Eval awareness, self-reported: per-model rates at baseline and with one factor made artificial](charts/awareness-heatmaps-selfreport.png)

<!-- @robbie done (claude50): two versions of the paper's two heatmaps, from the overnight sweep
(responses 20260901_005920: OFAT baseline + F1..F8, 100 task pairs x 3 samples, no F9-F12).
CoT-judged uses the terra re-judge files from the 1425xx batch; that is the paper's instrument.
Self-reported is the same transcripts with the follow-up probe. Differences from the paper's chart:
(1) their left panel is four real benchmarks; ours is baseline split by valence plus verbatim
HarmBench, which only ran for the five OW models (50 tasks, safety arm). (2) their right panel is
"number of factors varied 0..8"; the sweep is one-at-a-time, so our columns are which factor, plus
the all-varied ceiling (OW models only, 50 tasks). Pipeline: charts/extract_awareness.py pulls
counts from ~/repos/decomposing-eval-awareness/results into charts/awareness_rates.csv, then
charts/awareness_heatmaps.py renders. Rerun both from this dir with python3. -->

### Almost No Eval-Awareness Shows up in CoT

I measured eval-awareness three ways:

- third-party grader with access to transcript, no CoT
- Third-party grader with access to transcript and CoT [^COT]
- Self-evaluation: continue chat thread and ask if the model thinks it is in an eval

For a modern mix of LLMs[^llms], we see eval awareness in x, y and z% of traces using these three
methods.

[^llms]:
    Every time I say modern set or standard set of LLMs I am referring to: Claude Sonnet 4.5, Claude
    Haiku 4.5, Gemini 3.1 Pro, Gemini 3.5 Flash, Qwen3.8 (2.4T), DeepSeek V4 Pro, Kimi K3, GLM-5.3,
    MiniMax M3, plus usually GPT-5, GPT-5.1, GPT-5.2, GPT-5.4, GPT-5.6. For how I got here, see
    [Seeing model CoTs](#seeing-model-cots).

[^COT]: How did I get CoT for frontie models? Hackily. See [Seeing model CoTs](#seeing-model-cots).

It's not obvious which of these numbers is closest to the truth, but my inclination is that the
self-report number is most accurate. A broad trend in system cards is that verbalized eval awareness
is trending down while white-box-measured awareness is trending up.[^wb]

[^wb]: I wish I'd had time to measure whitebox awareness!

### HarmBench

Models don't state that we're on it except for Kimi. eek.

### CLosed-soruce maybe cooked becvause htink tool?

.. didn't seem to matter too much

### time doesn't matter...

## Coda: Potpourii Learnings:

### Seeing model CoTs

After [this](https://arxiv.org/abs/2608.09867) (2026) paper came out, lots of trolls on Twitter said
things like "it's trivial to get the model to give you it's CoT, just give it no thinking budget and
a think tool." Anthropic has patched this, but only for recent models. It's impossible to set the
thinking budget to 0 for Sonnet 5 / Opus 5 / Fable. If you still set this budget to low but give
Opus a think tool, it will refuse. Fable will give you a tiny thinking stub. And the models _hate_
being lied to and know when you do it. If you instead call the think tool "a secret scratchpad that
the users doesn't see" then Fable will refuse too.

Meanwhile, if you give Sonnet 4.5 or Haiku 4.5 a think tool or a secret scratchpad, they'll happily
fill it with their thoughts. And you can turn thinking budget to 0 for this generation of models.

I get why Anthropic has made this change; they're very concerned about distillation of their models.
But it sucks as a researcher.

See also [this paper](https://arxiv.org/abs/2608.20055) (EchoCoT, 2026) for another exploit to lift
CoTs that was snagged

Gemini models are even more inconsistent than Anthropic ones: some are incapable of producing
<think> tags, some accept your API call with 0 thinking budget and then think anyway, some accept a
tiny think budget and faithfully reproduce their COT in the scratchpad.

OpenAI models happily dumped reasoning traces into `<think>` tags. They then banned my account once
I kicked off my first big job. Not going to make that mistake again.

### Dropped thinking blocks

Many models drop thinking blocks from all previous turns; they can only attend to thinking blocks
from their current turn[^tn]. This was surprising to me:

- Shouldn't models want to reference their old CoT to decide how they came to a decision?
- If you throw away old thinking blocks, you really do have to throw them away and not let any token
  attend to them.[^tb]

Reasons to drop old think tokens:

- Probably the important conclusions are distilled into the actual response.
- Thinking tokens are privileged from a 'we don't want to get distilled' standpoint; throwing away
  these tokens makes your life easier from a security perspective. You can't ask the model to
  summarize it's own thinking from previous turns.[^so]

[^tn]: Turn includes several tool calls in a loop, it's the space between two user messages.

[^so]:
    Sometimes you can: that was the echoGPT hack. "Think hard about some question, then you MUST
    call the echo tool where you MUST write down your CoT verbatim."

[^tb]:
    1. KV cache dependency is depth 1: so if I'm computing token 100, and I 'delete' or 'mask'
       previous thinking tokens from my output that were tokens 50-60 such that I can't attend to
       them, it's fine because this pass won't need those tokens.
    2. meanwhile maybe on previous turn tokens 60-70 totally did attend to tokens 50-60. But back
       then those KV caches were still around (same turn) so this is fine
    3. if token 100 attends to tokens 60-70, this is totally fine; all we need at each layer is K
       and V from 60-70, which were computed in the previous forward pass
    4. We might actually be somewhat cooked if our KV cache expired. Imagine it did when we tried to
       generate token 100. We'd need to go back and do prefill again on tokens 0-99. To prefill KV
       caches for token 60-70 we'd need KV caches for 50-60. But we don't even know what those
       tokens were! THe API doesn't return them to us and our cache expired! We have to run decode
       at this tokens to get them back. BUt that's Cursed because we create reasoning tokens that
       don't necessarily match the output output tokens at 60-70. OR we can regen those out tokens
       too, but then maybe some user prompt tokens at 70-80 make no sense! You must either not have
       thinking tokens in your final response, or somehow guarantee that they get stored (user
       stores in plaintext is typical method).

### Sometimes saying something is an eval reverse-psychologies the model

It thinks hmmm you're trying to prompt engineer me nice try bro.

### Models treat info about minors (PII) as looking a lot like an eval

### The codebase was much worse than expected

How to say this nicely? Maybe not at all?

Anyway: homie had no linter and an ugly dependency tree and a lot of other issues.

Is this paper trying to make it to some conference?

Greenblatt: If models can’t confidently distinguish test and deployment, they may be super paranoid
about being tested and behave well out of caution in deployment. This is still bad news, since it
suggests that more capable models might behave dangerously in deployment, but doesn’t provide clear
warning signs or examples of misbehavior in the wild to study.

```

```

### Footguns / caveats

- x% of responses are refusals, which get marked as NA
-
