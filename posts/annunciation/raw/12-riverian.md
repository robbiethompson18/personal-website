# "Glossary: How to Speak Riverian" (Nate Silver, _On the Edge_, 2024)

## How this was sourced (read first)

No full excerpt of the glossary is legally online. Almost everything below comes from **Google Books
search-inside snippets**. I pulled them from Google's legacy Atom feed
(`https://www.google.com/books/feeds/volumes?q=...`), which returns a ~40-word snippet of the
best-matching passage for each query. I ran ~300 queries of the form
`"how to speak riverian" "<Term>"`. Two volumes answered:

- **GB24** = `doPqEAAAQBAJ`, the Penguin Press hardcover/ebook, 2024-08-13 (hardcover ISBN
  9781594204128). https://books.google.com/books?id=doPqEAAAQBAJ
- **GB25** = `-uJYEQAAQBAJ`, the Penguin Books paperback with a new preface, 2025-08-12 (ISBN
  9780593491645). https://books.google.com/books?id=-uJYEQAAQBAJ

Every verbatim quote below was in a snippet I actually received. Snippets carry the running head
(`GLOSSARY: HOW TO SPEAK RIVERIAN | 483`), and that is where the page numbers come from. Both
editions show the same glossary page numbers, so the new 2025 preface must be paginated separately.
Raw hits are saved in
`/private/tmp/claude-501/-Users-robbie-repos-dotfiles/8823d054-20f4-4b50-a47d-27a4a4dc86c0/scratchpad/gbhits.jsonl`.

**Correction to the earlier research.** "Riverians are the Advantage Players of life" is **not
Silver's line and not in the glossary.** It is Zvi Mowshowitz's own sentence in his review: it sits
unquoted, with no Kindle location, in his framing section
([thezvi.substack.com, 2024](https://thezvi.substack.com/p/book-review-on-the-edge-the-fundamentals)).
It also did not turn up in Google Books. The glossary does have a nearby real entry, "Advantage
play: Being +EV at a casino game…"

---

## 1. Facts about the glossary

- **Exact title:** "Glossary: How to Speak Riverian". The library catalog lists it in the back
  matter as Acknowledgments, Methods, and Sources / **Glossary: How to Speak Riverian** / Notes /
  Index ([ICPL catalog](https://search.icpl.org/Record/1813419)).
- **Pages:** about **pp. 477–501** in both editions. The page anchors I saw were: Angle/Attention
  478; Bayes/Bankroll/Beard/Bid-ask 479; Card counting/CLV/Cooler 481; Deterrence 482;
  Doomer/Downriver/Drawing dead/Discount rate 483; Feedback loop 484; Freeroll/GTO/Fish 485;
  Limited/Sharp 488; the legalistic-disclaimer trope 491; Prior/Ponzi/Prediction
  market/Pot-committed 493; Rational 494; Rationalism/Rug pull/Risk of
  ruin/Regression/Results-oriented 495; Solver/Steam chasing/Steelman/St. Petersburg 497; LAG/Tilt
  498–499; Update/Upriver 499; Wordcel/WPT 500. That makes about 25 pages, which matches xquant's
  "25 page glossary"
  ([xquant, 2024](https://xquant.substack.com/p/on-the-edge-a-riverian-memoir-written)).
- **Number of entries:** UNVERIFIED estimate of **~250–300**. The snippets show 3–5 entries per ~40
  words of text, at roughly 10–13 entries per page across 25 pages. I confirmed **110+** individual
  entries.
- **Silver's framing (verbatim, from snippets):**
  - "This is a reasonably complete list of technical terms used in On the Edge from the various
    fields it covers, such as poker, gambling, finance, AI, crypto, and effective altruism."
  - "I've also included a small handful of terms that didn't make it into the main narrative, but
    which you'll frequently encounter in conversa[tions with…]" (the snippet cuts off there).
  - On asterisks: terms marked with "(*) are not in widespread usage. They reflect pithy phrases
    used by one of my sources, or that I came up with myself for this book."
  - "Entries in italics are related terms that did not receive…" (cut off; presumably "their own
    entry").
- **Silver-coined (asterisked) entries I confirmed:** (The) Archipelago\*, Upriver\*, Downriver\*,
  (The) Village\*, Moneyball-ization\*, EV maximizer\*, Bag of numbers\* (credited to OpenAI's Nick
  Ryder). Midriver\* and River\* are almost certainly asterisked too, but I never saw them.

### River, Village, and the regions

| Term                    | What Silver says (glossary unless noted)                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Who lives there                                                                                                                                                                                                   |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **River**               | Main text: "a sprawling ecosystem of like-minded people… a way of thinking and a mode of life" (Kindle loc 73, quoted by Zvi). Substack: "a place for people who are very analytical but also highly competitive" ([Silver Bulletin, 2024](https://www.natesilver.net/p/welcome-to-the-river)). 2025: "people who seek to maximize expected value at every opportunity" ([Silver Bulletin, 2025](https://www.natesilver.net/p/one-year-later-is-the-river-winning)). The glossary's own River entry: not seen. | Poker is the "archetypal activity". Also Silicon Valley, Wall Street, sports betting, crypto, EA (Silver Bulletin 2024).                                                                                          |
| **(The) Village\***     | "The rival community to the River, reflected most clearly in intellectual occupations with progressive politics, such as the media, academia, and government (especially when a Demo[crat is in the White House])"                                                                                                                                                                                                                                                                                             | NYT, Harvard, government. "basically the liberal establishment" (Silver Bulletin 2024).                                                                                                                           |
| **Upriver\***           | "A more intellectual part of the River focused around the raw production of Riverian ideas, such as those expressed in the EA and rationalist movements or in the development of AI for non-commercial uses."                                                                                                                                                                                                                                                                                                  | EA, rationalists, AI labs (non-commercial side), utilitarian philosophers. The entry adds: "Silicon Valley is influenced by Upriver but sits closer to Midriver."                                                 |
| **Midriver**            | Main text: "Midriver, which I picture as having lots of tall, angular buildings, as Manhattan does. This is where people apply…"                                                                                                                                                                                                                                                                                                                                                                               | Wall Street, Silicon Valley/VC (Drayton D'Silva's summary: "Midriver (Wall Street, Silicon Valley, etc.)", [Enterprise Value, 2024](https://enterprisevalue.substack.com/p/nate-silvers-on-the-edge-is-meh-but)). |
| **Downriver\***         | "The region of the River focused on casino gambling." Main text: "I imagine Downriver as Las Vegas meets New Orleans: lots of tourists and lots of gambling."                                                                                                                                                                                                                                                                                                                                                  | Casinos, poker, sports betting.                                                                                                                                                                                   |
| **(The) Archipelago\*** | "The region of the River encompassing gray-market activities such as unregu[lated] crypto exchanges; a place to avoid."                                                                                                                                                                                                                                                                                                                                                                                        | Offshore crypto (FTX-world), gray-market gambling.                                                                                                                                                                |

### The cognitive and personality clusters (main text, Introduction, ~p. 24)

A table in the Introduction, seen in a GB25 snippet: **COGNITIVE CLUSTER: Analytical, Abstract,
Decoupling. PERSONALITY CLUSTER: Competitive, Critical, Independent-minded (contrarian),
Risk-tolerant.** Note that "Critical" is a fourth personality trait the brief didn't list.

- "It begins with abstract and analytical reasoning." Abstract thinking is glossed as "model
  building" (Kindle locs 387–391, via Zvi).
- On decoupling: "the third part of the cognitive cluster, 'decoupling,' is probably less familiar.
  It's really just the same thought process as applied to philosophi[cal or political ideas]" (GB25,
  p. ~24; the "third part" is my reading of the snippet).
- "People in the River are trying to beat the market." "people in the River are often intensely
  competitive." Risk tolerance is included "whether they're degens or nits in other parts of their
  lives" (locs 422–436, via Zvi).
- "Riverians are sometimes accused of being contrarian when they're just being independent." (loc
  4307, via Zvi)

---

## 2. Confirmed entries

Source key: GB24/GB25 as above. "Quote" means text I saw in a snippet. Everything else is my
paraphrase. Origins are my own classification.

### Rationalist, EA, statistics, AI

| Term                                   | Silver's definition (paraphrase; short verbatim where seen)                                                                                                                                                                                                                | Origin                           | Src                |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ------------------ |
| Bayesian                               | Says you (1) hold initial beliefs, "or priors about the world," and (2) "update those beliefs based on the strength of new evidence."                                                                                                                                      | stats/rat                        | GB25 p.479         |
| Bayes' theorem                         | "A foundational concept in probability theory, attributed to Reverend Thomas Bayes, used to update the likelihood of an…"                                                                                                                                                  | stats                            | GB25 p.479         |
| Prior                                  | "In Bayesian reasoning, an initial belief that you're prepared to revise as more information is revealed." Originally a statistical estimate; "the term is now used widely in the…"                                                                                        | stats/rat                        | GB25 p.493         |
| Update (entry directly before Upriver) | Ends: used in the River "as a somewhat pretentious way to refer to changing one's mind." I saw only the tail, so the headword is inferred.                                                                                                                                 | rat                              | GB25 p.499         |
| Calibration                            | "the extent to which your predictions match your purported probabilities." Example: forecast something at 20% and it should happen ~20 times in 100.                                                                                                                       | stats/forecasting                | GB25               |
| Superforecaster                        | Tetlock's term for people with a demonstrated ability "to make well-calibrated…" forecasts                                                                                                                                                                                 | forecasting                      | GB24               |
| Fox (and hedgehog)                     | Tetlock's two decision-making personality types; Archilochus: "The fox knows many things, but the hedgehog knows one big thing"                                                                                                                                            | forecasting                      | GB25 p.485         |
| Model                                  | "A simplified representation of a complex system designed to replicate its essential features accurately…"                                                                                                                                                                 | stats                            | GB24               |
| Backtest                               | Evaluating a model on known past data; "Less reliable than using out-of[-sample]…"                                                                                                                                                                                         | stats/quant                      | GB25 p.479         |
| Regression analysis                    | A statistical method relating an independent variable to a dependent one                                                                                                                                                                                                   | stats                            | GB24 p.495         |
| Variance                               | "Statistical fluctuations resulting from randomness. It is defined mathematically as the square root of the standard deviation…" **This is wrong**: variance is the _square_ of the SD. The error survives in the 2025 paperback.                                          | stats/poker                      | GB25               |
| Black swan                             | Taleb's term for "purportedly extremely unlikely out[comes]…"                                                                                                                                                                                                              | finance/Taleb                    | GB25 p.479         |
| Tail risk                              | "A low-probability outcome, referring to the thin tails at either end of a bell curve."                                                                                                                                                                                    | finance/stats                    | GB24               |
| Normal distribution (inferred)         | Contrasted with "fat-tailed distributions, where outlier or 'black swan' outcomes are far more likely"                                                                                                                                                                     | stats                            | GB24               |
| Edge case                              | "An example occurring in extreme or unusual circumstances that might not be suitable for generalization."                                                                                                                                                                  | eng/rat                          | GB25 p.483         |
| Decoupling                             | "Separating the elements of a complex issue," e.g. judging a musician's vocal talent without weighing her politics. "Riverians love to decouple, thinking it allows for un[biased] analysis, whereas Villagers like to consider facts…"                                    | rat (Sarah Constantin's framing) | GB25               |
| Steelman                               | "The opposite of a strawman, a robust representation of an opponent's argument…" The main text calls it "a favorite technique of EAs and rationalists".                                                                                                                    | rat                              | GB24 p.497         |
| Motte-and-bailey fallacy               | "A nerdy Riverian term" for advancing a controversial claim (the bailey), then retreating to an easier-to-defend one (the motte)                                                                                                                                           | rat (SSC)                        | GB25               |
| Rational                               | "When defined by philosophers, not merely a [synonym for]…"                                                                                                                                                                                                                | philosophy                       | GB24 p.494         |
| Rationalism / rat                      | "A loosely defined intellectual movement associated with Eliezer Yudkowsky and Robin Hanson…" It is more "contrarian than EA, with less regard for social conventions. An adherent of rationalism is a rat."                                                               | rat                              | GB24 p.495         |
| Robust                                 | A philosophy/statistics sense of the word (snippet truncated)                                                                                                                                                                                                              | stats/phil                       | GB24               |
| Effective altruism                     | "A movement founded by Will MacAskill and Toby Ord that advocates for using rigorous analysis to determine how to do the most good." It started with charity and now extends further. "EA has origins in utilitar[ian] philosophy, although not all EAs are utilitarians." | EA                               | GB24/GB25          |
| Longtermism                            | "A philosophy championed by Will MacAskill and other EAs that assigns low or zero discount rates to…" future people                                                                                                                                                        | EA                               | GB25 p.488         |
| Discount rate                          | "The penalty assigned to future time periods when calculating utility or the EV of an investment."                                                                                                                                                                         | econ/EA                          | GB24 p.483         |
| Util, utility                          | "A quantifiable but dimensionless unit of 'goodness.'" Utilitarians want to maximize it.                                                                                                                                                                                   | EA/econ                          | GB25 p.~499        |
| Utilitarianism                         | "A branch of consequentialism that argues that the morality of an action is based on its utility…"                                                                                                                                                                         | EA/phil                          | GB25               |
| Rule utilitarianism                    | Act so that if your behavior "were universalized, it would maximize utility"                                                                                                                                                                                               | phil                             | GB25 p.500 (index) |
| Value of a statistical life (VSL)      | An empirical estimate from "people's revealed preferences" for how much they'd pay to reduce mortality risk                                                                                                                                                                | econ/EA                          | GB25               |
| St. Petersburg paradox                 | The observation, "originally by the…" Bernoulli(s) (truncated)                                                                                                                                                                                                             | prob/EA                          | GB24 p.497         |
| Progress studies                       | "A term proposed by Patrick Collison and Tyler Cowen for a multidisciplinary…" field                                                                                                                                                                                       | tech-intellectual                | GB25               |
| Existential risk                       | Referenced inside the EA and Doomer entries. A standalone entry is likely but I didn't see it.                                                                                                                                                                             | EA/AI                            | GB25               |
| Doomer                                 | "Someone with a high p(doom) who is extremely worried about existential risk from AI."                                                                                                                                                                                     | AI/rat                           | GB24 p.483         |
| e/acc (effective accelerationism)      | "a loosely defined and sometimes trollish movement (the name is a play on effective altruism)"                                                                                                                                                                             | AI/tech                          | GB24 p.483         |
| AGI                                    | "The term lacks a clear definition but refers to at least broad human-level…" capability                                                                                                                                                                                   | AI                               | GB24               |
| Alignment (AI)                         | "The quality of AI systems being 'well-behaved' and safely accomplishing their in[tended objectives]"                                                                                                                                                                      | AI/rat                           | GB24               |
| Takeoff (AI)                           | "The speed at which AI progress is achieved; doomers fear a fast takeoff…"                                                                                                                                                                                                 | AI/rat                           | GB24               |
| Attention (AI)                         | In a transformer, the mechanism weighting semantic relationships between pairs of tokens                                                                                                                                                                                   | AI                               | GB25 p.478         |
| Vector                                 | A magnitude and a direction ("an arrow pointing 5 paces east and 6 paces north"); in AI, a token's position in semantic space                                                                                                                                              | AI/math                          | GB25               |
| Bag of numbers\*                       | "A term conveyed to me by Nick Ryder of OpenAI for the mysterious inner workings of large language" models                                                                                                                                                                 | AI                               | GB25 p.479         |
| Wordcel                                | "A meme, popularized by roon…" (the shape-rotator vs wordcel split)                                                                                                                                                                                                        | tech-Twitter                     | GB25 p.500         |
| LLM, RLHF                              | "See:" cross-references only                                                                                                                                                                                                                                               | AI                               | GB24/GB25          |

### Poker, casino, sports betting

| Term                         | Definition                                                                                                                                                                                                   | Origin              | Src            |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- | -------------- |
| Expected value / EV          | Snippet: what you'd win "on average after many 'spins of the wheel,' given your knowledge of the odds when you place a bet or choose a…" The headword is inferred.                                           | gambling/econ       | GB25           |
| EV maximizer\*               | "A typical citizen of the River: the type of person who always likes to crunch the…" numbers                                                                                                                 | Silver              | GB24           |
| Advantage play               | "Being +EV at a casino game…"                                                                                                                                                                                | casino              | GB25           |
| Edge                         | Main text, not glossary: "'Edge' means having a persistent advantage in gambling—consistently making +EV bets."                                                                                              | gambling            | GB25           |
| Action                       | "A robust gambling term: (1) a lucrative or high-stakes but risky opportunity ('Where the action is'); (2)… loose, aggressive play"; (3) whose turn it is ("action's on you, sir")                           | gambling            | GB24           |
| Degen, degenerate            | "A person who has a tendency to gamble, especially for high stakes, or otherwise to engage in debaucherous behavior." "Often implies -EV gambling but can also mean making +EV bets beyond one's means."     | poker/crypto        | GB25           |
| Nit                          | "A poker player who is conspicuously risk-averse. It can also convey cheapness or neuroticism, being a stickler…"                                                                                            | poker               | GB24/GB25      |
| Tilt                         | "In poker and other gambling, an emotional state that results in suboptimal play." The archetype is chasing losses after a bad beat.                                                                         | poker               | GB24 p.498–499 |
| Bad beat                     | A strong hand losing to a long-shot draw. "Often extended by Riverians to everyday situations," e.g. a parking ticket during a five-minute Starbucks stop                                                    | poker               | GB25           |
| Cooler                       | "When you have a strong poker hand but your opponent has an even stronger one," so you lose despite playing reasonably                                                                                       | poker               | GB25 p.481     |
| Fish (poker)                 | "A -EV, typically inexperienced player who you want in your game." Possibly coined in opposition to "shark, i.e., a skilled player." The term "is insulting and players are advised not to 'tap the glass'". | poker               | GB25 p.485     |
| Whale                        | "In poker and casino gambling, a relatively poor player who gives action and gambles at high stakes." In crypto, by contrast, a large holder, with a positive connotation.                                   | poker/casino/crypto | GB25           |
| Angle                        | In sports betting, an edge from a proprietary insight. In poker, "a shady tactic that isn't strictly…" against the rules (the angle-shooting sense)                                                          | betting/poker       | GB24 p.478     |
| Game-theory optimal (GTO)    | Play "recommended by game theory, such as a Nash equilibrium derived by a…" solver                                                                                                                           | poker/game theory   | GB25 p.485     |
| Exploitative strategy        | "An approach designed to take advantage of an opponent who isn't playing a game-theory[-optimal]…" strategy                                                                                                  | poker               | GB24           |
| Mixed strategy               | When two or more options (raise/call) "have the same expected value and you should randomize between them."                                                                                                  | game theory         | GB25           |
| Pure strategy                | Game theory recommends an action "100 percent of the time instead of using a mixed strategy."                                                                                                                | game theory         | GB25           |
| Solver                       | "A poker computer program that calculates an approximation of the Nash equilibrium…"                                                                                                                         | poker               | GB24 p.497     |
| Node                         | A decision point in a game tree                                                                                                                                                                              | poker/game theory   | GB24           |
| Combo (poker)                | Permutations of a hand within a player's range                                                                                                                                                               | poker               | GB24 p.481     |
| Range (inside another entry) | "you should assign your opponent a range of hands and not guess her exact cards"                                                                                                                             | poker               | GB24 p.494     |
| Raise-or-fold situation      | "A circumstance in which you should either act aggressively or retreat, and the middle…" option is worst                                                                                                     | poker → life        | GB25           |
| Pot-committed                | "you can't fold because you'll have the right odds to call no matter…" what                                                                                                                                  | poker               | GB24 p.493     |
| Drawing dead                 | "literally no chance to win even if everything goes per[fectly]"                                                                                                                                             | poker               | GB24 p.483     |
| Freeroll                     | "A gambling situation in which you can't lose money but have a chance of winning some[thing]"                                                                                                                | gambling            | GB25 p.485     |
| TAG / LAG                    | Tight-aggressive, the "Doyle Brunson" style of playing "relatively few hands"; loose-aggressive is the opposite                                                                                              | poker               | GB24 p.498     |
| Aces                         | Pocket aces, "the best possible starting hand in Hold['em]"                                                                                                                                                  | poker               | GB24           |
| Bankroll                     | "The amount of money a player sets aside to gamble with."                                                                                                                                                    | gambling            | GB25 p.479     |
| Risk of ruin                 | "The probability of losing so much money that your ability to make further bets is se[verely] impaired"                                                                                                      | gambling/quant      | GB24 p.495     |
| Kelly criterion              | "A formula derived by John Kelly Jr. that calculates what percentage of your bankroll you should bet"                                                                                                        | gambling/quant      | GB25           |
| Gambler's fallacy            | Believing outcomes even out "in the short run," e.g. betting tails after a run of heads                                                                                                                      | prob                | GB25 p.481/485 |
| Card counting                | "In blackjack—specifically blackjack, don't use this for other card games—keeping track of which…" cards are left                                                                                            | casino              | GB25 p.481     |
| Pit boss / Locals casino     | Casino staff; a casino with "limited amenities" aimed at local residents                                                                                                                                     | casino              | GB25           |
| Vig / Vigorish               | "the house edge implicitly built into betting lines, typically 4 to 5 percent of a wager. Juice and hold are synonyms."                                                                                      | sports betting      | GB25           |
| Closing line value           | "A case in which the betting consensus moved in the direction of your bet."                                                                                                                                  | sports betting      | GB25 p.481     |
| Steam chasing                | "following steam—changes in betting prices at book[makers]…"                                                                                                                                                 | sports betting      | GB24 p.497     |
| Public (sports betting)      | "The sum total of action from unskilled, recreational bettors." It is often advisable "to fade the public (i.e., bet against the popular pick)."                                                             | sports betting      | GB24           |
| Limited                      | "Having your maximum wager reduced by a sportsbook because they think you're a sharp bettor."                                                                                                                | sports betting      | GB25 p.488     |
| Beard                        | Someone, "ideally a known whale or degen, who makes a bet on your behalf"                                                                                                                                    | sports betting      | GB25 p.479     |
| Punter                       | A British term for "a typically recreational gambling patron"                                                                                                                                                | betting             | GB25           |
| WPT, WSOP                    | Poker tour acronyms                                                                                                                                                                                          | poker               | GB25 p.500     |

### Finance, VC, crypto, game theory

| Term                                      | Definition                                                                                                                                                                                                  | Origin              | Src                 |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------- |
| Alpha                                     | "having an edge through skill or proprietary methods that allows you to achieve persistent above-market returns."                                                                                           | finance             | GB25                |
| Arbitrage (Arb)                           | "A strategy to earn risk-free profit by exploiting price differences of the same asset in different markets."                                                                                               | finance/betting     | GB24/GB25           |
| Bid-ask spread                            | "The typically narrow gap between the price at which you're offered to sell a stock (the 'bid')…" and buy                                                                                                   | finance             | GB25 p.479          |
| Adverse selection                         | "An asymmetry in which one party to a transaction has more information and takes advantage of it." Informally, attracting the customers you don't want, like an all-you-can-eat sushi restaurant does.      | econ/betting        | GB24                |
| Moral hazard                              | A party taking a risk "does not bear the full downside consequences"                                                                                                                                        | econ                | GB25                |
| Return on investment                      | "Your profits divided by your stake or investment."                                                                                                                                                         | finance             | GB24 p.495          |
| Accelerator                               | A competitive program giving mentorship and small investments to early-stage startups                                                                                                                       | VC                  | GB25                |
| Venture capital (VC)                      | Has an entry ("VC: See: venture capital"). Definition not seen.                                                                                                                                             | VC                  | GB25                |
| Moneyball-ization\*                       | "The process of turning things over to data science and algorithms, especially in fields that…"                                                                                                             | sabermetrics        | GB24/GB25           |
| Quant                                     | "A Riverian archetype who makes bets or decisions using statistical analysis."                                                                                                                              | finance             | GB24                |
| Prediction market                         | "A platform where people may bet on the outcome of real-world events, from presidential…" elections                                                                                                         | forecasting         | GB24 p.493          |
| HODL                                      | "Hold On for Dear Life; in crypto, a rallying cry used…"                                                                                                                                                    | crypto              | GB25                |
| Bored Ape / apeing                        | BAYC is "more often asso[ciated] with the NFT bubble of 2020–22." "Apeing refers to impulsively buying a new token or NFT collection without…" research                                                     | crypto              | GB24/GB25           |
| Rug pull                                  | "Hyping up a crypto project to attract…" money, then abandoning it                                                                                                                                          | crypto              | GB24 p.495–496      |
| Pump-and-dump                             | "Disingenuously hyping up an asset, and then…" selling                                                                                                                                                      | crypto/finance      | GB25                |
| Ponzi scheme                              | Charles Ponzi's con "that promises high investment returns…" paid from new deposits                                                                                                                         | finance/crypto      | GB25 p.493          |
| Provenance                                | "The prestige, origin, and chain of custody of an object," as with NFTs                                                                                                                                     | crypto/art          | GB25                |
| (unknown headword)                        | "Riverian trope for a legalistic disclaimer that means the opposite of what it says. The phrase was frequently employed by Sam Bankman-Fried in all caps…" Probably "Not financial advice", but UNVERIFIED. | crypto              | GB24 p.491          |
| Prisoner's dilemma                        | "A famous and broadly useful application of game theory, first described in 1950 by Melvin [Dresher and Merrill Flood]…"                                                                                    | game theory         | GB25                |
| Reciprocity                               | "responding to an action with an action that mirrors it—tit for tat or an eye for…" an eye                                                                                                                  | game theory         | GB24 p.495          |
| Deterrence / Doomsday machine / Arms race | Deterrence prevents aggression through the threat of retaliation. A doomsday machine "automatically retaliates if it detects a nuclear strike."                                                             | game theory/nuclear | GB24/GB25 p.482–483 |
| Feedback loop / virtuous cycle            | Effects that feed back into the system, e.g. melting glaciers lowering albedo. "Virtuous cycle: See: feedback loop."                                                                                        | systems             | GB24 p.484          |
| Results-oriented thinking                 | "Results-oriented thinking predomi[nates] outside the River, whereas Riverians strive to focus on process."                                                                                                 | poker → life        | GB24 p.495          |
| Analysis, analytics                       | "'Analysis' refers to the process of breaking down complex subjects into simpler components…"                                                                                                               | general             | GB25                |

### Probably present, unconfirmed

All of these are UNVERIFIED as glossary entries:

- Sharp, square, and steam as standalone entries. "Sharp" appears only inside Limited; only "Steam
  chasing" is confirmed.
- p(doom) and x-risk as standalone entries. They are referenced in Doomer and EA. The index has
  "p(doom)".
- Edge as a glossary headword (I only saw the main-text definition) and Expected value as a headword
  (only an inferred tail).
- Contrarian. It appears only inside the Rationalism entry.
- Signal/noise. The index has "signal-to-noise".
- Running good / heater. The index has "running good".
- Hedge, hedge fund, short, long, convexity, optionality, fat tails, bag holder, pot odds, implied
  odds, Nash equilibrium as a headword (it is used inside Mixed strategy and GTO), Pascal's mugging,
  repugnant conclusion, galaxy-brained, inside/outside view, shape rotator.

Queries for every one of these came back empty or with non-entry text. Absence from a snippet is
weak evidence, so these may still be in the book.

---

## 3. Shared vs tribe-specific, and how Riverians talk

**Genuinely shared across poker/trading and rationalism** (Silver defines them in ways that bridge
both):

- Bayesian/prior/update, calibration, EV and the EV maximizer, Kelly/bankroll/risk of ruin,
  variance, results-oriented thinking vs process, raise-or-fold, edge/alpha/advantage play, tail
  risk/black swan, steelman.
- The bridge is explicit in a few places:
  - Prior was originally a statistical term but is "now used widely" beyond stats.
  - Bad beat is "Often extended by Riverians to everyday situations."
  - Raise-or-fold carries a poker concept into general strategy.
  - The degen entry spans gambling and crypto. Whale is defined twice: negative in poker, positive
    in crypto.

**Assigned to one tribe:**

- **Upriver (EA/rat/AI):** motte-and-bailey ("nerdy"), rationalism/rat, longtermism, utilitarianism
  variants, doomer, takeoff, alignment, e/acc, wordcel, bag of numbers.
- **Downriver:** card counting, pit boss, locals casino, TAG/LAG, nit, fish, beard, public.
- **Midriver:** bid-ask, alpha, accelerator, Moneyball-ization.
- **Archipelago:** rug pull, pump-and-dump, Ponzi, apeing.

**Entries where Silver comments on the language itself** (the best material for a slang deep-dive):

1. **Update**: Riverians use it "as a somewhat pretentious way to refer to changing one's mind." He
   is self-aware about Bayes-speak as status signaling.
2. **Motte-and-bailey**: "A nerdy Riverian term."
3. **The SBF disclaimer trope**: a "Riverian trope for a legalistic disclaimer that means the
   opposite of what it says."
4. **Bad beat**: Riverians extend it to everyday life.
5. **Decoupling**: "Riverians love to decouple, thinking it allows for un[biased] analysis, whereas
   Villagers like to consider facts…" in context. Decoupling is framed as the cognitive-style marker
   that separates the River from the Village.
6. **Results-oriented thinking**: it "predomi[nates] outside the River."
7. **EV maximizer\***: "A typical citizen of the River".
8. **Quant**: "A Riverian archetype".
9. **Nit**: the word also connotes "cheapness or neuroticism."
10. **Fish**: an insult, hence "don't tap the glass." That is a norm about speech at the table.
11. **Card counting**: a usage policing note ("don't use this for other card games").

**How Riverians THINK, per Silver:** analytical, abstract (model-building), and decoupling form the
cognitive cluster. Competitive, critical, independent-minded (contrarian), and risk-tolerant form
the personality cluster (Introduction, ~p. 24). Elsewhere, risk-takers are "process oriented, not
results oriented" and "conscientiously contrarian" (Kindle locs 4067, 4306, via Zvi).

---

## 4. Critiques of the framing

1. **Leif Weatherby & Ben Recht, "The Bookmaker," _The Point_, 2024-08-22**
   ([link](https://thepointmag.com/politics/the-bookmaker/)). The map is incoherent: "As a
   geographical construction, it makes little sense." Silver didn't coin the Village: "the Village
   is, in fact, an old internet meme" (a progressive-blog insult for the DC establishment). Sharpest
   point: "the River is the casino itself, rather than the gamblers who play there." The house, not
   the EV-maximizing gambler, is the real winner.
2. **Dave Karpf, _Foreign Policy_, 2024-09-20**
   ([link](https://foreignpolicy.com/2024/09/20/on-the-edge-book-review-nate-silver-risk/);
   [Substack follow-up 2024-09-21](https://davekarpf.substack.com/p/what-nate-silver-gets-wrong-about)).
   The book "is an ode to the expected-value-maximizing gamblers' mindset" with no notion of
   systemic risk. Riverians "are winning because we have constructed a system that they are
   well-positioned to exploit." On the Riverian-vocabulary flattery: "Cost-benefit analysis is not
   some arcane Riverian wisdom. It is intro-level textbook material."
3. **Andrew Gelman, 2024-08-13**, "The River, the Village, and the Fort"
   ([link](https://statmodeling.stat.columbia.edu/2024/08/13/the-river-the-village-and-the-fort-nate-silvers-new-book-on-the-edge/);
   Cloudflare blocked my fetch, so this is secondhand via xquant). Two groups don't cover the space.
   He adds "the Fort," a right-wing, risk-averse establishment (Ted Cruz, Samuel Alito) mirroring
   the Village.
4. **xquant, "On The Edge: a Riverian memoir written for the Village," 2024**
   ([link](https://xquant.substack.com/p/on-the-edge-a-riverian-memoir-written)). "I couldn't
   properly pin down the River as a group." The River is really defined as Silver's personal overlap
   set, and the Village is its out-group by Scott Alexander's "proximity plus small differences."
   This also says something about the glossary: it is a dialect built around one person's résumé.
5. **Zvi Mowshowitz, 2024**
   ([link](https://thezvi.substack.com/p/book-review-on-the-edge-the-fundamentals)). Friendly but
   corrective. "What Nate Silver is calling 'contrarian' here is what I'd call 'oppositional.'" Real
   contrarianism is what Silver calls independence. Trump fits neither tribe. Also **Peter
   McCluskey, LessWrong, 2024-08-30**
   ([link](https://www.lesswrong.com/posts/jhzY8mTdrcJrL4J9s/book-review-on-the-edge)): like any
   tribal divide, some of the trait correlations are arbitrary, so don't over-theorize it.

Two more points. On the glossary itself, the **Variance** entry's "square root of the standard
deviation" is a straightforward math error in a glossary whose premise is quantitative fluency.
Drayton D'Silva
([Enterprise Value, 2024-08-16](https://enterprisevalue.substack.com/p/nate-silvers-on-the-edge-is-meh-but))
catalogs other finance errors (hedge-fund mandates, VC vs S&P, IRR) but not this one.

Silver responded a year later
([Silver Bulletin, 2025-08-12](https://www.natesilver.net/p/one-year-later-is-the-river-winning)).
He says the River is "more than just a literary device," concedes there is no neat one-to-one
mapping onto parties, and calls the River "less of a discrete community than the Village."

---

## 5. Where to read the full thing

- **Book:** Glossary at ~**pp. 477–501**. That pagination holds in both the 2024 Penguin Press
  hardcover (ISBN 9781594204128) and the 2025 Penguin Books paperback (ISBN 9780593491645, 576 pp.,
  new preface). It sits after "Acknowledgments, Methods, and Sources" and before the Notes. The
  cognitive/personality cluster table is in the Introduction, ~p. 24.
- **Online legally:** no full excerpt exists. Silver's Substack posts ("Welcome to the River," 2024;
  "One year later, is the River winning?," 2025) explain River/Village but don't reproduce the
  glossary.
  - **Google Books search-inside works per term.** Open
    https://books.google.com/books?id=doPqEAAAQBAJ in a browser and search a headword. The UI needs
    JavaScript, so curl gets a captcha page; the legacy feed is what I used.
  - Amazon "Look Inside" and Kindle samples cover only the front of the book, so they won't reach
    p. 477.
  - archive.org has no copy: an advanced search returned 0 hits.
- **Fastest full access:** a library ebook (Libby) or the Kindle edition. The glossary is searchable
  there and runs about 25 pages.
