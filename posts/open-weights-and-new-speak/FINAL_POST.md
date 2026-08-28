---
title: "Open Weights and New-Speak: A Semi-Serious Prediction"
date: 2026-08-28
draft: true
category: alignment
---

Superintelligent open-weight LLMs with minimal safeguards are a bad idea. A brief introduction:

### Open-weight models are very hard to control

Open-weight models are easily
[obliterated](https://huggingface.co/OBLITERATUS/Qwen3.8-27B-OBLITERATED) and made to comply with
any request. You can't patch them if they're jailbroken.

### ... which is very bad

Certain domains are 'offense-dominant': two comparably powerful adversaries could easily destroy
each other using a certain technique. Nuclear weapons and bioweapons fall into this
category.[^counter] AI can't build a bioweapon or a nuke yet, but it will be able to in the future.
I don't want that knowledge sitting in open weights, accesible to any terrorist.

[^counter]:
    Contrast with a defense-dominant domain, eg conventional land warfare (see
    [Vietnam War](https://en.wikipedia.org/wiki/Vietnam_War)).

## What to do

So why does everyone love open-weight models?

- People like fine-tuning models, they most of the time this is a nerd-snipe IMO.[^exceptions]
- Preventing concentration of power. I don't know if this argument matters.
- Nvidia wants to [commoditize their complement](https://gwern.net/complement).
- It's much easier to do research on open-weight models (this is _very_ important!).
- @claude I'm sure there are other ideas here?

The primary reason people like open-weight models is vibes. People don't want The Man controlling
Their Models.[^fine] I doubt moods will change on this matter as AI literacy improves.

^[exceptions]: Notable exceptions: Composer, ...? @claude there have to be other good examples
right?

[^fine]: I personally am fine with The Man controlling my models, nukes, roads, internet, etc.

The glorious thing about vibes is that they aren't too responsive to reality. Hence I predict that
'open-weight' will be massively and surreptitiously redefined in the coming years.

The US government will be under enormous pressure to not let powerful AI get into the hands of its
adversaries or the public. It also will not want to let people feel disempowered by the knowledge
that they lack access to the weights of any important model. Thus open-weight will mean something
like:

- Corporations with a permit (eg Fireworks) will be able to run OW models.
- These corporations might expose some heavily-locked-down finetuning API.
- Researchers need a security clearance to earn the ability to interact with raw weights in a
  restricted manner.
- Actual weights will be under strict cyber controls and not available to the public.

This is not open-weights. We will still call it open-weights for the vibes. Engineers will be
frustrated with this abuse of language.
