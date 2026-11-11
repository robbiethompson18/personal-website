# 08: Zoomer / Gen Alpha / internet slang: the non-obvious parts

Scope: how slang now starts, spreads and dies, algospeak, and typography as tone, plus where it
overlaps with rationalist, tech and trader slang. Glossary material is left out on purpose.
"Verified" means I opened the source (often the PDF) and checked the claim. UNVERIFIED means I only
saw it secondhand.

## 1. Most interesting findings

**1. A new member's first posts predict when they will leave the community, based on how they adopt
its slang.** Danescu-Niculescu-Mizil, West, Jurafsky, Leskovec & Potts (WWW 2013, best paper)
tracked BeerAdvocate and RateBeer users over 10 years. Users go through a "linguistic adolescence."
Their language moves toward the community's for about the **first third of their eventual
lifespan**. After that it rigidifies, and the community's norms drift away from them. The example:
reviewers who joined during the 2003 "Aroma" boom almost never switched to the later "S" (smell)
convention, and some used "Aroma" _more_. The cycle is "elastic": it stretches to fit total
lifespan, so someone who starts rigidifying after 20 posts is signalling an early exit. Features
from just the first ~20 posts (adoption of innovations, cross-entropy against the community's
language model, first-person-singular rate, which falls as people affiliate) add **2–12 points of
absolute F1 (4–40% relative)** to an activity-only churn baseline. This applies directly to Robbie
entering a rationalist scene: how fast you pick up the jargon, and when you stop picking it up, is a
measurable signal.
[Paper PDF, 2013](https://cs.cornell.edu/~cristian/Linguistic_change_files/linguistic_change_lifecycle.pdf)
(verified).

**2. A new word survives if it fits many sentence frames, not if many people use it.** Stewart &
Eisenstein (EMNLP 2018), "Making 'fetch' happen," studied about 1,120 growth words and 530 decline
words on Reddit. "Linguistic dissemination" is the number of unique trigram contexts a word appears
in, after controlling for frequency. It predicts both growth and survival. Social dissemination
(spread across users, subreddits or threads) adds almost nothing. In the Cox survival model,
linguistic dissemination has β = −0.33 (p < .001). Adding the social measures does not improve fit
(χ² = 4.6, p = 0.80). Growth probability is under 40% for the bottom decile of linguistic
dissemination and about 70% for the top decile. The paper's example pair: "kinda" has a
dissemination-to-frequency ratio of 0.270, against 0.055 for "sorta," the word that lost. This
explains why "-maxxing" and "based" lasted: they attach to anything.
[arXiv/ACL, 2018](https://ar5iv.arxiv.org/html/1709.00345) (verified).

**3. Online slang did not merge into one "netspeak"; it follows race more than distance.**
Eisenstein, O'Connor, Smith & Xing (PLoS ONE 2014) used 107M tweets across 200 US metro areas. The
strongest predictor of which cities pass words to each other is the gap in their shares of African
American residents. Geography plus population predicts influence links with 66.5% accuracy, and
adding demographics raises that to 74.4%. Examples: "ctfu" started around Cleveland, "ion" ("I
don't") in the Southeast, "suttin" in NYC, and "ikr" was 6x overrepresented in Detroit. The authors
conclude that online change "reproduces existing fault lines in spoken American English."
[PMC, 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4237389/) (verified).

**4. "AAE is the main source of lexical innovation on American Twitter," and Atlanta outweighs much
bigger cities.** Grieve, Nini & Guo (J. English Linguistics 2018) analysed 8.9B words from 980M
tweets (2013–14) and 54 emerging words. They found five innovation hubs: the West Coast, the Deep
South (Atlanta), Northeast/NYC, Mid-Atlantic/DC and the Gulf Coast (New Orleans). Press coverage
says three of the five are mainly AAE. Innovative areas in Georgia and North Carolina are "not
necessarily more populous" but have higher Black population shares. New words spread within cultural
regions first, which contradicts both the wave model and the city-hopping "gravity" model.
[Birmingham release, 2018](https://www.birmingham.ac.uk/news-archive/2018/analysis-of-billions-of-twitter-words-reveals-how-american-english-develops);
[theGrio summary, 2018](https://thegrio.com/2018/09/21/black-twitter-american-lexicon-study/). I
could not open the paper itself (403), so the 3-of-5 detail is secondhand.

**5. Most "new" slang sits dormant for years and then takes off. Its meaning can also generalise
within months.** In the companion study, Grieve, Nini & Guo ("Analyzing lexical emergence in Modern
American English online," English Language and Linguistics, 2017) found 29 emerging forms. Most had
Urban Dictionary entries years earlier ("bruh" 2003, "fuckboy" 2004, "bae" 2008) before they took
off in 2014. Growth was super-linear. It then either levelled into an S-curve (baeless, fleek,
gainz) or collapsed, often right after a frequency spike (celfie, bruuh). The case of "on fleek":
its 2014 rise traces to one Vine by Peaches Monroee (Kayla Newman). On June 26, 2014, 7 of the first
10 tweets were about eyebrows. By Nov 22 only 3 of 10 were, and the rest were about makeup, braids
and people. Newman was never paid. She launched a GoFundMe in 2017.
[Manuscript PDF, 2017](https://publications.aston.ac.uk/id/eprint/40102/1/ELL_078_Grieve_Nini_Guo_final.pdf)
(verified);
[Cosmetics Business on the GoFundMe, 2017](https://cosmeticsbusiness.com/woman-who-started-eyebrows-on-fleek-launches-gofundme-campaign-126182).

**6. Things that rise fast die fast.** This was measured on first names, which work like slang as
identity signals. Berger & Le Mens (PNAS 2009) ran a survival analysis on 2,570 French first names
(1900–2004). A sharper rise in popularity predicts faster death and lower total adoption. A survey
of 661 expecting parents found they avoid fast-rising names so the choice won't later look like "a
flash in the pan." A Stanford dorm field study by Berger, Heath & Ho (2005 working paper) found the
same thing when outsiders adopt a signal. Livestrong wristbands were sold to dorms, and once more
non-athletes wore them, wearing fell to 58% vs 88% in low-prevalence dorms. The paper names "teens
abandon slang when parents adopt it" as the same mechanism. Aleksic's version: "By the time boomers
are saying things like rizz… it seems a little bit forced."
[PNAS, 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2688844);
[working paper, 2005](https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Divergence.pdf)
(verified); [CBC, 2024](https://www.cbc.ca/1.7287363).

**7. Moderation works as selection pressure that speeds up lexical innovation, and much algospeak
may answer imagined filters.** Chancellor et al. (CSCW 2016) studied 2.5M Instagram posts from
2011–14. After Instagram banned pro-eating-disorder tags, variant spellings appeared that hadn't
existed before ("thyghgapp"). They grew more elaborate over time, and participation in the variant
communities rose 15–30%. On TikTok, Calhoun & Fawcett (Language@Internet 2023) and Steen, Yurechko &
Klug (Social Media + Society 2023, interviews with 19 creators) both stress that creators _guess_.
There's no published word list, Calhoun says there is "no publicly available statistical data" on
TikTok's moderation, and most creators suspected the audio was being scanned. Some algospeak is
literally machine-generated: "le dollar bean" is how TikTok's text-to-speech reads "le$bian."
[Chancellor, 2016](https://experts.umn.edu/en/publications/thyghgapp-instagram-content-moderation-and-lexical-variation-in-p/);
[Calhoun interview, 2024](https://news.illinois.edu/how-do-people-use-self-censorship-to-avoid-having-their-content-suppressed-on-sites-like-tiktok/);
[Steen et al., 2023](https://doaj.org/article/d818778da6c54591b57ed684cfe82894).

**8. "Unalive" crossed into sincere offline use within about two years.** In AP's 2023 reporting, a
Jersey City middle-school ESL teacher said students who may not know the word "suicide" say "I feel
so unalive" when their phones are taken away. Aleksic says he surveyed 1,000+ middle-school teachers
and found kids writing essays about Hamlet "unaliving" himself. In August 2024, a placard at
Seattle's MoPOP said Kurt Cobain "un-alived himself at 27." A companion card called the wording "a
gesture of respect." After backlash it was changed to "died by suicide." So an evasion code turned
into a polite register, the euphemism treadmill run in reverse.
[AP via CKPG, 2023](https://ckpgtoday.ca/?p=388377);
[NPR, 2025](https://www.npr.org/2025/07/20/nx-s1-5261011/adam-aleksic-discusses-algospeak-and-how-social-media-is-changing-how-we-talk);
[CNN via ABC17, 2024](https://abc17news.com/entertainment/cnn-entertainment/2024/08/17/a-museum-reportedly-used-unalived-to-describe-kurt-cobains-death-by-suicide-the-tiktok-term-is-likely-here-to-stay/).
The teacher survey's method is UNVERIFIED.

**9. "Maxxing" is Dictionary.com's 2026 Word of the Year, and the dictionary leaves out the incel
part of the origin.** The announcement (Oct 25, 2026) defines it as optimizing some part of life,
with examples tokenmaxxing (using as much AI at work as possible), looksmaxxing and nonnamaxxing. It
now works as a standalone verb. The etymology it gives is "maximum" → gaming "min-maxing" → "Reddit
and other forums," with only a nod to the "manosphere." Know Your Meme traces "looksmaxxing" to
PUAHate/Lookism forums (an Incel Wiki article from May 2014) and a 4chan /r9k/ post from 2015.
Wordorigins found "bench maxing" in a 2013 weightlifting tweet. So the incel-pipeline story is real
but probably not the whole lineage. In 2024 the "erasure" complaint concerned AAE; here the
dictionary has done the reverse and laundered an incel origin.
[Dictionary.com, 2026](https://www.dictionary.com/e/word-of-the-year-2026/);
[KYM](https://knowyourmeme.com/memes/maxxing);
[Wordorigins](https://www.wordorigins.org/big-list-entries/looksmaxxing-maxxing).

**10. "Based" went from crack-user insult to Lil B's self-acceptance to 4chan far-right and then to
generic approval. Its meaning got _vaguer_ as it spread.** Lil B reclaimed "basehead" (the 2007
album _Based Boys_; a 2010 interview defined it as being yourself). 4chan's music board took it up,
then /pol/. Hagen & de Zeeuw (Big Data & Society 2023) traced it across Twitter, Reddit and 4chan
from 2010 to 2021. The far-right sense persisted in places but blurred. A flexible core
("indifference to others' opinions + authenticity") let any politics attach to it. That matches
finding 2: semantic flexibility predicts survival. "Based in fact" is a folk etymology.
[Hagen & de Zeeuw, 2023](https://api.crossref.org/works/10.1177/20539517231163175);
[Merriam-Webster](https://www.merriam-webster.com/slang/based).

**11. WSB slang as a market signal.** Hayakawa, Otsubo, Poon & Wei (Economics Letters 2024) built a
"Vocabulary Herfindahl Index" over 150k+ WallStreetBets comments. When a few phrases dominate the
conversation ("collective effervescence"), return volatility rises afterwards, and the effect also
runs the other way. This is a concentration index applied to slang, the kind of thing a quant would
build. [IDEAS, 2024](https://ideas.repec.org/a/eee/ecolet/v244y2024ics0165176524005111.html)
(abstract only).

**12. Words take decades to become established, and the "adolescent peak" is around 17.** Petersen,
Tenenbaum, Havlin & Stanley (Sci. Reports 2012) used Google n-grams (1800–2008). A new word's
growth-rate fluctuations peak about **40 years** after introduction (range 30–50), roughly a human
generation. Word death rates rose sharply after the 1950s, and the authors blame copy-editing and
spell-checkers. In speech, Tagliamonte & D'Arcy (Language 2009) found adolescent peaks around age 17
for discourse-pragmatic changes in Toronto (e.g. intensifier "so," quotative "be like"). Sankoff &
Blondeau (Language 2007) found most adults stable after adolescence, but "a sizeable minority" kept
moving with the community. [Petersen, 2012](https://ar5iv.arxiv.org/html/1107.3707) (verified);
[Sankoff & Blondeau, 2007](https://muse.jhu.edu/article/228013).

## 2. Read these (ranked)

1. **Danescu-Niculescu-Mizil et al., "No country for old members"** (WWW 2013), 12 pp.
   [PDF](https://cs.cornell.edu/~cristian/Linguistic_change_files/linguistic_change_lifecycle.pdf).
   The best single paper here. It is quantitative and works as a mirror for anyone joining a
   jargon-heavy community.
2. **Stewart & Eisenstein, "Making 'fetch' happen"** (EMNLP 2018), 11 pp.
   [ar5iv](https://ar5iv.arxiv.org/html/1709.00345). A survival model for words with a clean,
   surprising result.
3. **Eisenstein et al., "Diffusion of lexical change in social media"** (PLoS ONE 2014), ~20 pp.
   [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4237389/). A vector-autoregressive model of which
   cities influence which.
4. **Grieve, Nini & Guo, "Analyzing lexical emergence in Modern American English online"** (ELL
   2017), ~45 pp. manuscript.
   [PDF](https://publications.aston.ac.uk/id/eprint/40102/1/ELL_078_Grieve_Nini_Guo_final.pdf). Read
   §5.3–5.6 for the dormancy, the S-curve vs crash, and the "fleek" semantic drift.
5. **Hagen & de Zeeuw, "Based and confused"** (Big Data & Society 2023), ~15 pp.
   [DOI](https://doi.org/10.1177/20539517231163175). The 4chan-to-mainstream pipeline traced with
   data rather than vibes.
6. **Taylor Lorenz, "Internet 'algospeak' is changing our language in real time"** (Washington Post,
   Apr 8 2022), ~1,800 words.
   [course-reader mirror PDF](https://mroberts1.github.io/fsu-smt-su25/pdf/algospeak.pdf) (verified
   there; the canonical WaPo URL is UNVERIFIED). The piece that popularised the term. Includes
   "cornucopia" for homophobia, "leg booty" for LGBT, and Twitch streamers having to say "saltines"
   because "cracker" is filtered.
7. **Berger & Le Mens, "How adoption speed affects the abandonment of cultural tastes"** (PNAS
   2009), 5 pp. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2688844). The hype-cycle math behind
   "cringe once your parents say it."
8. **Adam Aleksic, _Algospeak_** (Knopf 2025), ~250 pp. Reviewers say it reads like "fifty or so
   TikTok scripts," so pair it with Helena Aeberli's LARB review
   ([2025](https://lareviewofbooks.org/article/viral-language/)), which faults it for treating AAE's
   mainstreaming as a filter-bubble effect rather than digital blackface.
9. **Calhoun & Fawcett, "They Edited Out Her Nip Nops"** (Language@Internet 21, 2023), 30 pp. The
   academic account of algospeak's linguistic mechanisms: phonological substitution ("seggsy"),
   palm-colour gestures for race, and text-to-speech artifacts.
10. **Gretchen McCulloch, _Because Internet_** (Riverhead 2019). The standard book on typographic
    tone (lowercase, keysmash, the period) and "internet generations."
11. **Kiesling, "Dude"** (American Speech 2004), 25 pp.
    [PDF](https://linguist150.stanford.edu/readings/Kiesling2004.pdf). The model for analysing a
    slang word as a _stance_ ("cool solidarity"). It carries over to "bro," "king" and "unc."
12. **Chancellor et al., "#thyghgapp"** (CSCW 2016). The quantitative precursor to algospeak
    research.

## 3. Details

**Pipelines (sources of slang).**

- _Ballroom / Black queer culture:_
  - Shade and reading are canonical from _Paris Is Burning_ (1990). Dorian Corey: "shade comes from
    reading."
  - "Tea" traces to The Lady Chablis's "T" (truth, one's business) in _Midnight in the Garden of
    Good and Evil_ (1994), per Merriam-Webster
    ([M-W](https://www.merriam-webster.com/wordplay/tea-slang-meaning-origin)).
  - RuPaul's Drag Race (2009–) was the mainstreaming channel.
  - Historical parallel: Polari. After BBC radio's Julian and Sandy sketches broadcast it in the
    1960s, Paul Baker argues the secret was spoiled, and many gay men under 30 have never heard of
    it. A few words survived (naff, camp, zhoosh)
    ([Baker via Wikipedia](https://en.wikipedia.org/wiki/Polari)).
- _Appropriation:_
  - Ilbury (J. Sociolinguistics 2020), "Sassy Queens," analysed tweets by 10 gay British men. They
    used AAVE spellings to perform a persona built on an essentialised image of Black women as
    "fierce" ([Edinburgh PDF](https://core.ac.uk/download/524972364.pdf)).
  - Ilbury & Walcott, "'Gen Z language? Y'all mean AAVE'," is a conference abstract on how AAVE gets
    reframed as "internet/Gen Z language"
    ([abstract](https://ss25.m.tas.currinda.com/schedule/session/1140/abstract/19966)). I found no
    journal version.
- _Gaming/Twitch:_
  - PogChamp is a still from a Nov 2010 video of Ryan "Gootecks" Gutierrez. Twitch removed it in Jan
    2021 after his Capitol-riot comments and replaced it on a rotating basis
    ([KYM](https://knowyourmeme.com/memes/pogchamp)).
  - "Rizz": Kai Cenat says he and his friends coined it in the Bronx and popularised it in 2021
    ([KYM](https://knowyourmeme.com/memes/rizz)). Oxford WOTY 2023. Usage peaked in June 2023 after
    Tom Holland's interview, and Sept 2023 usage was more than 10x Sept 2022
    ([OUP](https://languages.oup.com/word-of-the-year-2023/)).
- _Incel/4chan:_
  - Gothard et al. (arXiv 2021) quantified the incel lexicon over about 3M Reddit comments
    ([arXiv](https://arxiv.org/pdf/2105.12006.pdf)).
  - "Cope and seethe" on 4chan dates to 2019 per KYM. "Copium" is a blend of cope and opium.
  - Aleksic's quip: "if a word doesn't come from 4chan, it's probably from AAE"
    ([LARB](https://lareviewofbooks.org/article/viral-language/)).

**Nonsense as signal.**

- "Brain rot" was Oxford WOTY 2024: usage up 230% year over year, first attested in Thoreau's
  _Walden_ (1854) ([OUP](https://corp.oup.com/news/brain-rot-named-oxford-word-of-the-year-2024/)).
- "6-7" was Dictionary.com's 2025 pick. It appeared 6x more in October 2025 than in all of 2024, and
  Dictionary.com called it "meaningless, ubiquitous and nonsensical"
  ([AV Club](https://www.avclub.com/dictionary-dot-com-2025-word-of-the-year-67)).
- Cambridge's 2025 entry for "skibidi": "can have different meanings such as 'cool' or 'bad' or can
  be used with no real meaning as a joke"
  ([NBC](https://www.nbcnews.com/pop-culture/pop-culture-news/cambridge-dictionary-adds-skibidi-tradwife-6000-new-words-rcna225566)).
- Read through findings 2 and 6: a semantically empty token has maximal linguistic dissemination (it
  fits anywhere), and that is exactly what makes it a cheap in-group test. Linguists quoted in the
  press make the exclusion argument
  ([MadeForMums](https://www.madeformums.com/apple-news/the-psychology-behind-gen-alpha-slang)). I
  found no peer-reviewed test of it.

**Algospeak's historical parallels.**

- China's "harmony" (和谐) became "harmonized" for censored posts. That was itself censored, so it
  became "river crab" (河蟹, a near-homophone). The 2009 "grass mud horse" song has the horse defeat
  the crab ([Wikipedia](https://en.wikipedia.org/wiki/Grass_Mud_Horse);
  [CDT, 2009](https://chinadigitaltimes.net/2009/03/china-censors-bar-mythical-creature/)). Same
  whack-a-mole recursion as "seggs" getting flagged.
- Lev Loseff, _On the Beneficence of Censorship: Aesopian Language in Modern Russian Literature_
  (1984, open access at [DOAB](https://directory.doabooks.org/handle/20.500.12854/28387)). His key
  point: Aesopian text carries no new message, because readers decode only what they already know.
  That is also how algospeak works.

**Typography as tone.**

- Gunraj et al. (Computers in Human Behavior 2016; 126 undergrads): text replies ending in a period
  read as less sincere, and handwritten notes showed no effect
  ([SUNY](https://researchconnect.suny.edu/en/publications/texting-insincerely-the-role-of-the-period-in-text-messaging/)).
- Houghton, Upadhyay & Klin (CHB 2018): one-word replies with a period read as more negative
  ([ScienceDaily](https://www.sciencedaily.com/releases/2017/11/171114142322.htm)).
- McWhorter (TED 2013): texting is "fingered speech," and "LOL" has become a pragmatic particle
  marking empathy and accommodation, not laughter
  ([TED blog](https://blog.ted.com/the-linguistic-miracle-of-texting-john-mcwhorter-at-ted2013/)).
- D'Arcy (2017): discourse "like" has behaved in orderly ways "for at least a century." She
  dismisses the "female adolescent form" myth and finds men lead use of the particle
  ([LINGUIST review](https://listserv.linguistlist.org/pipermail/linguist/2018-August/091676.html)).
- Tagliamonte's intensifier work: "very" fell out of favour and is coming back because its rarity
  gave it novelty value ("A linguistic phoenix" (Brook & Tagliamonte,
  [Cambridge](https://resolve.cambridge.org/core/journals/language-variation-and-change/article/linguistic-phoenix-the-recycling-of-very-in-ontario-english/87E6273CE26B7E8C83B63C24A95E1305))).
  Slang recycles.

**Survival predictors.**

- Metcalf's FUDGE (_Predicting New Words_, 2002) scores Frequency, Unobtrusiveness, Diversity of
  users/situations, Generation of other forms, and Endurance of concept, 0–2 each. Words that are
  too clever do worse, and promotional campaigns fail. A 2008 test on Chinese neologisms found it
  predicts _failures_ better than successes
  ([wordorigins review](https://wordorigins.org/harmless-drudge/book-review-predicting-new-words)).
- Stewart & Eisenstein's linguistic dissemination is in effect a measurable version of the "D" and
  "G" factors.
- "Dude": first printed in an 1883 New York World poem about fops
  ([OUP blog, 2022](https://blog.oup.com/2022/12/dude-a-long-history-of-a-short-word/)).
- "Cool" is often credited to Lester Young. The sources hedge heavily.

**Overlap with Robbie's worlds.** maxxing (finding 9), based (finding 10) and cope/seethe come
straight from 4chan and incel sources. WSB:

- Agrawal, Buz & de Melo (AMCIS 2022) show the same users shift vocabulary between r/wallstreetbets,
  r/stocks and r/investing. This is audience design, i.e. code-switching
  ([AIS](https://aisel.aisnet.org/amcis2022/sig_sc/sig_sc/8)).
- Hayakawa et al. 2024 is finding 11.

## 4. Dead ends / contested

- **Is slang turnover actually faster?** I found no quantitative half-life study. Merriam-Webster
  lexicographers agree words get popular faster but are "more hesitant" that they fade faster
  ([Fast Company, 2024](https://www.fastcompany.com/91142295/rizz-skibidi-gen-z-gen-alpha-slang-experts)).
  Aleksic's "faster than ever" claims are unmeasured (Harvard Gazette 2025). Grieve's dormancy
  result and Petersen's ~40-year adoption cut against the simple "TikTok speeds everything up"
  story.
- **Does algospeak evade anything real?** Unknown. TikTok says moderation doesn't work that way, and
  no independent keyword audit exists. A 2022 poll cited by Wikipedia says nearly a third of US
  social-media users have used algospeak (UNVERIFIED).
- **"Unalive" origin:** Dictionary.com says a 2013 _Ultimate Spider-Man_ episode popularised it.
  Another account credits Deadpool. UNVERIFIED.
- **-maxxing:** incel forum vs gaming min-maxing vs gym "bench maxing" (2013). Probably several
  converging sources.
- **wagmi/ngmi:** usually traced to bodybuilder Zyzz (d. 2011). Crypto glossaries say 4chan /biz/
  instead. No primary source either way
  ([Vice](https://vice.com/en/article/the-tragic-true-story-behind-wagmi-cryptos-most-positive-catchphrase)).
- **"Diamond hands":** Dictionary.com says 2018 or earlier on WSB. KYM says popularised in 2020–21
  around GME.
- **"Pog" = "play of the game"** is a backronym.
- **"Slay" from 1920s "you slay me" to ballroom:** no documented chain.
- **Cockney rhyming slang as a criminal code** is contested. Many historians see it as market-trader
  wordplay from the 1840s
  ([History Hit](https://www.historyhit.com/origins-of-cockney-rhyming-slang/)).
- **💀 replacing 😂:** well documented in Brandwatch data and press (CNN 2021), but no peer-reviewed
  study.
- **Tone indicators (/j /srs /gen):** commonly attributed to neurodivergent Tumblr users. No
  scholarly origin found.
- **Vocal fry:** Anderson et al. (PLoS ONE 2014) found fry voices rated less hireable over 80% of
  the time. Language Log argued the stimuli were confounded with lower pitch overall
  ([Language Log](https://languagelog.ldc.upenn.edu/nll/?p=12774)).
- **Corrections to your brief:**
  - Del Tredici & Fernández (COLING 2018, "The Road to Success") is about _lexical_, not semantic,
    innovation. Its finding: innovators are central members with _weak_ ties, and small strong-tie
    cliques carry the spread ([arXiv](https://arxiv.org/pdf/1806.05838)).
  - Grieve et al. 2017 found 29 emerging forms, and the 2018 paper used 54.
  - The Berger & Heath (2008, JPSP) "geek dorm wristband" detail I could not verify. The 58% vs 88%
    figure above is from the 2005 Berger/Heath/Ho working paper.
  - Stan Twitter / K-pop: I didn't get to it, so it's uncovered.
