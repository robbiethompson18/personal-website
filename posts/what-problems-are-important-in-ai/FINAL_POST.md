---
title: Important Problems in AI
date: 2026-08-28
rating: 2
---

Epistemic status: Zero novel contributions, and probably not an outstanding summary either. Writing
this down to clarify my own thoughts.

First, it's worth stating the risks posed by AI:[^ex]

[^ex]: Not exhaustive.

1. Human extinction from misaligned AI (see [IABIED](https://ifanyonebuildsit.com/)). Human
   enslavement by machines.
2. Techno-oligarchy, concentration of power.
3. Mass casualty events from rogue actors with powerful AI (eg engineered pandemics).
4. [Crisis of meaning once almost no one can contribute meaningful work.](https://robbiewmthompson.com/blog/a-bullshit-job-for-every-american/)
5. Mass protests and economic turmoil from job displacement.
6. Not a risk per se, but it would be sad if friendly superintelligence is possible, but we don't
   build it because we can't figure out alignment or there's a massive backlash. I'm excited for the
   Glorious Transhumanist Future, conditioned on alignment being tractable.

Things get orders of magnitude less important as you move down this list, with the exception of
(6).[^fn]

[^fn]:
    Human civilization can be unimaginably larger and better than it is today. Plausibly the most
    important thing is to grab the GTF once we can reach it.

---

Next, it's worth stating what people are working on:[^ex2]

[^ex2]: Not exhaustive.

## 1. Alignment: Make AIs That Are Corrigible and Share Our Values

Alignment is the most important problem to solve in AI safety. Almost trivially, if the AI shares
our values it will help us and vice versa.

We have made lots of progress in 'quotidian alignment.' Claude won't assume the persona of Hitler or
tell you how to bully a child.

In addition to solving the problem of technical alignment, we need to determine our 'alignment
target.' Should superintelligent AI help us factory farm? Should humans be allowed to 'enslave' it?
To what extent should its values be corrigible?

There are strong theoretical arguments for why alignment is hard or impossible. I hope to summarize
these myself in the future; for today Claude will write a footnote with pointers to the most
important arguments.[^Claude]

[^Claude]:
    - Orthogonality + instrumental convergence: intelligence and goals are independent, and almost
      any goal is served by acquiring power and resisting shutdown
      ([Bostrom, 2012](https://nickbostrom.com/superintelligentwill.pdf);
      [Omohundro, 2008](https://selfawaresystems.com/wp-content/uploads/2008/01/ai_drives_final.pdf)).
    - Inner misalignment: a training process that selects for good behavior can produce a learned
      optimizer with a different objective that merely agrees on the training distribution
      ([Hubinger et al., 2019](https://arxiv.org/abs/1906.01820)).
    - Goal misgeneralization: capabilities generalize out of distribution while goals don't,
      demonstrated empirically in RL agents
      ([Langosco et al., 2022](https://arxiv.org/abs/2105.14111);
      [Shah et al., 2022](https://arxiv.org/abs/2210.01790)).
    - Specification gaming / Goodhart: any measurable proxy for what we want gets optimized in ways
      we didn't intend
      ([Krakovna et al., 2020](https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/)).
    - Deceptive alignment: a misaligned model that understands training has an incentive to act
      aligned until it's safe not to, and this behavior survives safety training once present
      ([Hubinger, 2022](https://www.alignmentforum.org/posts/A9NxPTwbw6r6Awuwt/how-likely-is-deceptive-alignment);
      [Sleeper Agents, 2024](https://arxiv.org/abs/2401.05566);
      [Alignment Faking, 2024](https://arxiv.org/abs/2412.14093)).
    - Corrigibility is anti-natural: an agent that wants X is incentivized to prevent you changing
      it away from X, so shutdownability fights against coherent goal-pursuit
      ([Soares et al., 2015](https://intelligence.org/files/Corrigibility.pdf)).
    - Value is fragile: human values are high-dimensional and getting almost all of them right still
      yields a worthless future
      ([Yudkowsky, 2009](https://www.lesswrong.com/posts/GNnHHmm8EzePmKzPk/value-is-fragile)).
    - Limits of human feedback: RLHF can't scale past the point where humans can evaluate outputs,
      and systematically rewards what looks good over what is good
      ([Casper et al., 2023](https://arxiv.org/abs/2307.15217)).
    - No retries: unlike every other engineering problem, the first superintelligence has to be
      aligned on the first try, with no ability to iterate on failure
      ([Yudkowsky, 2022](https://www.lesswrong.com/posts/uMQ3cqWDPHhjtiesc/agi-ruin-a-list-of-lethalities)).
    - For the counterargument that these are real but tractable, see
      [Christiano, 2022](https://www.lesswrong.com/posts/CoZhXrhpQxpy9xw9y/where-i-agree-and-disagree-with-eliezer).

## 2. Control: Build Robust Monitoring So That Misaligned AIs Can't Do Much Harm on Their Own

If we train a misaligned AI, how likely are we to catch it? We can run millions of alignment tests
during training and evaluation. If the model acts aligned in all of them, either:

- The model is aligned.
- The model can tell apart training and deployment with very high fidelity (plausible).
- The model acts misaligned with very low probability (still very scary).

Mitigations include:

- Lots of high-fidelity honeypots.
- Monitoring model outputs, escalating some for further (eventually human) review.
- Having untrusted models review or rewrite their own suspicious outputs (see
  [Ctrl-z](https://arxiv.org/pdf/2504.10374)).

## 3. Security

It would be really bad if:

- An AI escaped a datacenter.
- A foreign adversary stole frontier model weights.
- An AI surreptitiously took over all or part of the datacenter it runs on.
- An AI or foreign adversary hacked important things (the power grid, the military etc.).

Humanity should spend a huge amount of effort getting better at cybersecurity, and in particular, at
securing the weights to frontier models.

## 4. Safeguards

[Cambridge researchers reported](https://casp.ac/reports/ai-enabled-terrorism) on Boko Haram using
chatbots to build bombs. We'll be much sadder if they use Chat to build bioweapons or nukes.

Mitigations:

- Classifiers: block all model responses related to, say, biology (eg what Anthropic did to Fable in
  the early days).
- Jailbreak robustness: pay many red teams to try to elicit dangerous information out of your model.
- Unlearning: don't train your model on information about biology, or route that information to one
  expert in the network and then delete that expert, or use more complicated methods that get the
  model to forget information.

Safeguards work well, which is why I'm not a fan of open weight models. You can't run classifiers on
them. You can't patch jailbreaks. You can't revoke access if your model proves to be more dangerous
than anticipated.

## 5. Interpretability

Can we determine why models make the decisions they do? Which parts of the network and training data
are responsible? Are models aware they're being evaluated? Can we convince them otherwise? Do they
behave differently in deployment vs training? Can we detect misaligned models by studying their
weights and activations?

## 6. Pandemic Preparedness

Make far-UVC better, mass produce it, and install it in public places. Leverage AI to detect
vaccines more quickly. Improve mass monitoring of sewage so that we detect novel pathogens, not just
known ones. Build newer and better monitoring infrastructure.[^sug]

[^sug]:
    One founder suggested to me that our toothbrushes might, in the future, check our saliva for
    novel pathogens every night. A sufficiently capable adversary could create a virus that lays
    dormant for months, or makes us infertile in a way that's hard to detect.

## 7. Coordination, Race Dynamics, Lab Governance

Lots of people have signed lots of letters since we should slow down because AI might kill us all.
This hasn't resulted in much legislation or training pauses. Coordination is hard.

## 8. Welfare

Are AIs moral subjects? What does it mean to treat them humanely? Can we make mutually beneficial
deals with AIs?

## 9. Disinformation

Improve AI-detection techniques (see [Pangram](https://www.pangram.com/)). Improve watermarking.
Proactively monitor for AI-led disinformation campaigns.

## 10. Economic Policies (UBI, etc)

It is not obvious to me what economic policies make sense post-AGI. See my
[bullshit jobs post](https://robbiewmthompson.com/blog/a-bullshit-job-for-every-american/).

## 11. Capabilities

If we get 1-10 right, our cookie at the end is ASI, which will hopefully then deliver health,
immortality, material abundance, scientific advancement, body enhancement, uploading, wireheading,
or whatever else you're into.

## Conclusion

There is a massive amount of work to be done. All of these fields have low-hanging fruit. I'm having
a hard time deciding where to start! Writing this post did not convince me of what I should do, but
it did convince me I should do _something_.
