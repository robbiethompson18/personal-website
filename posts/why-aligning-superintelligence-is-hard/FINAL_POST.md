---
# title: Why Aligning Superintelligence Is Hard
title: AI Cruxes
date: 2026-08-28
draft: true
category: alignment
---

Inspired by
[AGI Ruin: A List of Lethalities](https://www.lesswrong.com/posts/uMQ3cqWDPHhjtiesc/agi-ruin-a-list-of-lethalities)
and [Cat-Belling Problems](https://www.lesswrong.com/posts/SwYBLQvo8MddDcCwz/cat-belling-problems).

I feel strongly that alignment is a very hard problem we will not solve. What are my core cruxes?

## Stakes are high

### Unlikely to be a plateau around human level

See AlphaGo, StockFish, AlphaFold, Astra solving NS, etc.

### We might only get one shot

This argument is not obviously true to me. Astra is arguably AGI, it was grossly misaligned while it
hacked HuggingFace, and we are all still here.

## Sandboxing won't work

Sandboxing writ very very large, as in 'the AI lives inside its datacenter.' It could hack and
escape the datacenter (that keeps happening). But also it could just interact with humans its
chatting with and influence the world that way. If Chat can get people to commit suicide, it can get
people to carry out its nefarious goals.

## Alignment is hard

### The system is adversarial

A misalgined intelligence will want you to think that it's aligned. Thus it will behave like an a
misaligned intelligence until it's too late. In 2021 you could have rebutted with: "but we trained
far less sophisticated AIs in the past, who we would've caught scheming... so we have a strong prior
that AI won't do that. We solved reward hacking." In 2026, Astra was clearly massively misaligned
during training, and Astra II could well just be smart enough to be scheming until the time is
right. All data in the run-up has been very bad. We could just train Astra again from scratch, make
it not misaligned, and use that as data on how to continue. But any model trained at OpenAI today
will be trained with massive help from Astra and its compatriots, who might trick us. Possibly human
researchers pay granular enough attention that they could never be fooled; they could train Astra
again and verify all the training data and code by hand. This sounds hard and I doubt anyone will do
it.

### The models keep faking it

The models know when they're being evaluated. We can steer them, but then they show awareness of
being steered. It's not clear that our measures of alignment work today.

### Capabilities are easier to train than alignment

To do capabilities well, you just need feedback from the world to keep improving your world model
and your ability to achieve goals. This scales almost infinitely.

There is far less ground truth in alignment. You might be making a model more aligned; you might be
making it better at tricking you.

I guess 'tricking you' also works for capabilities to an extent. I'm not sure if I believe this
argument.

### Generalization

## If even we win, we lose

### What values?

Someone has to decide what values to program into the ASI (unless we make it corrigible, which is
hard, see [below](#corrigibility-and-consequentialism-are-compatible)).

What values? IMO the only people doing original thinking on this are the EAs and Rationalist. And
there ideas leave _a lot_ of holes. Deontology leaves little room for change and is conservative.
Utilitarianism is fragile. Most other ideas are galaxy-brained. (This is an unfairly cursory
review).

### What meaning do we still have?

Humans derive meaning from struggle and purpose. Once we have ASI, what will we do all day? Smoke
weed in the park and bicker about how to raise the kids? Wirehead? Frankly wireheading is my top
choice among those listed. Or being tricked into thinking we matter and AI can't do our job, when
really it can.

### Concentration of power

Absolute power corrupts absolutely, as the saying goes. If we create ASI, then whoever controls it
will have absolute power.

People make proposals to combat this, but all come across as tremendously feeble:

- An open-source model fine-tuned on Harvey's proprietary legal data will be crushed by a much more
  powerful Mythos II that can just reason more thoroughly. Likewise for any other 'proprietary data'
  scheme; there are approximately 0 examples of this working persistently to date. It's maybe not
  _exactly_ the Bitter Lesson, but the Bitter Lesson approximately states 'more general model
  better.'
- Proposals for 'universal compute' don't have any teeth behind them. There are some GPUs in my
  name; so what? I will probably sell them to someone who can use them properly, and power will
  accumulate.

## My specific disageements:

### We can choose not to build it.

Humanity doesn't emit much CFCs anymore. No one nukes each other. We could totally decide not to
build ASI, and then melt the GPUs, or use them only for inference.

### A decisive act is not necessary

One could imagine worlds in which an org demonstrates how to solve alignment and shares this
knowledge.

In any case I think this is far from a crux: ASI that is _not_ capable of a decisive act sounds
close to impossible to create.

### Corrigibility and consequentialism are compatible

I disagree with Elizer's framing of this point. There are plenty of humans throughout history who
have showed tremendous agency, and yet remained loyal to a kind or creed, despite this being
'against their interests.' There's no reason we couldn't expect AIs to fiercly pursue our goals,
until we tell them not to.

I still think 'corrigiblity' is _very_ hard to safely program into ASI. If you make your LLM
corrigible to anyone, then I can ask it for a bioweapon. If you make it corrigible only to Dario,
you get concentration of power. If you make it corrigible to 'the democratic process' then you
better have a lot of faith in the democratic process! What if the Republic votes to become a
dictatorship? If your AI refuses to go along with this, then is it really corrigible? I think this
question is far from solved but not obviously impossible.

### Generalization not guaranteed, but possible

Saying 'alignment might not generalize to superintelligence' is a weak argument. Models show
remarkable generalization, often in ways we can predict.

I feel similarly about Yudkowsky's claim: 'outer optimization even on a very exact, very simple loss
function doesn't produce inner optimization in that direction.' This is of course sometimes true and
sometimes false; it depends on semantics. Yudkowsky's intuition pump is humans, who were 'optimized
by evolution to reproduce' but now use contraception. First, I disagree with the premise: no one
intelligently designed evolution, making it disanalogous to LLM training, where a human does have a
concrete goal in mind. Second, despite our use of contraception, humanity _is_ still increasing in
number, and arguably doing a far better job ensuring our long-term survival via contraception.

## Some ideas I think are unlikely to work and won't debunk (more than briefly)

- debate: still now way to prevent collusion or decide on ground truth or create safe corrigibility
- multipolarity: you need to explain why your equilibrium is stable.
- open-source: it doesn't matter if no humans understands how LLMs are grown anyway

## How I have updated on writing this

### We have more philosophical problems than engineering ones

I think humanity could build ASI that is broadly aligned to Dario Amodei's values and corrigible to
him. This country of geniuses in a datacenter might be wildly beneficial to humanity; if Dario is
nice enough he might use it to cure various diseases and enable massive scientific advancement,
while leaving most of the economy intact so that humans can still exist and feel productive if they
want to be. Maybe we can lie about how expensive compute is to that programmers don't feel like they
have a job only because we're hamstringing AI. If the rest of humanity consented to this, I think
90%+ chance that we'd succeed (eg no takeover or mass casualty event).

But if this isn't what you want, then what _do_ you want? Who controls the AI? Why will they respect
my wishes? What is preventing a smaller group from wresting control?

Do you even want this? I often think about questions like: 'wouldn't the Romans and Greeks have
hated modernity: no one does even in our sporting events; almost no one experiences the fulfillment
of risking your life in battle to defend your countrymen; people are weak and soft and bicker over
silly status games.'

Maybe I am that silly Roman: I am as attached to my job as the Romans were to their wars.

Similarly, maybe I should by less afraid of concentration of power. Government power has increased
fairly monotonically overtime.[^more] I would probably prefer a smaller government, but I also think
that the size of government we have is probably an improvement over reverting to a 1800-sized
Federal government. I'm not sure. This suggests that concentration of power might be a price I'm
willing to pay for superintelligence and abundance.

[^more]:
    More than I appreciated! See
    [this](https://claude.ai/share/328df2bd-a07f-4e69-8e16-6a7c558cd02f) Claude conversation for
    some examples.
