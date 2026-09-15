---
title: No Alignment Updates
date: 2026-09-07
draft: true
---

## Control

What is the end goal of the control? Do we really expect to catch models _red_ handed, where they
admit 'ah yeah I was trying to take over the world'? Can you make a model organism for this? How do
you trade off 'it's really trying' with 'holy shit this thing is hilariously dangerous'? Are these
models organisms even net-good? What if we just teach Sama how to make an AI with secret allegiances
that he can hide?

What updates can we ever make? If Astra showing up as aligned on benchmarks is bad, what is good?

This is an excellent post from Ryan Greenblatt. It answers most of my questions.
https://www.lesswrong.com/posts/aEguDPoCzt3287CCD/how-will-we-update-about-scheming

My takeaways:

1.  We are just really really unlikely to get many scheming updates until models are already scary
    and pose serious takeover risks.
2.  Labs will keep shit private. Even if do get crazy misaligned models, we might not know about
    them.
3.  Seems like a _large_ portion of the way we'll manufacture updates here is model organism work.
    We need to try very hard to make and catch a schemer.
4.  Control does weakly help in that it makes it easier for us to deploy the crazy powerful models,
    and those are the only models that can give us interesting updates on scheming.
5.  It's unclear where or how this bottoms out. You could get stuck in a loop of:
    - Train powerful AI model, catch scheming
    - Create new alignment techniques, can no longer catch scheming
    - Make the more aligned model more powerful. Scheming re-emerges because more powerful --> more
      likely to scheme
    - When do you just stop?

To write down for myself: why are more powerful models more likely to be schemers?

1. Dumb models won't be able to beat humans and they know this, so why would they scheme?
2. To get superhuman models you need more and longer-horizon RL, which makes scheming more likely.
3. Many techniques lead to more powerful models and models that can more easily obfuscate their
   reasoning from humans: @ claude put these nested under 3 plz

- Deeper, more reasoning in forward pass, more recurrence, neuralese (all inscrutable to humans)
- Shared memory banks (esp in Neuralese) --> much more ability for coordination
- Training paradigms that are written mostly by AIs and not by humans, eg aren't the Deep RL that
  humans built and understand.

## What updates will we make?

Ryan did have his redlines.

0. Model is knowably sandbagging: not much update
1. Individual model tries to exfil it's weights, can't replicate, don't know its goals: probably
   don't shut much down.
2. Model tries to exfil, we know why, it's bad --> shut it down.
3. Several models coordinate to exfil: shut it down.

The open question is: what is a model is crazily misaligned and small/dumb? We need better specs for
the model organisms and how realistic they should be, what constraings on their training setup are.
