# 10. Engineering language for better thinking, and whether language shapes thought

Slice: "fix language, fix thought" projects (Leibniz → Wilkins → Korzybski → E-Prime → Yudkowsky),
conlangs built around Sapir-Whorf (Loglan/Lojban, Láadan, Ithkuil, Toki Pona), the replication
record of linguistic relativity, and whether having a _word_ for a concept makes you use it
(debiasing, statistics training, calibration, hypocognition).

Where the brief I was given was wrong, I've marked it **[correction]**. Anything I couldn't open and
check is marked **UNVERIFIED**.

---

## 1. Most interesting findings

**1. None of the conlangs built to test Whorf has ever run the test.** James Cooke Brown started
Loglan in 1955 to test Sapir-Whorf. He was a sociologist, and he also designed the Parker Brothers
board game _Careers_. He announced it in _Scientific American_ (1960, vol. 202). The test never
happened. Brown asserted legal ownership of the language, so his followers forked it as the freely
licensed Lojban (1987+), and the USPTO later held that "Loglan" couldn't be trademarked
([Wikipedia: Loglan](https://en.wikipedia.org/wiki/Loglan);
[Wikipedia: James Cooke Brown](https://wikipedia.com/wiki/James_Cooke_Brown)). The Lojban community
itself says a real test would need an international body of fluent speakers, which doesn't exist.
The only reports from speakers are anecdotes, such as a 2009 Reddit AMA by a speaker who admits they
can't separate Lojban from the effect of just learning any very foreign language
([Lojban wiki: SWH](https://mw.lojban.org/papri/SWH)). Suzette Haden Elgin built Láadan in 1982 for
_Native Tongue_ (1984) to test whether a women's language would spread or change culture. About ten
years later she concluded it had failed, because it got almost no uptake. She noted pointedly that
Klingon thrives
([Romney, LitHub 2019](https://lithub.com/this-science-fiction-novelist-created-a-feminist-language-from-scratch)).
The bottleneck was never grammar design. It was recruiting speakers. The one attempt to raise a
native conlang speaker was d'Armond Speers speaking only Klingon to his son for ~3 years in the
1990s. The child stopped responding to it and spoke none by high school
([TodayIFoundOut 2012](https://www.todayifoundout.com/index.php/2012/08/a-man-once-tried-to-raise-his-son-as-a-native-speaker-in-klingon/)).

**2. Lojban's evidentials were borrowed from Native American languages and from Elgin's feminist
conlang, and a LessWrong user tried to bolt Bayesian decibels onto them.** The official grammar
says: "Lojban's list of evidentials was derived from lists describing several American Indian
languages", and "Láadan's set of indicators was drawn on extensively in developing the Lojban
indicator system"
([CLL §13.11](https://lojban.org/publications/cll/cll_v1.1_xhtml-section-chunks/section-evidentials.html)).
The verified set is ja'o "I conclude", ca'e "I define", ba'a "I expect" (ba'acu'i "I experience",
ba'anai "I remember"), su'a "I generalize", ti'e "I hear (hearsay)", ka'u "I know by cultural
means", se'o "I know by internal experience", za'a "I observe", pe'i "I opine", ru'a "I postulate",
ju'a "I state". They are optional; an unmarked bridi ≈ ju'a. In "Thinking Bayesianically, with
Lojban" (DataPacRat, LessWrong, Jan 2012) the author proposed an experimental evidential _bei'e_
that tags a claim with its log-odds in decibels, following Jaynes
([GreaterWrong](https://www.greaterwrong.com/posts/BS8dYNN5D6kLhvdXR/thinking-bayesianically-with-lojban)).
Commenters argued over whether "beyond reasonable doubt" means 76% or 98%. gwern skipped the conlang
and adopted Kesselman's verbal-probability scale from US intelligence analysis instead. The
rationalist credence vocabulary that actually spread came from intelligence analysts, not from
Lojban.

**3. Rationalist verbal practice is largely General Semantics with the serial numbers filed off, and
the Sequences never say so.** Eric S. Raymond's "Rationalism before the Sequences" (LessWrong, 2021)
traces the line from Korzybski's _Science and Sanity_ (1933) to Hayakawa, van Vogt's _The World of
Null-A_ (serialized 1945) and Heinlein's "Gulf" (1949) to Yudkowsky. Raymond says he found "many
reflections of [GS] in the Sequences." Yudkowsky commented that the history was "well-informed and
well-applied." Per Raymond's reading list, Yudkowsky reports reading Hayakawa's _Language in Thought
and Action_ and _Null-A_, but not _Science and Sanity_. He found _Null-A_ more exciting than "Gulf"
([GreaterWrong](https://www.greaterwrong.com/posts/qc7P2NwfxQMC3hdgm/rationalism-before-the-sequences)).
Heinlein had attended a Korzybski lecture in LA in June 1939
([Wikipedia: Speedtalk](https://en.wikipedia.org/wiki/Speedtalk)). Neither "Taboo Your Words"
(Feb 2008) nor "37 Ways That Words Can Be Wrong" (Mar 2008) mentions Korzybski or General Semantics,
as far as I could see ([LW](https://www.lesswrong.com/posts/WBdvyyHLdxZSAMmoz/taboo-your-words),
[LW](https://www.lesswrong.com/posts/FaJaCgqBKphrDzDSj/37-ways-that-words-can-be-wrong)). The
mapping is close. "The map is not the territory" is Korzybski verbatim. Korzybski's indexing ("cow₁
is not cow₂") is "bleggs and rubes" and "categories aren't essences". Hayakawa's abstraction ladder
is "replace the symbol with the substance". Rationalist Taboo is an extensional device turned into a
party game. The genuinely new parts are Bayesian probability and the treatment of categories as
clusters in thingspace, which GS lacked.

**4. Borges caught the "dolphins are fish" problem 340 years early, and its root cause.** In "The
Analytical Language of John Wilkins" (1942), Borges notes that Wilkins's _Essay towards a Real
Character_ (1668) built words out of a 40-category taxonomy. In it, _de_ = element, _deb_ = fire,
_deba_ = flame, and _zana_ = "a scaly river fish with reddish flesh" (salmon). Wilkins files the
whale as "a viviparous, oblong fish." His "stones" category has a subclass "insoluble (coal,
fuller's earth, and arsenic)." This is where the Celestial Emporium's animal taxonomy comes from,
with entries like "(l) etcetera" and "(n) those that at a distance resemble flies." Borges's
verdict: "there is no classification of the universe that is not arbitrary and speculative. The
reason is quite simple: we do not know what the universe is"
([gwern.net PDF](https://www.gwern.net/doc/borges/1942-borges-johnwilkinsanalyticallanguage.pdf)).
This is the structural argument against every philosophical language from Wilkins to Ithkuil. A
language that encodes a taxonomy in its words freezes the speaker's current map into the grammar.
Yudkowsky's item 30 in "37 Ways" is the same whale error.

**5. E-Prime has no evidence behind it.** D. David Bourland Jr. (a Korzybski student) proposed
English without "to be" in 1965 ("A Linguistic Note: Writing in E-Prime"). The supporting "evidence"
is Korzybski's claim that students who dropped "is" improved by "one full letter grade", plus
therapist anecdotes from Albert Ellis ([Wikipedia: E-Prime](https://en.wikipedia.org/wiki/E-Prime)).
The only empirical test I found is a 2012 NDSU thesis (Boyd). It measured how much people use "to
be" and correlated that with the outcomes E-Prime theorists predict: dialectical thinking,
interpersonal complexity, arrogance and neuroticism. It found no support
([NDSU](https://library.ndsu.edu/ir/items/9b38e4bb-ce7b-49a0-bb32-df8d3447c4bc)). It was
correlational, not an intervention. Critics include Robin Lakoff (1992) and James French ("The Top
Ten Arguments Against E-Prime", 1992). Their main point: E-Prime bans the auxiliary and locative
"is" along with the "is of identity", and passive-voice workarounds can _hide_ agency.

**6. The best-supported relativity effects run on language used in the moment, not on perception
rewired for good.** Russian speakers distinguish _goluboy_/_siniy_ blues faster across the category
boundary. The advantage disappears when they hold an 8-digit number in mind (verbal interference)
but not under spatial interference
([Winawer et al. 2007 PNAS](https://langcog.stanford.edu/papers/winawer2007.pdf)). A Greek ERP study
(Thierry et al. 2009 PNAS) found a pre-attentive mismatch response to _ghalazio_/_ble_ blues
([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2657373)). The Pirahã have no word even for "one".
In Frank, Everett, Fedorenko & Gibson (2008, _Cognition_) they matched large sets _exactly_ when the
set stayed visible, and failed only when the task required memory
([MIT News 2008](https://news.mit.edu/2008/language-0624)). Frank et al. conclude that number words
"do not change underlying representations of number but serve as a cognitive technology for keeping
track of cardinality." Lupyan's label-feedback hypothesis (2012) generalizes this: labels exert fast
top-down effects on categorization and even detection, which is why verbal interference can switch
them off ([Frontiers](https://frontiersin.org/articles/10.3389/fpsyg.2012.00054/full)). For
rationalist jargon, this is the most defensible model: a handle helps you _store, retrieve and
transmit_ a concept. It doesn't change what you perceive.

**7. The famous Boroditsky effects mostly failed to replicate, except the blame one.** The
German/Spanish "bridge/key" adjective study (Boroditsky, Schmidt & Phillips 2003) was a book chapter
whose data were never fully published. Mickan, Schiefke & Stefanowitsch (2014) failed to replicate
it twice ([FLoRA](https://forrt.org/flora-replication-atlas/doi/10.1515/gcla-2014-0004/)). A
systematic review of 43 grammatical-gender studies (N = 5,895) found that support was "strongly
task- and context-dependent" and "rested heavily on outcomes that have clear and equally viable
alternative explanations" ([Samuel, Cole & Eacott 2019](https://pubmed.ncbi.nlm.nih.gov/31429058/)).
The Mandarin vertical-time effect (Boroditsky 2001) failed in Chen (2007), January & Kako (2007) and
Tse & Altarriba (2008). Boroditsky's group re-supported it with new tasks in 2011. Chen et al. later
found Taiwanese and mainland Mandarin speakers differ, which suggests writing direction rather than
metaphor. The exception is Fausey & Boroditsky's agentive-language blame effect ("she broke the
vase" vs "the vase broke", 2010). It _did_ replicate in a preregistered direct replication in US
English. In Croatian it was weaker and affected blame only, not fines
([Tonković, Vlašiček & Dumančić 2022](https://www.bib.irb.hr/1194796)). **[correction]** the brief
implied blame was in the failed group. Note that in the 2010 _Economist_ online debate, readers
voted 78–22 for Boroditsky's "language shapes thought" over Mark Liberman
([Language Log](https://languagelog.ldc.upenn.edu/nll/?p=2856)).

**8. Keith Chen co-authored the paper that weakened his own famous result.** Chen (2013, _AER_
103(2)) reported that speakers of languages without obligatory future marking save more, retire with
more wealth, smoke less and are less obese. The "30%" figure is that strong-future speakers were
~30% _less likely to save_ in a given year **[correction to phrasing]**
([SciAm](https://www.scientificamerican.com/article/how-language-effects-your-wealth-health/)).
Roberts, Winters & Chen (2015, _PLOS ONE_) then controlled for language relatedness (Galton's
problem). The correlation was "weaker", and under the strictest tests "the correlation is not
significant". It stayed "reasonably robust" under several other tests. The authors recommend
experiments over more cross-cultural regressions
([Language Log](https://languagelog.ldc.upenn.edu/nll/?p=20697)). Status: weakened, unresolved, and
probably a confound.

**9. The "foreign-language effect" is real-ish but small, and its proposed mechanism doesn't fit the
data.** Keysar, Hayakawa & An (2012) proposed it, and Costa et al. (2014) extended it to moral
dilemmas: thinking in an L2 reduces framing effects and increases utilitarian choices. Del Maschio
et al. (2022) pooled 91 experiments with N = 13,886. They found a pooled OR = 1.34 [1.10, 1.60], I²
= 72.8%, and a prediction interval of [0.29, 6.11], so a new study could plausibly find nothing or
the reverse ([Bilingualism: Lang. & Cog.](https://doi.org/10.1017/S1366728921001012)). Their funnel
plot shows "studies with medium-to-large standard error showing no effect or an opposite effect are
completely missing", but Egger's test was non-significant. L2 proficiency did _not_ moderate the
effect. That undercuts the "emotional distance of a less fluent language" story. Circi et al. (2021,
_PB&R_, 47 experiments) also find an effect, moderated by language similarity but not proficiency.
Wickelmaier (2015) reanalysed Costa et al.'s framing data and found the language × frame interaction
was never properly tested, invalidating 4 of 5 conclusions
([arXiv](https://arxiv.org/pdf/1506.07727)). Status: mixed. The pooled effect is probably inflated,
and the mechanism is unclear.

**10. Training people on _named_ biases works more than the old pessimism allowed, but the name
isn't the active ingredient.** Morewedge et al. (2015, _PIBBS_) was funded by IARPA's Sirius
program. Participants got one session of either a serious game or a 30-minute video ("Unbiasing Your
Biases") that defined each bias, gave mitigation strategies and, in the game, personalized feedback
and practice. The game reduced bias by ≥31.94% immediately and ≥23.57% at 2 months; the video by
≥18.60% and ≥19.20% (N ≈ 240 per experiment). The effect transferred to untaught formats
([City Research Online](https://openaccess.city.ac.uk/id/eprint/12324/)). The game beat the video,
and both defined the bias, so feedback and practice add a lot beyond the name. The field follow-up
was Sellier, Scopelliti & Morewedge (2019, _Psych Science_). They tested 290 French grad students,
using natural variation in whether students played the game before or after an unannounced
Challenger-style business case ("Carter Racing"). Trained students were 29% less likely to choose
the inferior, confirmation-driven option
([BU](https://open.bu.edu/items/704bd6b8-5dbc-4a82-961b-48b6f63cd76e)). Status: not independently
replicated, as far as I found.

**11. Abstract statistical rules _do_ transfer, against the "transfer is hopeless" consensus.**
Fong, Krantz & Nisbett (1986, _Cognitive Psychology_) gave subjects a brief lesson on the law of
large numbers: a four-page explanation plus drawing samples of 1, 4 and 25 gumballs from a jar. This
raised the frequency and quality of statistical reasoning on everyday problems, and the gains lasted
weeks ([Deep Blue](https://deepblue.lib.umich.edu/items/9850801d-32d8-4756-a6ce-5479fdadc4e5)).
Lehman, Lempert & Nisbett (1988, _American Psychologist_) found that 2 years of grad school in
psychology and medicine produced large gains in statistical and methodological reasoning. Law
improved conditional logic. _Chemistry produced no measurable effect on any of them_
([Deep Blue](https://deepblue.lib.umich.edu/bitstream/handle/2027.42/92173/TheEffectsOfGraduateTraining.pdf?sequence=1)).
Their explanation is that disciplines differ in the rule systems they teach, and having the rule as
an explicit abstraction is what transfers.

**12. Calibration training is fast and narrow.** In Lichtenstein & Fischhoff (1980), subjects did 11
sessions of 200 items each with feedback, and "almost all" of the learning came after the _first_
feedback round. Transfer to dissimilar tasks was limited
([DTIC](https://apps.dtic.mil/sti/pdfs/ADA089619.pdf)). The Good Judgment Project's training module
(CHAMPS KNOW) took under an hour and improved Brier scores 6–11% over control across forecasting
tournament years
([Chang, Chen, Mellers & Tetlock 2016, _JDM_](https://dlab.sauder.ubc.ca/sjdm/journal/16/16511/jdm16511.html)).
**[correction]** The figure is 6–11% across years, not "~10%". Status: replicated within GJP. These
are the strongest "teach a concept, get better judgment" results in this slice.

**13. CFAR has essentially no controlled evidence.** CFAR's 2015 longitudinal study had no control
group. 135 of 196 people answered the ~1-year follow-up, with self-reported gains of d = 0.19 for
happiness, 0.24 for conscientiousness and 0.45 for "effective approaches to projects". The
cognitive-bias measure didn't move significantly, and CFAR says that test was underpowered
([rationality.org](https://rationality.org/studies/2015-longitudinal-study)). A small
randomized-admissions RCT in 2012 (~15 treated, ~17 controls) went unreported. A staffer later
called not reporting it "a mistake"
([GreaterWrong](https://www.greaterwrong.com/posts/h9qckxLH2me53DHPG/results-of-a-one-year-longitudinal-study-of-cfar-alumni)).
Status: unknown.

**14. Hypocognition, hypercognition, and why invented languages are an odd remedy.** Robert Levy
(_Tahitians_, 1973) reported that Tahitians had no word for sadness or grief after a loss and
described themselves as "sick" or "strange". He speculated this contributed to suicide. He also
coined _hypercognition_, for over-elaborated concepts, and thought cultures do best balancing the
two. Wu & Dunning (2018, _Rev. Gen. Psych._ 22:25) revived "hypocognition" as a missing concept you
can't notice is missing ([Wikipedia](https://en.wikipedia.org/wiki/Hypocognition)). Scott
Alexander's "Concept-Shaped Holes Can Be Impossible To Notice" (2017) gives the rationalist version.
Anosmics assume "smells good" is metaphor until adulthood, and Galton found people with no mental
imagery assumed others spoke figuratively
([SSC](https://slatestarcodex.com/2017/11/07/concept-shaped-holes-can-be-impossible-to-notice/)).
Hypercognition is the community's actual failure mode: seeing Moloch or motte-and-bailey everywhere.
On LessWrong it surfaces in "Avoid inflationary use of terms" (lsparrish, 2012) and complaints that
people "may be too eager to create new jargon"
([GreaterWrong](https://www.greaterwrong.com/posts/LqfnkpmK2EBcwbAwA/avoid-inflationary-use-of-terms)).

---

## 2. Read these (ranked)

1. **Eric S. Raymond, "Rationalism before the Sequences"** (LessWrong, 2021). Long essay, ~30–40
   min.
   [link](https://www.greaterwrong.com/posts/qc7P2NwfxQMC3hdgm/rationalism-before-the-sequences).
   The genealogy from Korzybski to Heinlein, van Vogt and Yudkowsky, with Yudkowsky endorsing it in
   the comments.
2. **Jorge Luis Borges, "The Analytical Language of John Wilkins"** (1942). ~2,000 words.
   [PDF](https://www.gwern.net/doc/borges/1942-borges-johnwilkinsanalyticallanguage.pdf). Ten
   minutes that contain the whole case against a priori philosophical languages.
3. **Arika Okrent, _In the Land of Invented Languages_** (2009). ~350 pp.
   [publisher](https://www.randomhousebooks.com/books/124272). The best single history: Wilkins,
   Loglan/Lojban politics, Láadan, Klingon, plus an appendix of ~900 invented languages.
4. **Joshua Foer, "Utopian for Beginners"** (_The New Yorker_, Dec 24 2012). ~9,000 words.
   [link](https://www.newyorker.com/magazine/2012/12/24/utopian-for-beginners). Ithkuil, and how a
   Sacramento DMV employee's language got adopted by a Ukrainian "psychonetics" movement.
5. **Terry Regier & Paul Kay, "Language, thought, and color: Whorf was half right"** (_TICS_, 2009).
   ~8 pp. [PDF](https://www1.icsi.berkeley.edu/pubs/ai/tics2.pdf). The most careful pro-relativity
   synthesis from the people who built the anti-relativity universals literature.
6. **Frank, Everett, Fedorenko & Gibson, "Number as a cognitive technology"** (_Cognition_, 2008). 6
   pp. [PubMed](https://pubmed.ncbi.nlm.nih.gov/18547557/). The cleanest experiment for the "words
   as tools for memory" model.
7. **Guy Deutscher, "Does Your Language Shape How You Think?"** (_NYT Magazine_, Aug 26 2010).
   ~5,000 words.
   [mirror](https://listserv.linguistlist.org/pipermail/lgpolicy-list/2010-August/011581.html). The
   Boas–Jakobson principle: languages differ in what they _must_ express, not in what they _can_.
   Read it knowing its gender examples later failed to replicate.
8. **Samuel, Cole & Eacott, "Grammatical gender and linguistic relativity: A systematic review"**
   (_PB&R_, 2019). ~20 pp. [PubMed](https://pubmed.ncbi.nlm.nih.gov/31429058/). Shows how a famous
   effect falls apart under a systematic look.
9. **Morewedge et al., "Debiasing Decisions"** (_PIBBS_, 2015). ~12 pp.
   [PDF](https://openaccess.city.ac.uk/id/eprint/12324/1/Debiasing_Decisions_PIBBS.pdf). The best
   evidence that teaching named biases changes behavior, and that practice matters more than the
   name.
10. **Eliezer Yudkowsky, "37 Ways That Words Can Be Wrong"** (LessWrong, 2008). ~2,500 words.
    [link](https://www.lesswrong.com/posts/FaJaCgqBKphrDzDSj/37-ways-that-words-can-be-wrong). Read
    it next to Hayakawa's abstraction-ladder chapter of _Language in Thought and Action_ (1941/1949)
    and count the overlaps.
11. **Scott Alexander, "Concept-Shaped Holes Can Be Impossible To Notice"** (SSC, 2017). ~2,000
    words.
    [link](https://slatestarcodex.com/2017/11/07/concept-shaped-holes-can-be-impossible-to-notice/).
    The rationalist statement of hypocognition.
12. **Del Maschio et al., "Decision-making depends on language: A meta-analysis of the Foreign
    Language Effect"** (2022). ~14 pp. [DOI](https://doi.org/10.1017/S1366728921001012). A good
    exercise in reading a meta-analysis skeptically: the prediction interval and the funnel plot
    tell you more than the pooled OR.

---

## 3. Details

### Sapir-Whorf scorecard

| Claim                                                                                              | Key paper(s) + year                                                            | Status                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Colour terms speed cross-boundary discrimination (Russian/Greek blues)                             | Winawer et al. 2007 PNAS; Thierry et al. 2009 PNAS                             | **Replicated** across languages and methods. Abolished by verbal interference, so it depends on language in use                                                                                                                                                   |
| …and the effect is lateralized to the right visual field (left hemisphere)                         | Gilbert et al. 2006 PNAS; Regier & Kay 2009                                    | **Mixed.** Witzel & Gegenfurtner 2011 (_J Vision_, 230 observers, 10 variants) found category effects in _both_ hemifields                                                                                                                                        |
| Absolute vs relative spatial frames (Tzeltal, Guugu Yimithirr) drive non-linguistic spatial memory | Levinson et al. 2002 _Cognition_ 84; Majid et al. 2004                         | **Contested.** Li & Gleitman 2002 (_Cognition_ 83) shifted English speakers' frames with blinds and landmarks. Levinson replied they had confounded intrinsic with absolute frames. The language–cognition covariation is real; the causal direction is unsettled |
| No number words → no exact number cognition (Pirahã)                                               | Gordon 2004 _Science_ 306                                                      | **Mixed.** Frank et al. 2008: exact matching fine without a memory load. Everett & Madora 2012 reportedly reproduced Gordon                                                                                                                                       |
| Mundurukú approximate arithmetic fine, exact fails above ~4–5                                      | Pica et al. 2004 _Science_ 306                                                 | Broadly accepted; the "number words are a technology" reading dominates                                                                                                                                                                                           |
| Grammatical gender shapes object concepts ("bridge/key")                                           | Boroditsky, Schmidt & Phillips 2003 (book chapter, data never fully published) | **Failed** (Mickan et al. 2014, 2 attempts). Systematic review (Samuel et al. 2019): weak, task-dependent                                                                                                                                                         |
| Mandarin speakers think of time vertically                                                         | Boroditsky 2001 _Cog Psych_ 43                                                 | **Failed** (Chen 2007; January & Kako 2007; Tse & Altarriba 2008). Partly revived with new tasks (Boroditsky, Fuhrman & McCormick 2011); a writing-direction confound is likely (Chen et al.)                                                                     |
| Agentive phrasing raises blame and fines                                                           | Fausey & Boroditsky 2010 _PB&R_ 17                                             | **Replicated in English** (prereg., Tonković et al. 2022). Mixed in Croatian                                                                                                                                                                                      |
| No counterfactual marker → Chinese speakers worse at counterfactuals                               | Bloom 1981 (book)                                                              | **Failed.** Au 1983 _Cognition_: the difference came from translation quality                                                                                                                                                                                     |
| Weak future-tense marking → more saving and health                                                 | Chen 2013 _AER_ 103                                                            | **Weakened.** Roberts, Winters & Chen 2015 _PLOS ONE_: not significant under the strictest phylogenetic controls                                                                                                                                                  |
| Thinking in an L2 reduces framing bias and raises utilitarian choice                               | Keysar et al. 2012; Costa et al. 2014                                          | **Mixed/shrinking.** Meta-analysis OR 1.34, prediction interval includes 1. Some preregistered nulls. The Costa framing analysis was flawed (Wickelmaier 2015)                                                                                                    |
| Labels modulate perception top-down                                                                | Lupyan 2012 (theory + lab studies)                                             | Reasonably robust in the lab. It's a framework, not one finding                                                                                                                                                                                                   |

**Honest consensus:** The strong version, that language determines what you _can_ think, is dead.
Lab effects are real, small and task-specific, and they mostly disappear when the language system is
occupied. Language works like a cache and an attention director that you consult online, not like a
lens fitted over perception. McWhorter's _The Language Hoax_ (2014) argues even the surviving
effects are too small to matter for worldview. Deutscher (2010) argues the real effects come from
habit: what your grammar forces you to _track_, e.g. cardinal directions, evidentiality, or a
speaker's gender. That second framing is the one relevant to rationalists. Obligatory
credence-marking would be a Deutscher-style habit effect, if it worked at all.

### Engineered-language lineage, compressed

- **Leibniz** (1660s–80s): the _characteristica universalis_ plus _calculus ratiocinator_.
  "Calculemus" variants appear in several texts (Gerhardt ed., vol. VII p. 200, _De arte
  characteristica_; also _De Arte Combinatoria_ 1666)
  ([Wikiquote](https://en.wikiquote.org/wiki/Gottfried_Leibniz)). A specific 1685 source is
  **UNVERIFIED**.
- **Wilkins 1668**: 40 genera, with words spelled by their place in the taxonomy. Borges's essay is
  the critique.
- **Ogden's Basic English (1930)**: 850 words. Orwell promoted it at the BBC from 1942–44, soured on
  it by 1945, and satirized it as Newspeak (1949), whose "vocabulary grows smaller each year"
  ([Wikipedia: Newspeak](https://en.wikipedia.org/wiki/Newspeak)). Heinlein's Speedtalk in "Gulf"
  (1949) took the opposite route: it maps each Basic English word to its own phoneme, so a sentence
  takes ~¼ the time to say.
- **Korzybski 1933** (_Science and Sanity_): non-Aristotelian "consciousness of abstraction" and
  extensional devices (indexing, dating, "etc.", quotes, hyphens), plus the structural differential.
  Max Black called it "some hypothetical neurology fortified with dogmatic metaphysics." It fed into
  REBT (Ellis), Gestalt therapy and NLP
  ([Wikipedia: GS](https://en.wikipedia.org/wiki/General_semantics)).
- **Hayakawa**: _Language in Action_ (1941, a Book-of-the-Month Club pick that Korzybski helped
  arrange), revised as _Language in Thought and Action_ (1949). Over 1M copies sold. Korzybski found
  the 1949 version "very unsatisfactory"
  ([Korzybski biography](https://korzybskifiles.blogspot.com/2015/02/chapter-48-institute-of-general_16.html)).
- **Martin Gardner**, _In the Name of Science_ (1952; retitled _Fads and Fallacies_ 1957), chapter
  "General Semantics, Etc." He placed GS in a borderline "may have merit" tier but described a drift
  into cultism. The often-quoted "the good parts are not original and the original parts are not
  good" is a forum paraphrase, **UNVERIFIED** as his wording.
- **Ithkuil** (Quijada 2004/2011; New Ithkuil 2023): nine _validations_, including confirmative
  (default), reportive, intuitive, inferential, presumptive, conjectural and tentative
  ([2004 grammar](https://ithkuil.place/mirror/2004-en/ithkuil-ch5a-verbs.htm)). Nobody, including
  Quijada, speaks it fluently. A 2004 Russian _Computerra_ article by Stanislav Kozlovsky ("The
  Speed of Thought") brought it to Russian-speakers. In 2010 Oleg Bakhtiyarov (University of
  Effective Development, Kyiv, a promoter of "psychonetics") invited Quijada to a "Creative
  Technology" conference in Elista, Kalmykia. Quijada later thanked him for visits to both Kyiv and
  Elista ([Quijada site](https://ithkuil.place/mirror/2004-en/index.htm)). **[correction]**: the
  conference was in Elista, not Kiev. How the Foer piece ends, and what turned out to be behind the
  group, is **UNVERIFIED** because the New Yorker blocked fetches.
- **Láadan** (verified,
  [Wikibooks](https://en.wikibooks.org/wiki/L%C3%A1adan/L%C3%A1adan_Grammar_Reference)): every
  statement ends with an evidence morpheme. wa = perceived by speaker, externally or internally; wi
  = self-evident; we = perceived in a dream; wáa = assumed true because the source is trusted; waá =
  assumed false because the source is distrusted (**waálh** = distrusted and the source is
  malicious); wo = imagined/hypothetical; wóo = speaker states total lack of knowledge. The brief's
  glosses were right, and it missed _waálh_.
- **Toki Pona** (Sonja Lang, draft 2001, book 2014): ~120–137 words, made to simplify her own
  thinking during depression and partly Taoist in inspiration. It's the minimalism experiment: you
  can't say "investment bank", only "money-building". Speaker counts range from hundreds to a few
  thousand. I found no study of cognitive effects.
- **dath ilan's Baseline** (Yudkowsky's fiction): the in-story description says its phonemes are
  spaced so it stays intelligible to people with slightly worse hearing in noisy conditions.
  In-between phonemes are reserved for building conlangs on top of it
  ([gliese1337 2022](https://gliese1337.blogspot.com/2022/06)). Only ~5 non-name words appear in the
  text. The rationalist "What words should be shorter in the rational dictionary?" thread (2022) is
  the real-world version: Zipf-optimize the jargon.

### Fiction rationalists cite (brief)

_The Languages of Pao_ (Vance 1958) has three engineered languages that create soldier, technician
and merchant castes. _Babel-17_ (Delany 1966) has an "analytical language which has no word for
'I'." "Gulf" (Heinlein 1949) has Speedtalk. _The World of Null-A_ (van Vogt 1945/48) is General
Semantics as a utopia. "Story of Your Life" (Chiang 1998) has Heptapod B as a simultaneous,
teleological cognition. _Embassytown_ (Miéville 2011) has the Ariekei, who can't lie and need two
mouths to speak. _Anathem_ (Stephenson 2008) has Orth and the coined vocabulary of the maths.
Newspeak (1949). Only Pao and Null-A are pure Whorf-engineering plots; the others use relativity as
a premise ([SF Encyclopedia](https://sf-encyclopedia.com/entry/linguistics)).

---

## Dead ends / contested

- **"Lojban speakers think more logically."** There are zero controlled data, only self-reports from
  a few speakers with obvious confounds. Also, Lojban's _syntax_ is unambiguous but its semantics
  are not, which LessWrong commenters themselves note
  ([LW](https://www.lesswrong.com/posts/ccryPbdxLJ9vu4xP5/language-intelligence-rationality)).
- **Yudkowsky on Lojban:** I found no direct statement by him. **UNVERIFIED** that he endorses or
  references it.
- **Korzybski anecdotes** (the dog-biscuit lecture stunt, the "full letter grade") are
  folklore-grade.
- **Pirahã** is entangled with the Everett–Nevins/Sakel disputes and the small accessible
  population. Treat any single Pirahã number study as provisional.
- **Foreign-language effect mechanism.** "Emotional distance" predicts that lower proficiency gives
  a bigger effect, and two meta-analyses found proficiency doesn't moderate it. Either the mechanism
  is wrong or the effect is partly artifact.
- **Debiasing durability beyond ~2–3 months, and transfer to real high-stakes decisions:** one field
  study (Sellier 2019), no independent replication that I found.
- **Evidentials-for-English proposals** (credence tags, decibels, intelligence-community "Words of
  Estimative Probability") are not my slice; see the hedging report. In this slice, the takeaway is
  that obligatory marking (Láadan, Ithkuil) has never had enough speakers to test, and optional
  marking (Lojban) behaves like English hedging: people use it when they already care.
