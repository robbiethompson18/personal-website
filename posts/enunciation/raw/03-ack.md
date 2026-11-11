# "Ack" and the family of acknowledgement tokens

## 1. Most interesting findings

**1. Conversation analysts found the Two Generals problem in human talk, and solved it the way TCP
does.** Clark & Brennan (1991) say every contribution needs _positive evidence_ of understanding,
then notice the regress: if B's "uh huh" is itself a presentation, it needs its own acceptance, and
so on forever. Their way out is that two kinds of evidence carry no separate presentation: the
_relevant next turn_ and _continued attention_. In protocol terms, the ACK is piggybacked on the
next data segment. TCP does the same thing with cumulative ACKs carried on data, plus the
delayed-ACK rule (an ACK must be delayed less than 0.5 s, and at least every second full segment
gets acked; RFC 1122, 1989). They also observe that "okay" is cheap to time face to face but
expensive in keyboard chat, where people fell back on radio's "o" for "over".
[Clark & Brennan 1991](https://web.stanford.edu/%7Eclark/1990s/Clark,%20H.H.%20_%20Brennan,%20S.E.%20_Grounding%20in%20communication_%201991.pdf),
pp. 130–145; [RFC 1122 (1989)](https://www.rfc-editor.org/rfc/rfc1122.txt) §4.2.3.2.

**2. "Okay" works as a stack push/pop. "Uh-huh" works as a step within the current frame.**
Bangerter & Clark (2003) split acknowledgement tokens into _vertical_ markers (okay, all right, got
it: entering or leaving a joint sub-project) and _horizontal_ markers (uh-huh, m-hm, yeah: keep
going). They draw the analogy to push and pop themselves. In a card-matching task, 65% of
descriptions ended in "okay" on first sight of a figure and 31% by the last trial, while "uh-huh"
rose from 5% to 19% as the pair built shared names and sub-projects disappeared. In a Lego task
"okay" ran at 43–49 per 1,000 words. A Slack "ack" usually closes a thread, so it is the vertical
kind.
[Bangerter & Clark 2003, _Cognitive Science_ 27](https://web.stanford.edu/~clark/2000s/Bangerter,%20A.%20_%20Clark,%20H.H.%20_Navigating%20joint%20projects%20with%20dialogue_%202003.pdf),
pp. 198, 206–211.

**3. Hacker "ACK" is younger than you'd guess.** I grepped the Jargon File archive. "ACK" appears in
none of the Jargon-1 versions from 1976–1981, and not in the 1983 _Hacker's Dictionary_ text
(v1.5.0). It first shows up in ESR's v2.1.1 draft of 12 June 1990, with a typo in the binary
("000110"). That entry gives two senses: "register one's presence… An appropriate response to PING",
and "[prob. from _Bloom County_] … 'Oop ack!'". By v2.9.6 (1991) the entry had added the
polite-interrupt sense ("Ack. Ack. Ack. I get it now"), "ACK?" for "are you there?" (the joke reply
is NAK, "I'm not here"), and "SYN SYN ENQ?" for "are you interruptible?". Absence from the File
doesn't prove nobody said it earlier, but it is the best dated record I found.
[jargon-file.org archive](https://www.jargon-file.org/archive/);
[Gutenberg text of v4.0.0 (1996)](https://www.gutenberg.org/ebooks/817).

**4. Every "ack" commits you to something different, and the engineered systems spell it out:**

- **Morse R:** "received, but does not necessarily indicate the message was understood". VE means
  verified/understood. [Wikipedia, prosigns](https://en.wikipedia.org/wiki/Prosigns_for_Morse_code)
- **ROGER:** "I have received all of your last transmission." **WILCO:** "I understand your message
  and will comply with it."
  [EU SERA.14045](https://regulatorylibrary.caa.co.uk/923-2012/Content/Regs/03440_SERA14045_Transmitting_technique.htm).
  "Roger, wilco" is redundant.
  [Wikipedia, procedure words](https://en.wikipedia.org/wiki/Procedure_word)
- **Navy "aye aye, sir":** understood and will obey. "O.K., sir" is improper (Navy training manuals
  via TPub; secondary).
- **PagerDuty "acknowledge":** "claims ownership of the issue and halts the escalation process". If
  the ack timeout runs out, the incident goes back to triggered, so the ack is effectively a lease.
  [PagerDuty docs](https://docs.pagerduty.com/incident-management/incidents/overview)
- **Linux `Acked-by:`:** "less formal than Reviewed-by", "does not necessarily indicate
  acknowledgement of the entire patch", and mergers "will sometimes manually convert an acker's
  'yep, looks good to me' into an Acked-by".
  [submitting-patches](https://docs.kernel.org/process/submitting-patches.html)
- **TCP ACK:** the bytes reached the peer's TCP stack. That says nothing about the application.
  Saltzer, Reed & Clark: the ARPANET's per-message RFNM ack "was never found to be very helpful to
  applications… The acknowledgement that is really desired is an end-to-end one… 'I did it', or 'I
  didn't.'"
  [End-to-End Arguments, 1981/1984](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf)

**5. An "OK" with an ambiguous referent killed 101 people.** In 1972, Eastern 401's crew was
absorbed by a nose-gear light. Miami approach saw the altitude dropping and asked "How are things
comin' along up there?" The crew answered "OK." They meant the gear, and the controller took it to
mean the altitude. In NASA ASRS data, Monan (1988) found "hearback" often missing: pilots signed off
with "an inadequate 'Roger' or 'okay'", and silence from the controller was taken as confirmation of
a wrong readback. Grayson & Billings classified 529 of 6,527 ASRS reports as "ambiguous
phraseology". [Cushing, _Flight Safety Digest_, July 1995](https://flightsafety.org/fsd_jul95).

**6. Tenerife (1977, 583 dead) is why "takeoff" is now a reserved word.** KLM radioed "We are now at
takeoff". The tower said "OK… stand by for takeoff, I will call you", but the second half was lost
in a squeal from Pan Am transmitting at the same moment. Current guidance says "take-off" may be
used only to issue or cancel a takeoff clearance; otherwise controllers say "departure" or
"airborne". SKYbrary ties the rule to "an accident in 1977".
[SKYbrary](https://skybrary.aero/articles/non-standard-phraseology). Linguist Steven Cushing reads
"at takeoff" as Dutch-English code-switching (Dutch _aan het_ + infinitive for the progressive).
That is one scholar's interpretation, not the official finding (FSD 1995).

**7. Readback is cheap and catches real errors, and railroads did it in the 1850s.** Barenfanger et
al. (2004) required readback on 822 lab calls reporting critical results. It caught 29 errors
(3.5%), with doctors worst at 6/95, and cost 12.8 s per call.
[PubMed 15198350](https://pubmed.ncbi.nlm.nih.gov/15198350/). In video of 387 pediatric-trauma
orders, only 26.1% were closed-loop, and those finished 3.6× sooner (HR 3.6, 95% CI 2.5–5.3;
observational, so confounded by who the order was directed to).
[El-Shafy et al. 2018](https://pubmed.ncbi.nlm.nih.gov/28780315/). Railroad train orders worked the
same way. Operators repeated the order back, the dispatcher underlined each word as it came back,
then sent "Complete". "Form 31" orders made the train stop for signatures; "Form 19" orders were
handed up at speed. Tuttle says the 31 was "considered more reliable" but was "in fact… no more
reliable than the '19'", which is a nineteenth-century argument about whether the expensive
handshake earns its cost. [Tuttle, Train Orders](https://mysite.du.edu/~etuttle/rail/to.htm).
Western Union's 92 Code (1859) already had numeric acks: 13 = "I understand", 20/24 = "Repeat this
back". [Wikipedia, Wire signal](https://en.wikipedia.org/wiki/Wire_signal)

**8. A phone ring is a SYN, and Schegloff described the handshake in 1968.** In ~500 calls to a
disaster centre, the person who answered spoke first in all but one case. That led Schegloff to the
summons–answer sequence:

- **Nonterminality:** a completed summons–answer "cannot properly stand as the final exchange".
  People who phone a shop and hear "hello", which already tells them it's open, still ask "Are you
  open?"
- **Retransmission and timeout:** "upon A's absence S may be repeated", and silence licenses the
  inference "no answer – no person".
- **Answers as questions:** "What?" obliges the summoner to speak again. Children exploit this with
  "You know what, Mommy?".

[Schegloff 1968, _American Anthropologist_ 70](https://conversationanalysis.org/mp-files/sequencing-in-conversational-openings.pdf)

**9. A 👍 was ruled a contract signature.** In _South West Terminal v. Achter Land_ (2023 SKKB 116),
the buyer texted a photo of a flax contract with "please confirm"; the seller replied 👍. He argued
it only acknowledged receipt (ROGER). The court held it was acceptance (WILCO) and awarded
~C$82,200. The Court of Appeal affirmed in a split decision (2024 SKCA 115).
[Canadian Lawyer 2023](https://www.canadianlawyermag.com/news/general/thumbs-up-emoji-constituted-acceptance-of-contract-saskatchewan-court-rules/377287);
[CBC 2024](https://amp.cbc.ca/news/canada/saskatchewan/court-of-appeal-thumbs-up-emoji-contract-1.7415247)

**10. Terse acks carry a measurable social cost outside cultures that use them natively.** Fang,
Zhang & Maglio ran 8 studies with more than 5,300 people. Texts with abbreviations read as less
sincere and got fewer replies, and 80% of participants predicted others wouldn't care.
[APA release, 2024; _JEP: General_ 154(1), 2025](https://www.apa.org/news/press/releases/2024/11/texting-abbreviations-insincere).
Gunraj et al. found that one-word replies ("Okay.") ending in a period read as less sincere in texts
but not in handwriting.
[Binghamton 2015/_CHB_ 2016](https://sciencedaily.com/releases/2015/12/151208094229.htm). Liberman
calls the drift of "O.K." toward passive-aggressive, with "kk" as the friendly form, "pragmatic
staining", and notes "kk" saves no characters.
[Language Log 2019](https://languagelog.ldc.upenn.edu/nll/?p=45152). Applying this to "ack" is my
inference: among people who don't know the protocol meaning, "ack" probably reads as a low-effort
abbreviation.

**11. Bitcoin Core turned ACK into a typed review grammar, and the types keep drifting.** fanquake's
PR #5468 (Dec 2014, merged by jgarzik) defined Concept ACK, utACK, Tested ACK and NACK; laanwj added
"A loose ACK can be confusing." The current CONTRIBUTING.md has Concept (N)ACK, Approach (N)ACK and
`ACK <commit-hash>` plus a description of how you reviewed, and says "NACKs without accompanying
reasoning may be disregarded". Apache's −1 veto likewise needs a technical justification. A 2021
attempt to document tACK/utACK/crACK was closed; sipa: "people are already using them with very
different meaning." GitHub search today finds ~8.2k issues/PRs containing "Concept ACK" and ~6.6k
containing "utACK", out of ~25.5k PRs.
[CONTRIBUTING.md](https://github.com/bitcoin/bitcoin/blob/master/CONTRIBUTING.md);
[#5468](https://mirror.b10c.me/bitcoin-bitcoin/5468/);
[#22966](https://mirror.b10c.me/bitcoin-bitcoin/22966/)

**12. Japanese listeners backchannel roughly twice as often as Americans.** Maynard's comparisons
put aizuchi at about 2× the English rate. Japanese-only measures give 15–20 aizuchi per minute
(Mizutani 1988) and one every 6.1 s on the phone (Komiya 1986), per
[Hatasa (2007), CJK proceedings](https://nflrc.hawaii.edu/CJKProceedings/hatasa/hatasa.html). Clancy
et al. (1996) found Mandarin speakers backchannel least of the three languages. I could not open
Maynard's own tables (_Linguistics_ 24, 1986), so treat the ratio as secondary.

## 2. Read these (ranked)

1. **Clark & Brennan, "Grounding in communication" (1991)**, ~35 pp.
   [PDF](https://web.stanford.edu/%7Eclark/1990s/Clark,%20H.H.%20_%20Brennan,%20S.E.%20_Grounding%20in%20communication_%201991.pdf).
   The ACK protocol for conversation, including the regress, least-collaborative-effort, and eight
   media constraints with their costs (written before Slack, still accurate).
2. **Schegloff, "Sequencing in Conversational Openings" (1968)**, ~20 pp.
   [PDF](https://conversationanalysis.org/mp-files/sequencing-in-conversational-openings.pdf). The
   handshake, retransmission and timeout, all derived from phone recordings.
3. **Saltzer, Reed & Clark, "End-to-End Arguments in System Design" (1981 conf./1984 TOCS)**, 12 pp.
   [PDF](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf). Read the "Delivery
   guarantees" section to see why a transport ack isn't an "I did it".
4. **Cushing, "Pilot–ATC Communications: It's Not (Only) What You Say" (_Flight Safety
   Digest_, 1995)**, 24 pp. [PDF](https://flightsafety.org/fsd_jul95). Accident case studies where
   an "OK" or "Roger" failed.
5. **Bangerter & Clark, "Navigating joint projects with dialogue" (2003)**, 30 pp.
   [PDF](https://web.stanford.edu/~clark/2000s/Bangerter,%20A.%20_%20Clark,%20H.H.%20_Navigating%20joint%20projects%20with%20dialogue_%202003.pdf).
   Quantitative account of okay vs uh-huh.
6. **Halpern & Moses, "Knowledge and common knowledge in a distributed environment" (JACM 1990)**,
   ~40 pp. [arXiv](https://arxiv.org/abs/cs/0006009). Proves common knowledge "cannot be attained"
   in practical systems. For a lighter treatment, Pinker's _When Everyone Knows That Everyone
   Knows…_ (2025) is book length.
7. **Jargon File entries ACK, NAK, ENQ, T, NIL, talk mode (v4.x, 1996–2003)**, 5 min.
   [Gutenberg](https://www.gutenberg.org/ebooks/817). Talk-mode codes: O = over, OO = over and out,
   "BYE?" means "ready to unlink?". NIL as "no" predates LISP among radio hams.
8. **Linux `submitting-patches.rst`, the Acked-by/Reviewed-by sections (current)**, 10 min.
   [docs.kernel.org](https://docs.kernel.org/process/submitting-patches.html)
9. **Bitcoin Core CONTRIBUTING.md "Peer Review" plus PRs #5468 (2014) and #22966 (2021)**, 15 min.
   Watch a review vocabulary get standardized and then drift.
10. **Wilton, "OK / okay" and "roger" (Wordorigins)**, 10 min each.
    [OK](https://wordorigins.org/big-list-entries/ok-okay),
    [roger](https://wordorigins.org/big-list-entries/roger)

## 3. Details

**Timeline**

- **1838–39:** Boston abbreviation fad. _Boston Morning Post_ (editor Charles Gordon Greene) prints
  O.W. "oll wright" on 7 Feb 1839 and O.K. "oll korrect" on 23 Mar 1839. In 1840, Van Buren's "Old
  Kinderhook" O.K. Clubs spread it. Allen Walker Read established this in _American Speech_ in
  1963–64. By 1866 a telegraph company director was signing a cable "'O.K.' (all correct)".
  [Wordorigins](https://wordorigins.org/big-list-entries/ok-okay)
- **1859:** Western Union 92 Code. 30 = "the end" (hence "-30-"); 73 = later "best regards". The
  claim that 73 originally meant "my love to you" is weakly sourced.
- **1850s–1889:** Railroad train orders with repeat-back and "Complete"; codified in the Standard
  Code of 1889.
- **1879:** Phillips Code (Walter P. Phillips, AP), 1,760 abbreviations including SCOTUS. "OK" is
  not documented as an entry.
- **1898/1904:** British signalese: A = "ak", then "ack". **1916:** _Daily Mirror_ explains the
  "Ack-Ack" (anti-aircraft) gun. "Ack emma" = a.m. This "ack" is a different word from acknowledge.
  [phrases.org.uk](https://phrases.org.uk/meanings/ack-ack.html)
- **1912:** Q-codes internationalized at the London Radiotelegraph Convention. QSL = "I acknowledge
  receipt". [ARRL](https://www.arrl.org/ham-radio-history)
- **1927:** "Roger" = R in the US Navy _Bluejackets' Manual_. **1941:** the Air Corps uses "ROGER!"
  "instead of okay or right". **1956:** ICAO/NATO switch R to "Romeo", but the "roger"
  acknowledgement survives. "Received Order Given, Expect Results" is a backronym.
  [Wordorigins](https://wordorigins.org/big-list-entries/roger)
- **~1937–1940:** Ten-codes (Charles Hopper, Illinois State Police; APCO bulletin 1940). 10-4 =
  acknowledged. [Wikipedia](https://en.wikipedia.org/wiki/Ten-code)
- **1946–47:** Hendrik van Duuren's ARQ radiotelegraph (US2518405 filed 1946; Amsterdam–New York
  1947, per secondary sources). The return channel sends a repeat request on error. This is the
  first automatic NAK-style mechanism I found.
- **1961–68:** Bob Bemer submits an ASCII proposal to X3.2 in May 1961. In ASCII-1963, 0x05 = WRU
  ("Who are you?", the teleprinter answerback trigger) and 0x06 = RU ("Are you…?"). ACK sat at 0x7C
  in the printable block (inferred from Wikipedia's table). The 1965/67 revision put ENQ at 0x05,
  ACK at 0x06 and NAK at 0x15. ISO 1745 (1975) specified their use.
  [Wikipedia, ASCII](https://en.wikipedia.org/wiki/ASCII);
  [Aivosto](https://www.aivosto.com/articles/control-characters.html)
- **1970:** Yngve coins "back channel" ("On getting a word in edgewise", CLS 6). **1982:**
  Schegloff's "continuers". **1984:** Jefferson on "yeah" vs "mm hm" as acknowledgement tokens.
  **2001:** Gardner, _When Listeners Talk_, a monograph on mm.
- **1975:** Akkoyunlu, Ekanadham & Huber pose the problem, framed with gangsters. **1978:** Gray
  names it the "Two Generals Paradox".
  [Wikipedia](https://en.wikipedia.org/wiki/Two_Generals%27_Problem)
- **1981:** RFC 793: "The principle reason for the three-way handshake is to prevent old duplicate
  connection initiations from causing confusion"; ACKs are cumulative.
  [RFC 793](https://www.rfc-editor.org/rfc/rfc793.txt)
- **1990/1991:** ACK enters the Jargon File.
- **2007:** Andrew Morton documents Acked-by (posted 31 May, merged 8 June). The tag was already in
  routine use, but I couldn't find its first use. **2025:** Miguel Ojeda's patch clarifies Acked-by
  vs Reviewed-by. GitHub commit search finds ≥144k torvalds/linux commits with "Acked-by" (partial
  index, so a lower bound).
- **2014:** Bitcoin Core ACK taxonomy (#5468).
- **2016:** Google SRE book describes "Escalator", which escalates if a page isn't acknowledged
  within an interval. [SRE book ch. 16](https://sre.google/sre-book/tracking-outages/)
- **Today:** Slack's Bolt SDK requires the bot to call `ack()` within 3 seconds or Slack times out.
  [Slack docs](https://docs.slack.dev/tools/bolt-python/concepts/acknowledge). Your Slack "ack" is a
  meat-layer version of an RPC the platform itself requires.

**Other notes**

- **"Repeat" vs "say again":** in artillery, REPEAT means "the same volume of fire to be fired
  again" (ACP 125 U.S. Supp-2(A)), which is why radio users never say "repeat" when they want a
  re-send. "Over" and "out" are mutually exclusive, so "over and out" is a contradiction.
  [Wikipedia, procedure words](https://en.wikipedia.org/wiki/Procedure_word)
- **Rationalist acks:** LessWrong reacts include an ack vocabulary that is more granular than most.
  "I Saw This" (pure receipt), "Thumbs Up: I saw this, and feel vaguely good about it", "Question
  Answered", and "Bowing Out" (roughly a FIN). plex packaged them for Slack and Discord in Oct 2025.
  [LW reacts](https://www.lesswrong.com/w/lesswrong-reacts);
  [pack](https://www.greaterwrong.com/posts/eq2gYhZvuDrMpuhSc/lw-reacts-pack-for-discord-slack-etc).
  Screwtape's "Closing the loop" (LW, Jan 2026) argues for "yep, job done" messages, i.e. the
  end-to-end "I did it" ack.
  [GW](https://www.greaterwrong.com/posts/uBzDetYKD5LsXdCPn/closing-the-loop)
- **HN folk theory, one data point each:** "One ack gives you no new information", so restate the
  request instead, which amounts to a readback (xyzelement, 2023,
  [HN 34876453](https://news.ycombinator.com/item?id=34876453)). "even basic ACKs are important for
  reliable communication" (musicale, 2025, HN 45639751). Asking a question cold feels rude "without
  first going through the equivalent of a SYN+ACK handshake" (kijin, 2021, HN 25883724). That last
  one is the anti-nohello position.
- **T and NIL as yes/no:** from the Jargon File, a LISP hacker answers a flight attendant's
  "coffee?" with "T" and gets tea.

## 4. Dead ends / contested

- **When humans started typing "ack" to each other:** I found no dated Usenet or ARPANET instance
  before the 1990 Jargon File. Google Groups and Usenet archives weren't searchable from here. The
  OED wasn't accessible. Merriam-Webster's "first known use 2001" is for the dismay interjection.
  UNVERIFIED.
- **Which communities use "ack" today, and since when:** I found no corpus study. Evidence is
  anecdotal (HN comments, Slack etiquette blogs that talk about emoji acks rather than the word).
  The claim that it is common in trading firms or EA/rationalist Slack is UNVERIFIED.
- **Why X3.2 picked ACK/NAK:** no committee rationale found. That BISYNC's ACK0/ACK1 work like an
  alternating bit is from memory, UNVERIFIED.
- **When Acked-by was first used** (before 2007) is UNVERIFIED. A guess that Bitcoin's ACK culture
  came over from LKML via Jeff Garzik, a former kernel driver maintainer, is my speculation.
- **Exact ICAO Doc 9432 note** that ROGER is "under no circumstances" to be used for readbacks or
  yes/no answers: I only saw it quoted secondhand. The ICAO PDF wouldn't download.
- **A study saying "K" is the most hated text reply** (_Int. J. Mobile Communications_, reported by
  Fast Company/Global News): I couldn't find the paper. A claimed "75% error reduction from
  closed-loop communication in an ED" also couldn't be traced. Both UNVERIFIED.
- **Folk etymologies:** OK from Choctaw _okeh_, Greek _ola kala_, etc. (no evidence); ROGER =
  "Received Order Given, Expect Results" (backronym); PING = "Packet INternet Groper" (the author of
  ping denies it, per the Jargon File); 73 = "my love to you" in 1857 (weak sourcing).
- **Contested:** Cushing's code-switching account of "at takeoff" is one linguist's view. Bill the
  Cat's "Ack!" vs Cathy's "Ack!": the Jargon File says "prob. from Bloom County", and which strip
  came first with the word is unresolved. The 1963 position of ACK at 0x7C is inferred from a
  flattened table.
