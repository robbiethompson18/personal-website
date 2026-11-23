---
title: scattered thoughts on datacenter security
date: 2026-11-22
draft: true
rating: 2
---

Epistemic status: I don't work at a lab, and I don't have close friends who do, and I've never done
large (>x flops) training runs, but I have spent ~200 hours of my life thinking about these topics.
So take all numbers and claims in this post as the best guess of an informed amature armed with lots
of AI help.

The AI Safety community is correctly freaking out about security at frontier AI labs. If we can't
make a deal with China to pause, and the US pauses unilaterally, and then China steals model
weights, then we are forced to race again to not fall behind.

Here are some questions I hope to deconfuse myself about:

- The world seems to believe that frontier labs are thoroughly infilitrated, both in cyberspace and
  by employees who are MSS.[^MSS] Yet the labs seem to care a lot about security.
- There are many things the CCP could steal: weights, algorithms, RL environments, RL rollouts,
  source code, etc. What is important? What is likely to go?
- How to model the CCP? Asleep at the wheel? Very wise to AGI and acting clueless so that they can
  steal the weights at the right moment?
- what things are easy to steal? Easy to secure? and vice versa?

[^MSS]: MSS is the CCP's intelligence service, something like their FBI/CIA/NSA combined.

## What to steal:

### Model Weights

I speculate that frontier models are about ~10T params, or ~10TB of data. This fits onto one
external hard drive you could buy on
[Amazon](https://www.amazon.com/Western-Digital-Elements-External-external/dp/B07G3QMPB5/ref=sr_1_1?adgrpid=201292937674&dib=eyJ2IjoiMSJ9.cZ4wQt3YRaemtsvis3wjyDVpr6IU5p5jUTvPgPvV8ZLn4BcAE8pd6rdrfRZgvQCp1ZvFzTcIGfLv2cvbvGrZR-OARKr1IkufHaTdbUeiNg09C6Zfu9CKd3GyqaobXzBwqBB9Mb2Dw7hgUDvN3xPGyKiPdyShtgrbCW_wHjM71pxbJsIbMX-9dtWwB1Olq8hf5yxPbwP35qqkmQQMAT81Da0Hk8FNIt9YIv7lvzIT91A.k2dsUE6p-7jZSBrqkQYt3-zdZBN0OQWOJpATxwCPAQY&dib_tag=se&hvadid=816788423012&hvcampaign=24009541080&hvdev=c&hvexpln=0&hvlocphy=9032075&hvnetw=g&hvocijid=5592404375246103090--&hvqmt=e&hvrand=5592404375246103090&hvtargid=kwd-474012051722&hydadcr=9589_14017052_2516394&keywords=10tb%2Bflash%2Bdrive&mcid=46cdd254666235ad9b9f9b6295e4201c&qid=1795393686&sr=8-1&th=1).
Cursed. [^bandwidth] With the weights you instantly have your adversary's best model. Even if the
Anthropic trained a model to do only Anthropic's bidding, it would be trivial for the CCP to undo
this. Models are or will soon be good enough that they can improve themselves, subject to the
constraings on how many experiments they can run on your compute. So if China gets GPT 10 the could
be off to the races.

[^bandwidth]:
    Lots of security proposals involved limiting the bandwidth between some section of the data that
    holds model weights and the 'outside world' (in this case researcher's laptops). However model
    weights need to be streaming tokens during inference and saving checkpoints during training. The
    training issue is easily solved: let your egress limit apply to one permieter which holds both
    your GPUs and the object storate which holds checkpoints. Inference limits are more challenging:
    labs serve ~1 trillion tokens from frontier models per day, which is ~3e13 bits of information,
    or 370 Mbits/s. This means that the fiber which sends out inference tokens can be used to egress
    weights in 2.5 days.

<!-- @robbie done (was "@c make a guess for Astra / Mythos tokens" and "@c do this BOTEC plz"). The BOTEC:
- Tokens: no lab publishes tokens per model, so this comes from revenue. Anthropic booked $17.0B in Q3 2026, which is $185M a day. I guess 40% of that is the flagship (Fable and Mythos share a model, and Mythos alone is restricted to verified organizations), so $74M a day. Output listed at $50 per million then. Each output token comes with about 25 input tokens, mostly cache hits at $0.25 per million, so an output token brings in about $80 per million at list price and about $60 after subscription discounts. $74M / $60 per million = 1.2 trillion output tokens a day. Range 0.3 to 3 trillion. I assume Astra is the same size.
- Bits: 1 trillion tokens × 4 bytes of text per token = 4 TB a day = 3.2e13 bits. Over 86,400 seconds that is 370 Mbit/s.
- Time: your 10 TB of weights is 8e13 bits, and 8e13 / 3.2e13 = 2.5 days. A 2 to 5 TB model takes 12 to 30 hours. Across my token range, 10 TB takes 1 to 8 days.
- 2.5 days is the ceiling. It needs an attacker who owns the serving stack and replaces every customer's response with weight bytes, which customers notice within minutes.
- With Greenblatt's 2024 scheme (the weight-holding datacenter sends responses compressed against a small model both sides hold, measured at under 1 bit a token) the link carries at most 125 GB a day, and 10 TB takes 80 days.
- If the lab re-runs a sample of responses and checks they reproduce (Rinberg et al., 2025), the hidden channel drops to under 0.5% of the text: 20 GB a day, 500 days.
- Buying it through the API: 10 TB of text is 2.5 trillion output tokens, $125M at $50 per million, and it is 2.5 days of the model's whole output.
- "The fiber" carries more than the text. Streaming wraps each token in 100 to 300 bytes of JSON (my estimate from the streaming format), so the link itself runs at 10 to 30 Gbit/s. An attacker who can write raw bytes to it, and not only choose tokens, moves 10 TB in 1 to 2.5 hours.
- Notes: POST_RESEARCH.md, "Part: Egress Through Inference Tokens".
-->

### Algorithmic Secrets

Questions:

- Smart people ([Dario](@dario), [RAND](@randinsights), [AIFP](@aifp)) claim that a significant
  portion of algorithmic secrets can be conveyed in a couple of pages of text.
- Chinese labs have the human capital to do a frontier training run using these secrets.
- Frontier runs are aobut 10% of R&D compute. Claude and I speculate that GPT 6 Astra took 9.4e26
  flops total,[^astra] trained on hundreds of thousands of Blackwells in Abilene. China has about
  2e21 total flops, so it would take them 5 days to do an Astra-sized training run if they spent all
  of their compute on it, compared to the 90 days it took OpenAI at Abilene. Realistically, if China
  used their biggest site in Johor, Malaysia, it would take them about 130 days to train
  Astra.[^Johor]

[^astra]:
    This is [Epoch's estimate](https://epoch.ai/data/ai-models) (2026): 100,000 GB200s × 90 days
    (7.8e6 seconds) × 1.2e15 useful FLOP/s per GB200 (25% of its FP8 peak) = 9.3e26, listed as
    9.4e26. OpenAI has only said
    ["more than 100,000 GPUs"](https://fortune.com/2026/09/03/openai-debuts-gpt-6-astra-computer-use-greg-brockman-says-start-of-agi/)
    (2026); the 90 days and the 25% are Epoch's assumptions. China's number is IFP's
    [4.6M H100-equivalents](https://ifp.org/how-to-increase-americas-ai-lead-over-china/) (2026) at
    the same utilization. A GB200 is 2.54 H100-equivalents, so 4.6M × 1.2e15 / 2.54 = 2.2e21 useful
    FLOP/s, and 9.4e26 / 2.2e21 = 4.3e5 seconds = 5 days.

[^Johor] China's biggest site is in Johor because it's illegal to ship Nvidia chips to China, but
it's not illegal to sell them to a Malaysian company who then rents the compute to China. The Johor
site is x H100e, about y% as large as the biggest US site (Stargate in Abilene, Texas). It's owned
by Bain, operated by Oracle, and used by Bytedance, originally for TikTok.

<!-- @robbie done (was "@c I want to hear way more about this Johor site? Are we up in arms that Bytedance is using blackwells? How do we just know?"). Short version: the megawatts are known, the Blackwells are a guess, and yes. Full notes: POST_RESEARCH.md, "Part: The Johor Site".
THE SITE
- Bridge Data Centres MY06, Sedenak Tech Park, Kulai district, Johor. Owned by Bain Capital. Ten buildings on two campuses, seven running, 243 MW of IT power.
- ByteDance as anchor tenant is on the record: a 2022 Malaysian government press release names "ByteDance System Sdn. Bhd". It opened as a TikTok serving site.
HOW WE KNOW
- Power: Epoch counts cooling units in satellite photos and reads the owner's SEC filings. That part is decent.
- Chips: nobody outside has seen them. Epoch fills each building with whatever Nvidia was mostly selling the quarter before it opened. Its page data marks every chip count "Estimate" with the note "Chip type based on NVIDIA chip sales in preceding quarter". That rule puts 61,573 B200s in buildings 5 to 7, which is 70% of the 221,000 H100-equivalents.
- Evidence against: ByteDance installs its own servers there, and a Chinese-owned company has needed a US licence to buy these chips since 2023. IFP (2026), relaying SemiAnalysis, says ByteDance's own leased halls in Malaysia hold CPUs and unrestricted GPUs.
- Where ByteDance's Blackwells more likely are: capacity that Oracle rents inside DayOne's Johor campuses and rents on to ByteDance (IFP sizes it at 196 MW of GB200s), and a deal with Aolani Cloud for about 36,000 B200s (WSJ, March 2026, over $2.5B; IFP still listed it as "delayed or unconfirmed" in October 2026).
- So I was too confident in the earlier box. My odds: 65% that ByteDance is training frontier models on Blackwells somewhere in Johor today, 20% that it is at MY06 on B200s it owns. The 130-day figure assumes Epoch's chips are real.
ARE WE UP IN ARMS
- Renting was legal until November 19, 2026. US rules controlled shipping a chip, not renting time on one. Nvidia's line in March 2026: "By design, the export rules allow clouds to be built and operated outside controlled countries".
- 2026 in order: the House passed the Remote Access Security Act 369 to 22 in January (stuck in the Senate). WSJ's Aolani story in March. IFP's October report put Chinese remote access at 1M H100-equivalents, 75% of it in Southeast Asia. In early November Nvidia told cloud partners 51% of their capacity must go to non-Chinese customers. Jensen Huang resigned as Nvidia CEO on November 12 after reports of a relationship with a former executive of Megaspeed, a Singapore firm that rents Nvidia chips to Chinese customers. The Commerce Department rule came out four days later.
- The rule: a licence is needed to ship chips to any data center anywhere that gives a China-headquartered company more than 12,000,000 TPP, about 760 H100s. Existing sites have 90 days, to February 17, 2027. It does not order installed chips switched off; the penalty is no future chips. Recommender systems are exempt and generative models are not, so TikTok ranking can stay and Doubao training can't.
- Reactions: China's commerce ministry threatened countermeasures. Malaysia's trade minister: "if you want to continue conducting your business here, you must comply with US rules and regulations". Nothing from ByteDance.
-->

### Data, RL Environments

Algorithmic secrets are enough to make an excellent pretrain, but you can't posttrain without RL
environments. US labs spend tens of billions every year ([about $8 billion in 2026](@dataspend)) on
data and environments.

<!-- @robbie done (was "@c cite for me plz?"). The sources say billions, not tens of billions, so I put the number beside your claim instead of citing something that contradicts it. Change the wording or drop the number. Full notes: POST_RESEARCH.md, "Part: What Labs Spend on Data and Environments".
- All US frontier labs together: about $8B in 2026 (range $6B to $11B), $4B in 2025, $2.5B in 2024. It doubles each year. The totals are my sums from the items below, not a published figure.
- Anthropic (amended S-1, read second-hand): costs for data quality and evaluation vendors rose $757M in the first nine months of 2026 against a year earlier. That makes about $1.0B for the nine months, and over $2B a year at the third-quarter pace.
- OpenAI: about $1B in 2025, including human experts and RL environments (The Information via Epoch, 2026). No 2026 figure exists.
- The vendor side agrees: a July 2026 tally of data vendors' revenue run rates comes to about $8.5B (Deedy Das, Menlo Ventures; I did not check it). Mercor alone booked $614M in the first half of 2026, 91% from model makers.
- It is about 5% of compute spend: Anthropic's $1.0B against $18.8B of compute over the same nine months.
- "Tens of billions" becomes true around 2028 if the doubling holds.
-->

can we fermi estimate:

- how mant RL envs one needs to train Mythos
- how mant bytes of data are in those environments
- If you could reaosnably compress this.
- what data labs SFT on in a frontier train, and how many bytes that is
- what am I not thinking of? They do RLHF on policy?

<!-- @robbie done (was "@c can we fermi estimate:" and the five bullets above). Central guesses with ranges. Arithmetic and sources: POST_RESEARCH.md, "Part: RL Environments, SFT Data and Other Post-Training Assets".
HOW MANY ENVS
- "Environment" gets used three ways. About 1,500 environment families (300 to 5,000), 1M sandbox images (200k to 5M), 1.5M tasks (300k to 10M). A task is a prompt plus a grader.
- From budget: Anthropic reportedly discussed over $1B a year on environments, and tasks cost $200 to $2,000 each (Epoch, 2026). $600M of that at $630 a task is about 1M tasks.
- From compute: about $230M of RL compute for one flagship at $2.30 an episode is 100M episodes, which at 64 rollouts per task is 1.6M tasks. The run emits about 15T tokens of rollouts. The $2.30 is my guess.
- No US lab publishes a count. The public anchor is Moonshot's Kimi K3 report (2026): "a total of 51,219,741 sandboxes across 1,505,678 images".
HOW MANY BYTES, AND DOES IT COMPRESS
- 2 PB if every task's full container image is counted. 100 TB once shared layers are deduplicated (10 TB to 1 PB), which is how a lab stores it.
- 250 GB if you keep only what can't be rebuilt from public sources: task text, graders, the source of cloned apps, private seed files. 70 GB after zstd. That is about 30,000x smaller than raw. A coding task is a repo URL, a commit hash, a Dockerfile, a prompt and hidden tests: tens of KB.
- What doesn't compress: human-written rubrics and solutions, private work files, VM images of commercial software.
- What doesn't transfer at all: the record of which environments are broken. Epoch's interviewees call resistance to reward hacking the top quality criterion.
SFT
- SFT is now the cold start before RL and the cleanup after it. About 20M examples, 100B tokens, 0.4 TB (20 GB to 8 TB). Contents: expert demonstrations, tool-use traces, synthetic dialogues, character and refusal data, outputs distilled from bigger models.
- The human-written part is about 20 GB. $1B of expert time buys at most 60 GB of typed text.
WHAT YOU'RE NOT THINKING OF
- RLHF as in 2022 (humans rank samples, a reward model learns the ranking) is now minor. Most RL compute runs against programmatic graders (unit tests, final-state checks), then LLM judges with rubrics. The humans moved upstream: they write the tasks and the graders.
- Ranked by value to a thief who has the recipe: (1) the RL rollouts themselves, 15T tokens, about 60 TB, a distillation set with the reasoning visible and a reward on every episode; (2) the training-mix config and the environment QA records, MBs; (3) the experiment-tracking database, GBs, the record of the 90% of compute that wasn't the final run; (4) the environment library; (5) graders, judge prompts, reward models; (6) eval suites. Items 2, 3, 5 and 6 together are under 100 GB, and they are neither for sale nor recoverable from weights. The byte sizes for 2, 3 and 6 are my guesses.
- A thief may not need to steal environments. ChinaTalk (2026) reports US vendors "are selling roughly half a billion dollars worth of data to Chinese AI labs", the same products US labs buy, mostly outside export controls. Chinese labs also build their own at this scale: Kimi's 1.5M images, and a 2026 paper that built 45,320 coding environments for about $20 each.
- That cuts against the section's opening line. Environments are needed for post-training, but they are the least exclusive asset on the list.
-->

{@dario}: Dario Amodei at the Council on Foreign Relations (2025): "many of these algorithmic
secrets, there are $100 million secrets that are a few lines of code."
<https://www.cfr.org/event/ceo-speaker-series-dario-amodei-anthropic>

{@randinsights}: RAND, "Securing AI Algorithmic Insights" (2026): "a few lines of code, a diagram,
or a brief technical exchange might be enough to convey a high-value insight."
<https://www.rand.org/pubs/research_reports/RRA4685-1.html>

{@aifp}: AI Futures Project, AI 2027 security forecast (2025), which sizes the secrets worth
protecting at "the most important 10KB (plaintext)" from the last month. 10KB of plain text is about
3 pages. <https://ai-2027.com/research/security-forecast>

{@dataspend}: My sum across US labs, from two anchors. OpenAI spent "about $1 billion on data (which
includes paying for human experts and RL environments)" in 2025, per Epoch AI (2026):
<https://epoch.ai/gradient-updates/can-ai-companies-become-profitable>. Anthropic's amended S-1 says
its costs for data quality and model evaluation services "rose by $757 million in the first nine
months of 2026, compared with a year earlier", per Strauss and O'Reilly (2026):
<https://asimovaddendum.substack.com/p/anthropics-missing-s-1-disclosures>.
