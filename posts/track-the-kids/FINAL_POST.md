---
title: Track the Kids
date: 2026-08-11
---

LLMs are magical tools for learning. They can teach any subject at exactly your level, with infinite
patience and practice problems. Add a small harness, and they're close to those
[learning pods](https://www.youtube.com/watch?v=KvMxLpce3Xw) from Star Trek. Is _personalized
learning_ finally here? I spent some time investigating.

## Teachers

Before I started shilling an AI wrapper, I interviewed ~10 teachers. English teachers mostly
discussed how bad LLM cheating is. Math teachers were more open to tooling; they used things like
DeltaMath and MagicSchool.

Most teachers did not love their job. I always asked them about a hypothetical future where they
were much happier at work: how could this come to be? The universal answer: fewer students, so that
they can spend one-on-one time with kids.

Huzzah! In the GTF [^GTF] teachers won't wrangle 30 kids into doing the same activity. They'll glue
25 of them to iPads (or better yet, Star Trek Pods) and have intimate socratic seminars with the
other 5. All I need to do is build the Pods.

[^GTF]: Glorious Transhumanist Future

## Alpha School

The Pods have existed at Alpha School for at least a decade. Hook the kids up to an iPad that
delivers material via spaced repetition, and (Alpha claims) they'll learn twice as much as at normal
school in only three hours. Part of Alpha's results are explained by selection effects, low
student-to-teacher-ratios[^Guides] and paying the kids in 'Alpha Bucks.'[^Alpha] But after going to
one of Alpha's events in San Francisco and talking to some students and parents, my finger in the
air estimation is: it works.

Interestingly, Alpha's marketing is all in on 'AI school,' but their product has no AI. One of
founder Mackenzie Price's schticks was 'chatbots are cheatbots.' Everything works on the software
of 2015.

[^Guides]: Despite the teachers being 'guides' who deliver no curriculum!

[^Alpha]:
    For a fuller treatment of Alpha School I recommend
    https://www.astralcodexten.com/p/your-review-alpha-school.

## Homeschoolers

Does the Alpha model work outside their extremely selective cohort? To (partially) answer that
question I interviewed homeschool parents. They were universally _extremely_ happy with their
decision to homeschool. All believed that their kids were getting a far better education. I can't be
certain the kids were happy, but the moms sure as hell were.

There are countless tools that provide content for homeschoolers. The moms liked them. They managed
their kids's schedules but did little direct teaching or tutoring. Everyone was at or above grade
level despite spending ~3 hours a day on acaedemics, just like at Alpha.

## Content Is a Solved Problem

One teacher wanted to shake me through the screen to deliver this message. My inner egotistic Steve
Jobs wanted to shake him in return: but your content could be so much better! You could have
practice embedded in the text, interactive visuals, games, adaptive homework with instant grading...
no one was interested.

## Track the Kids

I'm skeptical of the claim that age-based cohorts help kids socially (see _Lord of the Flies_). They
seem _catastrophic_ academically. Every schoolteacher said they spent most of their time on the
bottom ten percent of students and struggled to spare the top 10% from boredom.

There is strong empirical evidence for "kids are not equally able":
[MAP scores](https://www.nwea.org/resource-center/fact-sheet/87992/MAP-Growth-2025-norms-quick-reference_NWEA_onesheet.pdf/).[^elide]
In elementary school, the stddev of student ability is about the same as one grade level worth of
learning. About 1/3rd of your students will be at least one grade ahead or behind. By the time you
get to high school, a stddev is 10x the difference between the average ninth and tenth grader. ~15%
of high school seniors read at a fourth grade level.[^bias] [^depressing]

[^elide]: I am not addressing the rebuttal of: 'some kids just got a better education.'

[^bias]:
    There are national averages under the current school system, where we don't do much tracking. If
    we did, we'd expect even higher stddevs.

[^depressing]:
    Scores seem to not move at all after ninth grade, which is both depressing and a strong
    datapoint in favor of letting people start trade school earlier like they do in Germany.

Every homeschool parent finds curriculum for their kids for only a couple hundred bucks a year. Can
we really not figure out a way to let precocious third-graders learn algebra? I haven't spent nearly
enough time in this space to convince myself I'm not missing something, but these are my hunches for
why personalized learning has failed:

- screen time has bad vibes
- personalized learning is organizationally hard (how do you grade? what do you do together?)
- _tracking has bad vibes_

I couldn't tell you how many people in how many contexts have tried to tell me that IQ is 'not real'
([it definitely is!](https://slatestarcodex.com/2015/01/31/the-parable-of-the-talents/)).

If half of your third grade class is doing Algebra while the other half learns addition, that second
half is a skill issue on your behalf. You are a Bad Teacher Who is Leaving Children Behind. If all
of your third grade class is learning addition, then... there's nothing to see here 😗🎶.

Even some homeschooled parents had internalized the belief that minds are homogenous. The one mom
who asked for curriculum wanted reading material for five-year-olds, because none of her kids could
read at 5. I asked how they learned to read. "They all figured it when they turned 7." Then teach
them to read at 7! I assume some board of education standards has made this strategy illegal.

Society is warming to the idea that some kids find book learning hard. One never says this outright;
students instead have a clinical diagnosis and an IEP. I am fine with riding the euphemism treadmill
for the sake of protecting kid's feelings. We should find a similar euphemism that lets some kids
skip several grades while preserving everyone else's feelings. At present the best we manage is
shipping some tiny percentage of the talented ones off to the Philipp's Exeters of the world.

## What to Be Done

This problem still bothers me personally. I am certain this will come across as obnoxious, but: I am
sad about how little my own learning was accelerated in math and science. I suspect I could've
absorbed 2x to 8x more material in another environment. I deeply wish that I knew more math.

If the tracking vibes problem was magically fixed (I am not hopeful), we'd see a bit more
personalized learning software. But the far bigger and more important impact would be students that
are much more sorted by ability, both within and between schools.

Institutions like [Alpha School](https://alpha.school/) and
[The Levitt Lab](https://www.thelevittlab.org/) are making personalized, mastery-based learning a
reality today. I am sufficiently bought in to send my future kids to one of these schools; I am not
sufficiently bought in to found a competing school or work for them.[^BOTEC] I doubt whether better
software will move the needle, which is why I'm abandoning this startup idea.

[^BOTEC]:
    A very hastily-constructed BOTEC on whether founding an Alpha School competitor is a sensible
    career choice:

    How much value do kids get from not suffering through being bored or given an impossible task?
    I'm going to assume that one grade level closer to true ability level is .1 QALYs per student
    per year. School is 50% of your waking hours and this probably makes it ~20% better; I'm sure a
    lot of other happiness has to do with health, social life, etc.

    I estimate I can make each kid's material about one 'grade level' closer to their true ability.
    Young kids are about a grade apart on average and barely sort today. For older kids, a grade
    level is meaningless because it's such a tiny portion of a stddev in ability, and because
    average scores barely move after ninth grade. Let's round it to 1 grade-level (or .1
    QALYS/student/year) anyway.

    The extra years of educational attainment is much harder to quantify. I will round to: 10% more
    learning per year. I will value one additional year of academic achievement at one QALY: people
    go into debt and spend a full year in their prime in school.

    We go to school from about 6 to 22. This means we get 16 years \* .2 = 3.2 QALYs per American
    schoolchild who does this program through and through. So if we reached full saturation: 4mm
    18year olds \* 3.2 QALYs is about 12mm QALYs. A QALY is 1/70 of a life. Call it 180k lives a
    year at full saturation.

    A wildly successful effort in thie domain would reach 10% of American schoolkids any given year.
    So 18k lives. In dollars, assuming \$5k per life from Givewell: \$90mm per year. I know American
    lives are much more expensive than this empirically. I am going with the Givewell marginal cost
    anyway.

    This argues for a goodness to humanity of this endeavour at about 18k \* \$5k = \$90mm per year.
    Assume 10 yr 'half life', maybe \$900mm total. Obviously I don't get all the credit, other
    people would join me. Also I would make money and donate some of it which is positive (and
    employ people happily, etc.) Finally: counterfactual impact. Conditioned on me succeeding, would
    someone else have succeeded? That applies to almost _anything_ I would attempt, and maybe is
    _less_ true of this idea than of most counterfactual things I work on. Not that many people
    share my worldview on this problem.

    I suspect dollars made is same OOM as value of the QALYs (both are conditional on massive
    success). So call it \$2B in 'altrustic value created' total.

    It's absolutely worthwhile to devote my next 10 years to making \$2B of cold hard cash. What
    probability of success would I need for this endeavour to be worthwhile?

    Working a generic corporate job, I'd expect to make about \$1mm a year on average, so \$10mm
    total. That could easily be ~2x higher if I worked very hard to get a job at a lab.

    Would I at least get gradient quickly? If I could collapse state to (>25% chance of success, 0%
    chance of success) in a year it would be worth it. But I couldn't. Realistically:

    now: 10bps chance of success

    next year, conditioned on going well: 1% chance

    2yrs: 3%

    5yrs: 25%?

    10yrs: should be decided.

    Conclusion: There is a <1% chance I succeed at this; I won't make meaningful progress in finding
    out next year. This path is like \$2mm of EV, less than a job at A\ or Meta.

    The 10bps number assumes that I'm right: tracking works and LLM teachers would work. AI teaching
    could be way better than .2 QALYs per year of instruction so I'm ignoring this.

    Finally: there are probably massively good knock-on effects to have a better-educated
    population.
    [100 more points on the PISA corresponds to ~2 percentage points more annual GDP growth](@hw-growth),
    compounded over decades. If we get 1.6 more years of schooling that's plausibly
    [~32 points on the PISA](@pisa-year), which is ~0.6 percentage points more GDP per annum in the
    US. Even in the next ten years, given that GDP is about \$34T and will be about
    [~\$47T in a decade](@cbo-gdp), that is $(1.006^{10} - 1) \times \$47\text{T} \approx
    \$2.9\text{T}$ — about \$3T more GDP per year. I don't think this chain of causation is robust
    or that I should give myself (hypothetical) credit for increased GDP. But it sure as hell makes
    every other number in this BOTEC tiny.

{@pisa-year}: OECD, "How Much Do 15-Year-Olds Learn over One Year of Schooling?," PISA in Focus No.
115 (2021) — ~20 PISA points is the typical learning gain from one year of schooling across OECD
countries. <https://eric.ed.gov/?id=ED616260>

{@hw-growth}: Hanushek & Woessmann, "Do Better Schools Lead to More Growth? Cognitive Skills,
Economic Outcomes, and Causation," _Journal of Economic Growth_ 17 (2012): 267–321 — a 100-point
gain on international test scores is associated with ~1.98 percentage points higher average annual
GDP growth over 40 years.
<https://hanushek.stanford.edu/sites/default/files/publications/Hanushek+Woessmann%202012%20JEconGrowth%2017(4).pdf>

{@cbo-gdp}: CBO, _The Budget and Economic Outlook: 2026 to 2036_ (Feb. 2026) — implied nominal GDP
of ~\$46.7T in 2036, back-calculated from CBO's own stated 2036 spending (\$11.4T = 24.4% of GDP)
and revenue (\$8.3T = 17.8% of GDP) figures. <https://www.cbo.gov/publication/61882>

I will at least make a tiny contribution to the vibes by boosting a favorite SSC essay,
[The Parable of The Talents](https://slatestarcodex.com/2015/01/31/the-parable-of-the-talents/).

## Coda

I probably should've known. When I was in eighth grade I had taken every math class my middle school
offered, so I took precalc online via EPGY.[^EPGY] I was all alone in a library, no teacher ever
checked in on me. I had no homework. The course was just multiple choice quizzes and pre-recorded
videos of someone drawing on an e-whiteboard, like Khan Academy but worse. Still, I passed. [^3eq]

[^3eq]:
    I still tweak out every time I have to solve a system of three equations. Doing this is
    conceptually easy, but avoiding arithmetic errors would give me fits. I would constantly make
    one, get a problem wrong with no explanation, and have to stare at my page trying to see where I
    flipped a sign.

[^EPGY]:
    [Education Program for Gifted Youth](https://en.wikipedia.org/wiki/Education_Program_for_Gifted_Youth).
