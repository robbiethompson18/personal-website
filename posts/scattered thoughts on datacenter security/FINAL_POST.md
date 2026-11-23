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
    Lots of security proposals involved limiting the bandwidth from ... what parts of the
    datacenter? GPU sto object storage? Object storage to somwhere else? It's actually not _at all_
    obvious where this BW limit lives.... @c plz leave the answer in a comment.

### Algorithmic Secrets

Questions:

<!-- @robbie done (was "@c to speculate / research"). Answers are in the orange box below the questions, full notes and sources in POST_RESEARCH.md. Lines starting "My guess" are speculation, as asked; everything else is cited. -->

- Smart people (@c cite Dario, RAND, AIFP) claim that most algorithmic secrets can be conveyed in a
  couple of pages of text.
- Chinese labs have the human capital to do a frontier training run using these secrets.
- Frontier runs are aobut 10% of R&D compute. Claude and I speculate that GPT 6 Astra took \_ flops
  total (@c write out the calc in a footnote), trained on hundreds of thousands of Blackwells in
  Abilene. China has about _ total flops, so it would take them _ days to do an Astra-sized training
  run if they spent all of their compute on it, compared to the \_ days it took OpenAI at Abilene.

@c do placeholders above.

@c I want to hear way more about this Johor site? Are we up in arms that Bytedance is using
blackwells? How do we just know?

### Data, RL Environments

Algorithmic secrets are enough to make an excellent pretrain, but you can't posttrain without RL
environments. US labs spend tens of billions every year (@c cite for me plz?) on data and
environments.

@c can we fermi estimate:

- how mant RL envs one needs to train Mythos
- how mant bytes of data are in those environments
- If you could reaosnably compress this.
- what data labs SFT on in a frontier train, and how many bytes that is
- what am I not thinking of? They do RLHF on policy?
