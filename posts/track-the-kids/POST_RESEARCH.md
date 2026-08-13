# Research: does tracking actually work?

Compiled 2026-08-12 by Claude from three parallel research passes (meta-analyses; causal/econ
studies; acceleration + detracking). All URLs verified live at compile time unless flagged. Effect
sizes in SD units (Cohen's d / Hedges' g) unless noted.

## TLDR — the shape of the evidence

The literature is much more coherent than the "tracking is contested" reputation suggests, but the
answer depends on _which_ tracking:

1. **Between-class tracking with an unchanged curriculum ≈ zero.** Every major synthesis agrees:
   Slavin 0.00/−0.02, Kulik & Kulik +0.03 (n.s.), Steenbergen-Hu et al. 0.04–0.06 (n.s.), Terrin &
   Triventi −0.06 (n.s.). Sorting kids into "high 3rd grade" and "low 3rd grade" and teaching the
   same material at both does nothing.
2. **Grouping that changes what's taught works, and works more the more it changes.** Within-class
   grouping +0.17 to +0.34; cross-grade/Joplin grouping +0.26 to +0.45; special gifted classes +0.37
   to +0.41; **acceleration +0.70 to +0.88 vs. same-age equally-able peers** (and accelerants match
   the older kids they join, g ≈ 0.0–0.09 vs. older peers). The Kuliks' thesis: effects scale with
   curricular adjustment.
3. **The causal/econ literature backs the mechanism.** The one clean RCT of tracking itself (Kenya,
   Duflo–Dupas–Kremer 2011) found all quantiles gained, including the bottom half, and the gains
   persisted after the program ended; the mechanism analysis says the win comes from teachers being
   able to teach at the class's level. US quasi-experimental work finds no causal evidence low-track
   kids get hurt.
4. **Low achievers are not harmed on the outcomes people worry about.** Achievement effects
   ~flat-to-positive for low groups in the meta-analyses and RCT; self-esteem for low-track students
   is slightly _up_ (+0.19), and slightly down for high-track students (−0.15) — the opposite of the
   Oakes-era harm story.
5. **The real counterevidence is specific:** (a) European-style sorting into separate _school types_
   at age 10 raises inequality and probably lowers means — a different policy sharing the word
   "tracking"; (b) the robust big-fish-little-pond effect: selective grouping lowers academic
   _self-concept_ (β ≈ −0.2 to −0.3) even while raising achievement; (c) one good RCT
   (Dee–Huffaker 2024) shows detracking _with heavy instructional support_ can also work —
   instructional targeting, not the grouping label, is what matters.
6. **Detracking's flagship real-world test failed.** SFUSD delayed algebra for everyone in 2014: no
   achievement gains, AP calc participation fell, racial gaps in advanced course-taking _grew_,
   families bought workarounds that re-created the tracks, and the city reversed it (82% ballot
   support for reinstatement).
7. **For the "let precocious kids move faster" claim specifically:** acceleration is the
   best-supported intervention in gifted education. SMPY matched-cohort data: grade-skippers were
   ~2x as likely to earn STEM PhDs than matched non-skipped peers. Social-emotional effects of
   acceleration: no detected harm, modest positive.

Caveat that cuts both ways: the classic grouping effect-size base is primary research from before
~1994, and a 2026 umbrella review rated none of the grouping meta-analyses as meeting modern quality
bars. The post-2000 causal studies are the stronger evidence, and they mostly point the same
direction.

## 1. The meta-analyses

### Slavin (1987, 1990) — the famous nulls

- Slavin, R. E. (1987). "Ability Grouping and Student Achievement in Elementary Schools: A
  Best-Evidence Synthesis." _Review of Educational Research_ 57(3): 293–336.
  <https://eric.ed.gov/?id=EJ366906>
  - Between-class ability grouping (self-contained grouped classes): **median ES = 0.00**.
  - But: **Joplin plan (cross-grade grouping for reading): +0.45**, the largest effect he found.
    **Within-class grouping in math: +0.34.**
  - His pattern: grouping works when it's per-subject, based on actual skill (not IQ), frequently
    reassessed, and teachers actually change pace/materials. It fails as a global inflexible label
    with the same curriculum.
- Slavin, R. E. (1990). "Achievement Effects of Ability Grouping in Secondary Schools." _RER_ 60(3):
  471–499. Full text: <https://files.eric.ed.gov/fulltext/ED322565.pdf>
  - 29 studies (6 randomized). **Overall median ES = −0.02.** By level: high +0.01, average −0.08,
    low −0.02.
  - Key passage: gifted programs show few effects "**unless the programs include acceleration**."
    Cites Mikkelson (1962): random assignment; enriched 7th-grade grouping → nothing; accelerating
    8th graders into algebra → substantially better on algebra, no worse on 8th-grade math.
  - Scope caveat: Slavin **deliberately excluded** gifted/accelerated program studies — the root of
    his dispute with the Kuliks.

### Kulik & Kulik (1982, 1992) — effects scale with curricular adjustment

- Kulik & Kulik (1982). _AERJ_ 19(3): 415–428. <https://eric.ed.gov/?id=EJ275516> — 52 secondary
  studies, average ES **+0.10**, driven by honors/enriched classes for high-ability students.
- Kulik & Kulik (1992). "Meta-analytic Findings on Grouping Programs." _Gifted Child Quarterly_
  36(2): 73–77. Full PDF:
  <https://newhorizons.ca/wp-content/uploads/2017/10/Meta-analytic-findings-on-grouping-programs-Kulik-Kulik-Gifted-Child-Quarterly-Spring-1992-.pdf>

| Program type                                             | k   | ES                                                     |
| -------------------------------------------------------- | --- | ------------------------------------------------------ |
| Multilevel (XYZ) between-class tracking, same curriculum | 51  | **+0.03** (n.s.) — high +0.10, middle −0.02, low −0.01 |
| Cross-grade grouping (Joplin)                            | 14  | **+0.30**                                              |
| Within-class grouping                                    | 11  | **+0.25** (high +0.30, middle +0.18, low +0.16)        |
| Enriched classes for gifted                              | 25  | **+0.41** (22/25 positive)                             |
| Accelerated classes vs. same-age equally-able controls   | 11  | **+0.87** (11/11 positive)                             |
| Accelerated classes vs. older non-accelerated peers      | 12  | **−0.02** (skippers keep pace)                         |

- Self-esteem (13 studies): overall −0.03; **low-ability +0.19, high-ability −0.15** — grouping
  slightly _raised_ low-track self-esteem.
- The Slavin–Kulik "dispute" is mostly scope: on plain XYZ tracking they agree (~0). Slavin excluded
  gifted/acceleration studies (selection-bias worries); the Kuliks included them and found the
  biggest effects exactly there. Slavin himself conceded "true acceleration" is justified.

### Steenbergen-Hu, Makel & Olszewski-Kubilius (2016) — the best single citation

- "What One Hundred Years of Research Says About the Effects of Ability Grouping and Acceleration on
  K–12 Students' Academic Achievement." _RER_ 86(4): 849–899. Second-order meta-analysis of 13
  grouping + 6 acceleration meta-analyses. ERIC: <https://eric.ed.gov/?id=EJ1121483> — full PDF
  mirror:
  <https://static1.squarespace.com/static/53ecd9dde4b0d7bcbf3158b7/t/59230999d482e90fb1a0cf67/1495468442931/Full+Study+-+100+Years+of+Research+Grouping+and+Acceleration.pdf>
  - Between-class grouping **g = 0.04–0.06** (n.s.) · within-class **0.19–0.30** · cross-grade
    **0.26** · special gifted grouping **0.37** · acceleration vs. same-age peers **0.70** (vs.
    older peers 0.09 n.s.; aggregated across forms 0.42).
  - **Effects did not vary across high/medium/low-ability students** — no detected harm to low
    achievers.
  - Self-stated limits: the 13 grouping meta-analyses only cover primary research through ~1994;
    authors call for a new first-order meta-analysis.

### Modern / counterweight meta-analyses

- **Lou et al. (1996).** _RER_ 66(4): 423–458. Small-group learning vs. none: +0.17; homogeneous
  beat heterogeneous small groups by +0.12.
- **Terrin & Triventi (2023).** "The Effect of School Tracking on Student Achievement and
  Inequality: A Meta-Analysis." _RER_ 93(2): 236–274. <https://eric.ed.gov/?id=EJ1369696> — 53
  publications (2000–2021), mostly European **between-school** tracking, econometric designs.
  Efficiency (mean achievement): **−0.063 (n.s.)**; inequality: **+0.117 (sig.)**. Best modern
  evidence against — but it's about sorting kids into separate school types, not within-school
  grouping.
- **Ferrándiz et al. (2026).** Umbrella review of 17 meta-analyses, _Frontiers in Education_
  11:1925181.
  <https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2026.1925181/pdf> —
  acceleration consistently positive; **no ability-grouping meta-analysis met their quality bar**
  (the grouping evidence base is old).
- **EEF "Setting and streaming" toolkit** (UK practitioner review): headline ~zero/slightly
  negative, negative for low attainers. **Not verified** (site 403s bots) — check in a browser
  before citing.

## 2. Causal / econ studies

### Duflo, Dupas & Kremer (2011) — the RCT

- "Peer Effects, Teacher Incentives, and the Impact of Tracking: Evidence from a Randomized
  Evaluation in Kenya." _AER_ 101(5): 1739–74.
  <https://www.aeaweb.org/articles?id=10.1257/aer.101.5.1739> — free WP:
  <https://www.nber.org/papers/w14475>
- 121 Kenyan primary schools split grade 1 into two sections; 60 randomly assigned to track by
  initial achievement, 61 to random assignment. The only clean randomization of tracking itself.
- **+0.14 SD overall after 18 months (+0.18 with controls); top half +0.19, bottom half +0.16 — all
  quantiles gained.** Still **+0.16 SD one year after the program ended.**
- Mechanism: RD at the median shows the marginal kid did equally well in the low section (weak
  peers, targeted teaching) as in the high section (strong peers, mistargeted teaching) — the gain
  comes from **teachers teaching at the class's level**, not peers.
- Caveats: Kenyan first graders; teachers there face convex teach-to-the-top incentives. Reanalysis:
  **Cummins (2017)**, _EconEdRev_ 56: 40–51
  <https://www.josephrcummins.com/uploads/2/3/8/2/23821874/cummins_2017_tracking_kenya.pdf> — the
  _top_ of the low track under regular (low-effort) civil-service teachers ended 0.35–0.45 SD below
  comparison; "Pareto-improvements from tracking are possible, but not guaranteed."

### Card & Giuliano (2016) — Broward County

- "Can Tracking Raise the Test Scores of High-Ability Minority Students?" _AER_ 106(10): 2783–2816.
  <https://davidcard.berkeley.edu/papers/card-giuliano-tracking.pdf>
- District rule: any school with ≥1 gifted 4th grader creates a separate gifted/high-achiever class;
  empty seats filled with non-gifted high scorers. RD + across-cohort designs.
- **~0.5 SD gains for Black and Hispanic high achievers** (comparable to best-practice charters),
  persisting to 6th grade; ~0 for white students; **no spillover harm to kids left in regular
  classes**; essentially zero cost (a reshuffle).
- Companion (2014, NBER w20453): _marginally gifted_ IQ-cutoff kids gained little — gains come from
  kids selected on achievement, not IQ.

### Cohodes (2020) — Boston AWC; long-run outcomes

- "The Long-Run Impacts of Specialized Programming for High-Achieving Students." _AEJ: Policy_
  12(1): 127–66. <https://www.aeaweb.org/articles?id=10.1257/pol.20180315>
- Fuzzy RD on accelerated classrooms, grades 4–6. Test-score impacts positive but imprecise;
  **raises high school graduation and college enrollment, driven by Black and Latino students**;
  mechanism looks like staying on advanced course pathways, not peers.

### The main negative US result

- **Bui, Craig & Imberman (2014).** "Is Gifted Education a Bright Idea?" _AEJ: Policy_ 6(3): 30–62.
  <https://www.aeaweb.org/articles?id=10.1257/pol.6.3.30> — Houston. RD at the GT cutoff + magnet
  lottery: **~zero achievement gains for marginal admits** despite peers ~1 SD stronger (lottery
  winners better only in science). Interpreted via an invidious-comparison (small-fish-big-pond)
  model. Cuts against Card–Giuliano/Cohodes; note it's marginal admits only.

### Does the low track get hurt? (US quasi-experimental)

- **Betts & Shkolnik (2000).** _EconEdRev_ 19(1): 1–15.
  <https://econweb.ucsd.edu/~jbetts/Pub/A23%20Betts%20Shkolnik%20EER%202000%20Ability%20Grouping.pdf>
  — comparing like-with-like across grouping vs. non-grouping schools: "little or no differential
  effects of grouping for high-achieving, average, or low-achieving students." Bonus finding:
  "non-grouping" schools group informally anyway and allocate resources almost identically.
- **Figlio & Page (2002).** _J. Urban Econ_ 51(3): 497–514. WP: <https://www.nber.org/papers/w8055>
  — IV design; **no evidence tracking harms low-ability students**; may help them (tracking programs
  attract affluent families into the school). Explicitly contra the older OLS result (Argys, Rees &
  Brewer 1996) that detracking helps the bottom at the top's expense.

### Between-school tracking (the European caveat)

- **Hanushek & Woessmann (2006).** "Does Educational Tracking Affect Performance and Inequality?"
  _Economic Journal_ 116(510): C63–C76.
  <https://hanushek.stanford.edu/sites/default/files/publications/Hanushek%2BWoessmann%202006%20EJ%20116(510).pdf>
  - DiD across countries (tracked-at-10 systems like Germany vs. comprehensive systems): early
    tracking **significantly increases inequality** (positive in 7/8 test pairs) and tends to
    **lower** mean performance (pooled −0.18, marginal); bottom percentiles lose most.
  - Caveats: 18–26 countries, non-independent test pairs, authors call it "preliminary"; and the
    object is sorting 10-year-olds into separate _school types_ — not within-school grouping.
- Within-Germany follow-ups agree: **Matthewes (2021)**, _EJ_ 131(637): 1269–1307 (later tracking
  helps low achievers at no cost to high); **Piopiunik (2014)**, _EconEdRev_ 42: 12–33 (moving
  tracking earlier in Bavaria lowered scores in both school types).

## 3. Acceleration (the "let precocious 3rd graders do algebra" evidence)

- **Steenbergen-Hu & Moon (2011).** _GCQ_ 55(1): 39–53 — 38 studies: academic effects positive;
  social-emotional: **no significant effect either way** ("at the very least, not harmful").
- **Rogers's synthesis** (in _A Nation Empowered_, 2015, ch. 2:
  <https://ncrge.uconn.edu/wp-content/uploads/sites/982/2022/12/ch2-A-Nation-Empowered-Vol2-2.pdf>):
  academic ES ~**+0.5** for both subject- and grade-based acceleration (elementary grade-based
  +0.67); socialization +0.16/+0.23; psychological adjustment +0.24/+0.34. Kulik & Kulik (1984):
  **0.88** vs. same-age peers.
- **SMPY — Park, Lubinski & Benbow (2013).** "When Less Is More: Effects of Grade Skipping on Adult
  STEM Productivity Among Mathematically Precocious Adolescents." _J. Educational Psychology_
  105(1): 176–198. <https://eric.ed.gov/?id=EJ1006602> — 40-year longitudinal, top-1% math kids, 363
  grade-skippers vs. 657 matched controls: skippers **~1.6x as likely to earn any doctorate, ~2x as
  likely to earn a STEM PhD**, more/earlier publications and patents. Caveats: matching on
  observables; top-1% sample; effects weaker for women.
- **The advocacy reports** (cite the numbers above, not the reports): _A Nation Deceived_ (2004)
  <https://www.accelerationinstitute.org/nation_deceived/> and _A Nation Empowered_ (2015).
- The one negative pocket: **early school entrance** — one meta: psychological −0.24; Gagné &
  Gagnier (2004): 37% of early entrants less well-adjusted.

## 4. Non-cognitive outcomes — the honest concessions

- **Big-fish-little-pond effect (robust, adverse, about self-concept not achievement):**
  - Marsh & Hau (2003). _American Psychologist_ 58(5): 364–376.
    <https://pubmed.ncbi.nlm.nih.gov/12971085/> — PISA 2000, N = 103,558, 26 countries:
    selective-school effect on academic self-concept negative in **all 26 countries**, avg β =
    −0.20.
  - Fang et al. (2018). _Frontiers in Psychology_ 9:1569.
    <https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2018.01569/full> —
    meta-analysis, N = 1.28M: **β = −0.28**, stronger in high school.
  - Counter-framing: Dai & Rinn (2008), _Ed Psych Review_ 20: 283–317 — practical significance
    overstated; a self-concept drop toward accurate self-appraisal may not be a harm. And note Kulik
    1992: tracking _raised_ low-track self-esteem (+0.19).
- **Boredom/engagement: gap.** No strong quantified source found for the "top kids are bored" claim
  specifically. Kulik & Kulik (1984) attitude ESs ~0. If the post needs a boredom citation, a
  separate pass is needed (candidate: Preckel, Götz & Frenzel 2010 on boredom in gifted classes —
  unverified).

## 5. Detracking natural experiments

### SFUSD (2014): delay algebra for everyone → failed, reversed

- District/advocate claim (Boaler et al., Hechinger 2018): algebra repeat rate 40% → 8%.
- **Loveless (2022), Education Next**
  <https://www.educationnext.org/san-franciscos-detracking-experiment/>: the district's own
  records-act-obtained documents show the drop came from **changing the placement/exam policy**, not
  learning; "advanced math" gains vanish once you exclude the compression course **UC refused to
  count**; 2015–19 SBAC flat while Black-White gap widened 15 pts (vs. 11 statewide) and
  Hispanic-White 31 pts (vs. 5).
- **Huffaker, Novicoff & Dee (2025), Educational Researcher** 54(2): 95–104
  <https://tom-dee.github.io/files/ER_2025.pdf> (peer-reviewed, ~4,000 students/cohort × 6 cohorts):
  AP math participation fell 5 pp (−15%), AP Calculus −21%; families re-created tracking via summer
  geometry/doubling up; **White-Black and White-Hispanic AP-math gaps _grew_ by 5 and 7 pp** — the
  equity goal failed on its own terms.
- Reversal: Feb 2024 pilot; March 2024 Prop G advisory passed **~82%**; March 2026 8th-grade algebra
  restored district-wide. Pilot: 9% of elective-track students retook Algebra 1 vs. 19%
  auto-enrolled. <https://missionlocal.org/2026/03/san-francisco-algebra-middle-school/>

### Algebra-for-all universal acceleration → hurt the marginal kids

- **Clotfelter, Ladd & Vigdor (2015).** _J. Human Resources_ 50(1): 159–188. WP:
  <https://www.nber.org/papers/w18161> — Charlotte-Mecklenburg pushed moderate performers into
  8th-grade algebra (50%→85%): accelerated students scored **significantly lower** on Algebra I EOC
  and were less likely to pass Geometry/Algebra II on schedule. District reverted within five years.
- **Domina, Penner, Penner & Conley (2014).** _Teachers College Record_ 116(8).
  <https://doi.org/10.1177/016146811411600801> — California districts that complied more with
  8th-grade-algebra-for-all saw **lower** 10th-grade math scores.

### The pro-detracking evidence (report honestly)

- **Burris, Heubert & Levin (2006).** _AERJ_ 43(1): 105–136.
  <https://campussuite-storage.s3.amazonaws.com/prod/1558748/bd01c7ae-765f-11e9-9402-0a56f8be964e/1971761/5a9ad626-c369-11e9-8811-0a9af7666a7a/file/1_Accelerating%20Mathmatics%20Achievement.pdf>
  — Rockville Centre, NY: minority students passing Regents Sequential Math I before HS **tripled
  (23%→75%)**; high achievers unhurt. **Crucial detail: they detracked by giving everyone the
  _accelerated_ curriculum with support classes — leveling up, the opposite of SFUSD's
  delay-for-all.** Caveats: author was a principal in the district and an open advocate; one
  affluent suburb; no external comparison group.
- **Dee & Huffaker (2024).** "Accelerating Opportunity: The Effects of Instructionally Supported
  Detracking." EdWorkingPaper 24-986.
  <https://tom-dee.github.io/files/Dee_Huffaker_A1_Initiative.pdf> — **random assignment**: 9th
  graders well below grade level put straight into Algebra I _with teacher training and
  instructional supports_: grade-11 math **+0.2 SD**, no harm to classroom peers. Genuine
  experimental evidence that supported detracking can work. Its own lit review concedes the causal
  literature finds "homogeneous student grouping carries benefits across the achievement
  distribution" (citing DDK, Card-Giuliano, Cohodes, Figlio-Page) with instructional targeting as
  the dominant mechanism.
- Correlational counterpoint to Burris: Loveless's Massachusetts study — schools with more math
  levels had more advanced-scoring students. Dueling-views coverage:
  <https://www.edweek.org/education/researchers-offer-dueling-views-on-tracking/2009/12>

## 6. Strongest evidence AGAINST tracking (steelman checklist)

1. Terrin & Triventi (2023): modern meta-analysis, mean effect ~0 and inequality up — though mostly
   between-school European tracking.
2. Hanushek & Woessmann (2006) + Matthewes (2021) + Piopiunik (2014): early between-school tracking
   raises inequality, probably lowers means.
3. Bui, Craig & Imberman (2014): zero gains for marginal gifted admits in Houston.
4. Cummins (2017): the Kenya "everyone wins" result breaks at the top of the low track under
   low-effort teachers.
5. BFLPE (Marsh; Fang et al. 2018): selective grouping reliably dents academic self-concept, β ≈
   −0.2 to −0.3.
6. Dee & Huffaker (2024): supported detracking produced +0.2 SD for low performers — the grouping
   label isn't the active ingredient, instruction matched to level is.
7. Evidence-quality caveat: the classic grouping ES base predates ~1994 and no grouping
   meta-analysis met the 2026 umbrella review's quality bar.

## Suggested load-bearing citations if the post only gets a few

- **Steenbergen-Hu, Makel & Olszewski-Kubilius (2016)** — the one-stop meta-analytic summary
  (between-class ~0, everything with curricular differentiation positive, acceleration +0.7).
- **Duflo, Dupas & Kremer (2011)** — the RCT; all quantiles gained; mechanism = teaching at the
  kids' level.
- **Card & Giuliano (2016)** — 0.5 SD for minority high achievers at zero cost, no harm to anyone.
- **Park, Lubinski & Benbow (2013)** — grade-skippers ~2x STEM PhDs.
- **Huffaker, Novicoff & Dee (2025) + Loveless (2022)** — SFUSD detracking failed on its own equity
  goals and was reversed.
