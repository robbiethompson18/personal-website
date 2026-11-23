---
title: Scattered Thoughts on Datacenter Security
date: 2026-11-23
draft: false
redirect_from: scattered thoughts on datacenter security
rating: 3
---

Epistemic status: I don't work at a lab, and I don't have close friends who do, and I've never done
large (>x flops) training runs, but I have spent ~200 hours of my life thinking about these topics.
So take all numbers and claims in this post as the best guess of an informed amateur armed with lots
of AI help.

The AI Safety community is correctly freaking out about security at frontier AI labs. If we can't
make a deal with China to pause, and the US pauses unilaterally, and then China steals model
weights, then we are forced to race again to not fall behind.

Here are some questions I hope to deconfuse myself about:

- The world seems to believe that frontier labs are thoroughly infiltrated, both in cyberspace and
  by employees who are MSS.[^MSS] Yet the labs seem to care a lot about security.
- There are many things the CCP could steal: weights, algorithms, RL environments, RL rollouts,
  source code, etc. What is important? What is likely to go?
- How to model the CCP? Asleep at the wheel? Very wise to AGI and acting clueless so that they can
  steal the weights at the right moment?
- what things are easy to steal? Easy to secure? and vice versa?

[^MSS]: MSS is the CCP's intelligence service, something like their FBI/CIA/NSA combined.

## What to Steal:

### Model Weights

I speculate that frontier models are about ~10T params, or ~10TB of data. This fits onto one
external hard drive you could buy on [Amazon](https://www.amazon.com/dp/B07G3QMPB5).
Cursed.[^bandwidth] With the weights you instantly have your adversary's best model. Even if
Anthropic trained a model to do only Anthropic's bidding, it would be trivial for the CCP to undo
this. Models are or will soon be good enough that they can improve themselves, subject to the
constraints on how many experiments they can run on your compute. So if China gets GPT 10 they could
be off to the races.

[^bandwidth]:
    Lots of security proposals involved limiting the bandwidth between some section of the data that
    holds model weights and the 'outside world' (in this case researchers' laptops). However model
    weights need to be streaming tokens during inference and saving checkpoints during training. The
    training issue is easily solved: let your egress limit apply to one perimeter which holds both
    your GPUs and the object storage which holds checkpoints. Inference limits are more challenging:
    labs serve [~1 trillion tokens](@tokens) from frontier models per day, which is
    ~$3\times10^{13}$ bits of information, or 370 Mbits/s. This means that the fiber which sends out
    inference tokens can be used to egress weights in 2.5 days.

### Algorithmic Secrets

Questions:

- Smart people ([Dario](@dario), [RAND](@randinsights), [AIFP](@aifp)) claim that a significant
  portion of algorithmic secrets can be conveyed in a couple of pages of text.
- Chinese labs have the human capital to do a frontier training run using these secrets.
- Frontier runs are [about 10% of R&D compute](@finalrun). Claude and I speculate that GPT 6 Astra
  took $9.4\times10^{26}$ flops total,[^astra] trained on over 100k Blackwells in Abilene. China has
  about $2\times10^{21}$ total flops, so it would take them 5 days to do an Astra-sized training run
  if they spent all of their compute on it, compared to the 90 days it took OpenAI at Abilene.
  Realistically, if China used their biggest site in Johor, Malaysia, it would take them about 130
  days to train Astra.[^Johor]

[^astra]:
    This is [Epoch's estimate](https://epoch.ai/data/ai-models) (2026): 100,000 GB200s × 90 days
    ($7.8\times10^6$ seconds) × $1.2\times10^{15}$ useful FLOP/s per GB200 (25% of its FP8 peak) =
    $9.3\times10^{26}$, listed as $9.4\times10^{26}$. OpenAI has only said
    ["more than 100,000 GPUs"](https://fortune.com/2026/09/03/openai-debuts-gpt-6-astra-computer-use-greg-brockman-says-start-of-agi/)
    (2026); the 90 days and the 25% are Epoch's assumptions. China's number is IFP's
    [4.6M H100-equivalents](https://ifp.org/how-to-increase-americas-ai-lead-over-china/) (2026) at
    the same utilization. A GB200 is 2.54 H100-equivalents, so
    $4.6\times10^6\times1.2\times10^{15}/2.54=2.2\times10^{21}$ useful FLOP/s, and
    $9.4\times10^{26}/2.2\times10^{21}=4.3\times10^5$ seconds = 5 days.

[^Johor]:
    China's biggest site is in Johor because it's illegal to ship Nvidia chips to China, but it's
    not illegal to sell them to a Malaysian company who then rents the compute to China. The Johor
    site is [221,000 H100e](@my06), about 22% as large as the biggest US site (Stargate in Abilene,
    Texas). It's owned by Bain, operated by a Bain subsidiary, and used by ByteDance, originally for
    TikTok. Just three days ago (Nov 19),
    [the Commerce Department started requiring licenses](@bisrule) to ship chips to datacenters
    which in turn serve Chinese companies, and intimated that they would enforce this restriction
    retroactively, ie require existing datacenter operators to get a license to serve Chinese
    companies, under threat of future export controls. 'Recommendation algorithms' (TikTok algos)
    are exempt; it's unclear to what extent this loophole will be abused.

### SFT Data

I estimate that frontier models SFT on ~1 token per param, based on the fact that
[Olmo SFTs on 1.4 tokens per param](@olmo).[^chinchilla] Thus frontier models use tens of terabytes
of SFT data.

[^chinchilla]:
    Sanity check: The [Chinchilla paper](https://arxiv.org/abs/2203.15556) (2022) claims that it's
    optimal to pretrain on ~20 tokens per param if you ignore the cost of inference, and
    [Meta's Llama 3 post](https://ai.meta.com/blog/meta-llama-3/) (2024) claims that labs
    empirically do about 10x this, for hundreds of tokens per param. 1% of tokens in SFT as in
    pretraining seems sane.

<!-- @robbie done (was two "@c address placeholders" and "@c link" in the SFT section). Where the numbers come from, and one problem:
- Olmo 3 Think 32B (Allen AI, 2025): SFT on 45.2B tokens (two epochs of a 2.25M-example set, 78 GB uncompressed) over 32B params = 1.4 tokens per param. Pretraining was 5.5T tokens, 172 per param. SFT is 0.8% of pretraining, which is the 1% in the footnote.
- The problem: Olmo 3 Think 7B used the same SFT set, 45.4B tokens, which is 6.5 tokens per param. Olmo's SFT data did not grow with the model, so carrying 1.4 tokens per param up to a model 300x larger is the weak step. It gives 10T params × 1 × 4 bytes = 40 TB, which matches your "tens of terabytes".
- Scaling by share of pretraining instead: 0.8% of a 50T-token corpus is 0.4T tokens, 1.6 TB. Olmo's set unscaled is 0.08 TB. So the range is 0.1 to 40 TB and "tens of terabytes" is the top of it. It fits on the drive either way.
- Meta's post supports "about 10x" for its 70B model (15T tokens, 214 per param) and says "two orders of magnitude" over Chinchilla for the 8B. It describes Meta, not labs in general.
- "Hundreds of tokens per param" fails at frontier size if params means total params. DeepSeek V4-Pro is 33T tokens over 1.6T params, 21 per param; GLM-5 is 38. They are mixture-of-experts models, and the hundreds only appear per active param (673 and 712). A 10T-param model at 200 tokens per param would need 2,000T tokens; the largest published corpus is 45T.
- Notes: POST_RESEARCH.md, "Part: SFT Tokens per Param, APEX-Agents Sizes and Rollout Length".
-->

### RL Environments

Algorithmic secrets are enough to make an excellent pretrain, but you can't posttrain without RL
environments. US labs spent ([about $8 billion in 2026](@dataspend)) on data and environments, about
5% of compute spend.

I have very high uncertainty about how many RL environments it takes to train a frontier model. I
speculate that it takes millions of environments,[^rumors] which are on average tens of megabytes of
data,[^mercor] meaning that stealing every environment is maybe tens of terabytes, the same order of
magnitude as the model itself. Possibly you can get away with orders of magnitude fewer bytes via
some compression scheme (eg LLM summarization or zstd).

[^rumors]:
    Claude and the rumor mill independently arrived at this OOM. Moonshot's Kimi K3 used
    [1.5 million sandbox images](@kimi).

[^mercor]:
    Claude fermi estimated these numbers, and I had them sanity-check by looking at some real-world
    data, specifically Mercor's public
    [APEX-Agents benchmark](https://huggingface.co/datasets/mercor/apex-agents).

<!-- @robbie done (was "@c link plz"). What I measured from that dataset's file listing: 33 worlds, 480 tasks, 8.9 GB zipped. Mean world 270 MB, median 177 MB, 19 MB per task. These are knowledge-work worlds; coding and computer-use environments are container or VM images and run larger. -->

### RL Rollouts

Stealing RL rollouts instead of environments allows you to train a slightly worse model for less
compute. If you steal the rollout, you can prefill it and run one backward pass. Prefill is
[about 5x cheaper than decode](@pricing) based on public API pricing. Your model would be worse if
trained this way: RL is much less effective when run off-policy. How much worse is not clear to me.

One rollout on an agentic environment would be [about 500,000 tokens](@mechanize), or 2 MB of text.
And you might run your model tens or hundreds of times per task. This means that RL rollouts would
be 1 or 2 OOMs more data than the environments themselves, maybe hundreds of terabytes.

<!-- @robbie done (was "@c fermi estimate... tens of millions of tokens?"). Tens of millions is 20 to 100x too high for the average:
- Mechanize (2025): frontier RL tasks produce "transcripts with an average length of around 100,000 tokens per task", growing 5x a year, so "around half a million tokens" a year on. That is where 500,000 comes from.
- The long tail is in the millions. Moonshot's Kimi K3 report (2026): "A single rollout may involve up to thousands of tool calls and millions of context tokens".
- This is the length of the transcript, which is what a thief copies. The compute bill is larger because the model re-reads its context every turn.
- Check on the paragraph: 500,000 tokens × 64 rollouts per task (the group size Mechanize cites) = 128 MB per task, against tens of MB for the environment. So rollouts are about 1 OOM more than environments, not 2. 1.5M tasks × 128 MB = 190 TB, so "hundreds of terabytes" holds.
- My earlier 60 TB figure averaged in short non-agentic episodes (math, chat) at about 20,000 tokens.
-->

There are likely many tricks you can do to make this number small, e.g. pulling only successful
rollouts and compressing or dropping tool calls.

---

My takeaways from writing this article:

- almost anything you could want to steal from a US AI lab would fit on a hard drive inside your
  clutch.
- Bandwidth limits are surprisingly effective: even if you directed 100% of Anthropic's inference
  bandwidth towards stealing weights, it would still take you a couple days to get them out.

{@tokens}: My estimate; no lab publishes tokens per model. Anthropic's revenue was $17.0 billion in
the third quarter of 2026, per Strauss and O'Reilly (2026), which is $185 million a day. If 40% of
that is the flagship model, and an output token brings in about $60 per million (the list price is
$50 per million output tokens, plus cached input, less subscription discounts), that is 1.2 trillion
output tokens a day. At 4 bytes of text per token it is 4 TB a day.
<https://asimovaddendum.substack.com/p/anthropics-missing-s-1-disclosures>

{@dario}: Dario Amodei at the Council on Foreign Relations (2025): "many of these algorithmic
secrets, there are $100 million secrets that are a few lines of code."
<https://www.cfr.org/event/ceo-speaker-series-dario-amodei-anthropic>

{@randinsights}: RAND, "Securing AI Algorithmic Insights" (2026): "a few lines of code, a diagram,
or a brief technical exchange might be enough to convey a high-value insight."
<https://www.rand.org/pubs/research_reports/RRA4685-1.html>

{@aifp}: AI Futures Project, AI 2027 security forecast (2025), which sizes the secrets worth
protecting at "the most important 10KB (plaintext)" from the last month. 10KB of plain text is about
3 pages. <https://ai-2027.com/research/security-forecast>

{@finalrun}: Epoch AI (2026) on OpenAI's 2024 compute spend: "around $5 billion on R&D compute that
year, with only about $500 million – roughly 10% – going to the final training runs that produced
released models". <https://epoch.ai/gradient-updates/r-and-d-vs-training-compute>

{@my06}: Epoch AI's data center directory, "Bridge Data Centres MY06" (2026): "an estimated 221k
H100-equivalents of AI compute, supported by 243 MW of IT power", with chips "likely owned and used
by ByteDance". The chip types are Epoch's assumption from Nvidia's sales mix, not an observation.
Epoch lists Stargate Abilene at 1,019k H100-equivalents. The 130 days is for a $10^{27}$ FLOP run at
the 20% utilization Epoch uses for Chinese sites.
<https://epoch.ai/data/ai-data-centers/directory/bridge-data-centres-my06>

{@bisrule}: Bureau of Industry and Security, "Addressing Remote Access to Advanced Semiconductors"
(2026), an interim final rule: <https://public-inspection.federalregister.gov/2026-23529.pdf>. CNAS
(2026) summarizes it: "Data centers already serving these customers must obtain a license to
continue doing so within 90 days."
<https://www.cnas.org/publications/cnas-insights/insights-unpacking-the-remote-access-rule>

{@olmo}: Team Olmo, "Olmo 3" (2025): Olmo 3 Think 32B was fine-tuned on 45.2B tokens and pretrained
on 5.5T, so 1.4 SFT tokens per parameter, and SFT is 0.8% of pretraining. The 7B model used the same
SFT data, which is 6.5 tokens per parameter. <https://arxiv.org/abs/2512.13961>

{@dataspend}: My sum across US labs, from two anchors. OpenAI spent "about $1 billion on data (which
includes paying for human experts and RL environments)" in 2025, per Epoch AI (2026):
<https://epoch.ai/gradient-updates/can-ai-companies-become-profitable>. Anthropic's amended S-1 says
its costs for data quality and model evaluation services "rose by $757 million in the first nine
months of 2026, compared with a year earlier", per Strauss and O'Reilly (2026):
<https://asimovaddendum.substack.com/p/anthropics-missing-s-1-disclosures>. That makes about $1.0
billion of data vendor costs for those nine months, against $18.8 billion of compute spend, per
Epoch AI (2026): <https://epoch.ai/data-insights/anthropic-openai-compute-spend-growth>.

{@kimi}: Kimi Team, "Kimi K3: Open Frontier Intelligence" (2026), section 5.3: "Throughout Kimi K3’s
training and evaluation, a total of 51,219,741 sandboxes across 1,505,678 images were created."
<https://github.com/MoonshotAI/Kimi-K3/blob/main/k3_tech_report.pdf>

{@pricing}: Anthropic's API pricing (2026): Claude Fable 5.2 costs $8 per million input tokens and
$40 per million output tokens. <https://platform.claude.com/docs/en/about-claude/pricing>

{@mechanize}: Mechanize, "Cheap RL tasks will waste compute" (2025): frontier RL tasks produce
"transcripts with an average length of around 100,000 tokens per task", growing 5x a year, and are
trained "with a group size of 64".
<https://www.mechanize.work/blog/cheap-rl-tasks-will-waste-compute/>
