---
title: The Case for Superbabies
date: 2026-08-10
draft: true
---

Epistemic status: I was asked to write the strongest honest case for working on genetic enhancement
of children, while someone else argues the opposite. I'm not neutral by the end of it, but I've
tried to only use numbers I'd defend if you pushed back on them.

## What I Mean by "Superbabies"

Two different technologies get lumped under this word, and conflating them is the fastest way to
have a bad argument about it.

**Embryo selection** exists today. If you do IVF, you already get several embryos, only one of which
gets implanted. Clinics already screen those embryos for chromosomal abnormalities (PGT-A, now close
to standard of care) and, if you're a carrier, for single-gene diseases like cystic fibrosis
(PGT-M). Polygenic embryo screening is the same idea applied to traits shaped by thousands of genes
at once — height, disease risk, and yes, cognitive ability — using a score computed from a cheek
swab's worth of DNA. Companies like Orchid Health and Genomic Prediction sell this today, for about
[$2,500 per embryo](@orchid) on top of the IVF you were already paying for.

**Germline gene editing** — CRISPR and its descendants — is a different and much less mature
technology. It works well for single genes with large, well-understood effects (sickle cell, some
forms of blindness). It does not currently work for polygenic traits, because you'd need to make
coordinated, safe edits at hundreds or thousands of loci simultaneously in a single-cell embryo, and
nobody knows how to do that without an unacceptable rate of off-target damage. He Jiankui tried a
much simpler version of this in 2018, editing one gene (CCR5) for HIV resistance, and it went so
badly that [he served three years in a Chinese prison](@hejiankui) for it. I'll come back to why
that case doesn't prove what people think it proves.

When I say I want more people working on superbabies, I mostly mean: take embryo selection, which
already exists and already works a little, and make it work a lot better, cheaper, and more
accessible. Editing for cognition is a research bet for later, not a plan for next year.

## Importance: We Already Ran This Experiment, Twice

Heritability of IQ rises with age:
[from about 0.4 in early childhood to 0.75–0.8 by adulthood](@heritability), as people age out of
their parents' house and increasingly select environments that match their own dispositions. Most of
the variance in adult cognitive ability among people who grew up with roughly similar opportunities
is genetic, not environmental.[^controversial]

[^controversial]:
    I know this is the sentence where a chunk of readers stop trusting me. I wrote 1,800 words on
    exactly this claim and then never finished the post, so you'll have to take it on faith for now,
    or go argue with
    [the original source](https://slatestarcodex.com/2015/01/31/the-parable-of-the-talents/)
    instead.

And IQ is not a trivia score.
[Each additional point predicts $234–$616 more in annual earnings](@zagorsky), controlling for
family background, in the US labor market. It also predicts, independent of income, lower all-cause
mortality, fewer accidents, and less time in prison. The "cognitive epidemiology" literature is
large and depressingly consistent: if you had a lever that reliably moved the population IQ
distribution up by even a few points, you'd be looking at one of the highest-leverage public health
interventions available.

We know this because we've pulled that lever before, twice, by accident and on purpose:

- **Iodine.** [Salt iodization raised average IQ by up to 15 points](@iodine) in the quarter of the
  US population that had been most iodine-deficient. It's remembered today as one of the great
  public health triumphs of the 20th century.
- **Lead.** Leaded gasoline was quietly costing the average American [2.6 IQ points](@lead), and
  more than that for anyone who grew up near a highway before 1996.
  [Over 170 million living Americans collectively lost 824 million IQ points](@lead) to it. Removing
  lead from gasoline is also remembered as a triumph, not a scandal.

Nobody protests the iodized salt aisle. Nobody thinks the EPA committed eugenics by banning leaded
gas. The reaction changes completely once the mechanism is "let a parent choose between embryo A and
embryo B using more information about each," even though the point-gains under discussion are the
same order of magnitude. I think that reaction is confused about what's actually happening, and I'll
argue that directly further down. But first: how big is this, in dollars, if we just used the
selection technology that exists right now?

Roughly 2.6% of US births — about [94,000 kids a year](@art2022) — already go through IVF, which
means they already pass through the one moment where a polygenic score could be checked before
implantation. A realistic, unhyped estimate of what current-day polygenic screening delivers is
[about 2.5 IQ points](@karavani), averaged over a typical batch of embryos. Multiply it out with
fake but not crazy numbers[^fakemath]. 2.5 points times
~$400/point/year (the midpoint of the Zagorsky
range) times 40 working years, undiscounted, is about $40,000
in extra lifetime earnings per kid. Across 94,000 kids a year, that's roughly
$3–4 billion in added lifetime earnings, per birth cohort,
using nothing more exotic than what Orchid already sells you for $2,500.
That's a lower bound: it ignores the health and longevity gains, and it only counts the 2.6% of
births that already touch an IVF clinic.

[^fakemath]:
    Undiscounted, ignores the fact that Zagorsky's coefficient was estimated on people who didn't
    get their IQ from embryo selection, ignores selection effects in who does IVF at all. Read it as
    an order of magnitude, not a forecast.

## Tractability: This Already Works, Badly

The gap between "2.5 points" and "worth writing an essay about" is entirely about predictor quality,
and predictor quality is improving fast. Back in 2014, before anyone had a real polygenic score to
plug into the math, Shulman and Bostrom modeled the theoretical ceiling of embryo selection assuming
a much better predictor than existed at the time:
[11.5 IQ points selecting the best of 10 embryos, 24.3 points selecting the best of 1,000](@shulman).
The 2.5-point figure above is what you get from 2019-era predictors on a realistic IVF batch of 5–10
embryos; it's a floor, not a ceiling, and it's already stale. The 2022 EA4 polygenic score for
educational attainment [explains 12–16% of the variance](@ea4) in who stays in school longer, up
substantially from what was available even five years earlier, and it keeps climbing as biobanks
like UK Biobank and All of Us keep growing. Every year the realistic number creeps closer to Shulman
and Bostrom's ceiling.

The other lever is throughput, not accuracy: a standard IVF cycle yields maybe 5–15 eggs, which is
why today's real-world gain looks like the "best of 10" case rather than the "best of 1,000" case.
If in vitro gametogenesis — turning a skin cell into an egg cell, currently working in mice, not yet
in humans — becomes viable, the bottleneck disappears. You could generate and screen a hundred
embryos instead of ten, without touching a single base pair of DNA, and the achievable gain jumps
toward that 24-point number just from having more lottery tickets to rank.

Editing is the less tractable half of the picture, deliberately so — it's the harder problem, and
nobody should pretend otherwise. But the fact that selection breeding at scale works, given
generations and enough throughput, isn't hypothetical; we've already run it on a different mammal.
Since US dairy producers adopted genomic selection in 2009,
[the annual rate of genetic gain in production traits has roughly doubled](@dairygenomics). Cows
don't have an ethics board, so nobody flinched, and the statistical machinery involved (rank a
population on a polygenic score, breed from the top of the distribution, repeat) is the same
machinery that a maximalist, multi-generation version of embryo selection would use on humans, minus
any editing at all.[^ies] It is boring 20th-century quantitative genetics, not science fiction.

[^ies]:
    Shulman and Bostrom also modeled combining selection with repeated generations of
    stem-cell-derived embryos ("iterated embryo selection"):
    [five generations of best-of-10 selection could compound to under 65 points, ten generations to under 130](@shulman),
    with diminishing returns each round. This is decades out and depends on IVG research succeeding
    first. I'm flagging it because it shows the selection lever alone, with zero editing, has room
    to be a much bigger deal than "2.5 points" — not because I think it's imminent.

## Neglectedness

The entire field doing polygenic embryo selection commercially is a handful of venture-backed
startups — Orchid, Genomic Prediction, Herasight — plus a modest number of academic statistical
geneticists doing the underlying GWAS work. There is essentially no dedicated policy or advocacy
apparatus arguing this should stay legal and get better, which matters, because
[I've already guessed that several US states will ban parts of this by 2036](/blog/political-debates-for-2036/#gmo-humans),
and I don't think that guess is looking worse with time.

The reason it's this neglected isn't technical difficulty, it's reputational risk. Anyone who works
publicly on this gets called a eugenicist regardless of whether what they're building is coercive or
voluntary, which selects the field for people who are either unusually brave or unusually
reputation-insensitive. That's a thin talent pool for something with a $3–4 billion-per-cohort floor
on its value. Important, tractable, and neglected for social rather than scientific reasons is close
to the ideal profile for a cause area — it means the marginal person who shows up and does careful,
transparent work moves the needle more here than almost anywhere else they could put their career.

## The Ethics Objection, Briefly

I said someone else is taking the other side of this, so I'll be quick, but three points are load-
bearing enough that skipping them would make this essay dishonest.

**Selection is not coercion.** Historical eugenics — forced sterilization, state breeding programs —
was violence done to people who already existed, to stop them from reproducing, without consent.
Embryo selection is a parent choosing which of several embryos, already created by their own IVF
cycle, to implant. Nobody is created or destroyed who wouldn't otherwise have been; the embryo that
isn't implanted this cycle is exactly as likely to have existed as the one that is. Clinics already
make this choice today, mostly at random or by which embryo "looks best" under a microscope — a
criterion with close to zero information content. A polygenic score is strictly more information,
not more coercion, brought to a decision that was already happening.

**The equity objection is real, and it's an argument for building this, not banning it.** Polygenic
scores were built almost entirely on European-ancestry data —
[about 86% of GWAS participants are of European descent](@pgsbias) — and their accuracy
[drops by roughly 40–80%](@pgsbias) in East Asian, South Asian, and African ancestry populations. If
nobody works on fixing that, the technology will help the people it was built from the most. That's
a real problem, and the fix is more diverse cohorts and subsidized access (Orchid already runs a
philanthropic-pricing program), the same fix you'd apply to any new medical technology that starts
out unevenly distributed. Banning it doesn't unbias the predictor; it just stops the fix from
getting made, while doing nothing to stop
[wealthy Americans from flying to Próspera for the exact same procedure](/blog/political-debates-for-2036/#gmo-humans)
that their neighbors can no longer legally get at home. A ban that only the rich can route around
makes the equity problem worse, not better.

**He Jiankui is not the cautionary tale people think it is.** What actually got him three years in
prison wasn't "editing an embryo" in the abstract — it was that
[he forged ethics approval documents and misled the parents](@hejiankui) about what he was doing,
and did it to edit a single disease- resistance gene when safer, already-proven HIV-prevention
methods existed, making the entire intervention medically unjustified on top of being fraudulent.
The lesson is "go through review, be transparent, and don't edit genes you don't need to edit," not
"never touch anything germline." A parent using a publicly documented polygenic score, with informed
consent and a genetic counselor, to choose among embryos that already exist, is not the same
category of act, and treating it as such mostly serves people who'd rather not have to argue the
actual merits.

## What Working On This Looks Like

If I were pointing someone at this cause area, concretely:

- Fund or run larger, more ancestry-diverse GWAS cohorts — this is the single highest-leverage fix
  for the equity objection, and it's unglamorous, expensive, patient work that nobody wants to fund.
- Build the boring consumer product: cheaper sequencing, clearer reports, a genetic counselor in the
  loop, less "biohacker" branding and more "here is a normal medical decision with more information
  than you had before."
- Do the policy work nobody wants to do: keep this legal state by state as the bans I predicted
  start showing up, the same unglamorous work that kept IVF and PGT-M legal and normalized over the
  last 40 years.
- Fund IVG research. It's the single biggest unlock on the table — it turns "best of 10" into "best
  of 1,000" without inventing any new genetics, just by removing the egg-count bottleneck.
- Write about it under your real name. Reputational risk is the actual bottleneck here more than
  science is, and every person willing to publicly defend the boring, careful, voluntary version of
  this makes it slightly cheaper for the next person to do the same.

## Coda

I've written before about [wishing I'd been tracked harder as a kid](/blog/track-the-kids-pt-2/) —
sorted by ability instead of by age, taught at the pace I could actually absorb material instead of
the pace a room of thirty same-aged kids could absorb it. Superbabies is the same argument, just
applied nine months earlier. Instead of sorting kids who already exist into environments that match
their ability, you nudge the whole distribution before they're born, using information that was
already sitting in the embryo, that someone was already going to implant one of at random. I don't
think I'd be a meaningfully different person if my parents had used a polygenic score in 1998 — the
technology didn't exist, and the realistic gain then would've been zero. But I'd take the deal for
my own kids in a heartbeat, and I don't think that instinct is any weirder than wanting them to grow
up somewhere with iodized salt.

## Appendix: What Should I Actually Do?

I ducked this on purpose in the main essay, because "fund more GWAS cohorts" is a fine thing to say
about the field and a useless thing to say to a specific person deciding what to do with their next
five years. Let's not duck it.

### Which Blocker Actually Binds, for Which Piece

"Superbabies" isn't one blocked thing, it's four differently-blocked things, and the blocker changes
which career move is even coherent:

- **Editing for polygenic traits** is blocked by science _and_ law, and the law is the binding
  constraint. Even a company with unlimited money and a perfect multiplex-editing tool cannot
  currently run a US clinical trial: the Dickey-Wicker Amendment (1996) bars federal funding for any
  research that destroys embryos, and separately,
  [a rider that Congress has re-attached to the FDA's appropriations bill every year since 2016](@fdarider)
  bars the FDA from even reviewing an investigational application for a heritable germline
  modification. Private money can fund lab work right up to the clinic door, and then there is no
  door. That's why Bootstrap Bio — the actual editing startup in this space,
  [founded around the end of 2023, with a CSO and a lab as of mid 2025](@bootstrapbio) — is doing
  preclinical work with no legal path to ever implant an edited embryo domestically unless Congress
  changes one line item. This is arguably the single most _tractable_ blocker on this whole list,
  because it's one narrow legislative fix rather than a moonshot biology problem. Nobody's fixed it
  because nobody's spent political capital on it, which is a PR problem wearing a regulatory
  costume.
- **In vitro gametogenesis** is blocked by science, full stop, and serious people disagree by a
  factor of five on the timeline:
  [Katsuhiko Hayashi puts viable lab-grown human sperm about seven years out; Rod Mitchell says five to ten years for either gamete; Paula Amato says at least a decade, citing chromosomally normal eggs as the real holdup](@ivgtimeline).
  2025 delivered both a first-ever report of fertilisable lab-made human eggs and a public stumble
  from one of the field's pioneers in the same month. This is a real, unsolved, wet-lab problem.
- **The statistical genomics behind selection** mostly isn't blocked by science anymore — it works,
  commercially, today. What's still open is narrower and more interesting: current polygenic scores
  mix your genes' direct effect on you with "genetic nurture" (your parents' genes shaping your
  environment), and only the direct-effect component is actually informative when you're ranking
  full siblings against each other, which is exactly what embryo selection does.
  [Sibling-design studies validate well for disease prediction but the field still argues about whether sibling designs cleanly isolate direct effects at all, or just introduce their own measurement error](@siblingdesign).
  That's a stats and study-design problem, not a biology problem, and it has zero Dickey-Wicker
  exposure because nobody's destroying an embryo to compute a regression.
- **Distribution and normalization** has no science or law blocking it at all. It's legal, it's for
  sale, and the entire obstacle is that almost nobody has heard of it and the people who have mostly
  associate it with Gattaca. Pure PR and go-to-market problem.
- **Artificial womb research** is real but I'd set it aside for this specific question. Ectogenesis
  solves gestation risk, not genetics — it doesn't move IQ, disease risk, or anything else the
  polygenic score is predicting. It matters downstream, as a way to gestate more IVG-produced
  embryos without needing a uterus per embryo, but it's a distinct technology chasing a distinct
  problem. Don't spend a PhD on it if the goal is specifically more superbabies, faster.

### Fieldbuilding: Ops for Tsvi / BGP

The Berkeley Genomics Project is a real, small, independent nonprofit; Tsvi Benson-Tilsen runs it
and writes most of its public output. Its own "[here's what you could help with](@bgp)" post lists,
concretely: submitting deregulation proposals against things like the Dickey-Wicker restrictions,
summarizing the patchwork of laws across jurisdictions, doing the statistics on whether "genomic
vectoring" can move polygenic traits by a lot, solving a genuinely gnarly scheduling-optimization
problem for iterated selection, contributing cell-biology or micromanipulation know-how, and writing
the explainers and FAQs that don't currently exist. No team size or budget is disclosed anywhere on
the site, which I read as its own answer: this is a very thin operation.

That thinness is the argument for you specifically. A tiny, reputation-taxed nonprofit's binding
constraint is almost never "we need one more research idea" — it's execution, fundraising, and
someone competent enough to run the org while the founder writes. Almost nobody will take that job,
because it pays badly and costs real reputation, which is exactly why the marginal person who does
take it moves the needle more here than in almost any other option on this list. It also sidesteps
the thing you already flagged to yourself once before, about not wanting to commit to founding your
own school: you wouldn't be founding anything, you'd be testing whether an existing scrappy
operation is worth betting five years on, which is a much cheaper experiment than starting one from
scratch. I can't verify from outside whether BGP is well-run or just one more LessWrong-adjacent
nonprofit with a blog and no traction — that's diligence only you can do, and in this community it's
normal and cheap to just email Tsvi and ask.

### A PhD: In Which Piece, and Should You

Of the three PhD-shaped problems you listed, two are genuinely PhD-native and one isn't:

- **IVG** is wet-lab stem cell biology. You're a software engineer. This would be starting over in a
  discipline you have no background in, for a 5–6 year, contested, slow-moving problem where the
  actual experts disagree by a factor of five on when it'll work.
- **Artificial womb** is further still from your skills (biomedical/tissue engineering), and, per
  above, more tangential to the actual goal.
- **The statistics** — direct-vs-indirect genetic effects, cross-ancestry portability, the sibling
  design debate — is the one problem here that plays to your actual comparative advantage: software
  engineering plus the willingness to read a stats paper closely. But it doesn't need a PhD. This
  field runs on startups, not academic departments; Herasight, Genomic Prediction, and BGP all need
  people who can do this math now, and none of them are gatekept by a doctorate the way a
  tenure-track job would be. A PhD here mostly buys you five years of credentialing an industry that
  doesn't require the credential. It's the right move only if you want the academic career itself —
  your own lab, teaching, the tenure track — as a terminal goal, not as a means to working on this
  faster.

### Working at a Company: Which One, Doing What

The field splits cleanly in two: Orchid and Genomic Prediction built the disease-focused, cautious
end of the market;
[Nucleus Genomics and Herasight are newer and explicitly do IQ prediction, having rejected their predecessors' more cautious positioning](@companysplit).

- **Orchid** is the best-funded, best-known, and actively
  [hiring for exactly the statistical- analysis-on-genetic-data work this needs](@orchidcareers).
  Lowest counterfactual impact per hire, because they're the easiest of these to staff — but also
  the lowest reputational risk, and the place currently shipping the selection technology to the
  most parents. Take this one if you want to get paid, learn the space fast, and ship product, not
  maximize marginal impact.
- **Genomic Prediction** is the original (Steve Hsu's company), smaller, more research-native.
- **Herasight / Nucleus Genomics** are the newest and boldest, doing the specific IQ-prediction work
  that's most stigmatized and most novel. Smaller shops mean each hire matters more, at the cost of
  betting on companies with less of a track record.
- **Bootstrap Bio** is the actual editing bet — the highest-variance option on this entire list. If
  it works, the counterfactual impact is enormous, because almost nobody else is seriously
  attempting it. But it's wall-blocked by the FDA rider regardless of the science, so realistic
  near-term output is preclinical work and political groundwork, not shipped embryos. I'd size this
  the same way you sized starting your own school once before: sub-1% odds of near-term payoff,
  venture-scale if it hits. Only take that bet knowingly.

### My Actual Read

Skip the PhD. Given your background, it buys you five years to arrive somewhere you could get to
directly. Between the other two, I'd lean toward a research or engineering role at Herasight or
Genomic Prediction over BGP as the first move, not because BGP is a worse bet, but because it's the
option that uses your actual comparative advantage (software plus statistics) most directly, on the
one sub-problem here that's genuinely open, fully legal, and gets you paid market rate while you
learn whether you even like the field. Treat BGP as the cheap parallel test: email Tsvi, read
everything on the site, see if it's a real operation before betting years on it. Orchid is the safe
option if you'd rather ship product than push the open research question. Bootstrap Bio is the one
to join only if you specifically want the high-variance, wall-blocked, editing-focused bet with eyes
open about the FDA rider standing between the company and anything shipping.

{@karavani}: Karavani et al. (2019), "Screening Human Embryos for Polygenic Traits Has Limited
Utility," _Cell_ 179(6):1424–1435 — realistic present-day polygenic embryo screening yields an
average gain of ~2.5 IQ points over a typical IVF batch.
<https://www.cell.com/cell/fulltext/S0092-8674(19)31210-3>

{@shulman}: Shulman, C. & Bostrom, N. (2014), "Embryo Selection for Cognitive Enhancement: Curiosity
or Game-changer?," _Global Policy_ 5(1):85–92 — theoretical ceiling with a well-powered predictor:
+11.5 IQ points selecting 1-in-10 embryos, +24.3 points selecting 1-in-1,000; iterated embryo
selection modeled at under 65 points over 5 generations and under 130 over 10, with diminishing
returns. <https://nickbostrom.com/papers/embryo.pdf>

{@ea4}: Okbay, A. et al. (2022), "Polygenic Prediction of Educational Attainment Within and Between
Families From Genome-Wide Association Analyses in 3 Million Individuals," _Nature Genetics_
54:437–449 — the EA4 polygenic index explains 12–16% of variance in educational attainment.
<https://www.nature.com/articles/s41588-022-01016-z>

{@heritability}: Briley, D.A. & Tucker-Drob, E.M. (2013), "Explaining the Increasing Heritability of
Cognitive Ability Across Development: A Meta-Analysis of Longitudinal Twin and Adoption Studies,"
_Psychological Science_ 24(9):1704–1713 — heritability of cognitive ability rises from ~0.4 in early
childhood to ~0.75–0.8 by adulthood. <https://journals.sagepub.com/doi/10.1177/0956797613478618>

{@art2022}: US CDC (2024), "2022 Assisted Reproductive Technology (ART) Fertility Clinic and
National Summary Report" — 98,289 infants born via ART in 2022, about 2.6% of all US births.
<https://www.cdc.gov/art/php/surveillance/index.html>

{@iodine}: Feyrer, J., Politi, D. & Weil, D.N. (2013), "The Cognitive Effects of Micronutrient
Deficiency: Evidence From Salt Iodization in the United States," NBER Working Paper 18034, published
in _Journal of the European Economic Association_ (2017) — salt iodization raised average IQ by up
to 15 points in the most iodine-deficient quarter of the US population.
<https://www.nber.org/papers/w18034>

{@lead}: McFarland, M.J., Hauer, M.E. & Reuben, A. (2022), "Half of US Population Exposed to Adverse
Lead Levels in Early Childhood," _PNAS_ 119(11):e2118631119 — average 2.6 IQ point loss per American
alive today from childhood leaded-gasoline exposure; ~824 million cumulative IQ points lost across
more than 170 million people. <https://www.pnas.org/doi/10.1073/pnas.2118631119>

{@orchid}: Genetic Literacy Project (2024) and CNBC (2025) reporting on Orchid Health's whole-genome
embryo screening, priced at $2,500 per embryo, screening for over 1,200 monogenic conditions plus
polygenic risk.
<https://geneticliteracyproject.org/2024/01/15/2500-per-embryo-tech-startup-claims-to-screen-potential-children-for-1200-genetic-disorders-but-experts-not-sure-its-worth-the-hype/>

{@hejiankui}: NPR and CNN (Dec 30, 2019) — He Jiankui sentenced to three years in prison and a ¥3
million (~$430,000) fine for illegal medical practice, after forging ethics approvals and misleading
patients to implant CRISPR-edited (CCR5) embryos; twins Lulu and Nana were born in October 2018.
<https://www.npr.org/2019/12/30/792340177/chinese-researcher-who-created-gene-edited-babies-sentenced-to-3-years-in-prison>

{@zagorsky}: Zagorsky, J.L. (2007), "Do You Have to Be Smart to Be Rich? The Impact of IQ on Wealth,
Income and Financial Distress," _Intelligence_ 35(5):489–501 — each additional IQ point predicts
$234–$616 more in annual earnings, controlling for family background, in the NLSY79 cohort.
<https://www.sciencedirect.com/science/article/abs/pii/S0160289607000219>

{@dairygenomics}: _Journal of Dairy Science_ (2022), "Changes in Genetic Trends in US Dairy Cattle
Since the Implementation of Genomic Selection" — the annual rate of genetic gain in production
traits has roughly doubled since US dairy producers adopted genomic selection in 2009.
<https://www.journalofdairyscience.org/article/S0022-0302(22)00709-3/fulltext>

{@pgsbias}: Martin, A.R. et al. (2019), "Clinical Use of Current Polygenic Risk Scores May
Exacerbate Health Disparities," _Nature Genetics_ 51:584–591 — about 86% of GWAS participants are of
European descent; polygenic score accuracy drops by roughly 37–78% in South Asian, East Asian, and
African ancestry populations relative to European ancestry.
<https://www.nature.com/articles/s41588-019-0379-x>

{@fdarider}: Johnston, J. (2020), "Budgets Versus Bans: How U.S. Law Restricts Germline Gene
Editing," _Hastings Center Report_ 50(3) — a rider first attached to the FY2016 Consolidated
Appropriations Act (signed Dec. 18, 2015) bars the FDA from reviewing any investigational
application involving a heritable human genetic modification; it has been reattached to FDA
appropriations every year since. <https://onlinelibrary.wiley.com/doi/10.1002/hast.1094>

{@bootstrapbio}: Bloomberg (June 25, 2025), "'Superbabies' Startup Seeks Funds for Controversial
Gene Editing Push" — Bootstrap Bio, founded roughly 18 months earlier, has hired a chief science
officer and opened a lab while raising seed funding to edit heritable genetic material in human
embryos.
<https://www.bloomberg.com/news/articles/2025-06-25/-superbabies-startup-bootstrap-bio-seeks-funds-for-gene-editing-company>

{@ivgtimeline}: Fertility 2025 conference reporting via Femtech World (2025) and STAT News (Sept.
30, 2025) — expert estimates for viable lab-grown human eggs/sperm range from ~7 years (Katsuhiko
Hayashi) to 5–10 years (Rod Mitchell) to at least a decade (Paula Amato, citing chromosomally normal
eggs as the main obstacle); 2025 saw both a first report of fertilisable lab-made human eggs and a
public setback in a leading lab's parallel effort.
<https://www.statnews.com/2025/09/30/fertility-pioneer-shoukhrat-mitalipov-research-update/>

{@siblingdesign}: Border, R. et al. (2024), "Interpreting Polygenic Score Effects in Sibling
Analysis," _PLOS ONE_ — within-family sibling designs validate well for disease prediction but the
field actively disputes whether they cleanly isolate a polygenic score's direct genetic effect or
introduce their own measurement-error bias.
<https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0282212>

{@bgp}: Benson-Tilsen, T. (2025), "Some Reprogenetics Related Projects You Could Help With,"
Berkeley Genomics Project — a public list of concrete open tasks spanning policy/deregulation
(including Dickey-Wicker), statistical genetics research, cell-biology implementation work, and
public communication; no team size or budget is disclosed.
<https://berkeleygenomics.org/articles/Some_reprogenetics_related_projects_you_could_help_with.html>

{@companysplit}: MIT Technology Review (Oct. 16, 2025), "The Race to Make the Perfect Baby Is
Creating an Ethical Mess" — Genomic Prediction and Orchid have led the cautious, disease-focused end
of embryo screening for roughly five years; Nucleus Genomics and Herasight are newer entrants that
have rejected that caution and moved into trait prediction including IQ.
<https://www.technologyreview.com/2025/10/16/1125159/ethics-embryo-screening-reproduction-baby/>

{@orchidcareers}: Orchid Health, "Careers at Orchid" — actively hiring for roles involving
statistical analysis of genetic datasets. <https://www.orchidhealth.com/careers>
