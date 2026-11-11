# 13. FX chat logs: the primary sources, read

Written for Robbie, 2026-11-11. Every chat quote below was copied from PDF text I downloaded and
extracted this session (pdftotext), or from a page I fetched. Spelling, case, typos, `[. . .]` and
the regulators' bracketed insertions are theirs. Where the PDF is an OCR'd scan (NYDFS BNP and
Goldman orders), OCR glitches are left in and flagged `[OCR]`. My own notes are in _italics_ or
marked "my note". Nothing here is reconstructed from memory; things I could not confirm are tagged
UNVERIFIED.

Caveats that matter for reading these:

- These are **settled regulatory findings and selected excerpts**, chosen by prosecutors to show
  misconduct. They are not a random sample of desk chat. The bank letters (Bank U, Firm A...) are
  per-document pseudonyms and are reused with different meanings in different sections.
- No individual is named in any of the bank-level documents. The UK Upper Tribunal held in 2016 that
  the FCA notices did **not** identify Chris Ashton, so don't attribute any quote to a named person.
- The three people criminally charged over "The Cartel" room were acquitted (section 5).

---

## 1. Primary documents table

| Regulator                                                                 | Date                    | Bank                                                                   | Direct PDF                                                                                                                                                                                                  | Chat content                                                                                                                                                                                   | Chat pages (PDF page no.)    |
| ------------------------------------------------------------------------- | ----------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| CFTC, "Examples of Misconduct in Private Chat Rooms" (press exhibit)      | Nov 2014                | Citi, JPM, UBS, HSBC, RBS (+ Barclays as Bank W, unnamed)              | https://www.cftc.gov/sites/default/files/idc/groups/public/@newsroom/documents/file/hsbcmisconduct111114.pdf                                                                                                | **The best single document.** Timestamped multi-line transcripts: Cartel membership debate, one GBP/USD 4pm fix played out across 7 rooms at once, "double team", "ammo", "pickun", "scores"   | 1–7 (all)                    |
| CFTC, same exhibit for Barclays                                           | 20 May 2015             | Barclays (+ JPM, UBS, Citi)                                            | https://www.cftc.gov/sites/default/files/idc/groups/public/@newsroom/documents/file/fxbarclaysmisconduct052015.pdf                                                                                          | Repeats the membership debate and "double team"; adds RUB "kopecks" fix (translated from Russian)                                                                                              | 1–2                          |
| CFTC order                                                                | Nov 2014                | Citibank                                                               | https://www.cftc.gov/sites/default/files/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfcitibankorder111114.pdf                                                                         | Membership debate with "add huge value to this cartell", "1 month trial", "sleep with one eye open"; "pickun"/"double team it"; "hosed", "wmr is impossible"                                   | 5–8                          |
| CFTC order                                                                | Nov 2014                | JPMorgan                                                               | https://www.cftc.gov/sites/default/files/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfjpmorganorder111114.pdf                                                                         | Same cartell debate; "maybe"; "Pickun"; "hosed"/"ditto"                                                                                                                                        | 6–8                          |
| CFTC order                                                                | Nov 2014                | RBS                                                                    | https://www.cftc.gov/sites/default/files/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfroyalbankorder111114.pdf                                                                        | "ammo", "all yours", "ramp it"                                                                                                                                                                 | 5–7                          |
| CFTC order                                                                | Nov 2014                | UBS                                                                    | https://www.cftc.gov/sites/default/files/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfubsorder111114.pdf                                                                              | cartell debate; "troyal fkn we"; "scores"                                                                                                                                                      | 6–7                          |
| CFTC order                                                                | Nov 2014                | HSBC                                                                   | https://www.cftc.gov/sites/default/files/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfhsbcorder111114.pdf                                                                             | "cable", "betty", "lhs in cable at the fix", "good amount", "building" (prose + short quotes)                                                                                                  | 6–9                          |
| CFTC order                                                                | 20 May 2015             | Barclays (FX)                                                          | https://www.cftc.gov/sites/default/files/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfbarclaysborder052015.pdf                                                                        | cartell debate, "scores", RUB "kopecks"                                                                                                                                                        | 6–8                          |
| FCA Final Notice                                                          | 11 Nov 2014             | Citibank N.A. (£225.6m)                                                | https://www.fca.org.uk/publication/final-notices/final-notice-citi-bank.pdf                                                                                                                                 | "3 musketeers", "1 team", numpty; ECB EUR/USD fix worked example ("mangle", "you're all clear"); defines ammo/filth/clearing the decks/building; stops                                         | 15–21                        |
| FCA Final Notice                                                          | 11 Nov 2014             | HSBC (£216.4m)                                                         | https://www.fca.org.uk/publication/final-notices/final-notice-hsbc.pdf                                                                                                                                      | "A-team", "people choke up", "u are uselees"; GBP/USD WMR worked example (same fix as CFTC exhibit pp1–4); stop-hunting ("slam some stops", "free money")                                      | 15–21                        |
| FCA Final Notice                                                          | 11 Nov 2014             | JPMorgan (£222.2m)                                                     | https://www.fca.org.uk/publication/final-notices/final-notice-jpm.pdf                                                                                                                                       | "A-team"; EUR/USD WMR "double team em"; "we were EPIC at the [WMR] fix yest"; "the 69 print"; "shall we go get these stops?"                                                                   | 15–21                        |
| FCA Final Notice                                                          | 11 Nov 2014             | RBS (£217.0m)                                                          | https://www.fca.org.uk/publication/final-notices/final-notice-rbs.pdf                                                                                                                                       | "1 team, one dream", "a co-operative", "a 3 way relationship built on immense trust"; GBP/USD WMR example; footnote glossing **betty = Betty Grable = cable**; "HIT IT … I'm out of bullets"   | 17–21                        |
| FCA Final Notice                                                          | 11 Nov 2014             | UBS (£233.8m)                                                          | https://www.fca.org.uk/publication/final-notices/final-notice-ubs.pdf                                                                                                                                       | "the players"; ECB EUR/USD example with "taking all the filth out", "shet" (=25m), "bully" (=50m), "best fix of my ubs career"; "butchering" stops                                             | 16–22                        |
| FCA Final Notice                                                          | 20 May 2015             | Barclays (£284.4m)                                                     | https://www.fca.org.uk/publication/final-notices/barclays-bank-plc-may-15.pdf                                                                                                                               | "the 3 musketeers"/"we all die together"; long month-end WMR example; full stop-loss hunt with "coiled cobra", "algos galore at 96", "held him in"                                             | 19–29                        |
| NYDFS Consent Order                                                       | 20 May 2015             | Barclays ($485m)                                                       | https://www.dfs.ny.gov/system/files/documents/2020/04/ea150520_barclays.pdf                                                                                                                                 | Names "Cartel"; dated chats; "i saved 500 for last second"; ZAR price-coordination; sales mark-ups incl. "if you aint cheating, you aint trying"; hand signals                                 | 5–16                         |
| NYDFS Consent Order                                                       | 24 May 2017             | BNP Paribas ($350m per press; order not re-checked for amount)         | https://www.dfs.ny.gov/system/files/documents/2020/03/ea170524_bnp_paribas.pdf                                                                                                                              | **"ZAR Domination"** cartel recruitment and spread-fixing; fake trades; fix "Christmas present"; "how easy was that to bully?"; barrier options; PTAX                                          | 4–20 (scanned, OCR)          |
| NYDFS Consent Order                                                       | 13 Nov 2017             | Credit Suisse ($135m per press)                                        | https://www.dfs.ny.gov/system/files/documents/2020/03/ea171113_credit_suisse.pdf                                                                                                                            | "whos got a massive fix I can front run"; code names "Satan", "Tanktop", "Shoefone"; "this chat is a compliance dream"; "walk it brotha"/"Collapsado"; internal front-running memos; last look | 5–20                         |
| NYDFS Consent Order                                                       | 1 May 2018              | Goldman Sachs ($54.75m per press, UNVERIFIED)                          | https://www.dfs.ny.gov/system/files/documents/2020/03/ea180501_goldman_sachs.pdf                                                                                                                            | "Young Guns" room; "fiddler", "hat and coat"; "I useto spooof"; "2 yards aud … the numbers disappeared off the screen"                                                                         | 4–9 (scanned, OCR)           |
| DOJ plea agreement                                                        | May 2015                | Barclays PLC ($650m + $60m)                                            | https://www.justice.gov/file/440481/download                                                                                                                                                                | No chat text; names the room "The Cartel" or "The Mafia"; defines pip                                                                                                                          | 4–5                          |
| DOJ indictment, _US v. Usher, Ramchandani & Ashton_ (S.D.N.Y. 17-cr-19)   | Jan 2017                | ex-RBS/JPM, Citi, Barclays                                             | https://www.justice.gov/opa/press-release/file/924206/download                                                                                                                                              | **No chat quotes.** "The Cartel" or "The Mafia" naming only                                                                                                                                    | 8                            |
| UK Upper Tribunal, _Ashton v FCA_ [2016] UKUT 0005 (TCC)                  | 12 Jan 2016             | —                                                                      | https://assets.publishing.service.gov.uk/media/5753ea7ae5274a6ed100003c/Christopher-Ashton-v-FCA-prelim-decision.pdf                                                                                        | Re-quotes UBS/Barclays notice and NYDFS chats; quotes FT/Bloomberg coverage of "The Cartel"; held he was not identified                                                                        | 5–11, 16–20                  |
| European Commission press releases (decision texts not obtained)          | 16 May 2019; 2 Dec 2021 | Barclays, RBS, Citi, JPM, MUFG, UBS; then UBS, Barclays, RBS, HSBC, CS | https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_19_2568/IP_19_2568_EN.pdf ; https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_21_6548/IP_21_6548_EN.pdf | Room names only: "Three way banana split / Two and a half men / Only Marge", "Essex Express 'n the Jimmy", "Semi Grumpy Old men", "Sterling Lads"; "standing down"                             | 1                            |
| Academic: Knorr Cetina & Bruegger, "Global Microstructures", _AJS_ 107(4) | 2002                    | Swiss bank, Zurich                                                     | https://kops.uni-konstanz.de/bitstreams/d755faf4-ce93-485f-b77e-702ac41c410e/download                                                                                                                       | Legit Reuters Dealing 2000 conversations from 1996: the clean baseline register                                                                                                                | journal pp. 927–928, 933–943 |

---

## 2. Verbatim excerpts

### The Cartel (EUR/USD room: Citi, JPM, UBS, Barclays, RBS)

**E1. Vetting a new member.** CFTC exhibit 2014, p.1; repeated in CFTC Citi order p.5–6, Barclays
exhibit 2015 p.1. EUR/USD room. Three traders decide whether a fourth (per NYDFS, a Barclays euro
trader, 2011) can be trusted with the room's order information.

```
Bank Z Trader:   7:49:55   are we ok with keeping this as is
                 7:50:27   ie the info lvls & risk sharing?
Bank X Trader:   7:50:27   well…
Bank Z Trader:   7:50:30   that is the qu[estion]
Bank X Trader:   7:50:32   you know him best obv…
                 7:50:39   if you think we need to adjust it
                 7:50:43   then he shouldn't be[] in chat
Bank Y Trader:   7:50:54   yeah that is key
                 7:51:00   simple question [Bank Z trader]
                 7:51:08   I trust you implicitly [Bank Z trader]
                 7:51:13   and your judgement
                 7:51:16   you know him
                 7:51:21   will he tell rest of desk stuff
                 7:51:26   or god forbin his nyk…
Bank X Trader:   7:51:46   yes
                 7:51:51   that's really imp[ortant] q[uestion]
                 7:52:01   dont want other numpty's in mkt to know
                 7:52:17   but not only that
                 7:52:21   is he gonna protect us
                 7:52:33   like we protect each other against our own branches
                 7:52:46   ie if you guys are rhs1.. and my nyk is lhs..ill say my nyk lhs in few
Bank Z Trader:   7:53:52   what concerns me is that i know he'll never tell us when at risk…
```

The Citi order (p.6) names Bank X as "Citibank Trader" and continues in prose: _After further
discussion of whether the fourth trader would "add huge value to this cartell," the traders decided
to invite the trader into the chat room for a "1 month trial," with the Citibank trader warning him,
presumably facetiously, "mess this up and sleep with one eye open at night."_ (The "1" after `rhs`
is a footnote marker; the Citi order prints it as `rhs 5`.) NYDFS Barclays order p.7: _"One
particular chat room, referred to by the participating traders and other traders as the "Cartel"
included FX traders from Citigroup, JP Morgan, UBS, RBS and Barclays who specialized in trading the
Euro."_ and the new member "ultimately survived his "trial"."

**E2. Citi + JPM "double team it".** CFTC exhibit 2014 p.5–6; Citi order p.7. EUR/USD, just before
the 4pm WM/R fix. Bank Y has a large fix sell order; instead of netting it against Bank X they both
pile up 800m to sell into the window.

```
Bank Y Trader:   3:51:21   ok, i got a lot of euros
Bank X Trader:   3:51:25   ?
                 3:51:28   you selling?
Bank Y Trader:   3:51:30   yes
Bank X Trader:   3:51:33   now
                 3:51:35   or pickun?4
Bank Y Trader:   3:51:39   pick un
                 3:51:46   u want it? …
                 […]
Bank X Trader:   3:52:24   ill take it [Bank Y trader]
                 3:52:26   if u dont want it
Bank Y Trader:   3:52:39   tell you what
                 3:52:42   lets double team it
                 3:52:45   how much u got
Bank X Trader:   3:52:46   ok
                 3:52:47   300
                 3:52:52   u?
Bank Y Trader:   3:53:01   ok ill give u 500 more
Bank X Trader:   3:53:05   wow
                 3:53:06   ok
                 3:53:08   ha
                 3:53:09   cool…
                 […]
Bank Y Trader:   3:53:20   so we have 800 each
                 3:53:21   ok
                 3:53:31   but we gotta both do some at fix
                 3:53:36   don't sell em all and take foot off haha
Bank X Trader:   3:53:40   i promise i will
Bank Y Trader:   3:53:47   me too
```

Footnote 4: _"Pickun" is a slang term for a fix order._ Then: _At 4:00:14 the Bank X trader reported
that he was "hosed." The Bank Y trader replied with "ditto."_ So it failed.

**E3. JPM + Barclays "double team them".** CFTC exhibit 2014 p.4 (labelled JPMorgan); Barclays
exhibit 2015 p.2 (labelled "Barclays, JPMorgan"); FCA JPM notice pp.18–20. EUR/USD WM/R fix. Bank Y
(JPM) has 105m EUR to buy, Bank W (Barclays) 150m; they combine.

```
Bank W Trader:   3:46:53   i'd prefer we join forces
Bank Y Trader:   3:46:56   perfick
                 3:46:59   lets do this…
Bank Y Trader:   3:47:11   lets double team them
Bank W Trader:   3:47:12   YESssssssssssss

Bank W Trader:   4:03:25   sml rumour we haven't lost it
Bank Y Trader:   4:03:45   we
                 4:03:46   do
                 4:03:48   dollarrr
```

FCA JPM adds (p.19–20): Firm A had a buy order _"for a top [account]"_, watched the brokers (_"i got
the bookies covered"_), and next day: _"we were EPIC at the [WMR] fix yest". Firm B responded
"yeeeeeeeeeeeeeeeeeeah". Firm A added "i dragged [JPMorgan] in , we covered all the bases b/w us".
Firm B commented "so couldnt have been that $hit a week!!"_ The FCA's version of the JPM line is
"perfick…lets do ths…lets double team em". JPM bought 134m and Firm A 125m in the 60-second window,
41% of volume; profit to JPM about USD33,000.

**E4. Citi ECB fix: "nice and clear to mangle".** FCA Citi notice pp.18–20. EUR/USD 1:15pm ECB fix.
Five banks net their orders so Citi alone carries a 542m EUR buy into the fix (client need: 83m).

> (3) At 12:56pm, Firm A informed Citi that it had netted off its sell orders with another
> counterparty. Firm A told Citi that "u shud be nice and clear to mangle". This is an example of
> "leaving you with the ammo". The Authority considers that the reference to "mangle" referred to
> the opportunity for Citi to attempt to manipulate the ECB fix.
>
> (4) At 12:57pm, Firm C disclosed that it had net sell orders for the fix of EUR39 million and
> offered to "shift it" (i.e. to trade the order with a third party outside the chat room). At
> 1:01pm, Firm C told Citi that it had "matched on fix here… you're all clear".
>
> (5) ... Firm D offered to transfer these net buy orders to Citi or execute this order in a way
> that would assist Citi ("u can have oir i can help [sic]").

Then four escalating EBS bids in 12 seconds (25m at 1.3216, 50m at 1.3218, 100m at 1.3220, 400m at
1.3222); Citi bought 73% of EBS purchases; ECB fixed at 1.3222. Aftermath (p.20): _"impressive",
"lovely" and "cnt teach that". Citi noted "yeah worked ok". When the fix rate was published to the
market, Firm A commented "22 the rate" and Citi replied "always was gonna be"._ Profit USD99,000.
_My note: NYDFS Barclays p.11 quotes the same line with a date and a sender: "on February 21, 2012,
the same trader employed the same strategy of clearing the decks by selling EUR 47 million to RBS to
assist his fellow Cartel member at Citi, noting "gave mine to try at rbs so u shud be nice and clear
to mangle."" So Firm A = Barclays and the date is 21 Feb 2012 (my inference from the identical
quote)._

**E5. UBS ECB fix: "taking all the filth out", "shet", "bully".** FCA UBS notice pp.19–21. EUR/USD
ECB fix, sell side.

> (4) At 12:48pm, Firm A disclosed that its net sell orders had reduced to EUR100 million, but that
> it was "…hopefully taking all the filth out for u…".
>
> (5) At 1:02pm, Firm A disclosed that it had sold EUR25 million to a client ... ("lose… shet [i.e.
> 25 million] though natch dont buy").
>
> (7) At 1:03pm, Firm A disclosed that ... its net sell orders at the fix had been reduced to EUR50
> million ("i getting chipped away at a load of bank filth for the fix… back to bully [i.e. 50
> million]… hopefully decks bit cleaner").
>
> (9) ... Firm B advised Firm C to "go late" (i.e. buy later when the rate would be lower).
>
> (10) At 1:14pm, Firm B copied into the chat a comment made by UBS at 12:04pm that day describing
> an earlier fix as "the best fix of my ubs career." Firm B then said "chalenge [sic]" and Firm C
> added the comment "stars aligned".

UBS sold 100m at 1.3092 one second before 1:15, three pips under the best bid; ECB fixed at 1.3092;
profit USD513,000. Aftermath (p.21): _"hes sat back in his chaoir [sic]…feet on desk…announcing to
desk…thats why i got the bonus pool" and "yeah made most peoples year"_. _My note: NYDFS Barclays
p.10 dates "hopefully taking all the filth out for you [UBS Cartel member]" and "hopefully decks bit
cleaner" to 15 Feb 2012 and attributes them to a Barclays trader._

**E6. NYDFS's dated Cartel lines.** NYDFS Barclays order pp.5–10.

> "we are 3 of the top 4 eur books on the planet . . . if we cant help each other with liquidity . .
> . who can?" (p.5–6)
>
> On January 6, 2012, one Barclays trader, who was also a Head of the FX Spot desk in London,
> attempted to manipulate the ECB fix by unloading EUR 500 million right at the fix time, stating in
> the Cartel chat room "i saved 500 for last second" and in another chat room "i had 500 to jam it."
> (p.8)
>
> A trader at another bank wrote to the Barclays trader: "u selling still? . . . get a late 20 so
> ive sold them" and stated that he was planning to "watch your magic haha." (p.8, 6 Dec 2011)
>
> on December 1, 2011, with a trader from Citigroup, a Barclays trader indicated "If u bigger. He
> will step out of the way. . . We gonna help u." (p.10)

Also p.7: _One method was known as "building ammo," whereby a single trader would amass a large
position in a currency and then unload the "ammo" just before or during the fix to try to move
prices._

### One GBP/USD 4pm fix across seven rooms (HSBC, Barclays, others; 28 June 2011)

_CFTC exhibit pp.1–4 follows one HSBC trader ("Bank U") working a 400m cable sell order through
several rooms in the hour before the WM/R fix. FCA HSBC pp.18–20 narrates the same day. NYDFS p.10
quotes "He paid me for 186 . . . so shioud have giot rid of main buyer for u" as a Barclays trader
to an HSBC trader on June 28, 2011, which pins Bank W = Barclays and the date. Result: HSBC sold
311m in the window, 51% of Reuters selling; the four firms 63%; fix 1.6003; HSBC profit about
USD162,000._

**E7. Room 1: "team whack it".** CFTC exhibit p.1–2.

```
Bank W Trader 1:  2:50:21 pm:   early days but im a seller cable at fix
                                [. . .]
Bank S Trader:    3:11:43 pm:   here also
Bank R Trader:    3:24:50 pm:   u got much to do in fix [Bank Trader W]
Bank W Trader 1:  3:25:07 pm:   im seller 130 cable that it
                                [. . .]
Bank W Trader 1:  3:28:02 pm:   hopefulyl a fe wmore get same way and we can team
                                whack it
Bank R Trader:    3:28:17 pm:   ill do some digging
                                [. . .]
Bank W Trader 1:  3:36:13 pm:   im seller 170 gbp atmofix
Bank R Trader:    3:36:26 pm:   we sellers of 40
Bank U Trader:    3:38:26 pm:   lhs in cable at the fix
Bank U Trader:    3:38:29 pm:   good amount

Bank R Trader:    4:00:35 pm:   well done gents
Bank W Trader 1:  4:01:56 pm:   hooray nice team work
Bank U Trader:    4:02:22 pm:   nice one mate
```

**E8. Room 2 (one-to-one): "get lumpy".** p.2.

```
Bank U Trader:    3:25:19 pm:   get lumpy cable at the fix ok
Bank W Trader 2:  3:25:32 pm:   ta mate
Bank W Trader 2:  3:25:35 pm:   150 here
Bank U Trader:    3:25:46 pm:   400 odd here
Bank U Trader:    3:25:50 pm:   lets go
Bank W Trader 2:  3:26:00 pm:   yeah baby
Bank U Trader:    3:26:03 pm:   [Bank W Trader 1] is too
                                [. . .]
Bank W Trader 2:  3:27:00 pm:   sry thats the [Bank W] flow
Bank W Trader 2:  3:27:23 pm:   [Bank W Trader 1] gets
Bank U Trader:    3:28:26 pm:   so its 150 all day wiht you guys?
                                [. . .]
Bank W Trader 2:  3:36:34 p.m.: 170 here

Bank W Trader 2:  4:01:03 pm:   nice job mate
Bank U Trader:    4:03:34 p.m.: haha
Bank U Trader:    4:03:40 pm:   i sold a lot up there
Bank U Trader:    4:03:46 pm:   and over sold by 100
Bank U Trader:    4:03:48 pm:   hahaha
                                [. . .]
Bank W Trader 2:  4:04:06 pm:   sweet nice job
                                [. . .]
Bank W Trader 2:  4:05:04 p.m.: bravo
```

_"over sold by 100" is the FCA's "overselling": trading more than the client order needs, to push
the rate._

**E9. Room 3: "have that my son".** p.3.

```
Bank U Trader:    3:28:45 pm:   lhs in about 300 quid cable for the fix
Bank V Trader:    3:28:54 p.m.: sweet
Bank U Trader:    3:29:42 pm:   can you do some digging and seeif anyoine is that way
Bank V Trader:    3:29:52 pm:   ofcourse mate
Bank V Trader:    3:34:49 pm:   im getting 83 at mom mate
Bank U Trader:    3:34:56 pm:   nice
                                [. . .]
Bank V Trader:    3:37:38 pm:   someone tells a guy here he is getting 170 cble at fix
Bank V Trader:    3:43:28 pm:   see that [Bank U Trader]
Bank U Trader:    3:43:57 pm:   thx

Bank V Trader:    4:00:51 pm:   have that my son
Bank V Trader:    4:00:52 pm:   hahga
Bank V Trader:    4:00:56 pm:   v nice mate
Bank U Trader:    4:04:53 pm:   that worked nice mate
Bank V Trader:    4:05:44 p.m.: big time mate.
```

**E10. Room 4: "betty on the mumble".** p.3.

```
Bank W Trader 2:  3:36:18 pm:   see first seller now
Bank Z Trader:    3:36:48 pm:   you gettingt betty3 on the mumble still [Bank W Trader 2] ?
Bank Z Trader:    3:36:51 pm:   we have nowt
Bank W Trader 2:  3:36:56 pm:   yep
Bank W Trader 2:  3:36:59 pm:   170
Bank Z Trader:    3:37:05 pm:   ta
Bank Z Trader:    3:37:21 pm:   get it up to 60/70 then bash the fck out of it
Bank U Trader:    3:38:26 pm:   lhs in cable at the fix
Bank U Trader:    3:38:29 pm:   good amount
Bank Z Trader:    3:38:35 pm:   ta
                                [. . .]
Bank Z Trader:    4:00:28 pm:   nice work gents
```

Footnote 3: _Like the term "cable", "betty" is also a shorthand name for British Pound Sterling used
by some FX traders._ The exhibit adds that at 3:38 Bank U pasted "lhs in cable at the fix" / "good
amount" into three more rooms simultaneously.

**E11. Room 5: "ive taken him out".** p.3–4. A bank outside the rooms is "building" a buy order in
the opposite direction; Bank W Trader 1 trades with him first so he won't be buying at the fix
("clearing the decks").

```
Bank W Trader 1:  3:43:52 pm:   right ive taken him out
Bank W Trader 1:  3:43:58 pm:   he paid me for 186
Bank U Trader:    3:44:09 pm:   ok thx
Bank W Trader 1:  3:44:15 pm:   so shud have giot rid of main buyer for u
Bank W Trader 1:  3:44:58 pm:   im stilla seller of 90
Bank W Trader 1:  3:45:06 pm:   gives us a chance and ive paid a load of bro ha
Bank W Trader 1:  4:05:03 pm:   yeah babyxx
Bank W Trader 1:  4:05:11 pm:   [Bank U Trader] [Bank W Trader 1] combo boom
Bank U Trader:    4:05:22 pm:   loved that mate
Bank U Trader:    4:05:26 pm:   worked lovely
Bank U Trader:    4:05:34 p.m.: pity we couldn't get it below the 00
```

FCA HSBC footnote 12: _The FCA considers that "00" is a reference to the rate of GBP/USD
i.e.1.6000._ FCA HSBC p.20 adds the line _"we need a few more of those for me to get back on track
this month"_ and from another room _"dont mess with our ccy [currency]"_.

**E12. Room 6: "down to my last tenner".** p.4.

```
Bank W Trader 3:  3:54:32 pm:   can u let me know when are down to your last tenner
Bank U Trader:    3:55:02 pm:   ok
Bank U Trader:    3:55:10 pm:   i'm down to my last tenner
Bank W Trader 3:  3:55:17 pm:   ok ta
Bank W Trader 3:  3:55:41 pm:   just sold some more
Bank U Trader:    3:55:49 pm:   hahaha
Bank W Trader 3:  3:55:51 pm:   hehehe
Bank W Trader 3:  4:00:57 pm:   nice on[e] son
Bank U Trader :   4:03:15 pm:   learnt from a good fella
Bank W Trader 3:  4:15:43 pm:   there u go
Bank W Trader 3:  4:16:48 pm:   go early, move it, hold it, push it
```

_"go early, move it, hold it, push it" is the whole fix playbook in eight words: pre-position before
the window, move the rate, defend the level, push through the window._

### RBS-centred cable and AUD fixes

**E13. "80 quid", "I don my hat".** CFTC exhibit p.5; FCA RBS notice pp.18–20. GBP/USD WM/R fix,
sell side. _By the FCA narrative, Bank V here = RBS (it posts "1.6218..nice"; the FCA says RBS
posted "1.6218…nice") and Bank U = the FCA's Firm A._

```
Bank V Trader:   15:45:35   im getting abt 80 quid now…fixing
Bank U Trader:   15:45:54   my ny 100 quid…
Bank V Trader:   15:51:19   getting more than u now [Bank U Trader] betty
Bank U Trader:   15:51:26   ok thx
Bank W Trader:   15:52:23   nice job gents
Bank U Trader:   15:54:16   [Bank V Trader], just matched with [Bank 1] and [Bank 2] for 100,
                            still lhs in about 140
Bank V Trader:   15:54:26   cool ….
Bank Z Trader:   16:00:58   i don my hat ….
Bank W Trader:   16:01:08   what a job
Bank Z Trader:   16:01:23   welld one lads
Bank W Trader:   16:01:28   bravo
Bank V Trader:   16:07:03   1.6218..nice
Bank U Trader:   16:07:33   worked ok that one....
```

FCA RBS adds: RBS's first reaction to Firm A's 200m was _"blimey … judging by liq today…"_; RBS told
a second room _"we getting alot betty11 at fix"_; post-fix _"[RBS] is god"_ and Firm A: _"we fooking
killed it right… [Firm C], myself and RBS"_. RBS "built" 202m of client selling to 399m; fix 1.6218;
profit USD615,000. Footnote 11: _"betty" is a slang term commonly used in the FX markets for
GBP/USD. It is derived from rhyming slang. Betty is short for Betty Grable, that is cable, which in
the market means the GBP/USD currency pair._

**E14. Traders share "ammo".** CFTC exhibit p.5; CFTC RBS order p.6–7. AUD fix: three banks hand
their small AUD buy orders to Bank V so one trader buys 220m into the fix.

```
Bank T Trader:   15:43:32   buying aud and nzd at the fix
Bank V Trader:   15:43:43   Tkx
Bank T Trader:   15:43:52   ntg big
Bank V Trader:   15:43:59   Im buying 50 aud can do yours if you want
Bank T Trader:   15:45:13   ok . . .60 plse . . .****
Bank V Trader:   15:45:56   Great
Bank P Trader:   15:50:00   I need to buy 25 aud at the fix too.. any int? more
                            ammo for you…?
Bank V Trader:   15:50:21   Sure [Bank P Trader]
Bank P Trader:   15:51:24   cool all yours [Bank V Trader]
Bank V Trader:   15:51:46   Buying 220 now
Bank P Trader:   15:51:57   good luck
Bank T Trader:   15:52:20   load up your 50 offrs . . .
Bank P Trader:   15:53:14   ill do those ones if you want
Bank V Trader:   15:53:19   haah
Bank T Trader:   15:53:20   ur fkg [Bank V Trader], ramp it
Bank T Trader:   16:00:41   nice one *****
Bank P Trader:   16:00:56   look at you!...-well done mate . . .
```

### Netting off and "scores"

**E15. CHF fix matched off, then EUR.** CFTC exhibit p.6 (labelled Citibank).

```
Bank X Trader:   3:53:35   can anyone help in chf fix
                 3:53:38   i lose 130 total
Bank Y Trader:   3:53:46   arb it for more ammo
Bank X Trader:   3:53:55   [Bank Z trader] ur guy want it?
Bank Z Trader:   3:54:09   nope he's flatish i think
Bank W Trader:   3:54:16   buy the eurchf and les hammer eur
                 3:54:18   come on
Bank Y Trader:   3:54:29   [Bank X trader] ill do it of u want
                 3:54:33   ive nothing else to do…
                 […]
Bank X Trader:   3:54:53   ok 130 usdchf mine
Bank Y Trader:   3:54:57   ok 130 u buy

Bank Y Trader:   3:55:01   u want small eurusd?
Bank W Trader:   3:55:19   so [Bank Z trader] u get eur now?
Bank Z Trader:   3:56:00   checkin
Bank Y Trader:   3:56:04   right who wants 40 eur
Bank Z Trader:   3:56:06   sub 30
Bank Y Trader:   3:57:53   gd lk fellas
```

_At 4:00:44 the Bank Y trader stated "no surre any winner there." Three minutes later, the Bank X
trader replied with "wmr is impossible."_ _Note "i lose 130" = I am a seller of 130 (I "lose" the
currency), and the trade confirmation "ok 130 usdchf mine" / "ok 130 u buy": both sides restate
size, pair and direction. That is the voice-desk confirmation protocol, typed._

**E16. "Scores" and "fix it at 07".** CFTC exhibit p.7; UBS order p.7; Barclays exhibit p.2.

> The Bank Y trader said "it cant be a good day to be [right hand side]." Once the four traders
> determined they were all the same direction, the Bank W trader asked if "we gonna be able to get
> it to 05" to which the Bank Y trader responded "is that the troyal fkn we." After the fixing
> window closed the Bank X trader said "nice call" and the chat room members gave their "scores" or
> profits from the fix. The chat room members each claimed they made between $60,000 and $220,000.

```
Bank V Trader:   15:57:45   come on [Bank Z Trader] we can do this
                 15:57:50   fix it at 07
Bank Z Trader:   15:57:54   ha
                 15:58:55   keep seeing citi on the bid
                 16:00:50   nice work
```

**E17. RUB fix by false submissions.** Barclays exhibit 2015 p.2 (from Russian, "unofficial
translation").

> In one chat a RUB/USD trader suggested "we should all lower fix by several kopecks" to which
> another trader replied "yes." A third trader agreed that "it is a right idea to lower the fix by a
> few kopecks." The Bank W trader responded "so what, 5 kopecks and all/everyone is splendid."

NYDFS Barclays p.12 names the room: the _"Curling 2010" persistent multi-bank chat room_.

### Barclays: a month-end fix and a stop hunt, start to finish

**E18. Month-end USD fix.** FCA Barclays notice pp.22–25. Currency pair redacted; FCA gives only the
last two digits of rates. Barclays builds 306m of client/other-desk buying to 505m.

> (1) ... ("…my rebal guys are paying me for 150…"). Firm A replied stating "first of my fixings is
> a buy but guess long way to go".
>
> (2) ... Barclays replied "weak…sell" ... Firm C replied "so fck knows". ... ("i lose 160…to the
> rebalancing guys…usually they 4 mil usd…today 160"). Firm C replied "mmm…interesting".
>
> (3) ... Barclays responded "i think gotta chill but so far i 160…if we find thats the way ofg
> it…then game on". Firm B commented "COME ON!!!!!…i liking this…i just askin my guy…if i got
> anything yet". Firm A added "i fancy it today" and Barclays noted that if they were all buying USD
> "i wud fancy it tohahah".
>
> (6) At 3:45pm, Firm B commented to Barclays and Firm A "boooyyyys…so we alot". Firm B also
> disclosed that an inter-dealer broker was looking to trade an additional USD135 million ...
> ("…wants to do another 135…we want any of it").
>
> (7) ... encouraged Firm B to trade with the inter-dealer broker ("u do that"). Firm B subsequently
> confirmed ... ("ok…360"). This is an example of Firm B "building".
>
> (8) At 3:47pm, Firm A asked "so how [much] we got to buy in total". Barclays replied "400 me" and
> Firm A said "200". Firm B then stated "if we get this 75 bid i will love u both forever".
>
> (9) At 3:51pm, Firm D asked if Barclays was "the otehr way" ... ("wud rather do the 430 but will
> match with u if u cant offload in broker").
>
> (10) At 3:52pm, Firm D indicated that the situation had changed ... ("complet fl;ip now…i lose 80
> odd…fkin joke"). Barclays responded "cool…suits".

Rate moved 57 → 72 before the window, 72 → 80 in it, fixed 77; profit USD286,000. Aftermath:

> Barclays responded indicating it thought it had bought USD200 million at an average rate of 60 and
> then "bgt the messiest 300 ever at 75-78". ... Firm B congratulated the others "boys well done…top
> work". Barclays added "well I bgt the ugliest 300 there i cud haha". Firm A said "[Firm B] u ask
> for 75" (i.e. a fix rate of 75) and Barclays added "we delivered…but i dont wanna kiss from u…i
> just take a beer". Later, Firm B stated "[Barclays] thks for the encouragement…with the
> building…making me do…xtra 135". Barclays responded "suited us all didnt it".

**E19. Stop-loss hunt: "coiled cobra".** FCA Barclays pp.26–28. Client stop to buy GBP77m at 95;
Barclays tries three times to print 97 so it can fill the client at 96.5.

> (1) At 10:38, Firm X asked Barclays and Firms Y and Z if they had any stop loss orders ("u
> got…stops ?"). Barclays responded that it had a stop loss order for "80 quid" at a level of 95.
> Barclays noted it was "primed like a coiled cobra…concentrating so hard…[as if] made of
> wax…[haven't] even blinked".
>
> (2) At 10:46, the rate increased to 84 and Firm X commented "…is higher sint it". Barclays
> responded "watch out…will be soon".
>
> (4) At 10:49, Firm X commented "hope that was a o.t" (i.e. a one-touch order). ... Firm Y also
> stated "i was just about to say that". Barclays replied "errr…long some…here".
>
> (5) At 10:51, Firm X told Barclays "we pick up a seller…guy i like…and just above the print u
> need". Barclays responded ("ok…ta").
>
> (6) ... the rate fell to 85 and Barclays noted "fooooooooooookkkkk". ... noted it was "dead".
>
> (7) ... ("…cudnt get the 97 print…despite trying super hard"). Barclays noted that there were
> "algos galore at 96".
>
> (8) ... Firm X noted "attemot number 3". ... The purchase at 97 enabled Barclays to execute the
> stop loss order. Barclays then confirmed this to the other firms ("done").
>
> 4.70 ... Firm X commented, ironically, that Barclays would have "one happy cleitn !". Barclays
> responded "he shud be as he wants minimal protection and really cud have been done with 96
> print…but we held him in"). ... 4.71 ... Firm Y responded to Barclays: "hahahah…hardly
> [Barclays]…thats not holding him in…gd work though". Firm X concurred: "helkd him in…with a lot of
> cursingf…u tried to carve him…and eventually succeeded". Firm Z stated that Barclays' comment
> about holding the client in "might have to go in the quote book". Barclays responded "hehe".

The 97 trade was the only print at that level until about 16:00. Net loss USD63,845 (the hunt cost
more than it made).

**E20. Other banks' stop talk, one line each** (FCA notices, p.21–22 of each): HSBC: _"going to go
for broke at this stop… it is either going to end in massive glory or tears"_, _"just about to slam
some stops"_, of a client's stops _"nah love them … free money"_. JPM: _"to get the 69 print"_,
_"shall we go get these stops?"_. Citi: _"had to launch into the 50 offer to get me stop done"_,
_"went for a stop"_. RBS: _"HIT IT … I'm out of bullets haha"_. UBS: _"i had stops for years but
they got sick of my butchering"_, _"just jamming a little stop here"_.

### Beyond the G10 fix: NYDFS orders

**E21. BNP "ZAR Domination".** NYDFS BNP order pp.4–8 (scanned PDF; OCR spacing errors like
"offirepower" are the scanner's, not the trader's). A New York EM trader recruits a rand cartel,
then fixes spreads.

> Trader 1, explicitly referring to this group as a "cartel," labeled it "ZAR Domination." (p.4)
>
> [W]e got a little cartel really brewing ... really try and move zar . . . wont take much to push
> it . .. we will know where all the orders are . .. we got like 200 bucks offirepower ...
> occasional blow up but we win . . . make one chat room ... call it Zar domination ... i think it
> is a million dollar plan ... we have to be proactive on it though. couple times a week for it to
> pay off. (p.5–6)
>
> "so we could alternate names ... so no one would get an idea of where the selling or buying is
> really coming from," and noted, "thats a lot offirepower i think in ny ... [and to] just keep that
> quiet." (p.5)
>
> It "just seems to me that zar [is] one of the few ripe mkts out there for people with some stick
> behind em so why not. not going to make our budgets offflow or nickel and diming euro around."
> (p.6)
>
> Trader 2 informed the group that he had received an order to buy $50 million of Rand, asking, "250
> pips? 300?" ... Trader 1 responded, "ill match ... lets widen this out on people . .. if we all
> consistent...it becomes standard ahah." ... "tht way 250 is the new 200." (p.6–7)
>
> "i have one word for BNP . .. guarantee." Trader 5 congratulated the group, saying "salute to
> first coordinated zar effort." Trader 1 responded, ''yep many more to come." (p.7)
>
> "my spread is my spread . . . if we all in ny keep the same spread that will become the norm ...
> we set the spreads ... and we stand by them ... 50 in ny is 200 ... 25 in ny is 125 ... you guys
> agree or am i off." ... "that is what we show in ny ... custys dont like oh well ... where they
> going to go?" (p.8)

Footnotes identify Trader 1 as the defendant in _US v. Jason Katz_ (pleaded guilty 4 Jan 2017) and
Trader 2 as _US v. Christopher Cummins_ (pleaded guilty 11 Jan 2017).

**E22. BNP fix and "bully".** NYDFS BNP pp.13–14.

> "u want a Christmas present," and offered a fix order to Trader 13. Trader 13 replied, "u don't
> wanna wollop it?" ... "schweeeeet! Thks bra extra helped .. . extra ammo helped loads."
>
> "any huge interest ecb?" ... Trader 15 responded, "/ am the same way ... u want some ammo ... see
> what u made ofl?]" ... "good luck amigo." [OCR: "/" = "I"]
>
> After Trader 21 concluded, rhetorically, "how easy was that to bully?" Trader 22 responded: [M]ate
> it worked lovely, in these markets when we have the ball, we need to make it count, as you were
> scaring the voice market, I was putting stupid bids in.

Footnote 6 on p.14 identifies Traders 12 and 15 as "alleged members of the chat room known as "The
Cartel"" charged in _US v. Usher_.

**E23. Credit Suisse.** NYDFS CS order pp.5–11.

> "I think there's some lhs 2 action today at the fix on the back of tht massive m+a . . . massive
> caveat, info is from sales desk . . . but 4 o clock. . . . 16 yrds . . ." (p.5)
>
> "gve u something to front run . . . I mean strategialcally [sic] position agst," to which [Trader
> 2] replied, "hahahah." (p.6) ... "whos got a massive fix I can front run"; ... "anyone got a big
> fix I can front run plse." (p.6 fn.5, Oct/Dec 2008)
>
> "if the m+a bird walks thru the dealing room doors im gonna get quite excited." (p.6,
> SABMiller/Foster's day, 21 Sep 2011)
>
> code names such as "Tanktop" and "Shoefone" ... "satan bgt 10 aud" ... "n000000000," ... "they r
> still selling[,] a little birdie tells me." ... "I remember the old days, your satan info was
> legendary." (p.7) ... "[Satan] does all his spot with u [Trader 3] on yr toy now." ... "satan
> sells 8 euros at 17," ... "good shout," ... "[Trader 3] finally adds value." (p.7–8)
>
> "can't walk it down with u in the way." ... "once I get enough in I will push it up to make the
> fill look good then you can walk it down all you like." (p.9)
>
> "get ready unload on nzd," ... "I am. Nearly hit it last time." ... "if he can't get it lower we
> may be in trouble." ... "come to poppa," ... "phew." (p.9)
>
> "go for it I"ll stick in a few bids sub 74." ... "ok pulling my bids," ... "smlls unethical haha"
> and "if custy ever found out we both dead." Another chat room participant ... stated (with evident
> sarcasm): "what the hell are u two planning . . . this chat is a compliance dream." (p.10)
>
> "u need the ammo . . . go to it . . . lay people out if you can." ... "I will be giving u 100 at
> the fix . . . I would . . . get short smalls here then clamor it a few mins b4 for at least 150 .
> . . tell all my [friends] 2 min before that u just got the mothere of all lhs fixes . . . and ring
> it thru the fix window with the balance…what is your wall street account? When rate comes out I
> book it to your account quickly." ... "cmon [Trader 15] . . . get them." ... "hope that went ok."
> (p.10–11)
>
> "can you walk down usdtry for me pls." Trader 18 replied, "Yeah, no problem." Customer 1 then
> stated, "just offer 1 at like 72 . . . just walk it brotha," to which Trader 18 replied, "No
> sweat." ... "come on . . . just walk it," to which Trader 18 replied, "Collapsado." ... "thks
> [Trader 18] for walking it down . . . great job . . . you really shellacked it." Trader 18 quickly
> replied, "pleasure." (p.11)

Internal (not chat) front-running notes, p.13–14: _"it is the name of the game if we front-run
orders. Sometimes you win sometimes you lose. It's up to us to define the front run rules."_; _"we
=kiddo made money with the frontrun."_ (_kiddo_ is apparently CS's algo; UNVERIFIED gloss.)

**E24. Goldman.** NYDFS Goldman order pp.4–9 (scan).

> code names ... the "fiddler," "hat and coat," and "dodgy aussie seller." (p.4)
>
> "go it thx [Trader 11] ... aalso just hearing decent buying expected at 4pm fix, so maybe keep
> ammo dry." (p.7) ... "pleeease stay down here usd cad hahaha used up a fair bit of ammo." ... "can
> we get kiwi lower please." (p.7)
>
> [Room named "Young Guns"] "totally between u and me ...my nyk got a few usdcad to sell at 115."
> Trader 1 replied, "tks mate appreciate" and "yu are a legend," (p.7)
>
> "well the people i don't trust I useto spooof ... so ifl wanna buy usdzaar I get on bid ... and
> give them an offer." Trader 8 replied, "haha does it work well," to which Trader 7 stated, ''.Yes
> I bgetfilled ... then I say u been selling ... they go no we havnt." (p.8)
>
> "You need to spoof usd at this time ... so hit the 40s hit the 38s but an offer in for 3 or
> something at 37 then ask the broker what his machine shows and take him for like 30 or something."
> (p.8)
>
> "what the largest fix you ever done? ... actually scratch that ... not appropriate question."
> Trader 1 ... responded, "2 yards aud [2 billion Australian dollars] ... its fine." Trader 11
> replied, "adn did you move it[?]" to which Trader l replied, "4 big figures ... the numbers
> disappeared off the screen." (p.8–9)
>
> "lets sign a pact . .. on spreads." Trader 1 quickly responded, "agree." (p.9; the same exchange
> appears in the CS order p.11)

**E25. Barclays sales: the famous line, in context.** NYDFS Barclays p.14. _Note: this is about
hidden sales mark-ups, not fix manipulation._

> "markup is making sure you make the right decision on price . . . which is whats the worst price i
> can put on this where the customers decision to trade with me or give me future business doesn't
> change . . . if you aint cheating, you aint trying." (5 Nov 2010)
>
> "i wouldnt normally admit to clients if you pip them. i think saying you rounded is fine." ...
> "said i was rounding." (p.15)

Also p.13–14: sales staff signalled mark-ups by hand on open phone lines, _"one finger held sideways
would indicate a one-pip markup, while two fingers held sideways would indicate a two-pip mark-up."_
And p.11, USD/ZAR: _"if you win this we should coordinate you can show a real low one and will still
mark it little lower haha."_ ... _"prolly shudnt put this on perma chat,"_ ... _"if this is the chat
that puts me over the edge than oh well. much worse out there."_

### Baseline: what legitimate interbank dealing chat looked like (1996)

**E26. Knorr Cetina & Bruegger (2002), AJS pp.933, 938, 942–943.** Reuters Dealing 2000-2
transcripts from a Swiss bank, 25 Nov 1996. `#` = the Zurich trader.

The minimal three-turn deal (p.933):

```
FROM GB4L GB4NY GLOB SPOT LDN * 0923GMT 251196 */3377
Our Terminal: GBIZ Our user: <Name of Spot Dealer>
   CHF 10 PLS
# <lnSD>6267
   67
# 10 MID AGREED
# VAL 27NOV96
# MY CHF TO DIRECT
# THANKS AND BYE
# #INTERRUPT#
```

Their gloss (p.935): _deals are basically performed in three turns ... volume and kind of currency
("CHF 10"), price ("6267"), and buy or sell request ("67") ... the caller may respond equally well
by indicating intent (e.g., "I BUY" or "BUY" or "MINE"), rather than the rate._ A repair sequence
(p.938): `HALLOOOOOO THIS IS SPOT AND NOT FWDS OK?I` / `YES MATE SRY CUST.` / `MY RISK PSE` /
`NWOSPE` / `6263` / `SELL`, glossed as _"Yes, mate; sorry, customer"_ and "MY RISK PL[EA]SE" = the
price is off. A reciprocity breakdown reprinted from the ACI Code of Conduct (p.927–928):

```
   OK tks anything in 3 M DEM
# Sorry ntg there friend
   srry???????? ever heard from
   reciprocity????????
   ? if u won't quote I will cancel previous deal
#Mom
# Really sorry but ntg in DEM for the mom so noth. done in CHF
   frnds
   consider this relations as finished Bibib
```

_So the 2008–2013 multi-bank rooms inherit their abbreviations (tks, ntg, mom, pls) from 1990s
bilateral dealing screens, but swap the terse, all-caps, price-first protocol for lowercase running
banter._

### Short: other public corpora

**LIBOR, Barclays (2012).** FSA Final Notice, 27 Jun 2012, p.19,
https://www.fca.org.uk/publication/final-notices/barclays-jun12.pdf :

> The external trader stated in an email to Trader G at Barclays "If it comes in unchanged I'm a
> dead man". Trader G responded that he would "have a chat". ... "Dude. I owe you big time! Come
> over one day after work and I'm opening a bottle of Bollinger".

CFTC order, Jun 2012, pp.9–10,
https://www.cftc.gov/sites/default/files/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfbarclaysorder062712.pdf
:

> "WE HAVE TO GET KICKED OUT OF THE FIXINGS TOMORROW!! We need a 4.17 fix in 1m (low fix) We need a
> 4.41 fix in 3m (high fix)" ... "For you ... anything. I am going to go 78 and 92.5." ... "Always
> happy to help, leave it with me, Sir." ... "Done ... for you big boy ... " ... (Euribor, p.16–17)
> "no problem, I had not forgotton. The [voice] brokers are going for 3.372, we will put in 36 for
> our contribution;" ... "I love you."

**LIBOR, UBS (2012).** FSA Final Notice, Dec 2012, p.12 (summary p.4),
https://www.fca.org.uk/publication/final-notices/ubs.pdf :

> "if you keep 6s [i.e. the six month JPY LIBOR rate] unchanged today... I will fucking do one
> humongous deal with you ... Like a 50, 000 buck deal, whatever. I need you to keep it as low as
> possible ... if you do that ... I'll pay you, you know, 50,000 dollars, 100,000 dollars ...
> whatever you want ... I'm a man of my word".

**ISDAFIX, Barclays (2015).** CFTC order, 20 May 2015, pp.3, 7–8,
https://www.cftc.gov/sites/default/files/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfbarclaysorder052015.pdf
:

> notional amounts traders were willing to spend to influence USD ISDAFIX as "ammo" or as amounts
> the traders could "burn," "waste," or "use" to "get the print" or "affect" the "fix." ... "what
> happens at eleven is the bloody thing moves like half a basis point up and down because
> everybody's trying to bang the screen."

_"ammo" and "the print" are the same metaphors as FX, on a different desk (US rates swaps, New
York), 2007. That suggests these were general dealing-room words, not FX-specific._

---

## 3. Glossary (terms that appear in the excerpts above)

| Term                                                                                                                                                                           | Meaning                                                                                                                                              | Where / etymology                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **lhs / rhs**                                                                                                                                                                  | Left/right-hand side: seller / buyer of the base (first-listed) currency                                                                             | CFTC footnote defines it. From the two-way quote "bid / offer": the left number is where you sell to the dealer                        |
| **nyk, ny**                                                                                                                                                                    | Your bank's New York office ("my nyk is lhs")                                                                                                        | E1, E8                                                                                                                                 |
| **numpty**                                                                                                                                                                     | Idiot; outsiders in the market                                                                                                                       | Scots/N. English slang (dating UNVERIFIED)                                                                                             |
| **cartell / cartel, the players, A-team, 3 musketeers, 1 team one dream, a co-operative, ZAR Domination, Young Guns, Curling 2010**                                            | Room/group self-names                                                                                                                                | E1, FCA notices, NYDFS                                                                                                                 |
| **info lvls & risk sharing**                                                                                                                                                   | How much order info is shared, and taking each other's positions                                                                                     | E1                                                                                                                                     |
| **cable**                                                                                                                                                                      | GBP/USD                                                                                                                                              | CFTC fn.2. From the transatlantic telegraph cable that carried sterling–dollar quotes (standard story; from 1866, see earlier report)  |
| **betty**                                                                                                                                                                      | GBP/USD                                                                                                                                              | FCA RBS fn.11: rhyming slang, Betty Grable = cable                                                                                     |
| **quid**                                                                                                                                                                       | Millions of GBP ("300 quid cable", "80 quid")                                                                                                        | Quid = pound (old London slang) scaled to the desk unit                                                                                |
| **yards, yrds**                                                                                                                                                                | Billions ("16 yrds", "2 yards aud")                                                                                                                  | From French _milliard_                                                                                                                 |
| **bucks**                                                                                                                                                                      | Millions of USD ("200 bucks of firepower")                                                                                                           | NYDFS BNP gloss "[$200 million]"                                                                                                       |
| **tenner**                                                                                                                                                                     | 10 million ("last tenner")                                                                                                                           | Pound-note slang scaled up                                                                                                             |
| **shet**                                                                                                                                                                       | 25 million                                                                                                                                           | FCA UBS bracket; origin unknown to me (UNVERIFIED)                                                                                     |
| **bully**                                                                                                                                                                      | 50 million                                                                                                                                           | FCA UBS bracket. Probably darts "bull(seye)" = 50, also London slang for £50 (UNVERIFIED)                                              |
| **400 odd, 80 odd**                                                                                                                                                            | About 400 / 80                                                                                                                                       |                                                                                                                                        |
| **the fix, WMR / wmr, 4pm**                                                                                                                                                    | WM/Reuters 4pm London closing benchmark; 60-second window around 4:00 at the time                                                                    | NYDFS p.3                                                                                                                              |
| **ECB fix**                                                                                                                                                                    | ECB reference rate at 1:15pm London                                                                                                                  | NYDFS p.3. Citi believed it was the first EBS trade at 1:15:00 (FCA Citi p.19)                                                         |
| **pickun / pick un**                                                                                                                                                           | A fix order                                                                                                                                          | CFTC fn.4. _My guess: "pick-up", i.e. take at the fix price; UNVERIFIED_                                                               |
| **ammo, building ammo, more ammo, keep ammo dry, out of bullets**                                                                                                              | Orders/position you hold to throw at the fix                                                                                                         | FCA: "giving you the ammo" = consolidate into one trader; "leaving you with the ammo" = opposite-side traders net off outside the room |
| **building / built**                                                                                                                                                           | Increasing your fix position by trading with outsiders                                                                                               | FCA defines                                                                                                                            |
| **clearing the decks / taking out the filth / bank filth / decks bit cleaner**                                                                                                 | Netting off opposite-direction orders held by outsiders before the fix                                                                               | FCA defines. Naval: clear the decks before action                                                                                      |
| **net off, matched, matched on fix, shift it, offload in broker**                                                                                                              | Pair off fix orders with another bank or broker so they never hit the market                                                                         |                                                                                                                                        |
| **overbuying / overselling, over sold by 100**                                                                                                                                 | Trading more than the client order needs                                                                                                             | FCA defines                                                                                                                            |
| **double team, join forces, team whack, combo**                                                                                                                                | Two or more banks pushing the same direction                                                                                                         |                                                                                                                                        |
| **mangle, bash the fck out of it, hammer, ramp it, wollop, bully, jam it, push it, walk it down, lay people out, clamor, ring it thru the fix window, shellacked, Collapsado** | Hit the market aggressively to move it                                                                                                               | "walk it down" = keep offering lower in small clips                                                                                    |
| **digging**                                                                                                                                                                    | Finding out other banks' positions                                                                                                                   |                                                                                                                                        |
| **same way / that way / the other way**                                                                                                                                        | Same / opposite direction to me                                                                                                                      |                                                                                                                                        |
| **lumpy**                                                                                                                                                                      | Large ("get lumpy cable")                                                                                                                            |                                                                                                                                        |
| **flow**                                                                                                                                                                       | Client order flow ("the [Bank W] flow", "budgets of flow")                                                                                           |                                                                                                                                        |
| **all day**                                                                                                                                                                    | Firmly, all of it ("150 all day")                                                                                                                    |                                                                                                                                        |
| **at mom / mom**                                                                                                                                                               | At the moment / one moment                                                                                                                           | Also 1996 Reuters ("Mom")                                                                                                              |
| **the mumble**                                                                                                                                                                 | UNVERIFIED. Context: "you gettingt betty on the mumble still" (asking about a fix order)                                                             |                                                                                                                                        |
| **nowt / ntg / noth.**                                                                                                                                                         | Nothing                                                                                                                                              | nowt: Northern English                                                                                                                 |
| **flatish**                                                                                                                                                                    | Roughly no position                                                                                                                                  |                                                                                                                                        |
| **i lose 130 / i lose 160**                                                                                                                                                    | I am a seller of 130 (I give the currency up)                                                                                                        | E15, E18                                                                                                                               |
| **mine / u buy / paid me for 186**                                                                                                                                             | Trade confirmation: "mine" = I buy; "paid me" = he bought from me (lifted my offer)                                                                  | E11, E15                                                                                                                               |
| **hit / hit it**                                                                                                                                                               | Sell to a bid; or trade through a level to trigger a stop                                                                                            | FCA RBS, Goldman                                                                                                                       |
| **bid, offer, "on the bid", "the 50 offer", "sub 30"**                                                                                                                         | Prices; "sub 30" = below 30                                                                                                                          |                                                                                                                                        |
| **00, 05, 07, 22, 75, 97, 69**                                                                                                                                                 | Last two digits of the rate ("pity we couldn't get it below the 00" = 1.6000)                                                                        | FCA HSBC fn.12, Barclays fn.12                                                                                                         |
| **big figure / big figs**                                                                                                                                                      | The handle above the pips; "4 big figures" = moved 4 big figures                                                                                     | Goldman                                                                                                                                |
| **pips**                                                                                                                                                                       | Smallest quoted increment                                                                                                                            | DOJ plea p.4: _"percentage in point" or "pip"_. "pip them" = mark them up a pip                                                        |
| **print**                                                                                                                                                                      | A trade appearing on the platform at a level ("the 97 print", "69 print")                                                                            | Also ISDAFIX "get the print"                                                                                                           |
| **stops, stop loss, go get these stops, slam some stops, butchering**                                                                                                          | Client stop-loss orders, and trading to trigger them                                                                                                 |                                                                                                                                        |
| **o.t**                                                                                                                                                                        | One-touch order (fills if the market touches the level once)                                                                                         | FCA Barclays fn.14                                                                                                                     |
| **held him in**                                                                                                                                                                | Didn't fill the client's stop at a level the market did trade                                                                                        | FCA Barclays 4.70                                                                                                                      |
| **carve him**                                                                                                                                                                  | Rip off the client                                                                                                                                   |                                                                                                                                        |
| **algos galore**                                                                                                                                                               | Algorithmic selling at a level                                                                                                                       |                                                                                                                                        |
| **long / short / long some**                                                                                                                                                   | Position                                                                                                                                             |                                                                                                                                        |
| **barrier, knock out**                                                                                                                                                         | Option barrier levels to be triggered or defended                                                                                                    | NYDFS BNP p.15–16                                                                                                                      |
| **front run**                                                                                                                                                                  | Trade ahead of a known client order                                                                                                                  | CS                                                                                                                                     |
| **m+a, the m+a bird**                                                                                                                                                          | M&A-driven FX flow, the client walking in                                                                                                            | CS                                                                                                                                     |
| **custy / custys / cust**                                                                                                                                                      | Customer                                                                                                                                             |                                                                                                                                        |
| **Satan, Tanktop, Shoefone, fiddler, hat and coat, dodgy aussie seller**                                                                                                       | Client code names                                                                                                                                    | CS, Goldman                                                                                                                            |
| **toy**                                                                                                                                                                        | Electronic trading platform ("on yr toy")                                                                                                            | CS (my reading)                                                                                                                        |
| **spoof / spooof**                                                                                                                                                             | Place orders you don't intend to fill to mislead                                                                                                     | Goldman 2008                                                                                                                           |
| **perma chat**                                                                                                                                                                 | Persistent chat room (logged)                                                                                                                        | NYDFS Barclays                                                                                                                         |
| **bookies**                                                                                                                                                                    | Inter-dealer brokers                                                                                                                                 | FCA JPM ("i got the bookies covered")                                                                                                  |
| **kiwi / aussie**                                                                                                                                                              | NZD / AUD                                                                                                                                            |                                                                                                                                        |
| **scores**                                                                                                                                                                     | P&L from the fix                                                                                                                                     | CFTC                                                                                                                                   |
| **troyal fkn we**                                                                                                                                                              | Sarcastic "the royal we"                                                                                                                             |                                                                                                                                        |
| **perfick**                                                                                                                                                                    | "Perfect" in a rustic accent; widely associated with Pop Larkin, _The Darling Buds of May_ (H. E. Bates, 1958) (attribution from memory, UNVERIFIED) |                                                                                                                                        |
| **natch**                                                                                                                                                                      | Naturally                                                                                                                                            |                                                                                                                                        |
| **blimey, fooking, fooooookkkkk, fkin, fck**                                                                                                                                   | British swearing/exclamation                                                                                                                         |                                                                                                                                        |
| **mate, son, my son, lads, gents, boys, boooyyyys, bro, bra, brotha, fella, amigo, friend, frnds**                                                                             | Address terms                                                                                                                                        |                                                                                                                                        |
| **have that my son, combo boom, yeah baby, YESssss, hooray, bravo, I don my hat, what a job, EPIC, dollarrr, come to poppa, schweeeeet**                                       | Celebration                                                                                                                                          |                                                                                                                                        |
| **ta, thx, tks, tkx, cheers, ok, kk**                                                                                                                                          | Thanks / acknowledgment (kk: zero hits)                                                                                                              |                                                                                                                                        |
| **gd lk fellas, good luck, gl**                                                                                                                                                | Good luck before the window ("gl" itself: not found)                                                                                                 |                                                                                                                                        |
| **hosed, dead, ditto**                                                                                                                                                         | Lost money                                                                                                                                           |                                                                                                                                        |
| **game on, fancy it, suits, cool…suits**                                                                                                                                       | Agreement / it suits me                                                                                                                              |                                                                                                                                        |
| **standing down**                                                                                                                                                              | Refraining from trading so another room member can                                                                                                   | EC press releases                                                                                                                      |
| **kopecks**                                                                                                                                                                    | RUB fix unit                                                                                                                                         | CFTC Barclays exhibit                                                                                                                  |

**Standard FX-desk terms needed to follow these, not themselves quoted above:** base/quote currency
(FCA Barclays fn.11: rate = units of quote per one base); EBS and Reuters Matching (the two
interdealer electronic platforms; EBS for EUR/USD, Reuters for GBP/USD); voice vs electronic; spot =
T+2 settlement; given/lifted (sell to a bid / buy an offer; "lifted" not in these excerpts, but
"paid" is its synonym); axed, square, handle, choice, nfa, loonie, swissy: **did not appear** in
anything I read.

---

## 4. Register

- **Turn structure.** Messages are 1–8 words, sent as rapid bursts (E3: "we" / "do" / "dollarrr" in
  three messages over 3 seconds). Sentence breaks are carried by `…`, `..`, `. . .` instead of
  punctuation. Typos are left uncorrected ("hopefulyl a fe wmore", "giot rid", "attemot"), because
  speed beats accuracy and everyone can decode.
- **Case.** Lowercase by default. Capitals are emphasis ("YESssssssssssss", "COME ON!!!!!", "HIT
  IT"). The 1996 Reuters dealing screens were the opposite: all caps, price-first, 3 turns.
- **Compression.** Vowel-dropping (bgt, gd, thx, tks, ntg, smlls, sml, plse, pls, wud, cud, shud),
  numbers without units because the unit is implicit (millions of base currency; "300 quid"), rates
  by last two digits ("fix it at 07").
- **Dialect.** London/Essex working-class register worn by people at global banks: "my son", "have
  that", "blimey", "nowt", "ta", "fooking", "quid", "tenner", rhyming slang (betty). The EC named
  one room "Essex Express 'n the Jimmy" _"because all the traders but "James" lived in Essex and met
  on a train to London."_ The New York ZAR room is US register: "dude", "bucks", "custys".
- **Nicknames and code names**: for clients (Satan, Tanktop, fiddler) to evade compliance (CFTC:
  "code words to evade detection"); BNP traders proposed misspelling to look like typos (_"it will
  look more like a typo, also it will be much better than using stuff. .. which actually look like
  codes"_, BNP p.12).
- **Rituals.** Pre-fix: position disclosure in a fixed format ("lhs in cable at the fix" / "good
  amount", pasted to several rooms at once), then "gd lk fellas". Post-fix (within 60 s of 4:00):
  "well done gents", "nice job mate", "bravo", "I don my hat", then P&L "scores". Teasing via the
  "quote book".
- **Acknowledgment and confirmation.** Information receipt: "ta", "thx", "tks/Tkx", "ok thx", "ok",
  "nice", "cool", "sweet", "cheers". Trade confirmation restates the trade: "ok 130 usdchf mine" /
  "ok 130 u buy"; stop filled: "done"; acceptance: "all yours", "u do that", "ok…360", "cool…suits".
  In the 1996 dealing transcripts: "10 MID AGREED", "MY CHF TO DIRECT", "THANKS AND BYE", "MINE",
  "SELL".
- **"ack": confirmed absent.** Zero tokens of "ack", "acked" or "kk" in about 265,000 words of
  extracted text (all documents above, regulator prose included). The acknowledgment slot is filled
  by "ta", "thx", "ok", "cool". This matches the earlier finding: "ack" is not voice/chat FX idiom
  in this corpus.

---

## 5. Outcomes

1. **Fines (verified in the documents).** Nov 2014: CFTC $1.475bn (Citi 310m, JPM 310m, RBS 290m,
   UBS 290m, HSBC 275m); FCA £1,114.9m (Citi 225.6m, HSBC 216.4m, JPM 222.2m, RBS 217.0m, UBS
   233.8m). May 2015 Barclays: CFTC $400m, FCA £284.4m, NYDFS $485m, DOJ $650m criminal fine plus
   $60m for breaching its LIBOR NPA. DOJ guilty pleas (May 2015, press summary via search, not
   opened): Citicorp $925m, JPM $550m, RBS $395m; UBS $203m (LIBOR wire fraud). EC: €1.07bn
   (May 2019) + €344m (Dec 2021).
2. **Prosecuted.** Corporate parents pleaded guilty (May 2015). Individuals: Jason Katz (BNP) and
   Christopher Cummins (Citi) pleaded guilty Jan 2017 (NYDFS BNP footnotes); Usher, Ramchandani and
   Ashton indicted Jan 2017 (S.D.N.Y.).
3. **Usher acquittal.** Manhattan jury acquitted all three of conspiring to violate the Sherman Act
   on 26 Oct 2018. Defence: "there was nothing illegal about competing traders exchanging
   information about their positions"; ex-Standard Chartered trader Matt Gardiner testified that he
   took part in the chats.
   [Reuters via investing.com](https://www.investing.com/news/stock-market-news/london-forex-traders-found-not-guilty-in-us-rigging-case-1662036)
   (2018). The indictment itself contains no chat quotes.
4. **Mark Johnson (HSBC).** Convicted Oct 2017 (E.D.N.Y.) of wire fraud and conspiracy for
   front-running a $3.5bn Cairn Energy currency trade; "spent two years in prison" (per Reuters).
   The 2nd Circuit vacated the conviction 3–0 on 17 Jul 2025 because the "right to control" theory
   was repudiated in _Ciminelli v. US_ (2023), with "grave doubt" about the misappropriation
   fallback.
   [Reuters via Yahoo](https://www.yahoo.com/news/hsbc-executives-fraud-conviction-voided-181459783.html)
   (2025).
5. **UK.** No individual FX prosecutions found in what I read; the SFO closing its FX probe (2017)
   is UNVERIFIED. Ashton's attempt to get third-party rights over the FCA notices failed: Upper
   Tribunal, 12 Jan 2016, held he was not identified.

---

## 6. What I could not access

- **EC decision texts** (Three Way Banana Split C(2019) 3631, Essex Express C(2019) 3621, Sterling
  Lads C(2021) 8612). The EC case-search page returned an empty JS shell; no `dec_docs` PDF link
  found. Only the press releases (room names, "standing down") were read. The non-confidential
  decisions may contain chat extracts; a less-redacted Sterling Lads version was disclosed in the UK
  CAT _Evans v Barclays_ class action (2024).
- **DOJ plea agreements for Citicorp, JPM, RBS** (only Barclays' read) and the DOJ press release
  text (justice.gov returned empty; figures above come from search snippets).
- **Usher trial exhibits / transcript**: not public in anything I found. No chat lines from the
  trial.
- **NYDFS Deutsche Bank (2018) and Standard Chartered (2019) orders**: URL patterns I tried 404'd.
- **Federal Reserve and OCC orders** (OCC fined Usher and Ramchandani $5m each, per search snippet,
  UNVERIFIED).
- **Knorr Cetina, "Global markets as global conversations", _Text & Talk_ (2007)**: not attempted;
  the 2002 AJS paper was obtained instead.
- **Senate PSI London Whale exhibits (2013), spoofing cases, Enron tapes, RBS and Rabobank LIBOR
  notices**: skipped for time; FX came first.
- **Bloomberg "Inside the cartell" (2014)**: not re-read; superseded by the primary sources above.

Downloaded PDFs and extracted text:
`/private/tmp/claude-501/-Users-robbie-repos-dotfiles/8823d054-20f4-4b50-a47d-27a4a4dc86c0/scratchpad/fx-pdfs/`
and
`/private/tmp/claude-501/-Users-robbie-repos-dotfiles/8823d054-20f4-4b50-a47d-27a4a4dc86c0/scratchpad/fx-txt/`.
