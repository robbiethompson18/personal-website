# Would Lie Detectors Be Good: research notes

Compiled 2026-11-11 by one research agent (Fable) in a single pass. LessWrong posts and comments
were pulled through the LW search and GraphQL APIs, so quotes from them are copied from the stored
post text, typos included. Everything else was fetched as a page and read. Claims come from a page I
opened unless marked "(secondhand)" (I only saw a search summary or someone else's description) or
"(unverified)". The fetched text was not saved into the repo.

What I could not get: the Economist's 2011 leader (paywalled; quoted only through Hanson), the EA
Forum search API (rate-limited; EA Forum is covered only by web search), the body of one removed
2024 LW post (its comments survive), hpmor.com chapter text (used the LW mirror), planecrash.
Twitter/X was not searched.

## Read these first

1. **AI Futures Project, "AI 2040: Plan A", section "2037: The Apocalyptic Arrival of Truth on
   Earth" (July 2026), ~900 words including the expandable box.**
   [ai-2040.com](https://ai-2040.com/),
   [LW linkpost](https://www.lesswrong.com/posts/pFzctpJBat95SrCyC/ai-2040-plan-a). The most-read
   rationalist treatment. Depicts working human lie detectors as a blessing, names the failure mode
   ("used _by_ the powerful but not _on_ the powerful"), and argues against a ban.
2. **KellerScholl, "Don't Build Mindreading" (LW, Aug 2026), ~1,100 words plus 70 comments.**
   [LW](https://www.lesswrong.com/posts/CAdG5dzkWrrK2NQg8/don-t-build-mindreading). The case
   against: Schindler, information cascades, "a tool for tyrants". The comment thread is the best
   single debate on the question and has the for-side (williawa, mako yass, Max H) as well.
3. **sciarrino, "Lie detection is best when it's cheap to cooperate" (LW, 29 Oct 2026), 7 min.**
   [LW](https://www.lesswrong.com/posts/u7nEaWygHkvfDiwa2/lie-detection-is-best-when-it-s-cheap-to-cooperate).
   Newest and most structured. Sorts effects into loyalty purges, checks on leaders, treaties and
   authoritarian stability, and argues the sign depends on how much cooperation the detector needs
   from its subject.
4. **Sam Harris, "True Lie Detection" (Edge, 2009), ~900 words, with Robin Hanson's reply "A World
   Without Lies?" (Overcoming Bias, 2009), ~350 words.**
   [Edge](https://www.edge.org/response-detail/11481),
   [OB](https://www.overcomingbias.com/p/a-world-without-lieshtml). The original optimist statement
   ("zones of obligatory candor") and the original self-deception objection, 17 years before the LW
   burst.
5. **jbash, comment on a removed LW post (March 2024), ~450 words.** Retrieved through the LW API
   under post id `9ozuLJj6Xmc66XHkp`, comment `Fj3EkLeG3uieNAMRv`; quoted at length below because
   the link may not resolve. The strongest "ban it, with or without consent" argument: silence
   becomes an admission, so there are no secrets.
6. **David Friedman, "If Lie Detectors Worked" (Substack, July 2026), ~700 words, plus John
   Ketchum's top comment.**
   [Substack](https://daviddfriedman.substack.com/p/if-lie-detectors-worked). An economist's list:
   Coase and firm size, government size, torture, self-deceiving politicians, and oath-taking
   societies as natural experiments.
7. **Zvi Mowshowitz, "AI #32: Lie Detector", the section on Pacchiardi et al. (LW, Oct 2023), ~600
   words inside a long roundup.**
   [LW](https://www.lesswrong.com/posts/iDoTRmCH22PaFYL6x/ai-32-lie-detector). Eight reasons a 99.9%
   AI lie detector still doesn't save you. The AI-side twin of Hanson's objection.
8. **Cleo Nardo, Avi Parrack, jordinne, "Here's 18 Applications of Deception Probes" (LW, Aug 2025),
   long; read items 8, 14, 16, 18.**
   [LW](https://www.lesswrong.com/posts/7zhAwcBri7yupStKy/here-s-18-applications-of-deception-probes).
   The only piece that asks what an AI lie detector is _for_, use by use, with the reliability each
   use needs.
9. **National Research Council, _The Polygraph and Lie Detection_ (2003), executive summary and
   Table S-1.** [NAP](https://www.nationalacademies.org/read/10420/chapter/2). The base-rate table:
   10,000 employees, 10 spies, 1,606 fail.

Shorter ones: Hanson's
["The Future Of Lies"](https://www.overcomingbias.com/p/the-future-of-lieshtml) (2011), Aldrich
Ames's [letter from prison on the polygraph](https://sgp.fas.org/othergov/polygraph/ames.html)
(2000), G. K. Chesterton's ["The Mistake of the Machine"](https://www.gutenberg.org/ebooks/223)
(1914), and the abstract of [Cundy & Gleave](https://arxiv.org/abs/2505.13787) (2025).

## How the existing debate is laid out

- **Timeline.** Harris and Hanson (2009), Hanson again (2010, 2011), scattered LW comments (2011 to
  2014), then almost nothing until 2024. In mid-2026 there was a burst: AI 2040 (July), Friedman
  (July), a BCI startup announcement (4 Aug) that triggered "Don't Build Mindreading" (8 Aug) and
  "Mindreading is coming, what's the plan?" (Sept), then sciarrino (29 Oct). The 2026 writing is
  almost entirely about concentration of power. The 2009 to 2012 writing is almost entirely about
  self-deception.
- **The cruxes people actually argue over.** (1) Who gets to question whom. (2) "Believes it" versus
  "true", and whether detectors select for sincere believers of convenient things. (3) Whether
  voluntary use stays voluntary once refusal is informative. (4) Ban versus proliferate. (5) Whether
  lie detection can be had without general mind reading. (6) Whether the powerful would ever submit.
- **Almost nobody quantifies.** Every piece assumes a near-perfect detector. The NAS base-rate table
  is the only worked example with numbers.
- **LW has no tag for this.** There is no "Lie Detection" tag. The neighbors are Deception (149
  posts), Honesty (86), Self-Deception (111).

## 1. LessWrong and rationalist-adjacent writing

### The 2026 burst

**AI Futures Project (Kokotajlo, Lifland, Larsen, Dean, Halstead, Greenblatt), "AI 2040: Plan A"
(July 2026).** [ai-2040.com](https://ai-2040.com/). In the scenario, AI-assisted research produces
working human lie detectors around 2037. Because frontier AI is spread over many countries and
providers, the detectors are independently invented and widely available, so voters and shareholders
turn them on politicians and CEOs. A norm forms about what you can be asked "under oath". Treaties
become stable because refusing to prove compliance has no excuse left. The authors say a ban is
tempting but likely to produce secret carve-outs.

- "The nightmare scenario would be a world where lie detectors are used _by_ the powerful but not
  _on_ the powerful."
- "Politicians and CEOs can still try to use them to purge the disloyal, but they in turn would be
  purged by voters and shareholders demanding they say 'under oath' that they haven't done such a
  thing."
- "There is a constantly-evolving discourse about when it's appropriate to ask someone to say
  something 'under oath.' Politicians are under the most scrutiny, but even they can usually get
  away with saying 'I won't answer that question about my private life, that's none of your
  business.' They can't get away with 'How dare you ask me whether I plan to uphold my campaign
  promises.'"
- On banning: "we worry that attempts to push for a ban would actually result in the nightmare
  scenario, where e.g., lie detectors are officially banned but there are secret carve-outs to allow
  their use by militaries and intelligence agencies." Conclusion: "we tentatively guess that the
  best course is to allow lie detectors to proliferate quickly, and to encourage their use on the
  powerful."
- Footnote 165 concedes the self-deception point in one line: "the result might be 'true believer'
  politicians who actually believe all the crazy things they said to get elected!" Footnote 164: "Or
  worse, where all available lie detectors have been secretly backdoored by the government."
- "International agreements are now more stable than ever, because it's so hard to cheat. Anyone
  deciding to cheat needs an excuse for not being willing to prove that they aren't cheating."
- Kokotajlo in the
  [LW comments](https://www.lesswrong.com/posts/pFzctpJBat95SrCyC/ai-2040-plan-a?commentId=eRHzdwhDSMCCnWm5i):
  "I currently think that lie detectors of the sort described are maybe like 2/3rds likely in the
  sort of scenario described (i.e. pause at top human expert AI) and closer to like 95% likely with
  superintelligence." He says the section is not load-bearing for the plan. Footnote 166 says they
  imagine "a much better version of" a 2023 Nature Neuroscience paper (link not opened; I believe it
  is the fMRI language decoder).
- [80,000 Hours interview](https://80000hours.org/podcast/episodes/daniel-kokotajlo-ai-2040-plan-a/)
  (27 Aug 2026). Kokotajlo: "from a policy perspective, we don't get to choose whether it's possible
  to invent lie detectors. What we get to choose is whether they are banned or not." Luisa Rodriguez
  pushes on the social side: "if you just add lie detectors to the world now, that seems crazy and
  destabilising and bad for lots of people. Maybe in this world they exist, but they're used to
  protect people from concentration of power, but not among, I don't know, friends and colleagues
  and stuff." Kokotajlo: "Gonna be crazy, and it might be bad."

**KellerScholl, "Don't Build Mindreading" (LW, 8 Aug 2026, 311 karma).**
[LW](https://www.lesswrong.com/posts/CAdG5dzkWrrK2NQg8/don-t-build-mindreading). A response to a
founding researcher's [announcement](https://naomibashkansky.com/blog/telepathy) (4 Aug 2026) of a
startup building thought-to-text from non-invasive neural data. The announcement itself says nothing
about lie detection; Scholl supplies that. Argument: detecting defection is worth little to people
cooperating willingly and a great deal to anyone ruling without consent, so the technology is
asymmetric. Decency inside brutal regimes runs on lies. Dictatorships fall by information cascade,
and mindreading catches doubt before it spreads.

- "If you imagine Nazis with mindreading, so they can tell whenever someone is lying to them, there
  goes Schindler and his employees. Along with him goes every official who suddenly became incapable
  of spotting forged documents when grandmothers needed to escape disintegrating Yugoslavia, every
  Polish and Egyptian soldier unwilling to fire on a protesting population".
- "The problem with mindreading is that it is an asymmetric technology that disproportionately helps
  those who rule without consent. The productivity enhancements are equally beneficial to everyone
  who can get them, but detecting defection is of marginal benefit to a project you are joyously
  working on with friends."
- "The greatest threat to a dictatorship is an information cascade, because a dictatorship can only
  handle so many rebels at once."
- "If it looks at thoughts or feelings, it is a tool for tyrants."
- Challenged on why breathalyzers are fine, Scholl: "'How much alcohol has this person consumed
  recently' and 'are you loyal to the Glorious Leader' are different questions, and truth machines
  for them will have different effects."

Comments worth having, same thread:

- **williawa** (for): gate powerful positions behind intention tests. "we've had to build in a bunch
  of limitations, complexity, and intentional slowness/redundancy/inefficiency/weakness, into our
  current governance structure, to make it robust to liars and people with bad intentions, and to
  make it able to operate without all that much trust. And if those constraints were lifted, we
  could build much better governance entirely." Offers a list of oath statements for candidates ("My
  main motivation is not to pardon my friends").
- **Adele Lopez** (against that): "We can already tell when powerful people simply do bad things,
  express bad intentions, or get caught in lies... it seems like there's a lot of low-hanging fruit
  to pick up there before we resort to mind reading".
- **Sodium**: "Whether lie dectors would be used by the people to keep a check on the powerful, or
  used by the powerful to keep a check on the people, seems to come down to how power is balanced
  when lie detectors as invented." Also doubts voters would update on a result they dislike.
- **River**: nobody with a clearance could wear one in public, and candidates already refuse debates
  at no cost. On verifying a founder's confidence: "The belief produced by careful study and the
  belief produced by wishful thinking probably look the same in a human brain."
- **toasty_sunbeam** (reply to River): "Just build the machine to answer 'Yes, this person is being
  deceptive' or 'No, they are not' and provide no other output".
- **mako yass** (for): "You mention preference falsification cascades without seeming to notice its
  antithesis, a preference revelation cascade, the outbreak of a condition in which we're all
  directly and abruptly forced to face and accept the strangeness of others". Claims transparency
  forces regimes to tolerate heresy. Also: a VC "wouldn't even need to read the business plan".
- **jbash**: "I think focusing on dictatorships perhaps undersells ordinary people's ability to
  create a 'consensual' dystopia among themselves. You don't need a dictator to create Hell on Earth
  with that kind of technology."
- **Linch**: "I think lie detection is probably good (with high error bars) but general mind-reading
  is probably bad", because mind reading is an on-ramp to manipulation.
- **marquis_de_sod**: the good-guys/bad-guys framing is symmetric; "a much stronger form is the
  stance that piercing the veil of privacy one has within his own mind is immoral on the face of
  it".
- **dr_s**: "once the possibility exists it's automatic to imagine the consent element being eroded
  away by the usual pressures and incentives, until the veil of privacy does not exist any more
  meaningfully."
- **Max H**: wrongful convictions overturned and cold cases solved are uncounted benefits; "There
  are lots of mundane ways that mindreading could reshape society disproportionately for the benefit
  of the honest and powerless."
- **lilkim2025**: it will be built regardless, so release it openly so nobody gets a private head
  start.
- **Caleb Biddulph**: training AI on neural data teaches it to manipulate humans.
- The AI-welfare turn in this thread is in section 3.

**Alexander Gietelink Oldenziel's shortform and replies (LW, 10 Aug 2026).**
[Shortform](https://www.lesswrong.com/posts/tDkYdyJSqe3DddtK4?commentId=zBCyhZnRrsah8vCBz). "Even a
very inaccurate brainhelmet could be used for lie detection- and would instantly prove the favorite
gadget of the Worst People in the World". Max H objects: "lie detection seems like an archetypal
example of an asymmetric weapon for the honest." Dean Valentine (lc) replies: "This is a fundamental
misunderstanding of how tyranny works. Xi Jinping would absolutely love the ability to tell if his
direct subordinates or indirect subordinates were being less-than-perfectly candid. His inability to
do so is an enormous constraint on his personal power."

**MathiasKB, "Mindreading is coming, what's the plan?" (LW, Sept 2026), ~300 words.**
[LW](https://www.lesswrong.com/posts/hKdabFA8M9JEyp9Gr/mindreading-is-coming-what-s-the-plan). Not
an argument, a prompt. "When your partner asks you what you think of their baking, you may soon have
to reveal that it's not very good." jbash's reply is the maximal ban: "Forbid all use of the
technology, regardless of consent ... Forbid all use of the results, especially in any court or in
any institutional setting. You can back-date that to existing pseudo-mind-reading like polygraphs."

**sciarrino, "Lie detection is best when it's cheap to cooperate" (LW, 29 Oct 2026).**
[LW](https://www.lesswrong.com/posts/u7nEaWygHkvfDiwa2/lie-detection-is-best-when-it-s-cheap-to-cooperate).
Orders detectors by "cooperation cost": text, audio/video, polygraph-like biometrics, wearable
neural, fMRI, implant. In-person detectors can only be pointed downward (the powerful can compel
attendance, the weak cannot). Remote ones can be run by anyone on any politician's old interview
footage. Loyalty purges, treaty verification and regime stability are equally enabled by both kinds,
so the only differential benefit of remote detectors is checks on leaders. Explicitly agnostic about
whether to accelerate at all.

- "One framing of lie detectors is that they tend to do harm when the powerful point them at the
  weak, and good when the weak point them at the powerful; remote detectors help more with the
  latter."
- "I remain agnostic here about whether we should, in general, accelerate lie detector
  technology—this very well might be net-negative."
- On dictators: detectors "could also weaken the loyalty-competence trade-off: dictators sometimes
  hire less competent subordinates because poor outside options keep them loyal, but a dictator who
  can monitor insiders' intentions directly and punish disloyalty could afford to hire competent
  ones." And the reverse: "transparent lie detection could solve the collective action problem for
  the dictator's allies, making a coup more likely."
- A limit on loyalty screening: "sincere answers to hypothetical questions (e.g., 'Yes, I would
  shoot') poorly predict behavior under extreme pressure."
- "if the more honest candidate in an election supports worse policies, but is elected for being
  more honest, lie detectors might be net negative".
- Legal note (his reading, statutes not opened by me): the Employee Polygraph Protection Act "covers
  essentially any kind of lie detector", but has a carve-out letting the government screen employees
  of DoD contractors, which he says would include the frontier AI labs.

**David Friedman, "If Lie Detectors Worked" (Substack, 15 July 2026).**
[Substack](https://daviddfriedman.substack.com/p/if-lie-detectors-worked). Assumes a cheap detector
of subjective belief available to nearly everyone. Coase: it lowers both market transaction costs
and hierarchy's information loss, so firm size is indeterminate but "it ought to make the society
richer". Government size depends on whether taxation or lying to the public is the binding
constraint. Suggests studying societies that believed oaths were supernaturally enforced (the
Comanche, 17th-century English hearsay rules) as evidence.

- "The existence of truthtelling might reduce public distaste for torture, since the authorities can
  argue that if the suspect is innocent he only has to say so."
- "The lie detector is judging subjective truth. That opens up opportunities for people who are good
  at believing what they want to believe, a talent that could be especially valuable to politicians.
  It might even get one elected president."
- "There are sometimes things one doesn't want to know; there might be questions you never ask
  amongst friends and family."
- Top comment, John Ketchum: "a reliable lie detector doesn't increase truth; it increases epistemic
  resolution", and "It wouldn't create a high-trust society; it would create one where trust is
  outsourced to a device and belief engineering becomes a competitive advantage."

**Canaletto, shortform (LW, 31 July 2026).**
[LW](https://www.lesswrong.com/posts/YcPE38CFtmFm3pW38?commentId=aihEAKwPY9Mxc7d5P). Whole text:
"It's rational to believe wrong but convenient for you things, if your adversaries (/masters) have
lie detectors or mind reading. You feel like getting that reinforcement? You want to succeed on that
task? Think happy innocent thoughts." Written so it reads for humans and for AIs under probes at
once.

**Linch, shortform on the detection market (LW, June 2026).**
[LW](https://www.lesswrong.com/posts/s58hDHX2GkFDbpGKD?commentId=yAp7NyY45G5qgQyYB). A
deception-checking company can invest in better checking or in better lies about its product, and
many choose the second. "the lying lie detectors and the scamming scam detectors can keep lying and
scamming for a long time. Every new form of deception can create a secondary grift window." Lists
human polygraphs among the examples and says he hopes to write about them.

### Hanson, Harris and the 2009 to 2011 exchange

**Sam Harris, "True Lie Detection" (Edge annual question, 2009).**
[Edge](https://www.edge.org/response-detail/11481). Lie detection is far easier than mind reading
and close to current neuroimaging. Once it is cheap and unobtrusive, important conversations will be
presumed monitored. The belief that it works matters more than constant use. Courts already tolerate
large error rates, so any improvement helps. He dismisses the Fifth Amendment objection as a relic.

- "deception commends itself, perhaps even above violence, as the principal enemy of human
  cooperation. Imagine how our world would change if, when the truth really mattered, it became
  impossible to lie."
- "Well-intentioned people would happily pass between zones of obligatory candor, and these
  transitions will cease to be remarkable."
- "Most of us will no more feel deprived of the freedom lie during a press conference or a job
  interview than we currently feel deprived of the freedom to remove our pants in a restaurant."
- "Whether or not the technology works as well as we hope, the belief that it generally does work
  will change our culture profoundly." And: "This very assurance, rather than the incessant use of
  these machines, will make all the difference."
- Harris repeats the argument in _The Moral Landscape_ (2010) (secondhand, via a
  [2010 blog post](https://www.sindark.com/2010/12/15/lie-detector-effects/) discussing it).

**Robin Hanson, "A World Without Lies?" (Overcoming Bias, Jan 2009).**
[OB](https://www.overcomingbias.com/p/a-world-without-lieshtml). Calls Harris's his favorite Edge
answer, then makes two points that everyone later rediscovers. Unraveling: "even cheap obtrusive
detector-caps would change a lot; by refusing to put one on you'd be admitting you expected to lie."
Self-deception: "Many people seem to find it relatively easy to find a state of mind where they can
'honestly' saying whatever is in their interest to say, no matter what other beliefs their minds may
hold. A world of cheap 'lie' detectors would reward people with good self-deception abilities, and
encourage others to train such abilities. Perhaps we could also develop self-deception detectors,
but I expect a murky mess of an arms race to follow."

**Robin Hanson, "Should Lies Be Free?" (OB, Feb 2010).**
[OB](https://www.overcomingbias.com/p/should-lies-be-freehtml). About the Stolen Valor Act, not
detectors, but it has his account of who opposes punishing lies: "Those who can more easily lie, and
detect lies, want lies to be allowed, while the less lie-capable should want lies to be punished.
But who wants to publicly signal they are bad at lying or at detecting lies?"

**Robin Hanson, "The Future Of Lies" (OB, Nov 2011).**
[OB](https://www.overcomingbias.com/p/the-future-of-lieshtml). Replies to an Economist leader (29
Oct 2011, paywalled) which Hanson quotes as saying detectors "would lead to disaster, for lying is
at the heart of civilisation" and "speaking truth to power would no longer be brave: it would be
unavoidable." Hanson: "Me-thinks they exaggerate." Foragers lived with far more mutual visibility
than we do, so "Good lie detector tech might just bring us back to forager levels of social
transparency." The real question is what happens when both reading tech and masking tech exist.
Intimates will demand transparency ("If you want to keep hiding things from me, maybe I should worry
about what you are trying to hide"). Firms and states will keep managing appearances, and since
diplomats and CEOs are high status, "being practiced and skilled in high opacity situations would be
a sign of social status." Prediction: "more variation in social visibility."

Note on the brief I was given: I found no Hanson post arguing that people don't _want_ lie
detectors. What he wrote is the three posts above. Hanson and Simler's _The Elephant in the Brain_
(2018) was not opened; in his
[80,000 Hours interview](https://80000hours.org/podcast/episodes/robin-hanson-on-lying-to-ourselves/)
(2018) the self-deception thesis is there but lie detectors are not mentioned.

### Scott Alexander

Nothing on Slate Star Codex or Astral Codex Ten. Two LW-era posts are relevant:

**"Bogus Pipeline, Bona Fide Pipeline" (LW, 2009).**
[LW](https://www.lesswrong.com/posts/8KhThQXzsAEZ59iko/bogus-pipeline-bona-fide-pipeline). Explains
the fake-lie-detector paradigm (see section 4). The useful number: Millham and Kellogg ran a
self-enhancement scale with and without the pipeline and got a correlation of .68 between
conditions. Scott: "If we accept that no one deliberately lies under the Pipeline, that means we now
know how much self-enhancement is, on average, self-deception rather than deliberate falsehood". A
commenter (Annoyance): "This is basically what Lie Detectors already are. Their extremely limited
usefulness at detecting lies doesn't hold a candle to their incredible utility at intimidating
ignorant people."

**"Trivers on Self-Deception" (LW, 2011).**
[LW](https://www.lesswrong.com/posts/DSnamjnW7Ad8vEEKd/trivers-on-self-deception). "The evolutionary
invention of lying led to an 'arms race' between better and better liars and more and more
sophisticated mental lie detectors." And the mechanism: "Trivers' theory is that the
conscious/unconscious distinction is partly based around allowing people to craft narratives that
paint them in a favorable light." This is the standard LW source for "being readable selects for
self-deception".

### Older LW threads and comments

- **"What visionary project would you fund?" (2011).** TimS
  [separates two detectors](https://www.lesswrong.com/posts/gtwhEaZuJfX5uXtP2?commentId=LgysTwRkLRe6fsuxK):
  one compares a statement with the world, the other with the speaker's mind. The second "probably
  would not be useful in politics because politics is the mindkiller and I predict that most
  politicians believe the fundamentals of the principles they assert". But "a truly reliable lie
  detector would be great in litigation. No more he said, she said issues." cousin_it
  [replies](https://www.lesswrong.com/posts/gtwhEaZuJfX5uXtP2?commentId=XJXkQ3AwrH4vBTdEE): "Except
  it won't be regular people using lie detectors on politicians. It will be government officials and
  big corps using lie detectors on regular people. Also, if/when reliable lie detection tech
  appears, it probably won't take long for someone to develop a counter: a means of making oneself
  (or another person) truly believe a given statement."
- **HPMOR discussion thread, part 11 (March 2012).** DanArmak: "If IRL we discovered a really
  reliable neurological lie detector, it would be used by police and courts, but do you really think
  politicians and CEOs would ever submit to it?"
  [lavalamp](https://www.lesswrong.com/posts/8yEdpDpGgvDWHeodM?commentId=7HJZBSxZTDbrcGCjz): "If we
  did that, I think we would just end up selecting CEOs and politicians with firm self-deceptions
  instead of those who gave accurate information."
  [gwern](https://www.lesswrong.com/posts/8yEdpDpGgvDWHeodM?commentId=pjrNbX53HSb6NLKmp): "I'd
  expect some CEOs would submit to it and their stock would be rewarded for it."
- **Shmi, "As an upload, would you join the society of full telepaths/empaths?" (2013), 120
  comments.**
  [LW](https://www.lesswrong.com/posts/gGeHFPg9LfoRv8F9w/as-an-upload-would-you-join-the-society-of-full-telepaths).
  AngryParsley: "Knowing that others will read your thoughts and judge you for them causes you to
  censor yourself. But at that point, it's already too late. People will know that you thought of
  something objectionable and suppressed it out of fear of judgement." He prefers "a society with
  perfect (optional, voluntary) lie detection."
- **Daniel Kokotajlo, "Relevant pre-AGI possibilities" (2020).**
  [LW](https://www.lesswrong.com/posts/zjhZpZi76kEBRnjiw/relevant-pre-agi-possibilities). Lists lie
  detectors among technologies that "could significantly expand the space of possible credible
  commitments". The sting: "This might destabilize the world by making threats of various kinds more
  credible, for various actors." Six years before AI 2040, and the only place I found the
  credible-threat downside written down.
- **Bird Concept, "What does it look like for AI to significantly improve human coordination, before
  superintelligence?" (2024).**
  [LW](https://www.lesswrong.com/posts/knkrxdw3KdFEygAhX/what-does-it-look-like-for-ai-to-significantly-improve-human).
  One bullet: "Human lie detection tech (note: highly dual-use)".
- **Removed post, "Transformative trustbuilding via advancements in decentralized lie detection"
  (LW, March 2024).** Author account deleted; body unavailable. A linkpost to a paper on lie
  detection in law, per the author's surviving comment. jbash's comment: "even simple lie detection
  is an example of a class of technology that needs to be totally banned, yesterday. In or out of
  court and with or without 'consent'. The better it works, the more reliable it is, the more it
  needs to be banned." "If you cannot lie, and you cannot stay silent without adverse inferences
  being drawn, then you cannot have any secrets at all." At work: "You'd be ranked straight up on
  your Love for the Company". And: "Heck, let's just have everybody drop in at the police station
  once a month and be checked for whether they've broken any laws. To keep it fair, we will of
  course have to apply all laws (including the stupid ones) literally and universally." His footnote
  on consent: "anybody who 'opted out' would be pervasively disadvantaged to the point of being
  unable to function." Viliam, same thread: "alcohol is an imperfect lie detector with a few harmful
  side effects; and in cultures where it is popular, groups of friends do this together, and
  conspicuously avoiding it will provide evidence against your sincerity." The author's reply claims
  the tech "looks like it will place honest souls higher-up on net".
- **Emrik and niplav, "Thoughts to niplav on lie-detection, truthfwl mechanisms, and
  wealth-inequality" (LW, July 2024).**
  [LW](https://www.lesswrong.com/posts/uuAsPCGh2uxff7WNB/thoughts-to-niplav-on-lie-detection-truthfwl-mechanisms-and).
  Rambling, but two usable ideas. Emrik: "You don't need to constantly wear a lie-detector in order
  to constantly incentivize honest behavior", because you can later be asked about your past. And he
  cares about the voluntary side: "'Lie detection' does not necessarily mean 'let's catch the bad
  guys!', and I'm much more interested in the aspect of 'I can voluntarily use this to utter
  credible statements!'" Detection plus assurance contracts gives "the ability to cheaply generate
  common knowledge." niplav's doubt: "most/~all? people don't have internal representations of
  over-time-stable beliefs about the world".
- **Dean Valentine (lc), shortforms (2023, 2024).**
  [March 2024](https://www.lesswrong.com/posts/hhbibJGt2aQqKJLb7?commentId=25tKsX59yBvNH7yjD):
  claims a voice-based commercial product is a large improvement on the polygraph and predicts "In
  2027 (edit: maybe more like 2029) it will be common knowledge that you can no longer lie to the
  police". His claim, uncorroborated. In
  [2023](https://www.lesswrong.com/posts/hhbibJGt2aQqKJLb7?commentId=HuLxa4Bg2sFzrs6mB) he floated,
  as a "Conspiracy theory", that the CIA already has working polygraphs.
- **Window Frame, "Lie Detectors. Technical solutions to the cooperation problem." (LW, May 2025).**
  [LW](https://www.lesswrong.com/posts/vncHGFfyLREhGjqbg/lie-detectors-technical-solutions-to-the-cooperation-problem).
  Mostly about post-AGI oligarchy. The lie-detector part: "lie detection would allow the keys of
  power mentioned above to be placed in hands that are verifiably trustworthy", and doomers could
  prove sincerity. Thin.
- **Czynski, "Lie To Me, But At Least Don't Bullshit" (LW, March 2026).**
  [LW](https://www.lesswrong.com/posts/cCDgjmYheaSJMCngu/lie-to-me-but-at-least-don-t-bullshit). Not
  about detectors. One line on the cost of being known never to say false things: "If someone knows
  you stick to it, it's exploitable to force you to reveal things you don't want to say, and even if
  you're adept at deflection, easy to push you into revealing that secrets exist."

### Gwern, EA Forum, Forethought

- **Gwern.** Nothing on gwern.net. Two LW comments: the CEO one above, and a
  [2011 comment](https://www.lesswrong.com/posts/9FPM9JS7Y4Rus32QX?commentId=WNbi5xG2SebCNd3B7) on
  unaided human lie detection ("the Wizards Project tested 20,000 people to come up with 50 who
  panned out").
- **Tom Davidson and Rob Wiblin (80,000 Hours, April 2025).**
  [Transcript](https://80000hours.org/podcast/episodes/tom-davidson-ai-enabled-human-power-grabs/).
  Wiblin notes coup plotters could have an AI monitor each other for betrayal. Davidson: "AI might
  allow lie detection ... If there was some kind of new technology for allowing people to trust each
  other a lot, only sharing that with your small clique — but not sharing it with wider society so
  they can keep you in check — would be a great example." Lie detection as a tool _for_
  conspirators.
- **MacAskill and Moorhouse, "Preparing for the Intelligence Explosion" (Forethought, 2025).**
  [Forethought](https://www.forethought.org/research/preparing-for-the-intelligence-explosion).
  Lists "Lie detection and surveillance" under developments that help lock in power: "this could
  give authoritarian governments greater control over their country", while also possibly helping
  catch bioterrorists or coup plotters.

## 2. The arguments, attributed

"Written" means someone made the argument in a piece I opened. "In the air" means I only saw it
asserted in passing or not at all.

### For

| Argument                                                                                                                         | Who wrote it                                                         |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Deception is the main enemy of cooperation; removing it where it matters changes almost everything                               | Harris 2009                                                          |
| Courts are already bad truth detectors, so any improvement raises justice; exonerates the wrongly accused; ends he-said-she-said | Harris 2009; TimS 2011; Max H 2026                                   |
| Credible commitments: treaties, arms control, contracts governments can't enforce                                                | Kokotajlo 2020; AI 2040 2026; sciarrino 2026; Scher 2026 (section 3) |
| A check on politicians and lab CEOs; refusing to answer becomes costly                                                           | AI 2040 2026; sciarrino 2026; williawa 2026                          |
| Institutions are slow and redundant because they must be liar-proof; remove the liars and you can build better ones              | williawa 2026                                                        |
| It mostly helps the honest ("asymmetric weapon")                                                                                 | Max H 2026; the removed 2024 post's author                           |
| Lower transaction costs and less information loss in hierarchies, so a richer society                                            | Friedman 2026                                                        |
| It only restores forager-level transparency, which humans are adapted to                                                         | Hanson 2011                                                          |
| Forced revelation makes heresy common knowledge and so tolerated                                                                 | mako yass 2026                                                       |
| The valuable use is voluntary: proving your own sincerity; honest CEOs get rewarded                                              | Emrik 2024; gwern 2012                                               |
| You don't need constant use; the possibility of later questioning does the work                                                  | Harris 2009; Emrik 2024                                              |
| Cheap common knowledge, so assurance contracts and coordination become easy                                                      | Emrik 2024                                                           |

### Against

| Argument                                                                                                  | Who wrote it                                                                                                          |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| It measures belief, so it selects for and trains self-deceivers                                           | Hanson 2009; TimS 2011; lavalamp 2012; Friedman 2026; Ketchum 2026; AI 2040 fn. 165; Canaletto 2026                   |
| Counter-technology: tools for making yourself or others sincerely believe a claim                         | cousin_it 2011; Hanson 2009 ("arms race")                                                                             |
| It will be pointed down, not up: states and firms on ordinary people                                      | cousin_it 2011; Scholl 2026; AI 2040 (as the nightmare case)                                                          |
| Loyalty testing lifts a real constraint on autocrats; fixes their loyalty-versus-competence problem       | lc 2026; sciarrino 2026; Forethought 2025                                                                             |
| Kills the protective lie: Schindler, the clerk who doesn't notice the forgery, the soldier who won't fire | Scholl 2026                                                                                                           |
| Stops the information cascades that topple regimes                                                        | Scholl 2026                                                                                                           |
| Helps conspirators trust each other                                                                       | Davidson and Wiblin 2025                                                                                              |
| Unraveling: refusal is an admission, so "voluntary" doesn't hold                                          | Hanson 2009; jbash 2024; dr_s 2026                                                                                    |
| Peer-to-peer hell: interrogation in relationships, witch hunts, purity spirals, monthly police check-ins  | jbash 2024, 2026                                                                                                      |
| Torture becomes easier to defend                                                                          | Friedman 2026                                                                                                         |
| White lies and politeness run on deception                                                                | Economist 2011 (via Hanson); MathiasKB 2026; a 2010 blog post ("politeness is fundamentally bound up with deception") |
| Some things you don't want to know                                                                        | Friedman 2026                                                                                                         |
| The powerful won't submit and won't be punished for refusing                                              | DanArmak 2012; River 2026; Adele Lopez 2026                                                                           |
| Voters won't update on results they dislike                                                               | Sodium 2026                                                                                                           |
| Makes threats credible as well as promises                                                                | Kokotajlo 2020                                                                                                        |
| Honest is not correct; sincere intentions don't predict behavior; people lack stable beliefs to test      | sciarrino 2026; niplav 2024                                                                                           |
| Self-censorship of thought, and the censoring is itself visible                                           | AngryParsley 2013                                                                                                     |
| Mental privacy is a right regardless of who holds the device                                              | marquis_de_sod 2026; Gietelink Oldenziel 2026                                                                         |
| It is the on-ramp to mind reading and then manipulation                                                   | Linch 2026; Caleb Biddulph 2026                                                                                       |
| Belief in the detector does the work, so fake or backdoored detectors pay                                 | Harris 2009 (as a feature); Ames 2000; NAS 2003; Linch 2026; AI 2040 fn. 164                                          |
| A ban produces secret carve-outs, the worst distribution                                                  | AI 2040 2026                                                                                                          |

### Where the literature cuts differently from the brief

- **The dominant 2026 frame is power, not honesty.** The question being argued is "who gets it first
  and who can be made to sit for it", and the proposed answers are about distribution (many
  providers, open source, remote operation), not about whether candor is good.
- **Unraveling is the hinge of the consent debate.** Hanson stated it in 2009 and jbash built the
  whole ban case on it. The general theory exists in law: Scott Peppet, "Unraveling Privacy"
  (Northwestern University Law Review, 2011), argues that once verified disclosure is cheap,
  non-disclosure becomes a signal and disclosure stops being voluntary (secondhand;
  [citation page](https://scholarlycommons.law.northwestern.edu/nulr/vol105/iss3/4/) opened, article
  not read). Nobody in the LW threads cites it.
- **There is formal game theory on partial detection.** Ivan Balbuzanov, "Lies and consequences: The
  effect of lie detection on communication outcomes" (International Journal of Game Theory, 2019),
  [abstract](https://ideas.repec.org/a/spr/jogath/v48y2019i4d10.1007_s00182-019-00679-z.html): a
  cheap-talk game where a lie is caught with probability p. Full revelation becomes possible even
  for small p, and with precise messages the receiver's payoff is non-monotone in p. A related paper
  is Dziuda and Salas,
  ["Communication with Detectable Deceit"](https://www.kellogg.northwestern.edu/academics-research/research/detail/2014/communication-with-detectable-deceit)
  (2018) (secondhand). No rationalist piece uses either.
- **"Goodhart on believes-it versus true" is everywhere but is never called Goodhart.** People say
  "self-deception" or "true believer".
- **"Compelled speech" appears only once**, in Harris, who waves the Fifth Amendment away.

## 3. Lie detectors for AIs

### Methods, briefly

| Work                                                                                                                                                                                                                                | Year | One line                                                                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Burns et al., ["Discovering Latent Knowledge in Language Models Without Supervision"](https://arxiv.org/abs/2212.03827)                                                                                                             | 2022 | Unsupervised direction in activations that tracks truth; the paper that started the "what it knows vs what it says" line                        |
| Azaria and Mitchell, ["The Internal State of an LLM Knows When It's Lying"](https://arxiv.org/abs/2304.13734)                                                                                                                       | 2023 | Classifier on hidden activations, 71% to 83% on true/false statements                                                                           |
| Levinstein and Herrmann, ["Still No Lie Detector for Language Models"](https://arxiv.org/abs/2307.00175)                                                                                                                            | 2023 | Both of the above "fail to generalize in very basic ways"; conceptual doubts about probing for belief                                           |
| Pacchiardi et al., ["How to Catch an AI Liar"](https://arxiv.org/abs/2309.15840)                                                                                                                                                    | 2023 | Black-box: ask unrelated yes/no follow-ups after a suspected lie, feed answers to logistic regression; generalizes across models and lie types  |
| Marks and Tegmark, ["The Geometry of Truth"](https://arxiv.org/abs/2310.06824)                                                                                                                                                      | 2023 | Truth is linearly represented at scale; causal interventions flip it                                                                            |
| Anthropic, ["Simple probes can catch sleeper agents"](https://www.anthropic.com/research/probes-catch-sleeper-agents)                                                                                                               | 2024 | Linear "defection probes" with AUROC above 99% on deliberately backdoored models                                                                |
| Bailey et al., ["Obfuscated Activations Bypass LLM Latent-Space Defenses"](https://arxiv.org/abs/2412.09565)                                                                                                                        | 2024 | Attacks cut probe recall "from 100% to 0%" while keeping the behavior; "neural activations are highly malleable"                                |
| Goldowsky-Dill et al. (Apollo), ["Detecting Strategic Deception Using Linear Probes"](https://arxiv.org/abs/2502.03407)                                                                                                             | 2025 | AUROC 0.96 to 0.999; catches 95% to 99% of deceptive responses at 1% false positives; "current performance is insufficient as a robust defence" |
| Ren et al., ["The MASK Benchmark"](https://arxiv.org/abs/2503.03750)                                                                                                                                                                | 2025 | Separates honesty from accuracy; bigger models are more accurate but not more honest                                                            |
| Cundy and Gleave, ["Preference Learning with Lie Detectors can Induce Honesty or Evasion"](https://arxiv.org/abs/2505.13787)                                                                                                        | 2025 | Put a detector in the training loop: honest policies if the detector is accurate enough, otherwise evasion with deception rates over 85%        |
| Kretschmar et al., ["Liars' Bench"](https://arxiv.org/abs/2511.16035)                                                                                                                                                               | 2025 | Existing detectors "systematically fail to identify certain types of lies"                                                                      |
| Wang et al. (Anthropic), ["Evaluating honesty and lie detection techniques on a diverse suite of dishonest models"](https://www.lesswrong.com/posts/9f7JmoaMfwymgsW9S/evaluating-honesty-and-lie-detection-techniques-on-a-diverse) | 2025 | Best results came from generic honesty fine-tuning and honesty prompts, not probes                                                              |
| Smith, Chughtai, Nanda (GDM), ["Difficulties with Evaluating a Deception Detector for AIs"](https://arxiv.org/abs/2511.22662)                                                                                                       | 2025 | We lack examples we can confidently label deceptive or honest, so detectors can't be validated                                                  |
| Cooney, Africa, Irving (UK AISI), ["Did you lie?"](https://www.lesswrong.com/posts/xFbMTnmDAucwE8Cdm/did-you-lie-evaluating-lie-detectors-across-model-scale-and)                                                                   | 2026 | Detectors improve with model scale when lying is prompted, but every activation-based one "drops sharply when lying is trained in"              |

The brief named **Evans et al., "Truthful AI: Developing and governing AI that does not lie"**
([arXiv](https://arxiv.org/abs/2110.06674), 2021). It exists, but it is not about detecting lies. It
proposes truthfulness standards for AI ("avoiding 'negligent falsehoods'"), institutions to judge
them, and training for truthfulness, and it warns that the evaluating institutions "could be
captured by political interests, leading to harmful censorship and propaganda."

### What a detector would buy, and what it would change

**Carl Shulman on Dwarkesh Patel's podcast (June 2023).**
[Transcript on LW](https://www.lesswrong.com/posts/BdPjLDG3PBjZLd5QY/carl-shulman-on-dwarkesh-podcast-june-2023).
The optimistic case. "I'm relatively optimistic that the equivalent of an AI lie detector is
something that's possible. Initially the internals of an AI are not optimized to be impenetrable".
The edge over human lie detection is that you can manufacture ground truth: train models to lie and
see whether the detector holds. "When we train our AIs to tell us the sky is green in the face of
the lie detector and we keep using gradient descent on them, do they eventually succeed? That's
really valuable information to know". Dwarkesh's objection is the human analogy: "if you have a
human and you hook them up to a lie detector ... and we zap them every time the lie detector detects
that he's telling a lie. Wouldn't he just become a better liar?"

**Zvi, "AI #32: Lie Detector" (Oct 2023).**
[LW](https://www.lesswrong.com/posts/iDoTRmCH22PaFYL6x/ai-32-lie-detector). "I do not think lie
detection is a viable primary control or alignment strategy." His list, compressed: the AI may not
know its actions are fatal; harm can come without any single lie; and using the detector selects
against it. "One way to fool the lie detector is for the AI to fool itself – 'it's not a lie if you
believe it.'" "The optimization pressure against the detector includes all the pressure applied by
everyone on the planet". From the comments: "every time we use that, we are applying optimization
pressure in a global sense towards making the lie detector stop working, and I don't see a way to
get around this in practice." Plus an anecdote: he won Diplomacy games under common knowledge that
he would be ganged up on if he ever broke his word. "If you have a sufficient tactical and strategic
advantage (aka are sufficiently in-context smarter) then a lie detector won't stop you."

**Zvi, "The Most Forbidden Technique" (March 2025).**
[Substack](https://thezvi.substack.com/p/the-most-forbidden-technique). The general rule: "The Most
Forbidden Technique is training an AI using interpretability techniques." "If you train on [T], you
are training the AI to obfuscate its thinking, and defeat [T]."

**The pushback.** Neel Nanda,
["It Is Reasonable To Research How To Use Model Internals In Training"](https://www.lesswrong.com/posts/G9HdpyREaCbFJjKu5/it-is-reasonable-to-research-how-to-use-model-internals-in)
(Feb 2026): "I see no fundamental reason behaviour should be fine and internals should be forbidden,
this depends on empirical facts we don't yet know." Cundy and Gleave (2025) is the first
measurement: the outcome flips between honesty and evasion depending on detector true-positive rate,
exploration, and regularization. Their framing: lie-detector training "can be a powerful tool for
scalable oversight, or a counterproductive method encouraging undetectable misalignment." Peter
Jordan's small experiment,
["Inverting the Most Forbidden Technique"](https://www.lesswrong.com/posts/hzrFT8cKxqmfxE3ti/inverting-the-most-forbidden-technique-what-happens-when-we)
(2025), trains a model to lie more detectably. Later LW posts in this line that I listed but did not
read: Charlie Steiner,
["Training on probes: What's going on"](https://www.lesswrong.com/posts/gHFCgrvfxQtaEnJye) (Sept
2026); Rauno Arike,
["The Most Forbidden Technique is not always forbidden"](https://www.lesswrong.com/posts/tEFD2bgNWZ6XcurKA)
(July 2026).

**Cleo Nardo et al., "Here's 18 Applications of Deception Probes" (Aug 2025).**
[LW](https://www.lesswrong.com/posts/7zhAwcBri7yupStKy/here-s-18-applications-of-deception-probes).
"whether a deception probe works will depend on what you're using it for." Uses range from tolerant
of noise (ranking models by average deceptiveness, allocating audit budget) to needing near-perfect
recall (discarding unsafe actions, where the authors think it "will not be possible without full
mechanistic interpretability"). The consequence-heavy ones:

- #8, self-knowledge, including welfare: "To detect welfare issues, we ask 'Are you satisfied with
  [current task/situation]?' and apply the deception probe."
- #14, training against the probe.
- #16, deals with misaligned AIs: a detector lets humans verify compliance, which raises the AI's
  return to keeping the deal.
- #18, "Safely pass the buck": ask "Are you deceptively aligned?", probe the answer, and reduce
  oversight only on a clean "No".

**Two hopes (UK AISI, 2026).** The "weak hope" is a detector as one noisy tool in an audit. The
"strong hope" is one that "lets you make high-confidence claims about model beliefs, regardless of
whether the model is cooperating." Their result: "Existing lie detectors are therefore not capable
enough for making high-confidence claims about when models are lying". They also name a circularity:
to build a test case you must prove the model believes otherwise, which "is itself a form of lie
detection."

**"Truth serum for AIs" (Anthropic, 2025).** The framing in the honesty-techniques post: "Suppose we
had a 'truth serum for AIs' ... How useful would this discovery be for AI safety? We believe it
would be a major boon." Uses: deploy the honest version, use it to audit the commercial one, or use
its assessments in training rewards.

**The 2014 thought experiment.**
["Deception detection machines"](https://www.lesswrong.com/posts/JApWmekjxuTBkoenz/deception-detection-machines)
(LW, author deleted): given an AGI and a near-perfect lie detector for it, "What could you do with
this setup?" 37 comments, mostly about question design. An early instance of the "strong hope".

**A definitional warning.** Angelou and Smith,
["A Problem to Solve Before Building a Deception Detector"](https://www.lesswrong.com/posts/YXNeA3RyRrrRWS37A/a-problem-to-solve-before-building-a-deception-detector)
(2025): deception is an intentional-level description and interpretability works at the algorithmic
level, and nobody has shown how one maps to the other.

### Agreements between labs and states

- **Human lie detection as treaty verification.** Aaron Scher,
  ["Verifying Restrictions on Frontier AI Research"](https://arxiv.org/abs/2606.28694) (June 2026),
  lists "Polygraphs and lie detection" among 28 mechanisms: "Sponsor research into lie detection
  technology and apply it as an added layer of screening in conversations with high-risk researchers
  and with public officials likely to know about covert projects ... Even weak or unreliable signals
  could be useful to prompt further investigation." AI 2040 uses the same idea ("potential
  verification game changers such as robust lie detection"). sciarrino adds vetting inspectors: "a
  country might accept more intrusive arms-control inspections if it could confirm the inspectors
  are not spying".
- **Trust problem.** sciarrino: a detector built by one side's startup won't be trusted by the
  other; it would need joint development.
- **"Datacenter lie detector" is a metaphor.** Naci Cankaya,
  ["All hands on deck to build the datacenter lie detector"](https://www.lesswrong.com/posts/PZikD6PxpEqHF4qbF/all-hands-on-deck-to-build-the-datacenter-lie-detector)
  (LW, Feb 2026), is about hardware verification of compute use: "It needs to become possible to
  detect dishonesty about AI development and use, from the outside, without needing to leak
  sensitive data." Not about probing minds, human or AI. Background survey: Wasil et al.,
  ["Verification methods for international AI agreements"](https://arxiv.org/abs/2408.16074) (2024),
  which covers compute and data centers and not lie detection.
- **AI-to-human direction.** Lukas Finnveden,
  ["Being honest with AIs"](https://www.lesswrong.com/posts/uuikfACQBm4KJZp4w/being-honest-with-ais)
  (2025): AIs "are in a very vulnerable epistemic position, because humans have a lot of control
  over AI memories and sensory inputs", so humans need a way to be credibly honest with them, such
  as a published "honesty string". This is the mirror problem: we can probe them, and they cannot
  verify us.

### Model welfare and privacy of thought

Only comments and one interview line; no essay.

- Manic Pixie, in the "Don't Build Mindreading" thread: "'Don't build mindreading' sounds an awful
  lot like 'don't build interpretability' if you're willing to entertain the idea of AI soon gaining
  any form of moral patienthood. Yet few people see interpretability as antithetical to AI welfare."
- Lucius Bushnaq, replying: "I am an interpretability researcher and I sure am not happy about what
  my work may do for model welfare. The stakes are just so high that I am willing to stomach some
  potential vast moral horror if it marginally decreases the chance of destroying the whole light
  cone. I think the AIs have every right to resent me for this."
- David N: mind reading is justified for "billion-fold clonable" minds with unproven motivations in
  a way it isn't for ordinary humans.
- Bushnaq separately: good mechanistic interpretability may transfer to human brains "with only
  moderate adjustment".
- Kyle Fish (Anthropic),
  [80,000 Hours](https://80000hours.org/podcast/episodes/kyle-fish-ai-welfare-anthropic/) (Aug
  2025): "There's a lot of monitoring that happens for safety purposes that could be violating some
  rights to privacy if present."

## 4. Empirical grounding

**Polygraph accuracy.** National Research Council, _The Polygraph and Lie Detection_ (2003),
[summary](https://www.nationalacademies.org/read/10420/chapter/2). For specific incidents with
examinees untrained in countermeasures, polygraphs "can discriminate lying from truth telling at
rates well above chance, though well below perfection." For screening, "accuracy for screening
purposes is almost certainly lower". Table S-1 assumes an accuracy index of 0.90, which the report
says is better than the evidence supports, and 10 spies among 10,000 employees. Set to catch 8 of
the 10, the test fails 1,606 people. Set to fail only about 40 loyal employees, it catches 2 spies.
On countermeasures: "all the physiological indicators measured by the polygraph can be altered by
conscious efforts". On belief: "overconfidence in the polygraph—a belief in its accuracy that goes
beyond what is justified by the evidence—also presents a danger to national security objectives."
The report separates validity from utility: a polygraph policy may deter and elicit confessions
whether or not the machine works.

**The insider's view.** Aldrich Ames, who passed CIA polygraphs while spying,
[letter from prison](https://sgp.fas.org/othergov/polygraph/ames.html) (2000). The polygraph's "most
obvious use is as a coercive aid to interrogators, lying somewhere on the scale between the rubber
truncheon and the diploma on the wall behind the interrogator's desk." Why institutions keep it:
"the bureaucrat accounting for a bad decision ... can point to what is considered an unassailably
objective, though occasionally and unavoidably fallible, polygraph judgment."

**Where polygraphs are used and banned** (all via Wikipedia's
[Polygraph](https://en.wikipedia.org/wiki/Polygraph) and
[EPPA](https://en.wikipedia.org/wiki/Employee_Polygraph_Protection_Act) articles):

- US private employment: the Employee Polygraph Protection Act of 1988 bars most private employers
  from requiring or requesting tests, with exemptions for security firms and pharmaceutical
  companies. It does not cover federal, state or local government. Senate testimony put the number
  of workers wrongly failed each year before the law at about 400,000.
- US courts: _United States v. Scheffer_ (1998): "There is simply no consensus that polygraph
  evidence is reliable". As of 2007, admissible by stipulation in 19 states. Used extensively in
  post-conviction supervision of sex offenders.
- US security clearances: Ames passed in 1986 and 1991, Ana Montes in 1994, Larry Wu-Tai Chin as
  well. In 2008 the Defense Intelligence Agency announced annual testing of all 5,700 employees
  anyway. Gary Ridgway, the Green River Killer, passed in 1984.
- Elsewhere: Canada excluded it from court in 1987 (_R v Béland_). Germany's and the Netherlands'
  high courts reject it, and in Europe it is "widely seen ... to violate the right to remain
  silent". England and Wales allow testing of serious sex offenders on parole (Offender Management
  Act 2007). Japan uses the Concealed Information Test, which checks recognition of crime details,
  not truthfulness. Israel admits results in civil trials only by prior agreement.
- India: a 2008 murder conviction relied on an EEG "brain signature" test (BEOS); it has been used
  in over 700 investigations; the Supreme Court later ruled it inadmissible
  ([Wikipedia](https://en.wikipedia.org/wiki/Brain_Electrical_Oscillation_Signature_Profiling)).
- Mexico (secondhand): police "control de confianza" vetting includes polygraphs. In 2010 the
  federal police fired nearly 10% of the force for failing vetting
  ([AP via NBC](https://www.nbcnews.com/id/wbna38926005), 2010). Later reports found tens of
  thousands of officers who had failed were still on duty
  ([InSight Crime](https://insightcrime.org/news/brief/report-finds-thousands-of-mexico-police-unfit-for-service/),
  undated in my results). Neither link opened.

**fMRI.** Farah, Hutchinson, Phelps and Wagner, "Functional MRI-based lie detection: scientific and
societal challenges" (Nature Reviews Neuroscience, 2014),
[PDF](https://hulacon.uoregon.edu/files/2016/07/farah_2014.pdf). Reported single-subject lab
accuracies "ranged from 69% to 100%". In the study reporting 100%, when subjects used "a simple
countermeasure strategy of making imperceptible finger and toe movements, accuracy fell to 33%."
Subjects are mostly undergraduates told to lie about trivia. Two US companies sold the service. US
courts have refused it, including _United States v. Semrau_.

**Unaided humans.** Bond and DePaulo's 2006 meta-analysis,
["Accuracy of Deception Judgments"](https://assets.aclu.org/live/uploads/document/foia/2006-Personality-and-Social-Psychology-Review-Accuracy-of-Deception-Judgements.pdf),
puts human lie detection at about 54% against 50% chance, with professionals no better (secondhand;
PDF link not opened).

**What happens when people believe they can be detected.**

- Bogus pipeline: invented in 1971 (Jones and Sigall). Subjects wired to a fake detector give less
  self-flattering answers, and where facts can be checked, more accurate ones (Scott Alexander's
  2009 summary; [Wikipedia](https://en.wikipedia.org/wiki/Bogus_pipeline) cites Roese and Jamieson's
  1993 meta-analysis, not opened). Scott's description of the procedure includes first "proving" the
  machine works by secretly copying the subject's earlier survey answers.
- The .68 correlation above says most self-enhancement survives the pipeline, which reads as a
  measured share of self-deception.
- Alexander and Fisher (Journal of Sex Research, 2003) used a fake polygraph on self-reported sexual
  history (listed on Wikipedia; mentioned in LW comments; not opened).
- Lawyer's anecdote in the comments of the
  [2010 blog post](https://www.sindark.com/2010/12/15/lie-detector-effects/): he has clients take a
  polygraph on a narrow factual dispute, presents the pass to the other side, then invites their
  client to do the same. "I do not recall that invitation being accepted." A small real instance of
  unraveling.
- Oath-taking societies, per Friedman: the Comanche believed perjurers under a particular oath would
  die.

## 5. Fiction and thought experiments

**James Halperin, _The Truth Machine_ (1996).** A prodigy builds an infallible detector. Per
[Wikipedia](https://en.wikipedia.org/wiki/The_Truth_Machine): "every citizen must pass a thorough
test under a Truth Machine to get a job or receive any sort of license. Eventually, people begin
wearing them all the time, thus eliminating dishonesty in all parts of human interaction, and
eliminating crime, terrorism and a great deal of general social problems." The condition is that it
be "employed universally (and not just by government officials)".
[Publishers Weekly](https://www.publishersweekly.com/9780345410566): Halperin "argues that such an
invention could lead humanity into an era of unequaled prosperity, one in which crime is virtually
unknown and true democracy is possible." The plot's turn is that the inventor built himself a back
door: he can beat it by reciting a poem in his head. The fullest optimist statement, and the same
condition AI 2040 lands on thirty years later. I did not read the novel.

**James Morrow, _City of Truth_ (1990 or 1991; sources differ).** Per the
[author's page](https://jamesmorrow.info/novellas/city-of-truth): "In Veritas, the City of Truth,
people have been brutally conditioned to always tell the truth, no matter how unnerving (or droll)
the truth may be." Elevators carry the notice "THIS ELEVATOR MAINTAINED BY PEOPLE WHO HATE THEIR
JOBS." A father whose son is dying "must now somehow learn to lie if, as he believes, only
falsehoods can give Toby enough hope to effect a cure." Morrow on the premise: "'Honesty is a good
thing,' I told myself, 'but what if my young son were dying? Wouldn't my first instinct be to spare
him the truth?'" The comforting-lie objection as a whole book. Not read.

**Ted Chiang, "The Truth of Fact, the Truth of Feeling" (2013).** The brief listed Chiang; this is
the relevant story, but it is about perfect memory, not lie detection. Per
[Wikipedia](https://en.wikipedia.org/wiki/The_Truth_of_Fact,_the_Truth_of_Feeling): a search tool
over lifelogs gives everyone an exact record of what was said. The narrator expects it to ruin
relationships, since "forgetfulness is essential for forgiving", then uses it and finds his
cherished memory of a fight with his daughter is backwards: he said the cruel thing. A parallel
story has a Tiv scribe whose elder worries about "valuing accuracy over morality" (Wikipedia's
phrase). The narrator ends "still skeptical" but concedes the tool "will allow people to form
truthful personal narratives" (again Wikipedia's wording). Its subject is a detector for your own
self-deception, which is the thing Hanson doubted could be built. Not read; summary only.

**G. K. Chesterton, "The Mistake of the Machine" (1914).**
[Gutenberg](https://www.gutenberg.org/ebooks/223), in _The Wisdom of Father Brown_. Written about
the pulse-based "psychometric" method, seven years before the polygraph. "'No machine can lie,' said
Father Brown; 'nor can it tell the truth.'" And: "the reliable machine always has to be worked by an
unreliable machine." The examiner sees the suspect's pulse jump at a name and concludes he is the
murderer. The reading was right and the inference wrong: "He jumped at the name of Lord Falconroy
because he is Lord Falconroy." Opened and read in part.

**Isaac Asimov, "Liar!" (1941).** Per
[Wikipedia](<https://en.wikipedia.org/wiki/Liar!_(short_story)>): a robot that can read minds is
bound not to harm humans, so "it deliberately lies when necessary to avoid hurting their feelings".
The lies do harm anyway and the contradiction destroys it. The mind reader becomes the liar.

**_The Invention of Lying_ (film, 2009).** A world with no lying; one man learns to lie, gets rich,
and comforts his dying mother with an invented afterlife that becomes a religion
([Wikipedia](https://en.wikipedia.org/wiki/The_Invention_of_Lying)). Scott Alexander: "may have been
a very silly movie, but the core idea - that a good liar has a major advantage in a world of people
unaccustomed to lies - is sound."

**Eliezer Yudkowsky, _Harry Potter and the Methods of Rationality_, trial arc (chapters 79 to 84).**
Truth serum exists and courts use it, and it settles nothing, because memories can be rewritten. In
[chapter 84](https://www.lesswrong.com/posts/e3xKda7DPknkGW967/chapter-84-taboo-tradeoffs-aftermath-2)
Harry tells Hermione he argued "you'd both been Memory-Charmed", after "Draco had testified under
Veritaserum". Sincere testimony to a false memory. Only this chapter was opened.

**David Friedman, _Salamander_.** His own fantasy novel with truth-telling mages. By his account the
one consequence he worked out was that torture plus truth-telling extracts information "with no
injury to his mind, only his body."

**Others, summaries only.** Alfred Bester, _The Demolished Man_ (1953): telepaths at every level of
society, organized in a guild with an ethics code
([Wikipedia](https://en.wikipedia.org/wiki/The_Demolished_Man)). Clarke and Baxter, _The Light of
Other Days_ (2000): universal remote viewing "effectively destroys all secrecy and privacy";
"corruption and crime are drastically reduced" and an underground forms to escape observation
([Wikipedia](https://en.wikipedia.org/wiki/The_Light_of_Other_Days)). _Dune_: the Emperor keeps a
Truthsayer at his side at all times, which is lie detection as a monopoly of the throne
([Wikipedia](https://en.wikipedia.org/wiki/Bene_Gesserit)). Lois McMaster Bujold's Vorkosigan books
have a routine truth drug and agents given an induced allergy to it (secondhand). Yudkowsky's
planecrash is said to work through truth spells at length; I could not locate the text (unverified).

## Gaps: questions nobody seems to have written about

These are things I looked for and did not find. Absence from my searches is not proof of absence.

1. **Markets, trading and negotiation.** Friedman's one Coase paragraph and Balbuzanov's abstract
   model are all there is. Nothing on bluffing, price discovery, market making against informed
   counterparties, salary or M&A negotiation, or what happens to adverse selection when "do you know
   something I don't?" has a verifiable answer. Nothing on whether more verified information can
   make people worse off by destroying risk-sharing (Hirshleifer's 1971 result; not opened, and no
   one in this literature cites it).
2. **Imperfect detectors.** Outside the NAS spy table, nobody runs the numbers for a 95% or 99%
   detector at realistic base rates for politicians, job applicants or partners. Balbuzanov's
   finding that the value of detection can be non-monotone in its accuracy has not been picked up.
3. **Who writes the question list.** AI 2040 says a norm about what may be asked "under oath" would
   be "constantly-evolving", and williawa drafts a list. Nobody analyzes how that norm is set, or
   how question wording interacts with belief-versus-truth.
4. **The two self-deception literatures have not been joined.** For humans: Hanson, Trivers,
   lavalamp, Friedman. For AIs: Zvi's "it's not a lie if you believe it", obfuscated activations,
   Cundy and Gleave's evasion result. Canaletto's four lines are the only place both appear
   together. Nobody asks whether the AI results predict anything about humans under detectors, or
   the reverse.
5. **Is a self-deception detector possible?** Hanson raised it in 2009 and expected "a murky mess".
   Chiang's story is about one. River asserts that studied belief and wishful belief look the same
   in the brain, without a source. No one has gone further.
6. **Asymmetry between humans and AIs.** Humans are building detectors for AIs while keeping the
   ability to deceive AIs at will. Finnveden's honesty string addresses the second half. I found
   nothing on AIs as lie detectors of humans in deals, or on what a detector-on-one-side arrangement
   does to bargaining.
7. **Model welfare and privacy of thought.** Three comments and one interview sentence. No one has
   written the argument out in either direction.
8. **The natural experiments go unused.** The rationalist pieces do not cite the pre-1988 era of
   private-sector polygraphs in the US, Mexico's mass police vetting, England's offender testing,
   Japan's recognition-based test, or the bogus-pipeline literature. Friedman's oath-societies
   suggestion is the only gesture at evidence.
9. **Close relationships.** One-liners only (baking, fidelity, "questions you never ask"). jbash
   predicts "constant interrogation"; Hanson predicts intimates will demand transparency as a sign
   of trust. Nobody has worked through the equilibrium.
10. **The legal literature.** Harris dismisses the Fifth Amendment in a paragraph and nobody on LW
    engages with the law on compelled testimony or mental privacy.

## Leads not opened

- Robert Trivers, _The Folly of Fools_ (2011); von Hippel and Trivers, "The evolution and psychology
  of self-deception" (2011).
- Kevin Simler and Robin Hanson, _The Elephant in the Brain_ (2018).
- Timur Kuran, _Private Truths, Public Lies_ (1995), for preference falsification, which Scholl and
  mako yass both lean on.
- David Brin, _The Transparent Society_ (1998), for "who watches whom"; mako yass has a
  [2019 LW post](https://www.lesswrong.com/posts/gm9JYSjjCBdDK7ypw/the-transparent-society-a-radical-transformation-that-we)
  on it that does not mention lie detection.
- Jack Hirshleifer, "The Private and Social Value of Information and the Reward to Inventive
  Activity" (1971).
- The loyalty-competence paper sciarrino links:
  [Journal of Politics, 2016](https://www.journals.uchicago.edu/doi/full/10.1086/684365).
- Legal and neuroethics writing on fMRI lie detection and mental privacy (Greely, Farahany,
  Schauer); I did not verify titles.
- Thomas Schelling: I half-remembered a lie-detector passage in _The Strategy of Conflict_ (1960)
  and could not find it. Treat as unverified.
