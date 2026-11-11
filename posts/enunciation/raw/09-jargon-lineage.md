# 09: The hacker/nerd-jargon lineage behind rationalist speech, and the science of why groups grow jargon

Scope: (A) where rationalist speech habits come from (Jargon File, TMRC, SF fandom, General
Semantics, Usenet, math/physics/econ/philosophy). (B) why groups grow private vocabularies, and what
absorbing them does and predicts. Rationalist slang itself, trader slang, "ack" and phonetics are
covered by other researchers.

## 1. Most interesting findings

1. **The lineage isn't a metaphor: it runs through the same person.** Eric S. Raymond took over the
   Jargon File in 1990 and edited it into _The New Hacker's Dictionary_ (MIT Press, 1991/1993/1996).
   In 2021 he also wrote the standard genealogy of the rationalist movement, "Rationalism before the
   Sequences", on LessWrong. Yudkowsky replied in 2024: "I endorse this history." Raymond says he
   got General Semantics from Wendell Johnson's _People in Quandaries_, a book his grandfather gave
   him. Yudkowsky, he says, "never read any of what I would consider core texts" and got the ideas
   second-hand. That fits Yudkowsky's own 2008 comment recommending Hayakawa's popularization
   _Language in Thought and Action_ ("An oldie but goodie"), and his reported debt to van Vogt's
   General-Semantics novel _The World of Null-A_ (1948). Sources:
   [Raymond 2021](https://www.greaterwrong.com/posts/qc7P2NwfxQMC3hdgm/);
   [Yudkowsky comment, 2008](https://www.greaterwrong.com/posts/RiQYixgCdvd8eWsjg/recommended-rationalist-reading);
   [Jargon File revision history](http://www.catb.org/jargon/html/revision-history.html).

2. **The Jargon File explains anthropomorphic tech-talk as "a mechanistic view of human behavior".**
   This is the philosophical root of rationalist phrasings like "my brain wants", "I don't have the
   cycles" and "my System 1 is screaming". The File says: "hackers who anthropomorphize are
   expressing not a vitalistic view of program behavior but a mechanistic view of human behavior… If
   consciousness is mechanical, it is neither more or less absurd to say that 'The program wants to
   go into an infinite loop' than it is to say that 'I want to go eat some chocolate'". It
   explicitly cites Dennett's intentional stance. It also gives a second, quietly therapeutic
   reading: "by displacing from 'I got confused' to 'It got confused', the programmer is not
   avoiding responsibility, but rather getting some analytical distance". That is very close to
   rationalist "my model of X says…" talk.
   [Jargon File: Anthropomorphization](http://www.catb.org/jargon/html/anthropomorphization.html).

3. **A sociolinguist independently recorded the "hacker speech style" in teenage nerds, including
   pronunciation.** The Jargon File claims (ESR-era text, ~1990s): "Hackish speech generally
   features extremely precise diction, careful word choice, a relatively large working vocabulary,
   and relatively little use of contractions or street slang… One should use just enough jargon to
   communicate precisely and identify oneself as a member of the culture; overuse of jargon… is
   considered tacky and the mark of a loser."
   ([Speech Style](http://www.catb.org/jargon/html/speech-style.html)).
   - Mary Bucholtz's fieldwork at a California high school
     ([Bucholtz 2001, _J. Linguistic Anthropology_ 11(1):84–100](https://escholarship.org/uc/item/0663j2rg))
     found the same register. She calls it "superstandard English": "lexical formality, carefully
     articulated phonological forms, and prescriptively standard grammar".
   - Concretely, nerds said "have to" not "hafta" and "going to" not "gonna", resisted
     consonant-cluster simplification, and used **spelling pronunciations of words learned from
     reading** (e.g. [folk] with an /l/).
   - Her summary: "The iconicity between resisting phonological pressure and resisting peer
     pressure". Careful pronunciation works as an identity marker. This connects to Robbie's
     pronunciation drift.

4. **People absorb a community's language for about the first third of their tenure, then freeze,
   and the freeze predicts when they leave.** Danescu-Niculescu-Mizil, West, Jurafsky, Leskovec &
   Potts
   ([WWW 2013](https://cs.cornell.edu/~cristian/Linguistic_change_files/linguistic_change_lifecycle.pdf))
   studied BeerAdvocate (1.59M posts, 33k users) and RateBeer (2.92M posts, 29k users), 2001–2011.
   - Users grow more receptive to community norms "up to about one third of her eventual lifespan"
     ("linguistic adolescence"). After that they stop tracking changes, so "at the moment they
     depart from the community most users are linguistically conservative". This holds for short-
     and long-tenure users alike.
   - Example: BeerAdvocate's convention for describing smell moved from "Aroma" to "S" around 2007.
     Users who joined in 2003 kept "Aroma" and even used it more. 2005 joiners drove the switch.
   - Linguistic features from a user's first few reviews improved departure prediction by 2–12
     points of F1 (4–40% relative) over activity-only baselines.

5. **Corporate version: email "fit" predicts promotion and firing, and the strongest alignment
   signal was swearing, not technical jargon.** Srivastava, Goldberg, Manian & Potts
   ([Management Science 2018](https://escholarship.org/uc/item/8qn146c5)) analysed 10.24M internal
   emails from 601 employees at a mid-sized tech firm. They measured fit as similarity over 64 LIWC
   style categories.
   - High-fit rank-and-file employees had a 48% cumulative chance of promotion to manager by year 3,
     1.5× the median-fit rate and 2.7× the low-fit rate.
   - Low-fit employees had a 46% chance of involuntary exit by year 3, 4× the median.
   - Speed of adaptation mattered on its own. Adapting by +1/3 SD per month in the first six months
     (about the 90th percentile) cut the hazard of being fired by about 30%, but did not change
     voluntary exit.
   - A _drop_ in fit after someone had enculturated foreshadowed them quitting.
   - Backward selection found "Swear Words" was the largest driver of fit, followed by "Religion".
     In other words, enculturation shows up in style and register, not only vocabulary.

6. **Linguistic accommodation tracks power, and the would-be-powerful accommodate most.** "Echoes of
   power" (Danescu-Niculescu-Mizil, Lee, Pang & Kleinberg,
   [WWW 2012](https://arxiv.org/abs/1112.3670)) studied 240,436 Wikipedia talk-page exchanges and
   50,389 Supreme Court oral-argument exchanges, measuring function-word echoing.
   - People coordinate more toward admins and Justices.
   - Lawyers coordinate more toward Justices who will vote _against_ them.
   - Future admins were already more accommodating _before_ promotion, and their accommodation fell
     once they gained power. Failed candidates accommodated _more_ after failing.
   - Female lawyers coordinated more than male lawyers.
   - So a newcomer soaking up group idiom is showing textbook low-power, high-ambition behavior.

7. **Low status causes more jargon, but the effect is modest.** Brown, Anicich & Galinsky
   ([OBHDP 2020, 161:274–290](https://www.gwern.net/doc/psychology/writing/2020-brown.pdf)) ran nine
   studies.
   - In 64,956 dissertation and thesis titles, lower-ranked schools used more complex language and
     more acronyms.
   - In a start-up pitch experiment (N=556), 40.8% of low-status participants chose the jargon-heavy
     pitch, versus 32.1% at same status and 29.2% at high status (χ², p=.05). A replication (N=378)
     gave 37.2% vs 26.8% (p=.03). A live-chat version also found the effect.
   - The mechanism is concern with audience evaluation rather than clarity.
   - Caveat: their "jargon" means buzzword/readability/acronym/legalese (e.g. "leverage the
     anticipated disruption… disintermediating"), not technical slang. The Jargon File's "overuse…
     the mark of a loser" norm is a folk version of the same finding.

8. **Jargon pushes outsiders away even when you define it.** Shulman, Dixon, Bullock & Colón Amill
   ([J. Lang. & Soc. Psych. 2020](https://news.osu.edu/the-use-of-jargon-kills-peoples-interest-in-science-politics/)),
   N=650, used texts on self-driving cars, surgical robots and 3D bioprinting.
   - Jargon versions lowered processing fluency, interest in science, and self-rated science
     ability.
   - Hover-over definitions did nothing. Shulman: "The use of difficult, specialized words are a
     signal that tells people that they don't belong."
   - Companion paper:
     [Bullock et al. 2019, _Public Understanding of Science_](https://comm.osu.edu/sites/comm.osu.edu/files/PUS%202019-%20Bullock%20et%20al..pdf)
     found jargon reduced persuasion and support for the technologies.
   - Rationalist self-critique says the same: Jeff Kaufman's
     ["Antijargon Project" (2013)](https://www.greaterwrong.com/posts/R6coM4SgNTu5uwHLD/antijargon-project).
     A commenter there adds that "we often judge someone's rationality based on jargon instead of
     the content of their message".

9. **You can watch jargon being born in about 20 minutes.** In Clark & Wilkes-Gibbs's tangram task
   ([Cognition 1986](https://web.stanford.edu/~clark/1980s/Clark.Wilkes-Gibbs.86.pdf)), directors
   used 41 words per figure on trial 1 and 8 by trial 6, F(1,35)=44.3. Self-repairs fell from 85
   to 7. The descriptions moved from "looks like an angel flying away or something. It's got two
   arms" to "Sixth one's the angel."
   - The original had only 8 pairs. Hawkins, Frank & Goodman
     ([Cognitive Science 2020](https://ar5iv.labs.arxiv.org/html/1912.07199)) replicated it with 83
     pairs in text chat. Each pair converged on its own stable label, and the words that best
     distinguished a figure early on were the ones that survived.
   - Garrod & Doherty ([Cognition 1994](<https://doi.org/10.1016/0010-0277(94)90048-5>)) found that
     people who rotate partners within a community converge more strongly than isolated pairs.
     Details are from secondary sources.

10. **Network shape decides whether one convention wins, and about 25% committed members can flip
    it.** Centola & Baronchelli ([PNAS 2015](https://arxiv.org/abs/1502.06910)) ran a naming game
    for a pictured face, with 24–96 players.
    - Homogeneously mixing populations converged on one name in every trial.
    - Spatial and random-graph populations broke into competing local conventions.
    - Centola, Becker, Brackbill & Baronchelli
      ([Science 2018](https://www.sciencedaily.com/releases/2018/06/180607141009.htm)): in 10 groups
      of 20, committed minorities below about 25% failed and those at about 25% tipped the whole
      group. Once, a single extra person made the difference.
    - Caveat: the stakes were trivial ($0.10 per coordination), and the authors say the threshold
      depends on context.
    - Bay Area rationalists are dense, highly mixed group houses plus one forum, which is the
      configuration that converges fastest.

11. **Learning named reasoning concepts does transfer, which supports the rationalist "words as
    tools" bet, with caveats.**
    - Fong, Krantz & Nisbett
      ([Cognitive Psychology 1986](https://deepblue.lib.umich.edu/items/9850801d-32d8-4756-a6ce-5479fdadc4e5)):
      brief lab training on the law of large numbers improved statistical reasoning about everyday
      problems. Their Experiment 4 found benefits "even when subjects are tested completely outside
      of the context of training".
    - Larrick, Morgan & Nisbett
      ([Psych. Science 1990](https://scholars.duke.edu/publication/893241)): training in
      cost-benefit and sunk-cost rules changed reasoning _and self-reported behavior_. A later
      follow-up found mixed effects on actual sunk-cost behavior.
    - Lupyan's label-feedback hypothesis
      ([Frontiers 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3297074)): words act on perception
      on-line, top-down, sharpening category features. The effects vanish under verbal interference,
      so it is a live effect, not a permanent rewiring.
    - The rationalist statement of the theory is Duncan Sabien's
      ["Sapir-Whorf for Rationalists" (2023)](https://www.lesswrong.com/posts/PCrTQDbciG4oLgmQ5/sapir-whorf-for-rationalists):
      "That which is not tracked in language will be lost."

12. **"Win", "lose", "hack", "cruft" and "kludge" come from a 1959 model-railroad club.** The TMRC
    dictionary, originally written in 1959 by Peter Samson
    ([TMRC](https://tmrc.mit.edu/old/dictionary.html)):
    - _hack_: "an article or project without constructive end".
    - _kludge_: "a crock that works".
    - _cruft_: "that rubbish which accumulates around the Clubroom; attacking it with a broom only
      produces more".
    - _lose_: "to not succeed; to not win"; _win_: "opposite of lose"; _winner_: "very rare at
      TMRC".
    - The win/lose binary, which became ITS-hacker "winnage/lossage", makes Yudkowsky's
      "rationalists should win" sound native to this register. The direct inheritance is my
      inference, UNVERIFIED.

13. **The Jargon File gives specific, checkable etymologies for "math-speak":**
    - _for values of_ comes from the 1960s MIT language MAD's `FOR VALUES OF X = 3, 7, 99` loop.
      Hence "π equals 3, for small values of π and large values of 3".
    - _modulo_ = "except for": "I feel fine today modulo a slight headache."
    - _orthogonal_ includes "This may be orthogonal to the discussion, but…".
    - _bandwidth_ in the human sense "began to go mainstream after the Internet population explosion
      of 1993-1994". Merriam-Webster now lists a
      [mental-capacity sense](https://www.merriam-webster.com/dictionary/bandwidth).
    - _cycle_ is "a notional unit of human thought power".
    - _IMHO_ is "from SF fandom via Usenet".
    - _sanity check_ sense 3: "saying 'sanity check' means you are requesting a check of your
      assumptions".
    - Sources: [modulo](http://www.catb.org/jargon/html/M/modulo.html),
      [for values of](http://www.catb.org/jargon/html/F/for-values-of.html),
      [bandwidth](http://www.catb.org/jargon/html/B/bandwidth.html),
      [IMHO](http://www.catb.org/jargon/html/I/IMHO.html),
      [sanity check](http://www.catb.org/jargon/html/S/sanity-check.html).

14. **The mind has always been described with the newest machine; hacker jargon is the computer-era
    layer.** Searle: "In my childhood we were always assured that the brain was a telephone
    switchboard… Sherrington… a telegraph system. Freud often compared the brain to hydraulic and
    electro-magnetic systems. Leibniz compared it to a mill, and I am told some of the ancient
    Greeks thought the brain functions like a catapult."
    ([Searle, "Is the Brain a Digital Computer?", APA Proceedings 1990](https://socphilinfo.github.io/news/2013/10/01/Publications-Classic-Texts-in-PI-Is-the-Brain-a-Digital-Computer.html)).
    - Lakoff & Johnson (1980) list THE MIND IS A MACHINE ("My mind just isn't operating today") as a
      standard ontological metaphor.
    - Hacker jargon sharpened it into a full I/O model of the mind: _swap in/out_, _page out_,
      _brain dump_, _thinko_, _cycles_, _bandwidth_, _ping_. Rationalist "cached thought", "compute"
      and "update" are the next layer.
    - History:
      [Cobb, _The Idea of the Brain_ (2020)](https://www.sciencenews.org/article/idea-brain-book-explores-evolution-neuroscience).

## 2. Read these (ranked)

1. **The Jargon File, Part I chapters 4–7 plus "Anthropomorphization"**: Raymond/Steele et al.,
   v4.4.7 (2003). <http://www.catb.org/jargon/html/construction.html> (use http; https cert is
   broken). About 30 min. The primary source for this whole question, and funnier than you expect.
2. **Eric S. Raymond, "Rationalism before the Sequences"** (LessWrong, 2021).
   <https://www.greaterwrong.com/posts/qc7P2NwfxQMC3hdgm/>. About 20 min plus comments. The Jargon
   File's editor tracing General Semantics, Golden Age SF and Zen into LessWrong. Yudkowsky endorsed
   it in 2024.
3. **Danescu-Niculescu-Mizil et al., "No Country for Old Members"** (WWW 2013).
   <https://cs.cornell.edu/~cristian/Linguistic_change_files/linguistic_change_lifecycle.pdf>. 12
   pp. The cleanest quantitative picture of absorbing, then freezing.
4. **Bucholtz, "The Whiteness of Nerds: Superstandard English and Racial Markedness"** (J. Ling.
   Anthropology, 2001). <https://escholarship.org/uc/item/0663j2rg>. 17 pp. Ethnography of nerd
   register, including pronunciation. Pair it with her "'Why be normal?'" (Language in Society,
   1999), <https://doi.org/10.1017/S0047404599002043>, which treats nerd identity as a _chosen_
   community of practice.
5. **Srivastava, Goldberg, Manian & Potts, "Enculturation Trajectories"** (Management Science,
   2018). <https://escholarship.org/uc/item/8qn146c5>. About 30 pp. Enculturation measured from 10M
   emails, with real career outcomes.
6. **Danescu-Niculescu-Mizil et al., "Echoes of Power"** (WWW 2012).
   <https://arxiv.org/abs/1112.3670>. 10 pp. Accommodation as a power readout. The admin-promotion
   natural experiment is the best part.
7. **Clark & Wilkes-Gibbs, "Referring as a Collaborative Process"** (Cognition, 1986).
   <https://web.stanford.edu/~clark/1980s/Clark.Wilkes-Gibbs.86.pdf>. 39 pp; read the transcripts.
   Then skim Hawkins et al. 2020, <https://arxiv.org/abs/1912.07199>, for the scaled replication.
8. **Brown, Anicich & Galinsky, "Compensatory Conspicuous Communication"** (OBHDP, 2020).
   <https://www.gwern.net/doc/psychology/writing/2020-brown.pdf>. 17 pp. Jargon as status
   compensation. Check the modest effect sizes yourself.
9. **Duncan Sabien, "Sapir-Whorf for Rationalists"** (LessWrong, 2023)
   <https://www.lesswrong.com/posts/PCrTQDbciG4oLgmQ5/sapir-whorf-for-rationalists>, plus **Jeff
   Kaufman, "Antijargon Project"** (2013)
   <https://www.greaterwrong.com/posts/R6coM4SgNTu5uwHLD/antijargon-project>. 15 min each. The
   community's own pro- and anti-jargon cases.
10. **Halliday, "Anti-Languages"** (American Anthropologist, 1976).
    <https://doi.org/10.1525/aa.1976.78.3.02a00050>. 15 pp. The theory that a group's relexicalized
    vocabulary is "generated by" its counter-society. A useful lens for which rationalist words are
    re-lexicalizations of ordinary ones.
11. **TMRC "Abridged Dictionary of the TMRC Language"** (from Samson, 1959).
    <https://tmrc.mit.edu/old/dictionary.html>. 5 min. The fossil layer.
12. **Centola et al., "Experimental evidence for tipping points in social convention"** (Science,
    2018). <https://doi.org/10.1126/science.aas8827>. 4 pp. Read it next to the critique that the
    task is trivial.

## 3. Details

### 3a. Lineage table

| Term / habit                                                                  | Earliest known source                                                                          | Route into rationalist speech                                                                                                                            |
| ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hack, win/lose, cruft, kludge, foo, mung                                      | TMRC dictionary, 1959 (Samson)                                                                 | MIT AI Lab/ITS → Jargon File 1975+ → Usenet/Unix → tech → rationalists ("rationalists should win", 2008, is my inference)                                |
| grok                                                                          | Heinlein, _Stranger in a Strange Land_ (1961)                                                  | SF fandom → Jargon File ("common"; "to say you 'grok' LISP is to claim… it has transformed your view") → tech/rationalist                                |
| mundane (non-fan)                                                             | SF fandom (date UNVERIFIED)                                                                    | Jargon File sense 2: "A person who is not in the computer industry"                                                                                      |
| IMHO                                                                          | SF fandom                                                                                      | → Usenet → mainstream (Jargon File)                                                                                                                      |
| TANSTAAFL                                                                     | Heinlein, _Moon Is a Harsh Mistress_ (1966); TINSTAAFL to 1952 per File                        | hackers ("high concentration of science-fiction fans and political libertarians") → libertarian/rationalist                                              |
| filk                                                                          | SF fandom typo for "folk"                                                                      | computer filks (Jargon File); rationalist Secular Solstice songs are a plausible descendant (my inference)                                               |
| modulo, epsilon, orthogonal, nontrivial, canonical, N, "interesting" (= hard) | mathematics                                                                                    | MIT/Jargon File → tech → rationalist                                                                                                                     |
| for values of                                                                 | MAD language `FOR VALUES OF` (1960s MIT)                                                       | MIT jargon                                                                                                                                               |
| -P questions ("Foodp?")                                                       | LISP predicate naming                                                                          | only "where LISPers flourish"; Gosper's "Split-p soup?"                                                                                                  |
| bandwidth, cycles, swap in/out, page out, brain dump, thinko                  | computing techspeak                                                                            | Jargon File "human" senses → corporate ("bandwidth" mainstream after 1993–94) → rationalist "compute", "cached thought"                                  |
| ping                                                                          | submariners' sonar → ICMP                                                                      | Jargon File sense 3 "to get the attention of" → Slack-era office speech                                                                                  |
| sanity check, handwave, bogus, random                                         | programming / magicians' gesture / Princeton late-1960s ("bogus")                              | Jargon File → tech → rationalist ("handwavy")                                                                                                            |
| signal-to-noise ratio                                                         | analog electronics                                                                             | Usenet flame wars → general                                                                                                                              |
| YMMV, IANAL, Ob-, FAQ, flame, troll                                           | Usenet 1980s–90s                                                                               | everywhere                                                                                                                                               |
| mu ("unask the question")                                                     | Zen via Hofstadter (_GEB_, 1979)                                                               | Jargon File → LessWrong                                                                                                                                  |
| cargo cult                                                                    | Feynman's 1974 Caltech talk                                                                    | Jargon File "cargo cult programming" → rationalist "cargo-culting"                                                                                       |
| "map is not the territory"                                                    | Korzybski (1931 lecture, _Science and Sanity_ 1933)                                            | Hayakawa (1939/1949), van Vogt's Null-A (1948), Heinlein → Yudkowsky ("Map and Territory" sequence)                                                      |
| intuition pump                                                                | Dennett, 1980 BBS commentary on Searle (per Wikipedia; venue not checked against the original) | analytic philosophy → rationalists                                                                                                                       |
| spherical cow                                                                 | physics joke; earliest print 1970 (A. O. Williams, Brown Univ.)                                | physics → engineering → rationalist                                                                                                                      |
| reflective equilibrium; bite the bullet; pro tanto                            | Rawls 1971 (after Goodman 1955); philosophy                                                    | EA/rationalist via Oxford philosophers (route plausible, not traced)                                                                                     |
| on the margin, revealed preference, Pareto                                    | economics (Marshall; Samuelson 1938)                                                           | econ-blogosphere (Hanson, Cowen) → rationalist (route plausible, not traced)                                                                             |
| verb doubling ("Lose, lose"), "mumble", "_sigh_", nouns-verbed                | pre-1970 TMRC/SPACEWAR/LISP culture per Jargon File                                            | File says verb doubling, overgeneralization, anthropomorphization and spoken inarticulations "have become quite general"; soundalike slang stayed at MIT |

Notable Jargon File passages:

- On literal logic, the origin of nerd pedantry about "or": asked "are you working on finding that
  bug now or leaving it until later?", a hacker answers "Yes!" Hackers also want a word like German
  _doch_ to answer negative questions
  ([Speech Style](http://www.catb.org/jargon/html/speech-style.html)).
- On quotation marks: hackers put punctuation outside quotes because "it is counter-intuitive to
  hackers to mutilate literal strings". The example is a vi tutorial where "dd." would delete two
  lines. The File claims a meta-rule: "precision of expression is more important than conformance to
  traditional rules" ([Writing Style](http://www.catb.org/jargon/html/writing-style.html)).
- On register: hackers "would never… 'productize', 'prioritize', or 'securitize' things… [they] have
  a strong aversion to bureaucratic bafflegab"
  ([Overgeneralization](http://www.catb.org/jargon/html/overgeneralization.html)). This is the
  ancestor of rationalist contempt for corporate-speak, even as hacker words became corporate-speak.
- On origin claims: "many hackish usages have been independently reinvented multiple times… the
  generative processes underlying hackish jargon formation have an internal logic so powerful as to
  create substantial parallelism across separate cultures"
  ([Distinctions](http://www.catb.org/jargon/html/distinctions.html)).
- Comparatives scale: "monstrosity brain-damage screw bug lose misfeature crock kluge hack win
  feature elegance perfection". The File adds that hackers "have even more words for equipment
  failures than Yiddish has for obnoxious people"
  ([Comparatives](http://www.catb.org/jargon/html/comparatives.html)).
- History: begun by Raphael Finkel at Stanford SAIL in 1975 (AIWORD.RF), copied to MIT by Mark
  Crispin in 1976, and expanded with Guy Steele. Excerpts appeared in _CoEvolution Quarterly_
  in 1981. Steele's _The Hacker's Dictionary_ followed in 1983, then a 7-year freeze. Raymond
  revived it in 1990, and the last official version is 4.4.7 (2003). "Steele-1983 was partly a
  monument to what its authors thought was a dying tradition"
  ([Revision History](http://www.catb.org/jargon/html/revision-history.html)).

### 3b. Science of jargon: the remaining pieces

- **Functions.** Three overlapping functions: compression, which the tangram studies show directly;
  identity, which is where communities of practice come in; and gatekeeping and status, covered by
  Brown et al. and Shulman et al.
  - Communities of practice: Lave & Wenger (1991). Eckert & McConnell-Ginet
    ([Annual Review of Anthropology 1992](https://web.stanford.edu/~eckert/csofp.html)) imported the
    idea into sociolinguistics: a group "defined simultaneously by its membership and by the
    practice in which that membership engages".
  - Enregisterment: Agha
    ([Language & Communication 2003](<https://doi.org/10.1016/S0271-5309(03)00012-0>)) describes how
    a set of forms becomes "a socially recognized register". His case is Received Pronunciation.
    "Rationalist-speak" being recognizable as a style, and parodied, is enregisterment in progress.
  - Anti-language: Halliday 1976 calls it relexicalization by a counter-society, partial rather than
    total ("not all words in the language have their equivalents").
- **Loaded language.** Lifton (1961, _Thought Reform and the Psychology of Totalism_, ch. 22): "The
  language of the totalist environment is characterized by the thought-terminating cliché. The most
  far-reaching and complex of human problems are compressed into brief, highly reductive,
  definitive-sounding phrases"
  ([quoted](https://pulledquotes.substack.com/p/robert-jay-lifton-on-the-thought)). Montell's
  _Cultish_ (2021) treats cultishness as a spectrum covering CrossFit, MLMs and start-ups. I found
  **no evidence she discusses rationalists or EA**.
  - Sabien's 2023 post argues the opposite design goal, a vocabulary where "things which are less
    true are less easy to say". Both describe language shaping thought; they disagree on which
    direction it pushes.
- **Curse of knowledge.** Camerer, Loewenstein & Weber
  ([JPE 1989, 97(5):1232–54](https://www.cmu.edu/dietrich/sds/docs/loewenstein/CurseknowledgeEconSet.pdf)):
  better-informed subjects cannot ignore what they know when predicting less-informed people.
  Feedback alone barely helped; market forces cut the bias by about 50%. The coinage is sometimes
  credited to Robin Hogarth, which I could not resolve.
  - Pinker's _The Sense of Style_ (2014) has a chapter applying it to academese.
  - The rationalist in-house version is Yudkowsky's
    ["Expecting Short Inferential Distances" (2007)](https://www.lesswrong.com/posts/HLqWn5LASfhhArZ7w/expecting-short-inferential-distances).
- **Style matching.** Niederhoffer & Pennebaker
  ([JLSP 2002, 21:337–360](https://journals.sagepub.com/doi/10.1177/026192702237953)) found people
  match function-word style turn by turn. The surprise is that matching is **unrelated to rated
  interaction quality**: it shows up as strongly in hostile Watergate-tape conversations as in
  friendly ones (per
  [Discover](https://discovermagazine.com/mind/choose-your-words-wisely-to-win-a-negotiation)). It
  measures engagement, not liking.
  - Ireland et al.
    ([Psych. Science 2011](https://sites.socsci.uci.edu/~lpearl/courses/readings/IrelandEtAl2011_RelationshipPrediction.pdf)):
    in 40 speed dates, matching predicted mutual interest (OR 3.05). In 86 couples' IMs, 76.7% of
    above-median matchers were still together after 3 months vs 53.5% (OR 1.95). The samples are
    small.
  - Gonzales, Hancock & Pennebaker
    ([Communication Research 2010](https://sml.stanford.edu/publications/2010/language-style-matching-predictor-social-dynamics-small-groups)):
    70 groups, 324 people; matching predicted cohesiveness, and predicted performance in
    face-to-face groups only.
- **Chameleon effect.** Chartrand & Bargh (1999) reported that mimicry increases liking. A
  pre-registered replication by Hale & Hamilton
  ([Sci. Reports 2016](https://discovery-pp.ucl.ac.uk/1531017/1/srep35295.pdf); Study 1 N=50, Study
  2 N=40) found rapport effects in Study 1 and **no effect** in the pre-registered Study 2. Treat
  "mimicry → liking" as fragile. Linguistic accommodation as a _readout_ of status (Echoes of power)
  is better supported than mimicry as a _cause_ of liking.
- **Lexical entrainment.** Brennan & Clark
  ([JEP:LMC 1996, 22:1482–93](https://www.cs.columbia.edu/~julia/papers/brennan96.pdf)) describe
  "conceptual pacts": a pair keeps saying "the loafer" even after the other shoes are gone. Whether
  pacts are partner-specific is still disputed.

### 3c. Dead ends / contested

- **No real study of math-speak in everyday talk.** I found no corpus study tracking "modulo",
  "orthogonal", "WLOG" etc. moving into casual English. The only hit was an unreviewed Reed College
  sociolinguistics blog post (2025) asserting that "nonzero/nontrivial/such that" mark community
  membership. The Jargon File is the best evidence there is. Dictionary senses (Merriam-Webster
  "bandwidth" sense 3) show the end state without dating it.
- **The Jargon File as evidence is partly ESR's self-portrait.** Critics accused Raymond of shifting
  the File toward Unix culture and "adding terms reflecting his own politics and vocabulary"
  ([Wikipedia](https://en.wikipedia.org/wiki/Jargon_File)). Steve Jackson (1991) objected to its
  editorializing. Its "hacker speech style" chapter is normative self-description, not observation.
  Bucholtz 2001 is the independent check.
- **Brown et al. 2020:** the effects are real but small (about 10 percentage points, p≈.03–.05 in
  the experiments). The dissertation coefficients are tiny per unit of school rank.
- **Centola 2018's 25%:** the lab task is trivial. Critics cite 50–65% thresholds for costlier
  behaviors. The authors themselves say the number moves with memory length and stakes.
- **Fong et al. 1986, Experiment 4:** I recall it as a phone survey disguised as a sports poll. The
  abstract confirms only "tested completely outside of the context of training". The
  telephone/sports detail is UNVERIFIED.
- **Searle quote:** verified in his 1990 APA address. It is commonly attributed to _Minds, Brains
  and Science_ (1984); I did not verify that it appears there. Daugman's "Brain metaphor and brain
  theory" (1990) is UNVERIFIED.
- **Fanspeak dates:** "fen" is in the 1944 _Fancyclopedia_ (Speer, as "John Bristol"). One secondary
  source says "egoboo" is absent from it. I could not date "mundane". UNVERIFIED.
- **Korzybski → Yudkowsky:** Raymond says the influence was second-hand. Yudkowsky's Hayakawa
  recommendation (2008) is verified. The Null-A influence comes from a 2019 comment saying Yudkowsky
  mentioned it; I did not find the primary statement.
- **Corrections to the brief:**
  - Brown, Anicich & Galinsky 2020 is OBHDP 161:274–290, confirmed.
  - Shulman et al. 2020 is confirmed; definitions were _hover-over_.
  - Srivastava et al.'s measure is LIWC _style_ fit, not jargon. The dominant category was swearing.
  - Centola & Baronchelli 2015 named a pictured _face_.
  - The "~41 → ~8 words" figure is exact (41 → 8, trial 1 → trial 6), but from only 8 pairs.
