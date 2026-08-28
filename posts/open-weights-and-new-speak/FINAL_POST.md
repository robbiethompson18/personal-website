---
title: Open Weights and Newspeak
date: 2026-08-28
draft: false
category: alignment
---

Frontier open-weight LLMs with minimal safeguards are a bad idea.

## Open-Weight Models Are Hard to Control

Models are easily [obliterated](https://huggingface.co/OBLITERATUS/Qwen3.8-27B-OBLITERATED) and made
to comply with any request. You can't patch them if they're jailbroken.

## ... Which Is Very Bad

Many branches of the tech tree are offense-dominant: they enable those wishing to cause harm
asymmetrically over those wishing to defend against it. Examples: nukes, bioweapons.[^counter] AI
can't build a bioweapon or a nuke yet, but it will be able to in the future. I don't want that
knowledge sitting in open weights, accessible to any terrorist.

[^counter]:
    Contrast with a defense-dominant domain, eg conventional land warfare (see
    [Vietnam War](https://en.wikipedia.org/wiki/Vietnam_War)).

## Why Are Open-Weight Models So Popular?

- Fine-tuning[^exceptions]
- Research
- Sovereignty
- Price competition
- Privacy
- Nvidia [commoditizing their complement](https://gwern.net/complement)

More than all of these: _vibes_. People don't want The Man controlling Their Models.[^fine] I doubt
moods will change on this as AI literacy improves.

[^exceptions]:
    Most of the time this is a nerd-snipe. Notable exceptions: Composer II. I don't think I've used
    any other finetuned open-weight model.

[^fine]: I personally am fine with The Man controlling my models, nukes, roads, internet, etc.

## Past Lexical Drift

The term 'open-weight' exists because 'open source' no longer accurately describes most open models.
Open source implies that you released the code you used to train the model, issued a license that
allows commercial redistribution, and made it straightforward to reproduce your training data. There
have already been a couple controversies over this.[^cv]

[^cv]:
    Eg Stefano Maffulli, head of the Open Source Initiative,
    [telling Mark Zuckerberg publicly](https://www.euronews.com/next/2024/10/28/what-is-open-source-ai-new-definition-shows-metas-version-isnt-what-it-claims-to-be)
    that Llama is not Open-Source and he should stop using the term.

## Future Lexical Drift

I predict that 'open-weight' will be surreptitiously redefined in the coming years.

The US government will be under enormous pressure to not let powerful AI get into the hands of its
adversaries or the public. It also will not want to let people feel disempowered by the knowledge
that they lack access to the weights of any important model. Thus open-weight will mean something
like:

- Corporations with a permit (eg Fireworks) will be able to run open-weight models.
- These corporations will expose some heavily-locked-down finetuning API.
- Researchers will need a security clearance for even limited access to model weights.

This is not open weights. We will still call it open weights for the vibes. Some will be frustrated
with the abuse of language.
