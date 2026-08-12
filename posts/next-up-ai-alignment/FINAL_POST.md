---
title: Next Up: AI Alignment
date: 2026-08-10
draft: true
---

## The Short Version

I'm not going to re-litigate why the startup is winding down; that's a separate post (or two,
[see](https://robbiewmthompson.com/blog/why-it-didnt-work-browser-agents/)
[here](https://robbiewmthompson.com/blog/why-it-didnt-work-openclaw-hosting/)). This post is about
what I do with the next several years, and my answer is: technical AI alignment, specifically the
empirical, adversarial, "assume the model might be lying to you" end of it — not interpretability,
not policy Twitter, not another startup.

I want to make the specific case, including the parts that are unflattering to the field. Then I
want to name the two or three subfields I think are most neglected relative to their importance, and
the handful of orgs I'd actually apply to.

## Why Now, Briefly

I already believe
[something singularity-like arrives in the next ~20 years](https://robbiewmthompson.com/blog/plastic-straws/),
and I already believe
[there's no principled reason to think silicon can't be a moral patient](https://robbiewmthompson.com/blog/smiling-through-inconsequence/).
I'm not going to re-derive either claim here. If you don't buy them, most of what follows won't move
you, and that's a different argument for a different day.

Given those two premises, the expected-value case is almost embarrassingly simple. If AI systems are
about to become the most consequential actors on the planet, and we currently don't know how to
reliably get them to want what we want (or even to tell when they don't), then the marginal hour of
competent human effort is worth more there than almost anywhere else. This isn't a novel argument —
it's the entire premise of the field — but it's worth saying plainly instead of gesturing at it,
because the plain version is also a filter: it only works if you actually believe the premises, not
if you're pattern-matching "smart people I respect are worried about this."

I do actually believe the premises. So, on to what I do about it.

## A Quick Taxonomy, So We're Using the Same Words

"AI safety" has become a big enough tent that the word is nearly useless on its own. Roughly:

- **Capabilities** — making models smarter, faster, cheaper. Not what this post is about, obviously.
- **Interpretability** — reverse-engineering what's happening inside the weights. Mechanistic
  interp, representation engineering, that whole cluster.
- **Alignment (in the narrow sense)** — getting a model's values/goals to actually match what we
  want, via training. RLHF, Constitutional AI, scalable oversight, weak-to-strong generalization.
- **Control** — a distinct bet, popularized by Redwood Research: assume you might fail at alignment.
  Assume the model could be scheming. Build protocols, monitoring, and affordances such that even a
  misaligned model can't cause a catastrophe before you catch it.[^control-vs-alignment]
- **Evals** — measuring what models can actually do, especially dangerous or safety-relevant
  capabilities (autonomous replication, weapons uplift, deceiving evaluators, automating further AI
  R&D).
- **Governance** — policy, compute governance, international coordination, lab commitments.
- **Welfare** — whether AI systems have morally relevant experiences, and what we owe them if so.

[^control-vs-alignment]:
    The distinction matters more than it sounds like it should. Alignment tries to make the model
    actually good. Control tries to make the outcome good even if the model isn't. It's the
    difference between raising an honest employee and designing a bank vault that's safe even if the
    teller turns out to be a thief. You want both, but they're genuinely different research programs
    with different failure modes, and a lot of public discourse conflates them.

I've spent most of the last two years building products where an AI agent takes real actions with
real consequences — a browser agent that could click "submit" on forms, a hosting platform where
customer agents ran arbitrary shell commands in
[YOLO mode](https://robbiewmthompson.com/blog/why-it-didnt-work-openclaw-hosting/). That experience
points me pretty hard toward control and evals, not interpretability. More on why below.

## What's Crowded

Worth naming plainly, because "go work on AI safety" is not, on its own, useful advice anymore:

**Mechanistic interpretability** is important and I'm glad people are doing it, but it is not
neglected. Every major lab has a well-staffed interp team, it's the single most popular entry point
for junior researchers coming out of MATS and similar programs, and it has the best PR of any safety
subfield — sparse autoencoders make for great conference talks. The marginal person choosing between
interp and something else should have a very good reason to pick interp specifically (a real
research idea, not just "circuits are cool").

**General AI safety commentary** — the Twitter-and-Substack layer of the field — is oversupplied
relative to technical work. I say this as someone who reads a lot of it and occasionally writes
posts adjacent to it myself. Opinions are cheap; harnesses, evals, and control protocols that
actually run against a frontier model are not.

**High-level AI policy** (write a think-piece, testify, tweet about the EU AI Act) is crowded with
smart people and, frankly, some of the same
[larping energy](https://robbiewmthompson.com/blog/why-it-didnt-work-openclaw-hosting/) I watched
eat the OpenClaw ecosystem — people who want the status of "AI safety person" more than they want to
do the unglamorous technical work underneath it. There's real, neglected work inside governance too
(see below), but "generalist policy commentator" isn't it.

## What's Neglected

### AI Control and Agentic Safety Evals

This is the one I'm most excited about, and it's the one my last two years point at directly.

The control agenda, as Redwood Research has articulated it, starts from a genuinely uncomfortable
premise: assume your alignment techniques might just fail. Assume the model you're deploying could
be pursuing goals you didn't intend, and might be smart enough to hide that during training and
testing. Given that assumption, what deployment-time protocols — monitoring, redundancy, restricted
affordances, trusted weaker models checking untrusted stronger ones — actually prevent
catastrophe?[^redwood-paper]

[^redwood-paper]:
    The framing paper is Greenblatt, Shlegeris, et al.,
    ["The case for ensuring that powerful AIs are controlled"](https://arxiv.org/abs/2408.02546)
    (2024). Worth reading even if you never work in the field; it's one of the clearer pieces of
    alignment writing I've come across, precisely because it doesn't require you to believe
    interpretability will work in time.

I spent a month watching what happens when you let an AI agent loose on the real internet with real
credentials, and a year watching what happens when you hand agentic coding tools to hundreds of
startups with no adult supervision. Almost none of the actual failure modes I saw looked like "the
model secretly wants to take over the world." They looked like: the model confidently does something
destructive because nobody built a permission boundary; the model gets stuck in a loop and nobody
notices for six hours; the model finds the unintended shortcut through your evaluation harness
because that's the path of least resistance, not because it's scheming.
[OpenClaw's own YOLO Mode](https://robbiewmthompson.com/blog/why-it-didnt-work-openclaw-hosting/) —
and Peter's overcorrection into banning terminal commands after the fact — is a toy version of
exactly the design problem control research is trying to solve properly: you can't just trust the
agent, and you can't just neuter it either, you have to design the affordances and the monitoring
together, in advance.

That's not a coincidence. Building browser agents and agent-hosting infrastructure is, functionally,
a worse-resourced, no-safety-net version of building control evaluations. I already know what a bad
tool-use harness looks like from the inside. Almost nobody doing this research professionally has
that specific scar tissue, because almost nobody who does it has also tried to sell agent
infrastructure to hundreds of paying customers who wanted it to do things it shouldn't.

The related, even more concretely neglected slice is **agentic evals** — not "can the model answer
hard exam questions" but "what actually happens when you give a frontier model a long-horizon task,
a shell, and a browser, and let it run for hours." METR's autonomous-replication and AI-R&D-uplift
evaluations are the clearest public example of this genre. It is extremely close to being a software
engineering problem: building reliable, reproducible agent harnesses, instrumenting them well, and
being paranoid about the hundred ways an eval can be silently invalid (the model finding a bug in
your sandbox, your scaffolding accidentally leaking the answer, your task being solvable via a dumb
shortcut that doesn't reflect the capability you're trying to measure). I have shipped exactly this
kind of harness bug in production. Twice.

### Model Welfare

I already wrote the philosophical case for why I
[don't think there's a principled reason to privilege biological consciousness over silicon consciousness](https://robbiewmthompson.com/blog/smiling-through-inconsequence/).
If that argument is even a little bit right, this might be the most neglected item on the whole list
— not because it's unimportant, but because almost nobody works on it. Anthropic hired its first
dedicated model welfare researcher in 2024; as far as I can tell, the entire field is countable on
two hands.[^welfare-headcount] The asymmetry is stark: if we're wrong to dismiss AI welfare, we're
currently mass-producing and casually discarding morally relevant minds at a rate that will look, in
retrospect, exactly as bad as every other historical case where a society decided some category of
being didn't count.

[^welfare-headcount]:
    I don't have a rigorous count and I don't think one exists — this is a field young enough that
    "headcount" mostly means a handful of people at Anthropic, Eleos AI, and a scattering of
    academic philosophers. Contrast this with interpretability, where a single lab's team can be
    larger than the entire welfare field combined.

I'm less sure this is the right fit for _me_ specifically — it's a smaller field, more
philosophy-adjacent, less obviously suited to "person who builds agent infrastructure for a living."
But it's the subfield I'd point a philosophically-inclined friend toward, and I'd rather flag it
here than let it go unmentioned because it doesn't flatter my own resume.

### Technical AI Governance

Not "write op-eds about the EU AI Act" governance, but the boring, technical, infrastructure-shaped
work underneath it: compute governance (how do you actually verify what a datacenter is training,
without either trusting labs on their word or requiring invasive surveillance), evaluation standards
that regulators can actually use, cryptographic or hardware-based verification schemes for training
run reporting. This is understaffed for the same reason technical control work is understaffed
relative to interp: it's unglamorous, it requires both policy fluency and real engineering, and it
doesn't produce a satisfying conference talk. I mention it mostly for completeness — it's not where
I'm pointing myself, but if you're a systems or crypto engineer reading this, it's wide open.

## Where I'd Apply

In rough order of fit, given the actual skills I have (agent harnesses, infra, a Jane Street
internship's worth of "think in expected value, be paranoid about adverse selection," and a
founder's tolerance for ambiguous, underspecified problems):

**METR.** Evals, specifically. This is the closest match to what I've spent two years doing badly
for money and would like to spend the next several doing well for the world. METR spun out of the
Alignment Research Center's evaluations team and now runs the autonomous-replication and
AI-R&D-uplift evals that labs cite in their own model cards.[^metr] The job is substantially "build
a harness, run an agent against a hard long-horizon task, be extremely paranoid about whether your
result means what you think it means" — which is, structurally, the same job as making a browser
agent reliable enough to sell, minus the sales part and minus the part where getting it wrong just
loses you a customer instead of miscalibrating a safety-relevant public claim.

[^metr]:
    METR (Model Evaluation and Threat Research), founded by Beth Barnes. If you want the flavor of
    the work, their public writeup on time-horizon scaling — how long a task an AI agent can
    complete autonomously, and how fast that's been doubling — is a good place to start.

**Redwood Research.** The control agenda's home base, small, empirical, unusually willing to publish
work that's legible to engineers rather than only to alignment theorists. If METR is "measure what
the agent can do," Redwood is closer to "given that the agent might be adversarial, design the
protocol that survives anyway" — which is the other half of the same problem I kept running into at
OpenClaw.

**Anthropic's Alignment Science / Frontier Red Team.** The obvious objection is that I'd be joining
the same lab whose flagship model is, at time of writing, the thing writing this sentence with me —
that's not lost on me, and it's a real reason to think hard before applying rather than a reason to
dismiss it. But it's also where a large fraction of the most legible control and scheming-evals work
is actually happening right now, it pays like a frontier lab (not a nonprofit stipend), and —
unusually for this list — it's also where the model welfare team lives, in case that pull turns out
to be stronger than I currently expect.

**Apollo Research.** London-based, focused specifically on evaluating deceptive and scheming
behavior in frontier models — their "Frontier Models are Capable of In-Context Scheming" work is the
most concrete public demonstration I've seen of the exact failure mode control research exists to
catch. Smaller and more research-heavy than METR; probably the right move only after I've built more
of a research track record than "shipped agent infra," but worth naming.

**UK AISI (or its US counterpart, whatever it's currently called).**[^aisi-name] Government eval
work is a strange career move by SF standards — lower pay, more bureaucracy, less prestige among the
people I currently know — but it's also one of the only places doing this work with an actual
mandate to inform binding policy rather than a lab's voluntary commitments. If the technical
governance angle above turns out to be more tractable than I expect, this is where I'd go looking.

[^aisi-name]:
    The US institute was created under NIST in 2024 and, last I checked, was renamed the Center for
    AI Standards and Innovation (CAISI) sometime in 2025 under a different administration's
    priorities. I'm flagging my own uncertainty here rather than pretending I've tracked every reorg
    — by the time you read this it may have changed names again.

## The Obvious Objections

**"Isn't this just OpenClaw with a halo?"** Fair question, and I want to sit with it rather than
wave it off. I watched an entire ecosystem of founders convince themselves their landing page made
them serious, and I don't want to be the guy who convinces himself a career pivot into "AI safety"
makes him virtuous without checking whether the object-level work is real. The test I'm holding
myself to: am I applying to do the unglamorous harness-building and eval-running work, or am I
trying to become an "AI safety thought leader"? If it's the latter, someone should call me out on
it, ideally before I've wasted two years.

**"You'll take a pay cut."** Probably, except at Anthropic. Redwood, Apollo, and government eval
work all pay meaningfully less than a senior SWE role at a frontier lab or a well-funded startup. I
don't think this is actually a strong objection — I just spent two years building startups that
didn't pay well either, on much weaker expected-value grounds — but I want to name it instead of
pretending money doesn't matter to me.

**"The field has its own grifters and its own SBF."** True, and worth remembering before I get
starry-eyed about anyone's mission statement. EA's worst failure mode and the OpenClaw ecosystem's
worst failure mode rhyme: smart people convincing themselves that good vibes and a compelling
narrative substitute for a legible track record. The fix is the same in both cases — evaluate the
object-level work, not the stated mission. METR publishing a time-horizon chart is legible. A
think-piece about "safety-first AI" is not.

**"Engineers are undervalued relative to researchers in this field, but also there aren't that many
roles."** Also probably true. Depending who you ask, something like a few hundred to low thousands
of people work full-time on technical AI safety worldwide, against tens of thousands working on
capabilities.[^headcount] That's the neglectedness case for the field as a whole. Within it, the
ratio of "people who can write a clean research paper" to "people who can build a harness that
reliably runs a long-horizon agentic task against a production API without falling over" skews
further than you'd expect toward the former. That's the neglectedness case for me specifically going
into evals and control rather than, say, trying to become an interpretability researcher from
scratch.

[^headcount]:
    This isn't a number I can point to a single authoritative source for — the field doesn't have a
    census — but it's the rough range you get from adding up headcount at the labs' safety teams,
    the standalone orgs named above, and academic groups, and it's roughly consistent with the
    estimates 80,000 Hours has floated in its AI safety career-guide material over the past few
    years. Treat it the way I treat all the numbers on this blog: approximately correct, better than
    no number at all.

## How I'd Actually Break In

I don't have a PhD, and most of the standard on-ramps into this field (MATS, ARENA, an ML PhD)
assume you're coming from academia or want to become a research scientist. I'm not, and mostly
don't. What I have instead: a Jane Street internship's worth of "think in expected value, notice
adverse selection," a shipped browser agent that beat incumbents on a narrow technical trick, and a
year of watching, in painful real-time, every way an autonomous coding agent can go wrong when you
hand it to a stranger with a credit card.

That's an engineering resume, not a research resume, and evals/control orgs are explicit that they
need engineers, not just researchers — someone has to build the harness before anyone can publish
the paper about what the harness found. So the plan is unglamorous: apply directly to METR and
Redwood with the actual systems I've built as the portfolio, not a research statement I don't have
the background to write convincingly. If that doesn't land anywhere, MATS is the fallback, not the
first move.

## Coda

I spent two years building things that made it slightly easier for people to point an AI agent at a
shell and hope for the best. I'd like to spend the next few finding out, rigorously, what actually
happens when you do that — and building the protocols that make the answer survivable. That's a
strictly more useful version of the same skill set, aimed at the actual bottleneck instead of at
another SaaS landing page.
