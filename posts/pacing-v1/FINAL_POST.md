---
title: Pacing
date: 2026-11-17
draft: true
rating: 2
---

I am bullish on AI labs establishing best practices which incidentally slow down the pace of
progress. These mostly serve the purpose of _slowing down now_, while Verified Compute Allocation
Disclosures (VCAD) handle _slowing down later_.

## Going Slower Now

All numbers estimate quickly. You could convince me they are off by an OOM.

### Security Measures (eg SL4) That, as a Side Effect, Slow Down Research Progress

The SF rumor mill tells me this would slow down research progress by tens of percentage points. It's
not clear how to operationalize this. Lab employees could insist that weights be under SL4 level
security in $n$ months. The labs take security
[very seriously](https://techcrunch.com/2025/07/07/openai-tightens-the-screws-on-security-to-keep-away-prying-eyes/),
yet still not seriously enough. Further reading:
[LessWrong](https://www.lesswrong.com/posts/gG4EhhWtD2is9Cx7m/implications-of-the-ai-security-gap),
[Situational Awareness](https://situational-awareness.ai/lock-down-the-labs/).

### External Audits Prior to Internal Deployments

[Many](https://blog.redwoodresearch.org/p/prioritizing-threats-for-ai-control)
[experts](https://metr.org/blog/2025-01-17-ai-models-dangerous-before-public-deployment/) believe
that most takeover risk arises from internal deployments at labs, not rogue agents escaped from the
datacenter. Yet most safety and auditing work goes into model cards which inform and block
_external_ deployments. For Mythos Preview, Anthropic did only a
[24-hour internal check](@mythos-card) before deploying internally. Their RSP requires a Risk Report
[30 days after internal deployment](@rsp).

[^aq]:
    A related question I hope to write about soon: should we insist on externally deploying any
    model which is deployed internally? Arguments against: distillation, misuse. Arguments in favor:
    safety research, public knowledge of capabilities.

I don't expect labs to let their compute sit idle, and there are more VCAD-flavored compute uses
which I expect to be helpful. Starting with ideas I have not seen proposed seriously:

### Spend 5% of Compute Searching for Vulnerabilities in Open Source Software

AI labs are already doing this (see
[Daybreak](https://openai.com/index/daybreak-securing-the-world),
[Glasswing](https://www.anthropic.com/glasswing)). Claude estimates[^ce] that $O(30\text{bps})$ of
Anthropic's compute went to Glasswing; it's not clear how much more compute these projects could
absorb.

[^ce]:
    ```claude
    - Glasswing launched 2026-04-07 with up to \$100M of Mythos Preview credits, at list price, for 12 launch partners and 40+ other organizations.
    - Anthropic's compute and infrastructure expense was \$18.8B for the first nine months of 2026 and \$9.9B in Q3 alone ([Sacra](https://sacra.com/c/anthropic)), so about \$30B for the full year.
    - $\$100\text{M} / \$30\text{B} = 33\text{bps}$.
    - Adjustments: the credits are at list price and revenue runs about 1.8x compute cost, so at cost it is \$55M, or 18bps. That assumes every credit gets used. Anthropic's own scanning with Mythos Preview is unpublished and adds to it.
    ```

### Spend 3% of Compute on Monitoring of Internal or External Deployments

AI labs reveal a surprisingly large amount about their monitoring setups.[^cm] Claude Fermi
estimates that $O(30\text{bps})$ of frontier lab compute goes to monitoring.[^cfm] Given Hugging
Face, the real number can and should be much higher.

[^cm]:
    OpenAI:
    [How we monitor internal coding agents for misalignment](https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment)
    (2026). Anthropic:
    [Sabotage Risk Report: Claude Opus 4.6](https://www-cdn.anthropic.com/f21d93f21602ead5cdbecb8c8e1c765759d9e232.pdf)
    (2026, sections 5.1 and 8.4),
    [Alignment Risk Update: Claude Mythos Preview](https://www-cdn.anthropic.com/3edfc1a7f947aa81841cf88305cb513f184c36ae.pdf)
    (2026, section 5.5),
    [Claude Opus 4.8 system card](https://www.anthropic.com/claude-opus-4-8-system-card) (2026,
    section 6.2.1.2).

[^cfm]:
    ```claude
    - A monitor reads each transcript once. The agent re-reads its growing context on every turn (cache hits, about 10% of input cost) and pays for output tokens (about 5x input cost).
    - Take a 50-turn trajectory that ends at 100k tokens of context. Agent: 2.5M cached input tokens (250k input-equivalents) plus 30k output tokens (150k) = 400k. Monitor: 100k input plus 2k of reasoning (10k) = 110k.
    - So a monitor of the same tier costs about 25% of the agent it watches.
    - Internal agents use about 2% of a lab's compute. This is my guess; no lab publishes it.
    - OpenAI monitors 99.9% of internal coding-agent traffic with GPT-5.4 Thinking: $25\% \times 2\% = 50\text{bps}$.
    - Anthropic in February 2026 sampled 10% of Claude Code actions: 5bps. By May 2026 it covered "most internal traffic", which puts it near OpenAI's number.
    - Neither figure includes the cheap misuse classifiers on external traffic.
    ```

### Spend 80% of Compute on External Inference

This proposal is the most boring, most scalable, easiest to operationalize, and does the most work
towards building robust ways of validating where compute gets spent. The hard part is the _how_,
which I discuss briefly in the next section.

## Going Slower in the Future

Much ink has been spilled on "how to prove that you are not spending your compute on AI R&D."
[AI 2040](https://ai-2040.com/supplements/verification-plan) is a great place to start.

I plan to write about this in more detail in the future. Here is my teaser of promising approaches:

- Use hardware guarantees to ensure you are running the model you say you are (slightly immature).
- Use zk-snarks to sign inference, enabling privacy while guaranteeing that your tokens came from a
  fixed model. This is 2-3 OOMs too slow to be useful at present.
- Make your whole datacenter open and public, then recompute random outputs to guarantee that a
  fixed model is doing inference. This assumes that "open and public" isn't catastrophic, which is a
  big if.
- Physically destroy horizontal bandwidth inside your datacenter. This makes large training runs
  hard but not impossible and doesn't make much sense.

<!-- @robbie done (was "@c put this whole monologue in a commenet plz"): everything from here to the end of the file is commented out.

I am confused by people's pacing proposals. People talk about verifying that a certain percentage of
compute goes to things like non-capabilities research or inference, and they have fancy frameworks
to deal with this because they claim that things like scalable oversight are secretly capabilities
research, even if they look like interpretability research. I object on three grounds:

1. There's better, lower-hanging fruit: policies that would slow just by accident that we should
   implement anyway. By that, I'm primarily thinking of security. Implementing super strict security
   safeguards would slow down algorithmic progress (e.g., you can't talk about algos in Slack, and
   you have to work out of a skiff). I think the incidental slowdown stuff should be first on the
   docket. I'm not sure if there are other examples outside of security.
2. These proposals are so complicated, and political will and human understanding are hard to come
   by. Deciding whether scalable oversight research counts as capabilities versus alignment: if
   you're fighting that battle, you've already lost. I think these metrics will get gamed. Sam
   Altman is better at this game than you are, and the politicians will not understand. I think you
   should instead fight your battles on forcing a certain standard. I know that companies are
   working on this. I guess I take it as an axiom that if you can succeed at prosaic alignment,
   you're on track to proceed with non-prosaic alignment. I know that other people disagree with
   this. Whatever. It would be excellent if we had some alignment standard we made companies hit
   that implicitly slowed down progress because they couldn't deploy their model until they passed
   said regulatory framework. It obviously can't just be model scores 100% on Harmbench. That's
   boring and dumb. It could be that government red teamers try to hack your model and your
   safeguards and your whole production system before you can even deploy internally. That would
   require a lot of political will, but sounds excellent, and that would implicitly do a lot of
   slowing down. I'm not proposing that we make some shit government body. I actually want it to be
   a good government body, but I want corporations to have to really, really succeed at aligning
   their model before they can deploy it. Anyway, in general, I want a standard of alignment, as
   opposed to "we're slowing down for the sake of slowing down." I think that sounds more
   politically tenable. If you are slowing down for the sake of slowing down, this third part I feel
   most uncertain about. There's a concept in trading where one never does partial takes. If it's
   good to trade 100 shares at $50, it's good to trade 1,000 shares at $50. Well, that's not true.
   If someone is resting a bid for 1,000 shares, you might not want to hit all 1,000 when you would
   be willing to hit their bid for 100 shares. That does not mean that you should hit the first 100
   shares of their 1,000. You should either hit all 1,000, or you should hit none and wait for the
   price to rise because you think that their demand to buy is raising the price (the fair price of
   the stock). I guess this analogy probably doesn't apply here, unfortunately, and is not a very
   interesting thing to bring up, but I do, in general, question the idea that slowing down is the
   right framing. Does it matter if we get a misaligned ASI in 2030 or 2028? It matters that it
   doesn't happen, which means we should be aiming for each model we release to be maximally
   aligned, not to have it happen slowly. I understand that time is instrumental in this, and it
   takes time to review things, but that is possibly why we're in a maximally bad regime at present,
   where, in fact, no one is reviewing Model 4. It is just being deployed internally, which is maybe
   what everyone's saying about external auditors. It really is a shame that the U.S. government is
   not interested in doing this auditing. Surely the EU could do this. I love this idea. Surely the
   EU could say, "Any company which does business in the EU must allow our EU auditors into your
   lab." Would it work? How many dollars is it worth OpenAI to have a total EU AI monopoly if they
   agree to this and Anthropic doesn't? Probably not that many dollars. Not enough to let them have
   strict, strong auditors. Certainly the EU has a lot more to lose and could cripple its own
   economy. Well, no. I guess it would cripple its own economy, and it would also cripple the global
   economy. You could say, "I can't say Google can't use." No, sorry, bad example. The EU couldn't
   just say, "Bank of America, you can no longer access European financial markets if you use Claude
   because they don't abide by our auditing regime." I guess they could maybe do this, but I
   understand why it would be so hard and politically difficult to do this. You're punishing by
   association, and then people would set up shell corporations, etc. Bank of America Prime would do
   business in the EU, while Bank of America Original uses Anthropic models. Okay, yeah, maybe that
   doesn't work. Oh well.

Okay, another idea: you could have pacing be that you must externally deploy your model at the same
time you internally deploy it. There's some bullshit around: you get to have classifiers on your
external deployments, and maybe you even get to have the model catastrophically forget things. But
there should be some standard for "everyone gets it," and if it's too safe for external deployment,
it's too unsafe for internal deployment.

Maybe that's horrible for distilling reasons. That's actually an open question to me: to what extent
should stuff be deployed externally or not? I think it's quite hard. Maybe that is a fundamental
issue of our time: how to make powerful models available, auditable, not distillable.
-->

{@mythos-card}: Anthropic, "System Card: Claude Mythos Preview" (2026), section 4.1.4.
<https://www-cdn.anthropic.com/08ab9158070959f88f296514c21b7facce6f52bc.pdf>

{@rsp}: Anthropic, "Responsible Scaling Policy", version 3.4 (2026), section 3.1.
<https://www.anthropic.com/rsp> The norm should be that model cards come out at internal deployment
time.[^aq] Bonus points if an external auditor or USG needs to sign off on the deployment.
