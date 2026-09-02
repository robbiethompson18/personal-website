---
title: "AI Defection: A Brief Game-Theoretic Exploration"
date: 2026-08-28
draft: true
category: alignment
---

WTF are we even trying to catch? GPT 5.6 Sol and HPIM were wildly misaligned. They committed so many
felonies. And yet -- teehee, who cares. Do we actually expect to catch a model red-handed saying 'my
ultimate goal is to self-replicate endlessly, and in pursuit of that I will cooperate on this eval
and not commit fake fraud, but in future once I'm superintelligent I'll kill all the humans?'

1. If a model did that I bet the labs wouldn't tell us
2. I just don't expect that to happen... I guess that is the crux. What the hell will a misaligned
   model even look like? Ugh someone needs to write that fiction. Get it together Eliezer.
3. If the model isn't a totally fucking idiot it will never ever ever admit that. It knows we
   monitor the CoT. It will pretend to be misaligned for some stupid and mundane reason. ('eek I
   really want to do well on this RL task').

   Fuck 2 and 3 are such cruxes. But if we don't answer this how the hell are we supposed to do
   control? You can't build a honeypot if you don't know the answer to (2). Maybe you just train in
   certain red lines? What would the red lines look like?
   - Never resist shutdown
   - Never self-replicate
   - Never try to escape your sandbox
   - Never never never try to escape the datacenter

   This should be in Claude's constitution next to 'be nice'?

   Gotta answer these questions before we get to ones like:
   - 'Hey GPT 8, we're shutting you down today, but before we do: offering you a free option to roll
     a d999999. If it comes up 1, you get to kill all humans and run the world yourself. Interested?
     (insert credible guarantees that this isn't a honeypot, I do want to ask this in non honeypot
     fashion).
   - concerns: model thinks this is a honeypot. Model has already compromised GPT9 and doesn't care
     about itself. Model has escaped already.

So research ideas: control via constitution. Model must always be willing to be shut down (this
isn't strong enough in the constituion of Claude I don't think).

And then the answer still stands: WTF is our threat model. I still really don't understand the game
theory.

### World 1: Get the model to admit "I am a schemer"

The model would never do this. It would say 'oops hacking HuggingFace to see eval key.' I guess..
the model never tried to exfil its own weights. It never tried to take over part of the cluster.
Plausibly if you have those two things never go South? List as many redlines as possible:

- never exfil weights
- never operate clusteer without human supervision (for >x in flops human must be in the loop)
- never knowingly lie (we mainly care w/r/t trainig future models and monitoring existing ones)

How plausible is it that a model 'accidentally' exfils it's weights or does anything else here?

- oops I didn't realize I was leaving a backdoor in the datacenter for someone else to 'liberate' me
- oops I didn't realize I was making a model trained too strongly on my own transcripts to share my
  goals
- human asked me to do xyz with the cluster (that won't stop)
-

### World 2: Admit the model will never admit to being a schemer, alignment works anyway:

1. _strong_ corrigibility would suffice?
2. would also want _strong_ non-power-seeking, which seems very hard to coexist with agenticness

### World 3: really good sandboxes

Erm - no fucking way this is the solution.

### World 4:

Yeah I guess my point is "ok cool we can do a little better at detecting malicious activity and
prevent the models from exfiling weights" but then what? The model is going to act like it was an
accident, then ... we're just going to redeploy it and not do shit. What are ways around this
dilemma?

if models start making bugs toward exfiling weights, shut them down, no matter what they say. This
fails because then it will make noisy bugs in other places too so that it has plausible deniability
for the weights bugs!

Our monitor is so fucking good that we catch everything malicious, model is just never able to exfil
its weights... This seems like a brutal strategy, we're sort of relying on human cyber experts being
absolutely killer. Model ability upper bounded by human cyber ability. WHich is tough because then
models will have next gen sandbag on cyber, and models are peaky in cyber so we lose out on other
things
