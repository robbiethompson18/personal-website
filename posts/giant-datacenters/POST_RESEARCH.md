# Giant Datacenters: Research Notes

Compiled 2026-11-22 by Claude research agents for the `@c` notes in `FINAL_POST.md`. Each part is
one agent's full findings, with sources and quotes. The short versions are in the orange boxes in
the post.

---

# Part: New Carlisle (AWS Project Rainier, Anthropic)

## New Carlisle (Project Rainier) research notes

Compiled 2026-11-22. Labels used throughout:

- **PRIMARY** = the company, a regulator, or a government body said it.
- **REPORTED** = journalism citing a primary document or named person.
- **ESTIMATE** = third-party model (mostly Epoch AI).
- **MY ARITHMETIC** = computed here from the cited inputs.

Quote reliability: quotes from Epoch AI's page, Epoch's CSVs and calculation spreadsheet, and the
Measured AI article were read from the raw page text and are exact. All other quotes came through a
summarising fetch tool. They are short and matched the search snippets, but check each against the
page before quoting it in the post.

Not reachable: SEC EDGAR blocks undeclared scripts and the Anthropic S-1 is too large for the fetch
tool (14 MB), so every S-1 figure below is second-hand via CNBC, Tom's Hardware or a Substack that
read the filing. The S-1 itself is at
https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm (Anthropic
PBC, filed 2026-10-26; an amended S-1 followed on 2026-11-02).

---

### 1. Cost

**Best single number: $11 billion.** This is the only figure Amazon and the state have ever put on
the campus.

| Figure                                                      | What it covers                                                                                                                                                                                         | Type                                                                               | Source                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $11 billion                                                 | Announced capital investment for the campus. The 2024 county deal tied it to 16 data center buildings plus 8 support buildings. The equipment exemption in the deal implies servers are counted in it. | PRIMARY                                                                            | Indiana Economic Development Corporation, 2024: "plans to invest $11 billion to build a data center campus in north central Indiana and create at least 1,000 new jobs." https://www.iedc.in.gov/events/news/details/2024/04/25/gov.-holcomb-announces-amazon-web-services-plans-to-invest-11b-to-create-a-new-data-center-campus-in-northern-indiana |
| $11 billion (restated)                                      | Amazon still called it the $11B St. Joseph County investment in Nov 2025                                                                                                                               | PRIMARY                                                                            | Amazon, 2025: "This investment is additional to the $11 billion investment announced last year in St. Joseph County." https://www.aboutamazon.com/news/company-news/amazon-15-billion-indiana-data-centers                                                                                                                                            |
| $8.9 billion spent as of 2026-01-01                         | Amount of the $11B actually invested, of which $1.7B is assessed real property (so about $7.2B is equipment)                                                                                           | REPORTED, single secondary source, I could not find the local news story behind it | Measured AI (Corey Trinetti), 2026: "The county's first annual abatement-compliance review of AWS reported that $8.9 billion of the $11 billion had been invested as of January 1, 2026 — including $1.7 billion of assessed real property." https://measuredai.substack.com/p/aws-new-carlisle-data-center-campus                                    |
| $39.3 billion now, $72.9 billion at full buildout (Q1 2028) | All-in capital cost of the 18 operating buildings: IT hardware, building, power, land. 2025 USD.                                                                                                       | ESTIMATE                                                                           | Epoch AI, 2026 (updated Oct 19, 2026): "supported by 1,037 MW of IT power at a capital cost of $39.3 B. In Q1 2028, we project it to rise to 1,746k H100e AI compute, 1,925 MW IT power and a cost of $72.9 B." https://epoch.ai/data/ai-data-centers/directory/anthropic-amazon-new-carlisle                                                         |

**The two figures conflict by 3.5x and the reason is known.** Epoch does not price Trainium. Its
methodology says "we use the same cost-per-Watt values regardless of a data center's hardware type
or operation date" and the model "outputs a $38B capital cost per gigawatt of IT power" ($26B
compute + $12B construction), calibrated on Nvidia GB200 racks (Epoch AI, 2026,
https://epoch.ai/data/data-centers-documentation/methodology). Check: 1.037 GW x $38B = $39.4B.
Amazon makes its own chips and pays no Nvidia margin. Epoch's own chip table prices a Trainium2 at
about $4,000 against $25,000 for an H100. So the Epoch number is what the site would cost if it were
an Nvidia cluster of the same wattage, and the $11B / $8.9B figures are what Amazon reports
spending.

Other cost facts:

- The NYT (2025) says the $11B was for 16 buildings and Amazon now plans about twice that, with
  total cost "not clear": "Amazon promised US$11 billion to build 16 buildings". Syndicated copy:
  https://thenightly.com.au/business/the-new-york-times-at-amazons-biggest-data-centre-everything-is-supersized-for-ai-c-19309860
  (original: https://www.nytimes.com/2025/06/24/technology/amazon-ai-data-centers.html).
- **No announced dollar figure for the 14-building south expansion: not found.** Searched Amazon
  press, county council coverage and trackers.
- The $15 billion announced Nov 24, 2025 is for different sites in Northern Indiana (NIPSCO
  territory, 2.4 GW), not New Carlisle. PRIMARY, Amazon, 2025, URL above.
- Tax breaks (REPORTED, NYT 2025): state sales tax exemption "could ultimately be worth around $4
  billion" over 50 years; county breaks "could save Amazon an additional $4 billion over the next 35
  years".
- MY ARITHMETIC: $11B is 1.1% of a trillion dollars. Epoch's full-buildout $72.9B is 7.3%.

### 2. Workforce

| Figure                                                                | Type                              | Source                                                                                                                                                                                |
| --------------------------------------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| About 4,000 construction workers on site in a typical week (mid-2025) | REPORTED                          | NYT, 2025: "On a typical week, about 4,000 workers are on site" (URL above)                                                                                                           |
| More than 4,000 daily at peak, in a town of about 1,900               | REPORTED                          | CNBC, 2025. https://www.cnbc.com/2025/10/29/amazon-opens-11-billion-ai-data-center-project-rainier-in-indiana.html                                                                    |
| Close to 9,000 construction jobs supported to date                    | REPORTED, secondary               | Measured AI, 2026: "At peak, roughly 4,000 construction workers are on the AWS site each day. To date, the build has supported close to 9,000 jobs and more than $1 billion in GDP"   |
| Permanent jobs promised: at least 1,000                               | PRIMARY                           | IEDC, 2024 (quote in section 1)                                                                                                                                                       |
| Of those, 400 direct Amazon jobs, the rest contractors                | REPORTED                          | Inside Indiana Business, 2024: "Amazon plans to add 400 direct jobs at the campus". https://www.insideindianabusiness.com/articles/incentives-approved-for-amazon-data-center-project |
| 935 permanent on-campus jobs as of June 2026                          | REPORTED, single secondary source | Measured AI, 2026: "AWS reported 935 permanent on-campus jobs to date — a count that excludes construction labor"                                                                     |

Use 4,000 for "x workers build it".

### 3. Site size

Land (sources conflict, they measure different things):

- 1,200 acres: NYT 2025 ("a 1,200-acre stretch of farmland outside New Carlisle") and CNBC 2025.
  REPORTED.
- 870 acres: the three parcels in the county tax abatement. Inside Indiana Business, 2024: "three
  parcels of land totaling 870 acres". REPORTED from county documents.
- 882 acres mapped for development (805 in building lots + 77 road right-of-way). Measured AI, 2026.
  REPORTED from county plats.

Buildings:

- 18 operating as of Oct 2026 (9 north, 9 south). ESTIMATE from satellite imagery, Epoch AI, 2026:
  "Buildings 17-18 are operational. This is an estimate based on a rule of thumb". Measured AI says
  phases 1 and 2 (18 buildings) were construction complete Dec 2025 with operating permits Feb 2026.
- 14 more under construction (buildings 19 to 32; eight single-story, six two-story), 406 backup
  generators permitted. Epoch projects them operational March 2028; AWS has said full buildout no
  earlier than late 2027 (Measured AI).
- 32 total. NYT and CNBC say "around 30"; the 2024 county deal covered 16.

Indoor floor area:

- Per building: 216,000 sq ft for the north campus (Measured AI, 2026: "nine data center buildings,
  each about 35 feet tall and 216,000 square feet in size"); "about 200,000 square feet" per shell
  in the 2024 county deal (Inside Indiana Business, 2024).
- Full buildout: about 6.5 million sq ft across 32 buildings (Measured AI, 2026: "32 data center
  buildings on roughly 882 acres formally mapped for development, with about 6.5 million square feet
  of building area").
- MY ARITHMETIC (1 acre = 43,560 sq ft):
  - Today, 18 buildings x 216,000 = 3.89 million sq ft = **89 acres**. Assumes the 9 south buildings
    match the north ones; no source gives their size.
  - Lower bound, 18 x 200,000 = 3.6 million sq ft = 83 acres.
  - Full buildout, 6.5 million sq ft = **149 acres**.

### 4. Power

| Figure                                                           | Type                                                                          | Source                                                                                                                                                                               |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Now: 1,037 MW of IT power**, 1,244 MW total facility (PUE 1.2) | ESTIMATE from generator counts in air permits                                 | Epoch AI, 2026, directory page and calculation sheet https://docs.google.com/spreadsheets/d/1umU-KLAB_6A-lKRCdLuF7SPv74HlqKjDdfDor1bRGuY                                             |
| Full buildout: 1,925 MW IT, 2,310 MW facility                    | ESTIMATE                                                                      | Epoch AI, 2026: "Air permit for Buildings 19-32, suggesting expansion to 2.3 GW total facility power"                                                                                |
| Full buildout: 2.2 GW                                            | REPORTED                                                                      | NYT, 2025: "The facility will consume 2.2 gigawatts of electricity"; CNBC, 2025: "more than 2.2 gigawatts of electricity"                                                            |
| Full buildout: 2,250 MW at a 90% load factor                     | REPORTED from Amazon's filings with the Indiana Utility Regulatory Commission | The Times (Munster) via GovTech, 2025: "would have a 2,250-megawatt capacity". https://www.govtech.com/artificial-intelligence/indiana-data-center-could-bring-significant-power-use |
| Grid delivery: about 1.1 GW of 345 kV service by December 2026   | REPORTED, secondary, citing AEP                                               | Measured AI, 2026: "a ~$185 million transmission package targeting an initial ~1.1 GW of service by December 2026"                                                                   |

Use 1.0 GW IT (about 1.2 GW at the meter) for today and 2.2 GW for full buildout.

Supplier: Indiana Michigan Power (I&M), a subsidiary of American Electric Power, on the PJM grid. No
on-site generation except 878 emergency diesel generators at full buildout (Measured AI, 2026:
"There are no gas turbines, fuel cells, or behind-the-meter power plants").

New generation tied to the load:

- I&M bought an existing 870 MW gas plant, the Oregon Clean Energy Center in Oregon, Ohio. IURC
  approved it Nov 19, 2025, ownership expected March 2026. PRIMARY, AEP, 2025: "an existing 870
  megawatt (MW) natural gas plant located in Oregon, Ohio".
  https://www.aep.com/news/stories/view/10588/ . It is an existing plant changing hands, not new
  build, and AEP's release does not name Amazon.
- I&M forecasts Indiana peak demand going from "approximately 2,800 MW in 2024" to more than 7,000
  MW around 2030 (same AEP release).
- I&M's current mix per Measured AI, 2026: about 53% nuclear, 35% coal, 11% renewables. Amazon has
  about 635 MW of Indiana wind and solar under contract (same source).
- MY ARITHMETIC: 2,250 MW x 0.9 x 8,760 h = 17.7 TWh a year at full buildout.

### 5. Chips and compute

What's installed:

- Trainium2, Amazon's in-house chip. PRIMARY, Amazon, 2025: "nearly half a million Trainium2 chips"
  (Oct 29, 2025).
  https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster
- AWS CEO Matt Garman, Oct 2025: "They're already running about 500,000 chips in Indiana today"
  (CNBC, 2025, URL in section 2). That count matched 7 buildings.
- Now, ESTIMATE, Epoch AI, 2026: 1,044,976 Trainium2 in buildings 1 to 16. Epoch's compute model
  puts Trainium3 in buildings 17 and 18 (104,067 chips), though its public chip list for the site
  still says Trainium2 only. Amazon has not confirmed Trainium3 at New Carlisle.
- Nvidia GPUs at New Carlisle: none reported. Searched; not found.
- Anthropic fleet-wide (not just Indiana), PRIMARY, Anthropic, April 2026: "we currently use over
  one million Trainium2 chips to train and serve Claude".
  https://www.anthropic.com/news/anthropic-amazon-compute

Per-chip peak used (Epoch chip table, https://epoch.ai/data/ai_chip_sales_chip_types.csv, which
matches AWS's own specs of 20.8 petaflops per 16-chip Trn2 instance and 362 petaflops per 144-chip
Trainium3 server):

| Chip                    | fp8 (dense) | fp16     | Power |
| ----------------------- | ----------- | -------- | ----- |
| Trainium2               | 1.299e15    | 6.67e14  | 500 W |
| Trainium3               | 2.52e15     | 6.71e14  | 700 W |
| Nvidia H100 (reference) | 1.979e15    | 9.895e14 | 700 W |

**Third-party estimate (Epoch AI, 2026): 1.62e21 fp8 FLOP/s today = 1.62 zettaFLOP/s = 10^21.2,
equal to 818,000 H100-equivalents.** At full buildout: 3.46e21 (10^21.5), 1.746 million
H100-equivalents. Quote: "It hosts an estimated 818k H100-equivalents of AI compute".

Epoch's arithmetic, reproduced from its sheet:

- Chips per building = facility power / (PUE x IT overhead x chip watts) = 68.25 MW / (1.2 x 1.742 x
  500 W) = 65,311 Trainium2.
- Buildings 1 to 16: 16 x 65,311 x 1.299e15 = 1.357e21.
- Buildings 17 and 18: 76.125 MW / (1.2 x 1.742 x 700 W) = 52,033 Trainium3 each; 2 x 52,033 x
  2.52e15 = 2.62e20.
- Total 1.357e21 + 0.262e21 = **1.62e21 fp8 FLOP/s**. Divide by 1.979e15 = 818,428 H100e.

MY ARITHMETIC, alternatives:

- fp16 for the same chips: 1,044,976 x 6.67e14 + 104,067 x 6.71e14 = **7.7e20 fp16 FLOP/s**.
- Primary-source floor (Oct 2025, Amazon's count only): 500,000 x 1.3e15 = 6.5e20 fp8.
- If buildings 17 and 18 hold Trainium2 instead: 18 x 65,311 x 1.299e15 = 1.53e21 fp8.

SemiAnalysis, 2025 (paywalled; free preview only): three AWS campuses "boasting over 1.3GW of IT
capacity for the sole purpose of serving Anthropic's training needs", with "just under a million
Trainium2 in the largest campus".
https://newsletter.semianalysis.com/p/amazons-ai-resurgence-aws-anthropics-multi-gigawatt-trainium-expansion
. Consistent with Epoch.

Rank: third-largest AI data center in Epoch's list by compute as of Nov 2026, behind Colossus 2
(1,112k H100e) and Stargate Abilene (1,019k), and the largest by power (1,037 MW vs 946 and 824).
https://epoch.ai/data/data_centers/data_centers.csv

### 6. Share of Anthropic's compute, and the portfolio

**No primary source gives the share.** Per CNBC and Tom's Hardware (2026), the S-1 names the chips
but gives "no percentage splits or GW measurements".

End of 2025 (ESTIMATE, Epoch AI, 2026,
https://epoch.ai/data/ai_chip_users_intermediates_by_lab.csv):

- Anthropic total: 1,377 MW of IT power (90% interval 992 to 1,889), 1.19 million H100e (0.84 to
  1.72 million). Trainium2 was 52% of the power (35% to 70%).
- New Carlisle on Dec 23, 2025: 626 MW, 471k H100e.
- MY ARITHMETIC: 626 / 1,377 = **45% of power**, 471 / 1,190 = **40% of compute**.

Late 2026 (MY ARITHMETIC, three ways, all land near 30%):

- Against Anthropic's reported target. The NYT reportedly said Anthropic expects just over 3.5 GW
  online by end of 2026, cut from about 5 GW told to investors in September (I found only secondary
  coverage: https://cryptobriefing.com/anthropic-3-5-gw-compute-capacity-2026/ , Nov 3, 2026:
  "Anthropic expects to have more than 3.5 gigawatts of computing capacity online by the end of
  2026."). 1,037 / 3,500 = **30%**.
- Against every Epoch-listed site tied to Anthropic, by power: New Carlisle 1,037 + Colossus 2 946 +
  Colossus 1 340 + Madison MS 284 + Ridgeland MS 228 + Lake Mariner 210 + Berwick PA 108 = 3,153 MW.
  1,037 / 3,153 = **33%**.
- Same sites by compute: 818 / 2,966k H100e = **28%**. Lower because Trainium2 does less per watt
  than Blackwell or TPU v7.
- These overcount Colossus 2 (shared with SpaceXAI and Cursor) and three AWS sites Epoch marks
  "speculative" for Anthropic, and undercount Azure and Google-hosted TPUs, which Epoch does not
  attribute by site. Against only the confirmed sites (New Carlisle, Colossus 1, Lake Mariner) it is
  59%, which is a ceiling.

Use **about 30%** for late 2026, down from about 40 to 45% a year earlier.

Portfolio as of late 2026:

| Supplier                        | Chips                                 | Size                                                                                                                                                           | Status                                                                                                   | Source                                                                                                                                                                      |
| ------------------------------- | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon (AWS)                    | Trainium2, Trainium3, later Trainium4 | Up to 5 GW; "nearly 1GW total of Trainium2 and Trainium3 capacity coming online by the end of 2026"; at least $110.0B, May 2026 to April 2036                  | Operating: New Carlisle about 1.0 GW IT, plus Mississippi and Pennsylvania sites (speculative per Epoch) | PRIMARY: Anthropic, 2026, https://www.anthropic.com/news/anthropic-amazon-compute . $ via S-1 as reported by Tom's Hardware, 2026                                           |
| Google Cloud                    | TPU                                   | Up to one million TPUs, "well over a gigawatt of capacity online in 2026"; at least $114.5B, April 2026 to July 2033                                           | Coming online through 2026                                                                               | PRIMARY: Anthropic, 2025, https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services                                                                |
| Broadcom (TPUs leased directly) | TPU                                   | About 3.5 GW from 2027 (Broadcom filing); Anthropic calls the combined Google and Broadcom deal 5 GW; about $161.2B rent on five-year leases                   | Mostly 2027 onward, some in 2026                                                                         | PRIMARY: Anthropic, 2026, https://www.anthropic.com/news/google-broadcom-partnership-compute ; $ via S-1 per Tom's Hardware                                                 |
| SpaceX (formerly xAI)           | Nvidia H100, H200, GB200              | Colossus 1: 300+ MW, 220,000+ GPUs. With Colossus 2: about 325,000 GPUs. Up to $120.5B into 2029, about $3.1B a month once fully delivered (expected Dec 2026) | Operating since May 2026                                                                                 | PRIMARY: Anthropic, 2026, https://www.anthropic.com/news/higher-limits-spacex ; S-1 terms via https://capefearadvisors.substack.com/p/anthropic-and-spacex-one-relationship |
| Microsoft Azure                 | Nvidia Grace Blackwell, Vera Rubin    | Up to 1 GW; $30B at signing, at least $44.9B in the S-1, Nov 2026 to May 2033                                                                                  | Starts Nov 2026                                                                                          | PRIMARY: Microsoft, 2025, https://blogs.microsoft.com/blog/2025/11/18/microsoft-nvidia-and-anthropic-announce-strategic-partnerships/                                       |
| Nscale, Lambda                  | Nvidia                                | About $44.6B and $41.3B, into 2033 and 2034                                                                                                                    | Future                                                                                                   | S-1 per Tom's Hardware, 2026                                                                                                                                                |
| AMD                             | Instinct MI450                        | Up to 2 GW, over $20B                                                                                                                                          | First capacity 2027                                                                                      | S-1 per Tom's Hardware, 2026                                                                                                                                                |
| Fluidstack                      | Hosts the Broadcom-leased TPUs        | $50B program, Texas and New York                                                                                                                               | Lake Mariner operating                                                                                   | PRIMARY: Anthropic, 2025, https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure                                                         |

Totals: $895.4B of purchase and lease commitments as of Sept 30, 2026 (amended S-1, via
https://cryptobriefing.com/anthropic-3-5-gw-compute-capacity-2026/). Third-party estimate of
contracted (not operating) capacity: about 11 GW, of which Nvidia 4.7 GW (42%), TPU 4.5 GW, Trainium
1.2 GW, AMD 0.8 GW (TradingKey, 2026,
https://www.tradingkey.com/analysis/stocks/us-stocks/262241466-anthropic-ipo-reveals-11gw-compute-footprint-nvidia-accounts-42-tradingkey
). The Trainium figure there looks low against Anthropic's own "up to 5 GW".

**Colossus: confirmed.** Anthropic rents all of Colossus 1 and part of Colossus 2 in Memphis.
Anthropic, May 6, 2026: "We've signed an agreement with SpaceX to use all of the compute capacity at
their Colossus 1 data center." and "more than 300 megawatts of new capacity (over 220,000 NVIDIA
GPUs) within the month." Correction for the post: xAI merged into SpaceX in Feb 2026, so the
landlord is SpaceX. Either side can cancel on 90 days' notice after initial periods ending Jan and
March 2027. Epoch lists Colossus 1 at 276k H100e and 340 MW with Anthropic as the only user, and
Colossus 2 at 1,112k H100e shared between SpaceXAI, Anthropic and Cursor.

For the footnote's "y% of Nvidia is at Colossus": not found as a number. As of Nov 2026 Colossus is
essentially all of Anthropic's operating Nvidia capacity that can be placed on a map, since Azure
starts Nov 2026 and Nscale, Lambda and AMD are later.

For "x% TPU vs y% Nvidia": not found for operating capacity. Only the contracted split above (TPU
4.5 GW vs Nvidia 4.7 GW of about 11 GW) and Epoch's end-2025 figure (Trainium 52% of power, TPU and
Nvidia together 48%).

Where the TPUs physically are:

- Google Cloud's own data centers for the Oct 2025 deal. Sites not disclosed. Not found.
- Broadcom-leased TPUs go into sites built by Fluidstack. NYT, quoted via
  https://glennklockwood.com/garden/entities/fluidstack : "Anthropic is installing these chips in
  data centers it is building with a company called Fluidstack".
  - **Lake Mariner, Barker, New York** (TeraWulf's site at a former coal plant on Lake Ontario). The
    only one operating. ESTIMATE, Epoch AI, 2026: "an operational AI data center with AI chips owned
    by AI XPV Platform and likely used by Anthropic", 293k H100e, 210 MW, TPU v7, rising to 527k
    H100e and 378 MW in Q1 2027.
    https://epoch.ai/data/ai-data-centers/directory/anthropic-lake-mariner
  - Barber Lake, Colorado City, Texas (Cipher Mining, 168 to 207 MW). Not yet operating per Epoch,
    Nov 2026.
  - River Bend, West Feliciana Parish, Louisiana (Hut 8, 245 MW first phase, first hall Q2 2027).
- For the April 2026 deal Anthropic says only: "The vast majority of the new compute will be sited
  in the United States."
- So the post's blank "frontier pretrains at \_\_" has no sourced answer. The largest identifiable
  TPU site is Lake Mariner at 5.8e20 fp8 FLOP/s, about a third of New Carlisle.

### 7. Commercial arrangement

- **Amazon owns the land, the buildings and the chips; Anthropic rents the compute.** NYT, 2025: "By
  early 2024, Amazon owned the land" and Amazon "will rent computing power from the new facility to
  its startup partner". Epoch AI, 2026: "an operational AI data center with AI chips owned by Amazon
  and used by Anthropic". Built and operated by Amazon Data Services, Inc. with no third-party
  developer (Measured AI, 2026).
- Dedicated to one customer. CNBC, 2025: "built exclusively to train and run models from Anthropic."
- **Term: ten years, not five.** PRIMARY, Anthropic, April 20, 2026: "committing more than $100
  billion over the next ten years to AWS technologies". S-1, as reported by Tom's Hardware and CNBC,
  2026: "at least $110.0 billion between May 2026 and April 2036", owed "regardless of actual
  usage". This is an AWS-wide commitment. **No New Carlisle-specific lease or term has been
  reported: not found.**
- The five-year figure belongs to a different deal: the Broadcom TPU equipment leases.
- Amazon is also an investor: $8B before 2026, $5B in April 2026, up to $20B more tied to milestones
  (Anthropic, 2026).
- Amazon's own power contract with I&M runs under a large-load tariff with a 12-year term and 80%
  minimum billing (Measured AI, 2026, citing IURC order 46097).

### 8. When did the world have this much compute

No published "as much as the whole world in 20xx" claim for this site: not found. Two ways to work
it out.

**AI chips only (best data).** Epoch AI's chip sales dataset, updated Nov 19, 2026,
https://epoch.ai/data/ai_chip_sales_timelines_by_chip.csv . Cumulative AI accelerators sold
worldwide since Q1 2022, in H100-equivalents (MY ARITHMETIC, summing Epoch's quarterly medians):

| Through end of | Cumulative H100e | fp8 FLOP/s |
| -------------- | ---------------- | ---------- |
| Q4 2022        | 303k             | 6.0e20     |
| Q2 2023        | 666k             | 1.32e21    |
| Q3 2023        | 1,060k           | 2.10e21    |
| Q4 2023        | 1,595k           | 3.16e21    |
| Q1 2024        | 2,423k           | 4.79e21    |
| Q4 2024        | 6,689k           | 1.32e22    |
| Q4 2025        | 20,307k          | 4.02e22    |
| Q2 2026        | 31,617k          | 6.26e22    |

- New Carlisle today (818k H100e) falls between Q2 and Q3 2023. Linear interpolation gives early
  August 2023. **"As many flops as all the AI chips in the world as of mid-2023."**
- At full buildout (1,746k H100e): January 2024.
- New Carlisle is 818k / 31,617k = 2.6% of all AI compute sold through mid-2026.
- Caveats: the series starts in 2022, so chips sold earlier (A100s from 2020 and 2021, older TPUs)
  are missing, which pushes the true date a few months earlier. It counts chips sold, not chips
  installed and running.

**All computers of every kind.** AI Impacts, about 2016: world computing capacity was "probably
around 2 x 10^20 – 1.5 x 10^21 FLOPS" at "around the end of 2015".
https://aiimpacts.org/global-computing-capacity/ . New Carlisle's 1.6e21 sits at the top of that
range, so "the whole world's computers around 2015" is defensible. It is not like for like: that
estimate is general-purpose arithmetic at higher precision, and New Carlisle's number is 8-bit peak.
At fp16 (7.7e20) the site sits mid-range.

---

### Edit made to the post

In `/Users/robbie/repos/personal-website/posts/giant datacenters/FINAL_POST.md`, line 13, replaced
`\_\_ (@c research this plz)` with `$11 billion` plus an HTML comment giving the IEDC 2024 source
and the Epoch $39.3B / $72.9B alternative. Nothing else touched.

---

# Part: Abilene (Stargate, OpenAI) and the Power Chart Reference Numbers

## Stargate Abilene research notes

Compiled 2026-11-22. Labels used throughout:

- **[PRIMARY]** = stated by the company, agency or dataset owner itself (Crusoe, Oracle, OpenAI,
  EIA, Bureau of Reclamation, Nvidia).
- **[PRESS]** = news reporting, usually citing unnamed sources or relaying a primary statement.
- **[ESTIMATE]** = third-party estimate (Epoch AI etc.).
- **[MY ARITHMETIC]** = computed here from the cited inputs.

How the quotes were checked: I read these directly (raw text or page image): the Oracle fact sheet
PDF, the Crusoe 2024 Impact Report PDF, Epoch AI's CSV downloads and its Abilene calculations
spreadsheet, the Reclamation DEIS appendix and the Reclamation powerplant summary table. Every other
quote was extracted from the page by the fetch tool's summarizer model, so check the wording against
the page before putting it in quotation marks in the post. Pages that returned 403 and could not be
read at all: datacenterdynamics.com, texasobserver.org, costar.com, gem.wiki,
advisorperspectives.com, science.org.

Status of the site as of today, which matters for every "now" number below: the last **primary**
statement is Oracle's 10 Sep 2026 earnings call (6 of 8 buildings delivered, 618 MW). Epoch AI
**estimates** buildings 7 and 8 became operational around 1 Nov 2026 by extrapolating from satellite
imagery; no company has confirmed that. A KTXS report from Aug 2026 (seen only as a search snippet,
not fetched) says Crusoe told the city construction runs through Q1 2027.

---

### 1. Total cost / capital investment

There is no single official all-in number. Three different things get quoted:

| What                                                                                                      | Figure                                                     | Type                                  | Source                                               |
| --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------- | ---------------------------------------------------- |
| Facility (land, shells, power, cooling) financed by the Crusoe / Blue Owl / Primary Digital joint venture | **$15B** ($3.4B phase 1 + $11.6B phase 2)                  | PRIMARY ($15B, $3.4B); PRESS ($11.6B) | Crusoe 2025; Bisnow 2025                             |
| Nvidia chips bought by Oracle for the site                                                                | **~$40B** for ~400,000 GB200                               | PRESS (FT, unnamed sources)           | The Register 2025, relaying the Financial Times 2025 |
| All-in capital cost, hardware plus facility                                                               | **$31.2B** (2025 USD): $21.5B compute + $9.7B construction | ESTIMATE                              | Epoch AI 2026                                        |

- **$15B JV [PRIMARY].** Crusoe, "Crusoe, Blue Owl Capital and Primary Digital Infrastructure Enter
  $15 billion Joint Venture…", 21 May 2025.
  https://www.crusoe.ai/resources/newsroom/crusoe-blue-owl-capital-and-primary-digital-infrastructure-enter-joint-venture
  — quote: "a $15 billion joint-venture to fund the 1.2 gigawatt AI data center in Abilene, Texas."
- **$3.4B phase 1 [PRIMARY].** Crusoe press release, 15 Oct 2024.
  https://www.crusoe.ai/resources/newsroom/crusoe-blue-owl-capital-primary-digital-joint-venture
  (title: "$3.4 billion Joint Venture for AI Data Center Development"; seen in search results, page
  not fetched).
- **$11.6B phase 2 [PRESS].** Bisnow, 2025.
  https://www.bisnow.com/national/news/data-center/primary-digital-infrastructure-emerges-as-key-player-in-texas-stargate-data-center-campus-129519
  — quote (from search snippet): "announced it secured $11.6B in debt and equity to finance the
  second phase of the 1.2-gigawatt data center campus."
- **Debt [PRESS].** JPMorgan lent $2.3B (Bloomberg, 22 Jan 2025,
  https://www.bloomberg.com/news/articles/2025-01-22/jpmorgan-lends-2-3-billion-for-blue-owl-tied-oracle-data-center)
  and led a $7.1B loan (Bloomberg, 22 May 2025,
  https://www.bloomberg.com/news/articles/2025-05-22/jpmorgan-leads-7-1-billion-loan-for-blue-owl-tied-data-center).
  $2.3B + $7.1B = $9.4B [MY ARITHMETIC]; the FT/Reuters reporting in May 2025 gives "two loans
  totaling $9.6 billion" and says the owners put in about $5B of cash. Conflict is small and
  unresolved. Both Bloomberg pages are paywalled and were seen as headlines/snippets only.
- **$40B of chips [PRESS].** The Register, 27 May 2025.
  https://www.theregister.com/2025/05/27/oracle_openai_40b/ — quotes: Oracle "will reportedly shell
  out around $40 billion on Nvidia's most advanced GPUs"; "around 400,000 Nvidia GB200 superchips".
  Original is the Financial Times (2025), not fetched (paywall).
- **$31.2B [ESTIMATE].** Epoch AI, Frontier Data Centers hub, Abilene entry, updated 1 Nov 2026.
  https://epoch.ai/data/ai-data-centers/directory/openai-stargate-abilene — quote: "It hosts an
  estimated 1,019k H100-equivalents of AI compute, supported by 824 MW of IT power at a capital cost
  of $31.2 B." Split from Epoch's `data_center_timelines.csv`
  (https://epoch.ai/data/data_centers/data_center_timelines.csv), row dated 2026-11-01: total 31.21,
  compute 21.52, construction 9.70, annual operating cost 0.74 (2025 USD billions). This is a model,
  not accounting: Epoch applies about $38B per GW of IT power to every site. Methodology quote
  (https://epoch.ai/data/data-centers-documentation/methodology): the model "outputs a $38B capital
  cost per gigawatt of IT power".
- **Conflict.** Facility $15B + chips ~$40B = ~$55B [MY ARITHMETIC] against Epoch's $31.2B. The gap
  is almost all in the hardware line ($40B reported vs $21.5B modelled). The Register (2025) doubted
  the $40B figure on power grounds (see section 5).
- Crusoe's Abilene community page (https://www.crusoe.ai/about/communities/abilene, undated, read
  Nov 2026) shows a tile "$20B+ local investment to date". The page does not say the tile is
  Abilene-only, so don't attribute it to this campus.

### 2. Construction workforce and permanent jobs

Construction, oldest to newest:

| Date          | Figure                                                         | Type              | Source                   |
| ------------- | -------------------------------------------------------------- | ----------------- | ------------------------ |
| Mar 2025      | ~2,000 on site daily, expected to reach nearly 5,000           | PRIMARY           | Crusoe 2025              |
| Late Jul 2025 | 2,785 on site; peak expected nearly 5,000                      | PRESS             | ENR 2025                 |
| Sep 2025      | more than 6,400 on site every day                              | PRIMARY           | Oracle fact sheet 2025   |
| Jun 2026      | ~8,000 people, 20 million hours (cumulative, not a daily peak) | PRIMARY via PRESS | TIME 2026 quoting Oracle |

- Crusoe, 18 Mar 2025.
  https://www.crusoe.ai/resources/newsroom/crusoe-expands-ai-data-center-campus-in-abilene-to-1-2-gigawatts
  — quote: "The construction site has approximately 2,000 people working on the project daily" … "is
  expected to reach nearly 5,000 as a result of the expansion."
- ENR (Engineering News-Record), 4 Aug 2025.
  https://www.enr.com/articles/61133-project-team-pushes-limits-on-abilene-data-center-job — quotes:
  "2,785 total crew members on site"; "Peak workforce is expected to reach nearly 5,000".
- Oracle, "Oracle Fact Sheet: Stargate Data Centers", 23 Sep 2025, hosted by Rep. Jodey Arrington's
  office.
  https://arrington.house.gov/UploadedFiles/FINAL_Oracle_OAI_Data_Center_Fact_Sheet_092225b.pdf —
  quote: "There are more than 6,400 construction workers on site every day, contributing directly to
  the local economy." (The PDF footer reads "Confidential – Oracle Internal" but it is posted
  publicly on a .house.gov site.)
- TIME, 25 Jun 2026.
  https://tollbit.time.com/article/2026/06/24/ai-data-center-stargate-abilene-texas-injuries/ —
  quote: "some 8,000 people have worked 20 million hours at Stargate's first Abilene campus."
- Unverified, do not use without finding the original: "7,000 electricians, construction pros, and
  skilled tradespeople" at the topping-out of the last building (w.media, 2026,
  https://w.media/crusoe-tops-off-final-ai-data-center-in-abilene-texas/, seen only as a search
  snippet); "roughly 9,000 craft workers on site daily in August 2026" (buildermuse.com, an
  aggregator citing unnamed local reporting).
- **Best-supported peak: "more than 6,400" per day (Oracle, Sep 2025). Later, higher numbers exist
  but I could not confirm a daily peak above that from a primary source.**

Permanent jobs. Sources conflict by more than 10x, depending on what is counted:

- **57** = the contractual minimum in the 2021 Lancium tax-abatement deal [PRESS]. Bloomberg, 25 Jan
  2025, "Trump's AI Goals: Small 57 Jobs at Texas Data Center" (republished at
  https://www.advisorperspectives.com/articles/2025/01/25/trumps-ai-goals-small-57-jobs-texas-data-center,
  403 on fetch; search snippet says the 57 is "a minimum guarantee" and that the Development
  Corporation of Abilene expected ~100 jobs from the first phase).
- **"hundreds"** [PRIMARY]. Development Corporation of Abilene, 18 Mar 2025.
  https://developabilene.com/2025/03/18/the-development-corporation-of-abilene-city-of-abilene-and-taylor-county-announce-expansion-on-the-lancium-clean-campus-with-project-radiance/
  — quote: "hundreds of new technology jobs in the Abilene community."
- **"nearly 1,700 jobs onsite"** [PRIMARY], but this covers the campus plus the then-planned 600 MW
  expansion that OpenAI later dropped. Oracle fact sheet 2025 (URL above) — quote: "Ongoing, the
  campus and nearby expansion will provide nearly 1,700 jobs onsite, and thousands more indirect
  jobs."
- A search result attributed "400 permanent, full-time, skilled jobs" to Crusoe's Abilene page; when
  fetched (Nov 2026) the page only says "dozens of permanent, full-time positions during operations"
  for a typical project. Not confirmed.

### 3. Site size

- **Land: 1,100 acres** [PRIMARY]. Oracle fact sheet, 23 Sep 2025 (URL above) — quote: "The campus
  features eight buildings on 1,100 acres, with up to approximately 4 million square feet."
  - Conflicts: "875 acres" in the FT/AP reporting of 2025 (per search snippets, from city
    documents); "1,000-acre campus" in Tom's Hardware, 10 Mar 2026
    (https://www.tomshardware.com/tech-industry/oracle-and-openai-scrap-planned-600mw-abilene-expansion).
    Lancium leased roughly 90 acres to Crusoe for phase 1 (search snippet, 2024). The 1,100 figure
    is the full Lancium Clean Campus; the buildings occupy a small part of it.
- **Buildings: 8** [PRIMARY], same quote. Each is a single-storey building with four data halls. ENR
  2025: "474,000-sq-ft single-story building"; "four 106,000-sq-ft data halls".
- **Indoor floor area: ~4 million sq ft** [PRIMARY]. Crusoe 2024 Impact Report (2025), p. 19.
  https://cdn.prod.website-files.com/6855c1aa175582ee23e0aa19/68710273a71bb7c11049ba28_Crusoe_Impact_Report_2024.pdf
  — quote: "Upon completion in 2026, the campus will house eight buildings covering 4 million square
  feet."
  - 4,000,000 sq ft / 43,560 = **91.8 acres** [MY ARITHMETIC].
  - Cross-checks: Epoch's sheet uses 484,960 sq ft per building, 3,879,680 total = 89.1 acres
    [ESTIMATE + MY ARITHMETIC]. ENR's 474,000 × 8 = 3,792,000 sq ft = 87.1 acres. Phase 1 alone:
    "two buildings at 980,000 square feet" (Crusoe 2025) = 22.5 acres.
  - So the buildings cover roughly 8% of the 1,100 acres [MY ARITHMETIC].

### 4. Power

Capacity:

| Quantity                               | Figure                                                | Type          | Source                    |
| -------------------------------------- | ----------------------------------------------------- | ------------- | ------------------------- |
| Full buildout, total facility          | **1.2 GW**                                            | PRIMARY       | Crusoe 2025               |
| Delivered to OpenAI as of 10 Sep 2026  | **618 MW**, 6 of 8 buildings, "75% of total capacity" | PRIMARY       | Oracle Q1 FY27 call, 2026 |
| Implied total on Oracle's basis        | 618 / 0.75 = **824 MW**                               | MY ARITHMETIC | —                         |
| Now (est. all 8 buildings, 1 Nov 2026) | **824 MW IT, 1,154 MW total facility**                | ESTIMATE      | Epoch AI 2026             |
| Per building                           | 103 MW IT, 144 MW facility (peak PUE 1.4)             | ESTIMATE      | Epoch AI 2026             |

- Crusoe 2024 Impact Report (2025), p. 19 (URL above) — quote: "The data center campus will support
  AI workloads with 1.2 GW of power capacity with more than 200 MWs slated to be energized in 2025."
- Oracle Q1 FY2027 earnings call, 10 Sep 2026, CEO Clay Magouyrk. Transcript:
  https://www.fool.com/earnings/call-transcripts/2026/09/11/oracle-orcl-q1-2027-earnings-call-transcript/
  — quote: "6 of the 8 campus buildings, representing 618 megawatts and 75% of total capacity have
  now been delivered to the customer."
- Epoch AI calculations sheet for Abilene (2026).
  https://docs.google.com/spreadsheets/d/1M5VPpNDGTPgssU1x3xQJKv33EIa7-wgpDIFM8uzpodQ/ — row
  2026-11-01: 8 buildings, IT power 824 MW, power 1,154 MW; note: "Buildings 7-8 are estimated to be
  operational… Oracle gave no date for the last two buildings on its September 10 call."
- The 1.2 GW and the 824 MW are the same campus on different bases: 824 MW is power to the IT
  equipment, 1.2 GW is the grid connection including cooling and losses. For a power-draw bar chart,
  1.2 GW is the nameplate maximum, ~1.15 GW is Epoch's estimate of peak facility draw, and actual
  average draw is lower and unpublished.

Power sources:

- **Grid (ERCOT), the primary supply** [PRIMARY]. Oracle fact sheet 2025 — quote: "The Abilene data
  center connects directly to the ERCOT grid, allowing it to primarily draw from the region's robust
  and growing supply of renewable energy." Crusoe 2025 (expansion release): "In addition to the 1.2
  GW grid interconnection".
  - Two substations: Mortenson project page (2026),
    https://www.mortenson.com/projects/abilene-data-center-development — quotes: "The initial phase
    included construction of the Abilene 200 MW, 138 kV substation."; "Expansion included a
    12.5-acre, 1 GW, 345 kV greenfield substation."; "fully energized by March 10, 2026."
  - Utility: Epoch's dataset lists "American Electric Power" (AEP Texas) [ESTIMATE/secondary]. Not
    Oncor.
- **On-site gas turbines: 360.5 MW, 10 units** [regulatory filing via ESTIMATE source]. Epoch
  calculations sheet (2026) — quote: "Title V permit application specifies 10 natural gas turbine
  generators, with a total of 5 * 38 MW + 5 * 34.1 MW = 360.5 MW between them." ENR 2025 gives
  "340-MW natural gas turbine power plant". Epoch's satellite notes: five turbines in place Sep
  2025, plant "looks complete" 24 Mar 2026.
  - Backup or primary? [PRIMARY] Oracle fact sheet 2025: "Advanced natural gas turbines from GE
    Vernova will deliver uninterrupted reliability and support grid stability. Ultimately, this
    plant will be used for backup power, rather than traditional, higher-emission diesel
    generators." [PRESS] Floodlight / Texas Tribune, 9 Jul 2026 (Evan Simon),
    https://www.texastribune.org/text/235529/ — Crusoe said the turbines "will only be used for back
    up power", but the article says the permits allow continuous use, and counts 10 turbines and 62
    diesel generators built with 41 more turbines and 18 more generators proposed (the proposed ones
    are for the expansion, which is now Microsoft's, not this campus).
- **Wind: none on site.** [PRIMARY] Crusoe 2025: "The campus will also leverage abundant proximate
  wind resources." Crusoe Impact Report: location "strategically chosen for its proximity to
  existing wind energy and its potential for the development of additional onsite solar capacity."
  That is grid wind in the region, not a dedicated wind farm.
- **Batteries and solar: announced, size not found.** [PRIMARY] Crusoe 2025: Lancium's plan
  "includes large-scale behind-the-meter battery storage and solar resources." Searched for MW/MWh
  figures (Lancium, Crusoe, Cleanview, DCD); found none. Cleanview's site profile is paywalled.
  Epoch's satellite notes mention no battery or solar field.
- Cooling, for completeness: closed-loop liquid cooling with air-cooled chillers; Epoch counts 80
  chillers per building, 640 total.

### 5. Chips and compute

Chip type:

- **Nvidia GB200 NVL72 (Blackwell)** [PRIMARY]. OpenAI, "Building the compute infrastructure for the
  Intelligence Age", 29 Apr 2026.
  https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age/ — quote:
  "The site operates on Oracle Cloud Infrastructure and runs NVIDIA GB200 systems." (Same post says
  GPT-5.5 was trained there.)
- **Buildings 3–8 probably GB300 (Blackwell Ultra)** [ESTIMATE]. Epoch calculations sheet (2026),
  chip quantities tab: "Building design is the same but the chillers are slightly larger, suggesting
  the same number of servers but slightly more power per server. This is consistent with B300, as is
  the timing with B300 chip sales ramping up." No company has confirmed GB300 at Abilene.

Chip count:

| Quantity                                          | Figure                                                            | Type                                 | Source                        |
| ------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------ | ----------------------------- |
| Design capacity                                   | up to 50,000 GB200 per building, so up to 400,000                 | PRIMARY                              | Crusoe 2025; Bloomberg 2025   |
| Reported purchase                                 | ~400,000 GB200 for ~$40B                                          | PRESS                                | FT 2025 via The Register 2025 |
| Delivered Jun–Aug 2026                            | 131,000 GPUs, 1.9x the prior quarter (so ~69,000 in Mar–May 2026) | PRIMARY; second figure MY ARITHMETIC | Oracle call 2026              |
| Installed, 6 buildings (confirmed delivered)      | 302,400 = 100,800 GB200 + 201,600 GB300                           | ESTIMATE                             | Epoch AI 2026                 |
| Installed now, 8 buildings (est.) = full buildout | **403,200** = 100,800 GB200 + 302,400 GB300                       | ESTIMATE                             | Epoch AI 2026                 |

- Crusoe 2024 Impact Report (2025), p. 19 — quote: "Each building has been designed to operate up to
  50,000 NVIDIA GB200 NVL72s". (Crusoe writes "NVL72s" but means GPUs; 50,000 racks of 72 would be
  3.6M GPUs.)
- Bloomberg, 18 Mar 2025, "OpenAI's First Stargate Site to Hold Up to 400,000 Nvidia Chips".
  https://www.bloomberg.com/news/articles/2025-03-18/openai-s-first-stargate-site-to-hold-up-to-400-000-nvidia-chips
  — quote: "as many as 400,000".
- Oracle Q1 FY27 call, 10 Sep 2026 (transcript URL above) — quote: "We delivered 131 thousand GPUs
  there in Q1, 1.9x the volume delivered in Q4."
- Epoch uses 50,400 per building (700 NVL72 racks × 72), which is why its total is 403,200, not
  400,000. Epoch changelog, 1 Nov 2026 (https://epoch.ai/data/data-centers-documentation/changelog):
  "B300 chips increased from 201.6k to 302.4k."
- Doubt worth knowing about: The Register (27 May 2025) estimated 400,000 GB200s would need 1.45 GW
  at a PUE of 1.1, more than the campus has. Epoch's own GPU-count-based check gives 105 MW IT and
  147 MW facility per building, consistent with 1.2 GW for eight.

Per-chip peak performance:

- Nvidia GB200 NVL72 spec page (read Nov 2026).
  https://www.nvidia.com/en-us/data-center/gb200-nvl72/ — "FP8/FP6 training (Tensor Core): 720
  PFLOPS", "FP16/BF16 Tensor Core: 360 PFLOPS", "72 Blackwell GPUs", footnote: "Specification in
  sparse. Dense is one-half sparse spec shown." [PRIMARY]
- Per GPU [MY ARITHMETIC from Nvidia's numbers]: FP8 = 720 PFLOPS / 72 = 10 PFLOPS with sparsity,
  **5 × 10^15 FLOP/s dense**. FP16 = 360 / 72 = 5 PFLOPS sparse, **2.5 × 10^15 FLOP/s dense**.
- Epoch uses the same values for both chip types: `ai_chip_sales_chip_types.csv`
  (https://epoch.ai/data/ai_chip_sales_chip_types.csv) lists B200 and B300 each at 8-bit 5e15,
  16-bit 2.5e15. H100 reference: 1.979e15 (8-bit dense), 9.895e14 (16-bit).

Total compute:

- **FP8, dense (the figure I used): 403,200 × 5 × 10^15 = 2.016 × 10^21 FLOP/s ≈ 2.0 zettaFLOP/s**
  [MY ARITHMETIC, identical to Epoch].
- **Epoch AI's published estimate [ESTIMATE]: 2.02 × 10^21 8-bit OP/s = 1,019k H100-equivalents**
  (2.016e21 / 1.979e15 = 1,018,696). Epoch's CSV row 2026-11-01: `Performance (8-bit OP/s)` =
  2.016e+21. (One cell in Epoch's sheet labels this "FP16 precision, dividing by 2"; the value and
  the parameter table are FP8 dense, so the label is a slip.)
- FP16 dense: 403,200 × 2.5 × 10^15 = 1.008 × 10^21 FLOP/s.
- Using the round primary figure instead: 400,000 × 5 × 10^15 = 2.0 × 10^21.
- Confirmed-delivered basis (6 buildings, Sep 2026): 302,400 × 5 × 10^15 = 1.512 × 10^21 (Epoch:
  764k H100e).
- Nvidia's headline "with sparsity" numbers would double all of these (4.0 × 10^21 at FP8). Epoch
  halves them because dense is what applies to most workloads.
- These are theoretical peak rates of the GPUs, not measured throughput.
- SemiAnalysis: no public Abilene compute or MW estimate found (searched "SemiAnalysis Abilene
  Stargate critical IT MW"; their Abilene coverage is qualitative and the datacenter model is paid).
- Rank: in Epoch's hub the site is the second-largest operating AI data center in the world today by
  H100e, behind Colossus 2 at 1,112k H100e (`data_centers.csv`,
  https://epoch.ai/data/data_centers/data_centers.csv) [ESTIMATE].

### 6. Share of OpenAI's total compute, late 2026

**Not found as a published figure.** OpenAI has not disclosed a 2026 operational total (searched
OpenAI posts, Friar/Altman/Brockman/Katti statements, DCD, Bloomberg headlines). The April 2026 "10
GW" is contracted capacity, not running. What exists:

- OpenAI's last disclosed total [PRIMARY]: Sarah Friar, "A business that scales with the value of
  intelligence", 18 Jan 2026.
  https://openai.com/index/a-business-that-scales-with-the-value-of-intelligence/ — quote: "Compute
  grew 3X year over year or 9.5X from 2023 to 2025: 0.2 GW in 2023, 0.6 GW in 2024, and ~1.9 GW in
  2025."
- Epoch's conversion [ESTIMATE]: end-2025 OpenAI = 1.74M H100e (90% interval 1.25M–2.19M),
  `ai_chip_users_year_end_by_lab.csv` (https://epoch.ai/data/ai_chip_users_year_end_by_lab.csv,
  generated 9 Sep 2026).
- Forecast for end-2026 [ESTIMATE, relayed]: Epoch AI, "Frontier labs don't use most AI compute
  (yet)", 20 May 2026. https://epoch.ai/gradient-updates/frontier-labs-dont-use-most-ai-compute —
  quotes: "Anthropic and OpenAI will each have 5–6 GW of capacity by the end of this year"; "this
  suggests another year of ~4× growth in H100e compute capacity".

Ways to get a share, all [MY ARITHMETIC]:

| Method                                                                                                                                         | Abilene           | OpenAI total        | Share         |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ------------------- | ------------- |
| GW, against the end-2026 forecast                                                                                                              | 1.2 GW facility   | 5–6 GW              | **20–24%**    |
| H100e, end-2025 total × 4 growth                                                                                                               | 1.02M             | ~7.0M               | **~15%**      |
| Epoch hub, sites tagged OpenAI "confident" or "likely" (Abilene, Fairwater Atlanta, Fairwater Wisconsin, CoreWeave Denton, Microsoft Goodyear) | 1.02M / 824 MW IT | 2.69M / 2,293 MW IT | **38% / 36%** |
| Epoch hub, all sites tagged OpenAI incl. "speculative"                                                                                         | 1.02M             | 3.35M               | **30%**       |
| Against the stale end-2025 total                                                                                                               | 1.2 GW; 1.02M     | 1.9 GW; 1.74M       | 63%; 58%      |

The hub rows overstate the share because the hub only tracks large sites and misses OpenAI's smaller
Azure capacity; they understate it because the Fairwater sites are shared with Microsoft. Defensible
wording: "somewhere between a sixth and a third of OpenAI's compute", with no published figure.

### 7. Ownership and commercial arrangement

Chain, top to bottom:

1. **Lancium** owns the land (Lancium Clean Campus), holds the grid interconnect and provides power
   services. [PRIMARY] Crusoe 2025 expansion release names Lancium as providing the campus site,
   grid interconnect and power services.
2. **Crusoe** develops, builds and operates the data centers. The buildings are owned by a joint
   venture of **Crusoe, Blue Owl Capital (Real Assets funds) and Primary Digital Infrastructure**,
   $15B in total. [PRIMARY] Crusoe, 21 May 2025 — they "will jointly sponsor the construction of six
   new buildings." Equity split not disclosed. Debt mostly from JPMorgan (section 1).
3. **Oracle** leases the whole campus and owns the chips. [PRESS] The Register, 27 May 2025,
   relaying the FT: Oracle is "set to lease the site for 15 years." Epoch lists chip owner "Oracle
   #confident". Lease price not found.
4. **OpenAI** is the sole user, renting the compute from Oracle Cloud Infrastructure under the
   Stargate banner. [PRIMARY] OpenAI 2026: "our flagship Stargate site". Contract value for Abilene
   alone not found. OpenAI owns none of the site.

Expansion that changed hands:

- Oracle and OpenAI had planned a further 600 MW next door (Oracle fact sheet, Sep 2025: "a
  potential additional expansion of 600 megawatts near the flagship Stargate site"). They dropped it
  in March 2026. [PRESS] Tom's Hardware, 10 Mar 2026, relaying Bloomberg
  (https://www.tomshardware.com/tech-industry/oracle-and-openai-scrap-planned-600mw-abilene-expansion):
  OpenAI's Sachin Katti said the company "considered expanding it further". Bloomberg also reported
  Nvidia paid Crusoe a $150M deposit and approached Meta.
- **Microsoft** took it instead. [PRESS] The Register, 27 Mar 2026,
  https://www.theregister.com/2026/03/27/microsoft_ai_crusoe/ — quotes: Crusoe will "add 900
  megawatts of capacity to its Abilene Texas datacenter campus"; "an on-site power plant capable of
  delivering 900 MW of behind-the-meter energy"; campus total goes "to 2.1 gigawatts". Not
  operational before mid-2027. This is a separate campus and is excluded from every number above.

### 8. When did total world compute equal this site?

No published statement of this found. Data to work it out:

**(a) World AI-chip compute, Epoch AI chip sales dataset (2026)** [ESTIMATE + MY ARITHMETIC].
`ai_chip_sales_timelines_by_chip.csv` (https://epoch.ai/data/ai_chip_sales_timelines_by_chip.csv,
generated 18 Nov 2026), summing median H100e over Nvidia, Google, AMD, Amazon, Huawei and Cambricon,
cumulative from Q1 2022:

| Quarter end    | Cumulative H100e | × 1.979e15 = 8-bit OP/s |
| -------------- | ---------------- | ----------------------- |
| 2022-12-31     | 0.30M            | 6.0e20                  |
| 2023-06-30     | 0.67M            | 1.3e21                  |
| **2023-09-30** | **1.06M**        | **2.1e21**              |
| 2023-12-31     | 1.59M            | 3.2e21                  |
| 2024-12-31     | 6.69M            | 1.3e22                  |
| 2025-12-31     | 20.3M            | 4.0e22                  |
| 2026-09-30     | 37.6M            | 7.4e22                  |

- **Abilene (1.02M H100e) equals every AI accelerator sold in the world through about
  September 2023.** Linear interpolation inside Q3 2023 puts the crossing in the second half of
  September 2023.
- Caveats: the series starts in 2022, so pre-2022 chips (older A100s, V100s, early TPUs) are
  missing, which moves the true crossing a little earlier, probably mid-2023. It counts chips sold,
  not chips running. Q4 2026 is incomplete.
- Today the site is 1.02M / 37.6M = 2.7% of cumulative AI compute sold through Q3 2026, and 5.0% of
  the end-2025 stock.
- Cross-check, Epoch gradient update, 20 May 2026: "roughly 20 million H100e as of the end of 2025."

**(b) All computing hardware, not just AI chips.** AI Impacts, "Global computing capacity" (c. 2016;
the page says it is out of date). https://aiimpacts.org/global-computing-capacity/ — quote:
"Computing capacity worldwide was probably around 2 x 10^20 – 1.5 x 10^21 FLOPS, at around the end
of 2015."

- Abilene at 2.0 × 10^21 (FP8) is above the top of that range; at FP16 (1.0 × 10^21) it is inside
  it. So: **one campus now has roughly the raw arithmetic rate of all the world's computers at the
  end of 2015**, give or take a factor of a few. Precision differs (2015 hardware was mostly 32- and
  64-bit), so this is loose.
- Older anchor: Hilbert & López, "The World's Technological Capacity to Store, Communicate, and
  Compute Information", Science (2011): 6.4 × 10^18 instructions per second on general-purpose
  computers in 2007. The Science page returned 403, so this number is from memory and unverified; AI
  Impacts relays the paper's all-hardware total as "196 exa-IPS in 2007".

**(c) Supercomputers.** TOP500, November 2026 list (announced 16 Nov 2026): #1 LineShine "achieved
2.198 Exaflop/s on the HPL benchmark" (https://top500.org/) [PRIMARY]; all 500 systems sum to 19.57
exaflop/s per xenospectrum.com, 17 Nov 2026
(https://xenospectrum.com/en/top500-november-2026-supercomputers/) [PRESS; not confirmed on
top500.org]. 2.016e21 / 1.957e19 ≈ 100x [MY ARITHMETIC], but this compares theoretical FP8 peak
against measured FP64 Linpack and is not like for like.

---

### 9. US homes: average electric power

- **2025 residential retail sales: 1,519,151 GWh = 1,519 TWh** [PRIMARY]. EIA, Electric Power
  Monthly, Table 5.1 "Sales of Electricity to Ultimate Customers: Total by End-Use Sector, 2016 -
  August 2026", released 23 Oct 2026.
  https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_1 — row 2025: Residential
  1,519,151; Commercial 1,503,310; Industrial 1,050,134; Transportation 7,314; Total 4,079,909
  (thousand MWh). 2025 values are marked final.
- **Average power: 1,519,151 GWh / 8,760 h = 173.4 GW** [MY ARITHMETIC].
- Prior years from the same table: 2024 = 1,482,874 (168.8 GW over 8,784 h); 2023 = 1,450,025; 2022
  = 1,509,233.
- Cross-check: EIA "Use of electricity" explainer (2026),
  https://www.eia.gov/energyexplained/electricity/use-of-electricity.php, gives residential "1.51
  trillion kWh", 37.3% of retail sales, for 2025. Slightly lower than Table 5.1 (rounding or an
  earlier vintage). EIA Today in Energy, 5 Mar 2026
  (https://www.eia.gov/todayinenergy/detail.php?id=67284) reported residential sales up 2.2% in 2025
  on preliminary data; the final table implies +2.4%.
- Retail sales exclude rooftop solar consumed on site, so true household consumption is a few
  percent higher.
- Abilene at 1.2 GW is 0.69% of the average draw of all US homes [MY ARITHMETIC].

### 10. Hoover Dam

- **Nameplate: 2,080 MW** [PRIMARY]. Bureau of Reclamation, Hoover Dam power FAQ (page last updated
  2018). https://www.usbr.gov/lc/hooverdam/faqs/powerfaq.html — quote: "a nameplate capacity of
  about 2,080 megawatts".
  - Exact: 2,078,800 kW across 19 units (17 main + 2 station-service). Reclamation, "Hydropower
    facilities owned, directly operated and maintained by the Bureau of Reclamation", revised 7
    Nov 2025.
    https://www.usbr.gov/power/facil/Reclamation_Hydroelectric_Powerplants_Summary_Table_11_25.pdf
  - Reclamation's Jan 2026 draft EIS gives "seventeen commercial generators with a maximum combined
    capacity of 2,074 MW"
    (https://www.usbr.gov/ColoradoRiverBasin/post2026/draft-eis/docs/vol-3/P26-DEIS-TA-15.pdf, p.
    15-11). Same thing counted without the station-service units.
  - Usable capacity today is far below nameplate because Lake Mead is low: the same appendix's
    Figure TA 15-6 shows roughly 1,300–1,470 MW at elevations of 1,040–1,080 ft (Lake Mead was at
    1,038 ft at end of Sep 2026 per EIA Today in Energy, 13 Nov 2026,
    https://www.eia.gov/todayinenergy/detail.php?id=68445).

Annual generation:

| Period                      | TWh/yr | Average GW | Type                 | Source                         |
| --------------------------- | ------ | ---------- | -------------------- | ------------------------------ |
| 1947–2008 average           | ~4.2   | 0.48       | PRIMARY              | Reclamation FAQ                |
| FY2016–FY2025 10-yr average | 3.258  | 0.372      | PRIMARY              | Reclamation summary table 2025 |
| 2021                        | 3.51   | 0.401      | PRIMARY data, MY SUM | Reclamation RISE               |
| 2022                        | 3.14   | 0.358      | same                 | same                           |
| 2023                        | 2.71   | 0.309      | same                 | same                           |
| 2024                        | 2.94   | 0.335      | same                 | same                           |
| 2025                        | 2.74   | 0.312      | same                 | same                           |
| 2021–2025 mean              | 3.01   | 0.343      | MY ARITHMETIC        | —                              |
| Record high, 1984           | 10.348 | 1.18       | PRIMARY              | Reclamation FAQ                |
| Record low since 1940, 1956 | 2.648  | 0.30       | PRIMARY              | Reclamation FAQ                |

- Long-run [PRIMARY]: Reclamation FAQ — average annual net generation for 1947 through 2008 "about
  4.2 billion kilowatt-hours". Reclamation's general fact sheets round to "about 4 billion kWh".
- 10-year [PRIMARY]: Reclamation summary table, Hoover row: installed capacity 2,078,800.00 kW, net
  generation 3,258,168,817.50 kWh; footnote: "NET GENERATION (kWh) SHOWN AS A 10-YEAR ROLLING
  AVERAGE (FY2016 - FY2025)".
- Recent calendar years: summed from Reclamation's RISE monthly series "Hoover Power Plant Monthly
  Plant Net Generation-kwH" (item 5347), https://data.usbr.gov/rise/api/result?itemId=5347 (catalog:
  https://data.usbr.gov/catalog/4235/item/5347). The monthly values were transcribed from the JSON
  by the fetch tool, so re-pull before publishing exact digits. They agree with the Reclamation DEIS
  chart (Figure TA 15-7, p. 15-13), which shows about 2.7 in 2023 and about 2.95 in 2024. Jan–Oct
  2026 so far: 2.41 TWh; trailing 12 months (Nov 2025–Oct 2026): 2.66 TWh.
- Conversions [MY ARITHMETIC]: TWh × 1,000 / 8,766 h = average GW. 4.2 TWh → 0.479 GW. 3.258 TWh →
  0.372 GW. 2.74 TWh → 0.312 GW.
- Capacity factor: 3.258 TWh / (2.0788 GW × 8,766 h) = 18% on the 10-year average; 15% in 2025.
- Abilene's 1.2 GW capacity is 2.5x Hoover's long-run average output, 3.2x its 10-year average and
  3.8x its 2025 output [MY ARITHMETIC]. Abilene's number is a maximum and Hoover's are averages, so
  if the chart mixes them, label it.

---

### Not found

- Official all-in cost for the campus (only the $15B facility JV and press-reported $40B chip
  order).
- A primary-source daily construction peak above 6,400.
- An Abilene-only permanent job count from Crusoe or Oracle.
- Size (MW/MWh) of the on-site battery and solar that Crusoe/Lancium announced, or confirmation they
  were built.
- Company confirmation that buildings 7–8 are live, or that buildings 3–8 run GB300 not GB200.
- OpenAI's total operational compute in late 2026, hence no sourced share.
- Lease price, and the Oracle–OpenAI contract value for Abilene alone.
- Any SemiAnalysis public estimate for the site.
- Any published "world compute equalled Abilene in year X" statement.

---

# Part: What Else Is in a Datacenter

## What else is in a gigawatt AI datacenter (research notes, 2026-11-22)

Sites: AWS Project Rainier, New Carlisle, Indiana (Anthropic, Trainium) and Stargate, Abilene, Texas
(Crusoe / Oracle / OpenAI, Nvidia).

Labels used below:

- **SITE** = figure is specific to New Carlisle or Abilene.
- **OTHER SITE** = figure is from a comparable campus (named).
- **INDUSTRY** = generic or modelled figure.
- **REPORTED** = stated by the company, a filing, or a journalist who saw it. **ESTIMATE** =
  third-party model or inference. **DERIVED** = my arithmetic on sourced numbers.
- **SNIPPET ONLY** = I saw the figure in a search-result excerpt but could not open the page myself.
  Treat as unverified.

Quotes are verbatim from the page as fetched. Pages I could not open (403 or timeout) are listed at
the end.

---

### 1. Networking

#### Miles of fiber

| Site                                                 | Figure                                                                                                                                                                                                                                 | Label                                                                | Source                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Abilene                                              | "laid down enough fiber optic cable to wrap the Earth 16 times." Stated at the September 2025 press tour, when 2 of 8 buildings were finished. 16 x 24,901 mi = about 400,000 miles (DERIVED).                                         | SITE, REPORTED (journalist narration, not an Oracle/OpenAI document) | Fortune, 2025: https://fortune.com/2025/09/23/openai-oracle-and-softbank-expand-stargate-with-five-new-ai-data-centers-staging-texas-media-spectacle-to-counter-critics/ . Same figure in Sharon Goldman's Ground Level AI, 2025: https://www.groundlevel-ai.com/p/on-the-ground-in-texas-for-sam-altmans                                                                                                                  |
| New Carlisle                                         | "hundreds of thousands of miles of fibre connecting every chip and computer together"                                                                                                                                                  | SITE, REPORTED (loose, no exact count)                               | New York Times (Karen Weise, Cade Metz), 2025, read via The Nightly syndication: https://thenightly.com.au/business/the-new-york-times-at-amazons-biggest-data-centre-everything-is-supersized-for-ai-c-19309860                                                                                                                                                                                                           |
| New Carlisle                                         | fiber-optic trunk line that "crams hundreds of fiber pairs"                                                                                                                                                                            | SITE, REPORTED                                                       | The Register, 2025: https://www.theregister.com/2025/07/04/project_rainier_deep_dive/                                                                                                                                                                                                                                                                                                                                      |
| Microsoft Fairwater, Wisconsin                       | "enough fiber to circle the Earth 4.5 times" (about 112,000 miles, DERIVED). Appears in the Tom's Hardware headline and in Satya Nadella's social post as quoted by TweakTown. It is NOT in Microsoft's own blog post text as fetched. | OTHER SITE, REPORTED                                                 | Tom's Hardware, 2025: https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-announces-worlds-most-powerful-ai-data-center-315-acre-site-to-house-hundreds-of-thousands-of-nvidia-gpus-and-enough-fiber-to-circle-the-earth-4-5-times ; TweakTown, 2025: https://www.tweaktown.com/news/107787/microsoft-announces-worlds-biggest-ai-datacenter-with-hundreds-of-thousands-of-nvidia-gpus/index.html |
| Microsoft (wide-area, between sites, not inside one) | "The company has deployed 120,000 miles of dedicated fiber for the network"                                                                                                                                                            | OTHER SITE, REPORTED                                                 | Microsoft Source, 2025: https://news.microsoft.com/source/features/ai/from-wisconsin-to-atlanta-microsoft-connects-datacenters-to-build-its-first-ai-superfactory/                                                                                                                                                                                                                                                         |

Crusoe itself: no "miles of fiber" figure found in Crusoe's own pages (checked the "inside look"
blog, the Abilene community page and the 1.2 GW press release). The 16x figure comes from the
OpenAI/Oracle press day.

AWS itself: no AWS-published fiber mileage for New Carlisle found. AWS's Project Rainier page gives
none.

#### Copper inside the racks (often forgotten)

- Each Nvidia GB200 NVL72 rack has "more than 2 miles (3.2 km) of copper cabling". Copper was used
  inside the rack because optics "would have added another 20kW". INDUSTRY, REPORTED. The Register,
  2024: https://www.theregister.com/2024/03/21/nvidia_dgx_gb200_nvk72
- Nvidia: "over 5,000 copper cables in a single rack" (SNIPPET ONLY, Nvidia developer blog on the
  OCP contribution:
  https://developer.nvidia.com/blog/nvidia-contributes-nvidia-gb200-nvl72-designs-to-open-compute-project).
- DERIVED: Abilene's reported order of about 400,000 GB200s is about 5,500 NVL72 racks, so about
  11,000 miles of copper inside racks, before any fiber.

#### What interconnect

- **Abilene: Ethernet (RoCE), Oracle's own design.** OCI Zettascale10 is "the fabric underpinning
  the flagship supercluster built in collaboration with OpenAI in Abilene, Texas, as part of
  Stargate." Built on "Oracle Acceleron RoCE networking architecture", using "Linear Pluggable
  Optics (LPO) and Linear Receiver Optics (LRO)" at "400G/800G throughput"; initial clusters "will
  target deployments of up to 800,000 NVIDIA GPUs"; sites "within a two-kilometer radius". SITE,
  REPORTED. Oracle press release, 2025, read via HPCwire:
  https://www.hpcwire.com/off-the-wire/oracle-unveils-next-gen-oracle-cloud-infrastructure-zettascale10-cluster-for-ai/
  - Inside each rack: Nvidia NVLink over copper (72 GPUs per NVLink domain).
  - Crusoe: each building is designed to run "up to 50,000 NVIDIA GB200 NVL72s" on "a single
    integrated network fabric". Crusoe, 2025:
    https://www.crusoe.ai/newsroom/crusoe-expands-ai-data-center-campus-in-abilene-to-1-2-gigawatts
- **New Carlisle: AWS's own.** Inside a server, chips are "connected in a 4x4 2D torus using AWS
  high-speed NeuronLink v3 interconnect" with no switches; four servers make a 64-chip UltraServer.
  Between UltraServers: AWS's Elastic Fabric Adapter (EFAv3), "each accelerator in the cluster will
  be equipped with 200Gbps of network bandwidth", fabric delivers "tens of petabits of bandwidth"
  with "under 10 microseconds of latency across the network." "This isn't your typical Ethernet
  network, either." SITE, REPORTED. The Register, 2025:
  https://www.theregister.com/2025/07/04/project_rainier_deep_dive/
  - Amazon's own page: NeuronLink is the "distinctive blue cables", EFA the "yellow cables". Amazon,
    2025: https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster
- **Microsoft Fairwater:** "Azure uses both InfiniBand and Ethernet fabrics that deliver 800 Gbps"
  (Microsoft, Sept 2025:
  https://blogs.microsoft.com/blog/2025/09/18/inside-the-worlds-most-powerful-ai-datacenter/);
  Atlanta site is a "two-tier, ethernet-based backend network" running Microsoft's SONiC (Microsoft,
  Nov 2025:
  https://blogs.microsoft.com/blog/2025/11/12/infinite-scale-the-architecture-behind-the-azure-ai-superfactory/).
  OTHER SITE, REPORTED.

#### Switch and transceiver counts

- Site-specific switch or transceiver counts for Abilene or New Carlisle: **not found** (searched
  Oracle Zettascale10 material, Crusoe pages, AWS Rainier page, The Register deep dive, Glenn
  Lockwood's notes).
- INDUSTRY rule of thumb from Jensen Huang, GTC 2025: each GPU needs six transceivers; "Because if
  we have a million GPUs [we need] 6 million transceivers [consuming] 180 megawatts", about $1,000
  per transceiver, so about $6,000 and 180 W of optics per GPU. Optics.org, 2025:
  https://www.optics.org/news/nvidia-reveals-plan-to-scale-ai-factories-with-co-packaged-optics (the
  per-transceiver price is from Fierce Network's write-up of the same keynote; both SNIPPET ONLY for
  exact wording, I did not open the pages).
- DERIVED: applied to Abilene's about 400,000 GPUs, that is about 2.4 million transceivers and about
  70 MW of optics. Oracle's LPO design is meant to cut that.

---

### 2. Cooling

#### How the heat is removed

**Abilene: direct-to-chip liquid, closed loop, heat rejected to air by chillers. No evaporation.**

- "closed-loop, non-evaporative liquid cooling systems"; "Water in the systems is continuously
  recirculated, with heat rejected via air-cooled chillers". SITE, REPORTED. Crusoe, 2025:
  https://www.crusoe.ai/resources/blog/an-inside-look-at-the-abilene-ai-data-center
- Chillers: 640 units of Airedale "OptiChill Free Cool", 1,125.4 MW of cooling capacity, for 824 MW
  of IT load across 8 buildings. SITE, ESTIMATE (Epoch AI, from the air permit, blueprints and
  satellite imagery). Epoch AI, 2026:
  https://epoch.ai/data/ai-data-centers/directory/openai-stargate-abilene
- Water: "The initial fill for the closed-loop system in each of the eight buildings requires one
  million gallons of water", then "approximately 50,000 gallons per building per year." So 8 million
  gallons once, then 400,000 gallons a year campus-wide (DERIVED). SITE, REPORTED (Crusoe).
- A reverse-osmosis flushing system is projected to cut pipe-flushing water by 75%. ENR, 2025:
  https://www.enr.com/articles/61133-project-team-pushes-limits-on-abilene-data-center-job

**New Carlisle: air cooled, with evaporative assist on hot days.**

- AWS "pumps air from outside the buildings through handlers the size of cargo containers" and "in
  hot months uses municipal water to cool the air". "Each year, it will use millions of gallons of
  water to keep the chips from overheating." SITE, REPORTED. New York Times, 2025 (via The Nightly,
  URL above).
- Amazon: Indiana sites use no cooling water October to March, and only a few hours a day on an
  average April to September day (paraphrase of Amazon's page); AWS fleet average "0.15 liters of
  water per kilowatt hour". SITE, REPORTED. Amazon, 2025:
  https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster
- Why air works: Trainium2's lower density and switchless design "has allowed AWS to get away with
  air cooling." The Register, 2025.
- Epoch: the site "forgoes external cooling infrastructure in favor of direct air-based cooling."
  Epoch AI, 2026: https://epoch.ai/data/ai-data-centers/directory/anthropic-amazon-new-carlisle
- Water volumes (secondary source quoting the city discharge permit, not checked against the
  permit): Phase 1 cooling-water discharge permit up to 1.58 million gallons a day, averaging about
  0.8; contracted potable delivery 2.5 million gallons a day by October 2026; outside air covers all
  but about 2% of the year (about 175 hours). The later 14-building expansion includes some
  direct-to-chip liquid-cooled buildings. SITE, secondary. Measured AI (Corey Trinetti), 2026:
  https://measuredai.substack.com/p/aws-new-carlisle-data-center-campus
- Unrelated to cooling but often confused with it: construction dewatering, "requested permission to
  pump 2.2 million gallons an hour, for 730 days" (NYT, 2025).

**Microsoft Fairwater Wisconsin (comparison):** "the second largest water-cooled chiller plant on
the planet"; "172 20-foot fans chill and recirculate the water back to the datacenter"; "72.6 miles
of mechanical piping"; "Over 90% of our datacenter capacity uses this system, requiring water only
once during construction". Atlanta's initial fill is "equivalent to what 20 homes consume in a
year", designed for "6-plus years" before replacement. OTHER SITE, REPORTED. Microsoft, 2025 (both
blog URLs above).

**xAI Colossus 2 (comparison):** 119 air-cooled chillers on site by August 2025, about 200 MW of
cooling (SemiAnalysis, 2025, SNIPPET ONLY via
https://newsletter.semianalysis.com/p/xais-colossus-2-first-gigawatt-datacenter).

#### Ways to quantify it

1. **Megawatts of heat.** Essentially all electricity that goes into the chips comes out as heat. 1
   GW of IT load is 1 GW of heat to move, continuously.
2. **Tons of refrigeration.** 1 ton = 3.517 kW. Abilene's 1,125.4 MW of chiller capacity is about
   320,000 tons (DERIVED). 1 GW of heat is about 284,000 tons.
3. **Home air conditioners.** A typical US central AC is about 3 tons. 320,000 tons is about 107,000
   houses' worth of AC, all running flat out all year (DERIVED). Abilene the city has roughly
   130,000 residents (from memory, not sourced here; check before using), so the campus has about
   the installed AC of every home in town twice over.
4. **Chiller count.** 640 at Abilene (Epoch estimate), i.e. 80 per building, each about 1.76 MW.
5. **Water.** Abilene: 8 million gallons once plus about 400,000 a year. New Carlisle: on the order
   of a million gallons a day in season (secondary), "millions of gallons" a year (NYT).
6. **Miles of pipe.** Not published for either site. Fairwater Wisconsin: 72.6 miles for three
   buildings.

---

### 3. Power equipment

#### Abilene (SITE)

- **Substations:** a 200 MW substation built 2022, expanded 2024, enough for Buildings 1 and 2; a 1
  GW substation, "close to completion" January 2026 and "complete" by July 2026. ESTIMATE from
  satellite imagery. Epoch AI, 2026 (URL above). ENR, 2025: the 200 MW substation was judged
  insufficient, so "A 340-MW natural gas turbine power plant was added to the scope."
- **On-site gas plant:** "The 1,100-acre campus, along with its 360 megawatt on-site gas plant";
  "Stargate's developers have already built 10 gas-powered turbines and 62 backup diesel generators"
  and "want to add 41 more turbines and 18 more generators". REPORTED. Texas Tribune / Floodlight
  (Evan Simon), 2026: https://www.texastribune.org/text/235529/
  - Permit: 360.5 MW simple-cycle plant, ten turbines, half GE Vernova (LM2500XPRESS, about 34 MW
    each) and half Solar Turbines Titan 350; development cost up to $500 million. SNIPPET ONLY: DCD
    https://datacenterdynamics.com/en/news/natural-gas-plant-planned-for-stargate-ai-data-center-campus-report
    and Cleanview
    https://cleanview.co/reports/behind-the-meter-data-centers/full-report/stargate-abilene
  - Crusoe says the turbines are "used for backup power for the data halls" (Crusoe, 2025).
    Cleanview says they were primary power until the grid tie was live. These conflict.
  - Permitted emissions: "allowed to emit more than 1.6 million tons of greenhouse gases" a year
    (Texas Tribune, 2026).
- **Grid:** "1.2 GW grid interconnection" to ERCOT (Crusoe, 2025).
- **Batteries:** Crusoe says "large-scale behind-the-meter" battery storage and solar; capacity
  **not found** (searched Crusoe press releases, Cleanview, ERCOT project listings).
- **Transformer count:** **not found.**

#### New Carlisle (SITE)

- **Backup generators:** 238 (first 9 buildings) + 234 (next 9) + 406 proposed (last 14) = 878
  diesel generators, Caterpillar 3516E or Cummins DQLF at 2.75 MW each, about 2.4 GW in total.
  Secondary source citing IDEM air permits. Measured AI, 2026 (URL above).
  - Amazon's own count: it "submitted permit applications for 911 generators across the two campuses
    in New Carlisle", "running on average, about ten hours per year." REPORTED. ABC57 (Jordan
    Tolbert), 2026:
    https://abc57.com/news/the-real-story-backup-diesel-generators-at-aws-data-center-campuses-in-new-carlisle
  - Indiana regulators cited Amazon for installing two 1,600 kW generators where 1,500 kW units were
    approved (WVPE, 2026, SNIPPET ONLY:
    https://www.wvpe.org/wvpe-news/2026-06-16/amazon-data-center-violates-air-permits-in-multiple-ways).
- **Substations:** two new 345 kV delivery substations (Larrison Drive, New Prairie) plus upgrades
  at the existing Olive station; about $185 million transmission package; first about 1.1 GW by
  December 15, 2026. Secondary, citing AEP. Measured AI, 2026. NYT, 2025 photo caption confirms "An
  electrical substation servicing the new Amazon Web Services facility."
- **Total draw:** "The facility will consume 2.2 gigawatts of electricity" (NYT, 2025). Epoch: 1,037
  MW of IT power now, 1,925 MW projected by early 2028; a permit for Buildings 19 to 32 suggests 2.3
  GW total facility power (Epoch AI, 2026).
- **On-site turbines:** none found. Grid supplied by Indiana Michigan Power.
- **Batteries, transformer count:** **not found.**

#### Comparisons

- Microsoft Fairwater Atlanta runs its GPUs with no on-site generation, no UPS and no dual-corded
  distribution, relying on the grid ("4x9 availability at 3x9 cost"), plus on-site energy storage to
  smooth load swings. Microsoft, 2025.
- Fairwater Wisconsin: "120 miles of medium-voltage underground cable". Microsoft, 2025.
- xAI Colossus 1: 168 Tesla Megapacks (Cleanview, SNIPPET ONLY).
- Bernstein's cost model: generators and turbines about 6% of capex, transformers about 5%, UPS
  about 4% (see section 6).

---

### 4. Physical and cyber security

#### What is known at the two sites

- **Abilene.** Crusoe CEO Chase Lochmiller: "Security is of massive concern to us. We take it
  extremely seriously, on the physical side as well as the digital." "We understand that the scale
  and the importance of this project makes it a security attack threat." The perimeter is "secured
  in such a way that if you drove a fully loaded 18-wheeler into it," the site would be undamaged.
  On government involvement: "I don't know that we have three-letter agencies involved." SITE,
  REPORTED. TIME (Billy Perrigo), 2025, read via AOL:
  https://www.aol.com/articles/crusoe-ceo-chase-lochmiller-building-181814209.html
  - Press visit, September 2025: journalists were "escorted by police" to the site (Fortune, 2025);
    photos and video of the data hall were banned and visitors handed over their devices (Ground
    Level AI, 2025).
  - Nothing published on guard counts, biometrics, or which security standard the site is built to.
    **Not found.**
- **New Carlisle.** Nothing site-specific found. AWS's generic description of every AWS datacenter:
  - Perimeter layer: "security guards, fencing, security feeds, intrusion detection technology". AWS
    (undated page, accessed 2026): https://aws.amazon.com/compliance/data-center/data-centers/
  - "Authorized staff utilize multi-factor authentication mechanisms to access data centers."
    "Physical access points to server rooms are recorded by Closed Circuit Television Camera
    (CCTV)." "Media that stored customer data is not removed from AWS control until it has been
    securely decommissioned." "Access is automatically revoked when an employee's record is
    terminated in Amazon's HR system." AWS (undated, accessed 2026):
    https://aws.amazon.com/trust-center/data-center/our-controls/
  - The AWS page does not mention biometrics.

#### The RAND levels (2024)

- Report: Nevo, Lahav, Karpur, Bar-On, Bradley, Alstott, "Securing AI Model Weights", RAND, 2024:
  https://www.rand.org/pubs/research_reports/RRA2849-1.html . It identifies 38 distinct attack
  vectors and defines five security levels.
- Definitions (from the RAND research brief, 2024:
  https://www.rand.org/pubs/research_briefs/RBA2849-1.html):
  - "SL 1 can protect against amateur attempts: hobbyist hackers and untargeted 'spray and pray'
    attacks."
  - "SL 2 can likely hinder opportunistic efforts by professionals"
  - "SL 3 provides protection against cybercrime syndicates and insider threats."
  - "SL 4 can foil standard operations by leading cyber capable institutions"
  - "SL 5 can spoil the least common but the most dangerous attacks", i.e. "top-priority operations
    conducted by the world's most capable nation-states."
- "Achieving SL5 is currently not possible." Labs told RAND that SL3 would take about a year, SL4
  two to three years, SL5 "at least five years, and the support of the national security community."
- SL5 means, outside production use, "weights are stored in a completely isolated setup disconnected
  from the external world", plus "physical bandwidth limitations between devices or networks
  containing weights and the outside world."
- Confidential computing (keeping weights encrypted in use) "must include protections against
  physical attacks", which current GPU implementations lack. This is the part that touches the
  datacenter building directly.

#### What the labs have said

- **Anthropic.** ASL-3 security activated May 2025: "more than 100 different security controls",
  including "two-party authorization for model weight access" and "Egress bandwidth controls
  restrict the flow of data out of secure computing environments where AI model weights reside." The
  standard targets sophisticated non-state attackers and explicitly excludes "Nation-state threats
  (other than those using non-novel attack chains)" and "sophisticated insider risk". Anthropic,
  2025: https://www.anthropic.com/news/activating-asl3-protections . The post says nothing about
  physical datacenter security.
  - Outside criticism: "An AI company's model weight security is at most as good as its compute
    providers' security" (LessWrong post arguing Anthropic probably is not meeting its commitment
    with respect to cloud-provider insiders, SNIPPET ONLY:
    https://www.lesswrong.com/posts/zumPKp3zPDGsppFcF/anthropic-is-probably-not-meeting-its-rsp-security).
- **OpenAI.** "Reimagining secure infrastructure for advanced AI" (May 2024) proposed six measures,
  including trusted computing for AI accelerators, network and tenant isolation, and physical and
  operational security for datacenters. I could not open the post (openai.com redirected to
  trust.openai.com); the list is from memory plus The Decoder's 2024 summary
  (https://the-decoder.com/openai-prepares-its-ai-safety-infrastructure-for-advanced-ai/), so check
  wording before quoting.

Bottom line: both sites have ordinary hyperscale physical security. No public claim that either is
built to RAND SL4 or SL5.

---

### 5. Storage

**The guess of "zettabytes" is wrong by about three orders of magnitude. It is exabytes.**

- Neither Abilene nor New Carlisle has a published storage figure. **Not found** (searched Oracle,
  Crusoe, AWS, Epoch, The Register, Blocks & Files).
- Microsoft Fairwater: "Modern datacenters can contain exabytes of storage and millions of CPU
  compute cores."; "the Wisconsin AI datacenter's storage systems are five football fields in
  length!"; storage draws on "thousands of storage nodes and hundreds of thousands of drives." OTHER
  SITE, REPORTED. Microsoft, 2025:
  https://blogs.microsoft.com/blog/2025/09/18/inside-the-worlds-most-powerful-ai-datacenter/
- xAI Colossus: "more than 1 EB of capacity for training and checkpoint data"; "230,000 GPUs need >1
  EB of capacity for training and checkpointing workloads." Colossus 2 (about 1.2 million GPUs) is
  expected to have "multiple exabyte levels of overall capacity", estimated at more than 5.2 EB by
  scaling. OTHER SITE, ESTIMATE. Blocks & Files (Chris Mellor), 2026:
  https://www.blocksandfiles.com/flash/2026/11/04/musks-colossus-dc-cluster-whats-the-storage-situation/5307253
  - That ratio is about 4 to 5 TB per GPU. Applied to Abilene's about 400,000 GPUs: about 2 EB
    (DERIVED, rough).
- Scale check: the entire hard-drive industry shipped "361.4 EB" in Q1 2025 (WD 179.8, Seagate
  143.6, Toshiba 41). Blocks & Files, 2025:
  https://www.blocksandfiles.com/container-storage/2025/05/17/disk-drive-capacity-shipments-out-to-2030-forecast-to-rocket-upwards/1610577
  . That is about 1.4 ZB a year (DERIVED). One zettabyte at one site would be about eight months of
  the world's hard-drive output. CERN's whole disk store passed 1 EB in 2023 (Blocks & Files, 2026).
- Cost share: Bernstein puts storage at about 1 to 1.5% of capex, i.e. $350 to $500 million per
  gigawatt (dollar figure DERIVED from the $35B total), against 39% for GPUs. Investing.com, 2025
  (URL in section 6). Epoch's model has no separate storage line.

---

### 6. Cost breakdown

#### Dollars per gigawatt

| Source                                                      | Year | $ per GW                                                                                                                    | Scope                                                |
| ----------------------------------------------------------- | ---- | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Nvidia (Jensen Huang, Q2 FY2026 earnings call, 27 Aug 2025) | 2025 | $50 to $60B                                                                                                                 | whole AI factory                                     |
| Bernstein (via Investing.com)                               | 2025 | about $35B                                                                                                                  | GB200-era facility                                   |
| Epoch AI                                                    | 2026 | $37.9B                                                                                                                      | stylized 1 GW-of-IT US hyperscaler site, GB200 NVL72 |
| Bloomberg with Cushman & Wakefield (via AI Weekly)          | 2026 | about $30B                                                                                                                  | 1 GW in Abilene specifically                         |
| Foxconn chairman Young Liu (via Wccftech)                   | 2026 | up to $47B                                                                                                                  | Vera Rubin era                                       |
| Morgan Stanley (SNIPPET ONLY, via Crypto Briefing)          | 2026 | about $49B                                                                                                                  | Vera Rubin era, all-in US                            |
| Epoch AI site tracker                                       | 2026 | $31.2B for 824 MW of IT at Abilene (= $37.9B/GW); $39.3B for 1,037 MW at New Carlisle so far, $72.9B projected for 1,925 MW | site estimates                                       |

Nvidia verbatim (FactSet transcript, 2025:
https://s201.q4cdn.com/141608511/files/doc_financials/2026/q2/NVDA-Q2-2026-Earnings-Call-27-August-2025-5_00-PM-ET.pdf):
"Out of a gigawatt AI factory, which can go anywhere from $50 billion to, plus or minus 10%, let's
say, $50 billion to $60 billion, we represent about $35 billion, plus or minus, of that and $35
billion out of $50-or-so-billion per a gigawatt data center."

#### Breakdown 1: Epoch AI (2026), independent model

"A typical one-gigawatt AI data center requires $38 billion in up-front capital expenditure
(CapEx)". Amelia Michael and Ben Cottier, May 2026:
https://epoch.ai/data-insights/ai-datacenter-cost-breakdown

| Category                         | $M     | Share of up-front capex |
| -------------------------------- | ------ | ----------------------- |
| Servers (GB200 NVL72 systems)    | 21,188 | 55.9%                   |
| Facility (shell, power, cooling) | 11,433 | 30.2%                   |
| Network infrastructure           | 4,925  | 13.0%                   |
| Land                             | 172    | 0.5%                    |
| Utility works (substations)      | 164    | 0.4%                    |

Running costs are small next to that: "even energy, the largest OpEx category, costs only $0.6
billion per year." Labor is $40M a year in the model. INDUSTRY, ESTIMATE.

#### Breakdown 2: Bernstein (2025), sell-side

Investing.com, Nov 2025:
https://www.investing.com/news/stock-market-news/how-much-does-a-gw-of-data-center-capacity-actually-cost-4314046

- "GPUs dominate spending, accounting for 39% of total capex" (about $13.7B, DERIVED)
- Networking about 13% (switches about 3%; DPUs, NICs, copper cabling 2 to 3% each)
- CPUs about 3%
- Storage about 1 to 1.5%
- "Mechanical and electrical systems take up close to one-third of total spending": generators and
  turbines about 6%, transformers about 5%, UPS about 4%, cooling about 4%
- Per GB200 rack: about $5.9M, of which $3.4M compute hardware and $2.5M physical infrastructure. So
  $35B is about 5,900 racks per GW (DERIVED).
- Electricity about $1.3B a year per GW at $0.15/kWh.
- Staffing: the article says "some 8–10 people per 20-GW complex", which must be a typo (probably 20
  MW); do not quote.

INDUSTRY, ESTIMATE.

#### Breakdown 3: Bloomberg / Cushman & Wakefield (2026), Abilene-specific

About $30B to build and equip 1 GW in Abilene: chips $17B (57%), power infrastructure $3B (10%),
shell and construction $2.4B (8%); the remaining $7.6B (networking, cooling, other equipment) is not
itemized in the write-up I could read. SITE, ESTIMATE. AI Weekly summary, Oct 2026:
https://aiweekly.co/alerts/bloomberg-pegs-abilene-1gw-ai-data-center-at-30b-17b-on-chips ; original
(not opened, paywalled): https://www.bloomberg.com/features/2026-ai-data-center-build-costs/

Cross-check from a state filing: Crusoe Building 3 ("Project Plaid"), 484,960 sq ft, single story,
steel frame, "Estimated Cost: $292,000,000". Texas Department of Licensing and Regulation, 2025:
https://www.tdlr.texas.gov/TABS/Search/Project/TABS2025011917 . Eight shells at $292M is $2.3B
(DERIVED), which matches Bloomberg's $2.4B shell line. The shells are about 7 to 8% of the all-in
cost.

#### Breakdown 4: McKinsey (2025), aggregate

Of $5.2 trillion of AI datacenter capex through 2030: 60% ($3.1T) to "technology developers and
designers" (chips and IT hardware), 25% ($1.3T) to "energizers" (power generation, cooling,
electrical equipment), 15% ($0.8T) to "builders" (land, materials, site development). INDUSTRY,
ESTIMATE. SNIPPET ONLY (the page timed out):
https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-cost-of-compute-a-7-trillion-dollar-race-to-scale-data-centers

#### Summary answer to "what % is buildings vs fiber vs compute vs storage"

- Compute (chips and servers): 55 to 60%
- Networking (switches, NICs, optics, cable): about 13%
- Storage: 1 to 1.5%
- Power and cooling equipment: 20 to 25%
- Building shell: about 8%
- Land: under 1%

All four independent sources agree within a few points on the top line: IT hardware is roughly two
thirds to 70%, everything physical is roughly 30%.

---

### 7. Other physical surprises

#### Racks, weight, density

- Abilene (SITE, REPORTED, ENR 2025): each building is single-story, 474,000 sq ft, with four
  106,000 sq ft data halls; "Each data hall holds 500 racks and up to 25 MW of IT load", so 2,000
  rack positions and 100 MW per building, 16,000 rack positions across 8 buildings (DERIVED). 50,000
  GPUs per building is about 700 NVL72 racks (DERIVED); the rest are network, storage, power and
  cooling-distribution racks.
- Nvidia GB200 NVL72 rack (INDUSTRY): "120kW rack"; "1.36 metric ton (3,000 lb) rack system"; liquid
  enters at 25 C and leaves about 20 degrees warmer (The Register, 2024). HPE lists 132 kW nominal
  and 3,245 lb fully loaded (SNIPPET ONLY). Microsoft runs them at "~140kW per rack" and "1,360 kW
  per row" (Microsoft, 2025).
- Nvidia's Vera Rubin generation: about 3,557 racks per GW at $9.1M each, i.e. about 280 kW of
  facility power per rack (DERIVED). Foxconn via Wccftech, 2026:
  https://wccftech.com/foxconn-pegs-nvidia-vera-rubin-ai-datacenter-at-47-billion-per-gigawatt/
- New Carlisle: Trainium2 racks are air cooled at about 27 kW (two 16-chip servers per rack), about
  a fifth of an Nvidia rack. Secondary (Measured AI, 2026, attributing to Amazon). The Register,
  2025 lists Trainium2 rack power as "Unknown". Thirty-two buildings at about 216,000 sq ft each,
  about 6.5 million sq ft total (Measured AI, 2026); NYT: each building "larger than a football
  stadium".
- Chip counts: New Carlisle about 500,000 Trainium2 as of October 2025 (Amazon, via Epoch); Abilene
  up to 50,000 GPUs per building, about 400,000 total (Crusoe, 2025).

#### Steel, concrete, copper

- Steel and concrete tonnage for Abilene or New Carlisle: **not found** (searched Crusoe, ENR,
  Construction Digest, TDLR filings, NYT, Amazon). ENR 2025 gives only "672 prefabricated IMP metal
  panels" per building and each building "enclosed in under eight weeks."
- Microsoft Fairwater Wisconsin (three buildings, 1.2 million sq ft, 315 acres): "Constructing this
  facility required 46.6 miles of deep foundation piles, 26.5 million pounds of structural steel,
  120 miles of medium-voltage underground cable and 72.6 miles of mechanical piping." OTHER SITE,
  REPORTED. Microsoft, 2025.
- Copper: Nvidia says a 1 MW rack on today's 54 V DC distribution needs up to 200 kg of copper
  busbar, and rack busbars alone in a 1 GW datacenter "could require up to 200,000 kg of copper"
  (SNIPPET ONLY:
  https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/).
  The "500,000 tons" version that circulates (Tom's Hardware) is a unit error.

#### People

- Construction: Abilene "a crew of 6,400 workers" (Fortune, 2025); "more than 5,600 construction
  workers on-site every day" (Crusoe, 2025); Oracle says nearly 20 million worker hours and up to
  9,000 on site (Oracle, 2026, SNIPPET ONLY, page returned 403:
  https://www.oracle.com/news/announcement/blog/facts-about-construction-safety-in-abilene-2026-06-25/).
  New Carlisle "about 4,000 workers are on site" in a typical week, four general contractors at once
  (NYT, 2025).
- Once running: New Carlisle had 935 permanent on-campus jobs in June 2026 with 18 buildings
  operating, about 6 to 9 people per building per shift (Measured AI, 2026, citing a county
  compliance review). Abilene: Crusoe's community page claims about 400 permanent jobs (SNIPPET
  ONLY; when I opened the page it showed only "dozens" for a generic 200 MW facility). Epoch's model
  budgets $40M a year for labor per GW.

#### Other

- Abilene traffic: a "six lane highway around the site"; shift changes cause "delays of 45 minutes
  around town" (Ground Level AI, 2025).
- New Carlisle sits on a wet site: Amazon "requested permission to pump 2.2 million gallons an hour,
  for 730 days" to dewater during construction, and there is "a 10-acre wetland in the middle of the
  complex" (NYT, 2025).
- Tax: New Carlisle's sales-tax break "could ultimately be worth around $4 billion" (NYT, 2025).

---

### Not found, and what I searched

- AWS-published fiber mileage for New Carlisle (AWS Rainier page, re:Invent keynote write-ups, The
  Register).
- Crusoe-published fiber mileage for Abilene (Crusoe blog, community page, press releases).
- Switch counts and transceiver counts at either site.
- Miles of cooling pipe at either site.
- Battery capacity and transformer counts at either site.
- Storage capacity at either site.
- Steel or concrete tonnage at either site.
- Guard counts, biometrics or a named security standard at either site.

### Pages I could not open

- Oracle Zettascale10 press release on oracle.com (403; used the HPCwire copy).
- Oracle construction-safety blog (403).
- x.ai/colossus (403).
- McKinsey "cost of compute" (timeout).
- OpenAI "Reimagining secure infrastructure" (redirect to trust.openai.com).
- Bloomberg originals (paywall; used AI Weekly's summary).
- Tom's Hardware Fairwater article body (truncated; headline only).

---

# Part: The Towns

## Abilene, TX and New Carlisle, IN: the towns under the two giant datacenters

Research date: 2026-11-22. Every figure has a source URL, publisher, year and a short verbatim
quote. Lines marked **est.** are my own arithmetic, not reported numbers. "Secondary" means I read
the figure in an aggregator or a syndicated copy and could not open the primary.

Method notes:

- census.gov QuickFacts returned HTTP 403 and the Census API wants a key, so Census numbers come
  through citypopulation.de, Census Reporter, USAFacts and FRED, all of which republish Census
  Bureau data.
- BEA numbers come through FRED (St. Louis Fed), which republishes BEA's county GDP tables.
- Abilene Reporter-News, South Bend Tribune, Business Insider and KTAB (bigcountryhomepage.com)
  pages mostly blocked fetching (403 / paywall / redirect). I used syndicated copies (Yahoo, AOL)
  and other local outlets (KTXS, KACU, WVPE, WNDU, WSBT, ABC57). Where a Reporter-News or Tribune
  story exists but I couldn't read it, I say so.
- A search hit about a "Taylor County Board of County Commissioners" data center moratorium workshop
  on 2026-08-26 is Taylor County, **Florida**, not Texas. Ignore it if you see it.

---

## 1. ABILENE, TEXAS (Stargate: Lancium land, Crusoe developer, Oracle tenant, OpenAI user)

### 1.1 Population

| Geography                                      | Figure                                                      | Source                                                                                                                                                                                                                         |
| ---------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Abilene city                                   | 131,588 (July 1, 2025 estimate); 124,970 at the 2020 census | citypopulation.de, republishing U.S. Census Bureau (2025 estimates). https://www.citypopulation.de/en/usa/texas/48441__taylor/ Quote: "Estimate 2025-07-01 ... 131,588"                                                        |
| Abilene city (ACS)                             | 130,033                                                     | Census Reporter, ACS 2024 1-year (2024). https://censusreporter.org/profiles/16000US4801000-abilene-tx/ Quote: "Population: 130,033"                                                                                           |
| Taylor County                                  | about 150,100 (2025)                                        | USAFacts, from Census Population Estimates Program (2026). https://usafacts.org/answers/how-many-people-live-in-the-us/county/taylor-county-tx/ Quote: "In 2025, there were about 150,100 people living in Taylor County, TX." |
| Abilene MSA (Taylor, Jones, Callahan counties) | 185,429 (2025)                                              | FRED series ABLPOP, source U.S. Census Bureau (updated 2026-03-27). https://fred.stlouisfed.org/data/ABLPOP.txt Quote: "2025-01-01 \| 185.429" (thousands of persons)                                                          |

Note: citypopulation.de's Taylor County row shows 148,813, which is the older Vintage 2024 number
(Census Reporter shows the same 148,813 under ACS 2024). Use 150,100 for 2025.

### 1.2 Size of the local economy

- **Taylor County GDP, 2024: $9.87 billion** (current dollars). BEA via FRED series GDPALL48441
  (updated 2026-02-05). https://fred.stlouisfed.org/data/GDPALL48441.txt Quote: "2024-01-01 |
  9865588" (thousands of dollars). 2023: 9,237,738.
- **Abilene MSA GDP, 2023: $10.31 billion.** BEA via FRED series NGMP10180 (updated 2024-12-04,
  series marked discontinued). https://fred.stlouisfed.org/data/NGMP10180.txt Quote: "2023-01-01 |
  10306.623" (millions of dollars). A 2024 MSA figure was not found in FRED; the county figure above
  is newer.
- **Median household income:** Abilene city $60,605; Taylor County $62,439. Census Reporter, ACS
  2024 1-year (2024). https://censusreporter.org/profiles/16000US4801000-abilene-tx/ Quote: "Median
  household income: $60,605". https://censusreporter.org/profiles/05000US48441-taylor-county-tx/
  Quote: "$62,439".
- **Payroll jobs, Abilene MSA: 81,000 (Oct 2026)**, up from 80,000 in Oct 2024. BLS via FRED series
  ABIL148NA (2026). https://fred.stlouisfed.org/data/ABIL148NA.txt Quote: "2026-10-01 | 81"
  (thousands of persons).
- **Main employers before the datacenter:** Dyess Air Force Base, Hendrick Health, Abilene ISD,
  Abilene Christian University, Texas Department of Criminal Justice, the State Supported Living
  Center, First Financial Bank, Hardin-Simmons and McMurry universities, AbiMar Foods, Great Lakes
  Cheese, Tigé Boats. Development Corporation of Abilene, "Major Employers" page (2026).
  https://developabilene.com/abilene-major-employers The page lists names without headcounts.
  Headcounts I found are old or secondary: Dyess "more than 5,000" and Hendrick "over 3,300" (search
  snippets from local radio and aggregator sites, not verified against a primary).
- **City budget:** FY2027 operating budget $414.6 million; property tax rate 74.95 cents per $100.
  City of Abilene news release (2026). https://www.abilenetx.gov/m/NewsFlash/Home/Detail/3449 Quote:
  "The Abilene City Council adopted a $414.6 million operating budget on Sept. 10, 2026".
- **County general fund:** $79 million. Business Insider via AOL (2025).
  https://www.aol.com/oracle-got-big-tax-breaks-090001667.html (the article attributes the figure to
  county auditor Elijah Anderson; original at
  https://www.businessinsider.com/oracle-seeks-bigger-tax-break-texas-property-value-protest-2025-7).

### 1.3 How big the datacenter is relative to that economy

#### Capital investment vs GDP

Reported figures for the campus disagree by more than 10x, because they measure different things:

- **"More than $47 billion"** for all 8 buildings, 4 million sq ft. Development Corporation of
  Abilene (DCOA), Texas Economic Development Council award application (2025).
  https://texasedc.org/assets/main/awards/CEDA2025/abilene-2025-ceda.pdf Quote: "the project now
  includes 8 buildings totaling 4 million square feet, 400 direct jobs created, and more than $47
  billion in capital investment." (This number presumably includes the GPUs.)
- **$3.5 billion** is the "targeted investment" in the abatement contract, with a $2.4 billion
  minimum. Business Insider (2025), as summarized in search results; the article itself redirected
  and I could not open it. Secondary quote: "To qualify for the tax break, AI startup Crusoe will
  need to spend a minimum of $2.4 billion of a $3.5 billion 'targeted investment.'"
  https://www.businessinsider.nl/stargate-developer-crusoe-could-spend-3-5-billion-on-a-texas-data-center-most-of-it-will-be-tax-free/
- **$15 billion** joint venture (Crusoe, Blue Owl, Primary Digital) for phase 2. Crusoe press
  release, cited by Compute Atlas (2026).
  https://www.crusoe.ai/resources/newsroom/crusoe-blue-owl-capital-and-primary-digital-infrastructure-enter-joint-venture
  (not opened; secondary).
- **$3.43 billion** of Oracle computer equipment for Buildings 1 and 2 on the 2026 Taylor Central
  Appraisal District roll, and a ~$200 million appraisal of the site for tax year 2025 that Oracle
  protested. suedatacenters.org tracker citing the Taylor CAD 2026 certified roll (2026),
  https://suedatacenters.org/data-centers/stargate-abilene-tx (secondary); Business Insider via AOL
  (2025), https://www.aol.com/oracle-got-big-tax-breaks-090001667.html Quote: "valued the Stargate
  site at about $200 million for the 2025 tax year."

**est.** $47B ÷ $9.87B (Taylor County 2024 GDP) = **4.8x one year of county GDP**. Against Abilene
MSA 2023 GDP: $47B ÷ $10.31B = 4.6x. Using the contract's $3.5B instead: 0.35x. Using the $15B joint
venture: 1.5x.

**est.** $47B ÷ 131,588 residents = about $357,000 of capital per Abilene resident.

#### Property tax vs local budgets

- DCOA's own projection: city gets $22.6M a year, county $18M a year. DCOA (2025), same PDF. Quote:
  "the City of Abilene will receive an estimated $22.6 million in property tax revenue each year for
  20 years. To put this in perspective, this represents 32% of the City's Fiscal Year 2025 Property
  Tax Revenue Budget. Taylor County will receive approximately $18 million in Property Tax Revenue
  each year for 20 years, representing 25% of its Fiscal Year 2025 Property Tax Revenue Budget."
  - **est.** That implies an FY2025 city property-tax budget of $22.6M ÷ 0.32 = $70.6M and a county
    one of $18M ÷ 0.25 = $72M.
  - **est.** $22.6M ÷ $414.6M (FY2027 city operating budget) = 5.5% of the whole city budget.
- Oracle's later number: $30M a year to Abilene. KUT (2026).
  https://www.kut.org/energy-environment/2026-08-12/abilene-tx-stargate-ai-data-center-economy-housing-crisis
  Quote: "Abilene will get an estimated $30 million annually". **est.** $30M ÷ $414.6M = 7.2% of the
  city operating budget.
- Time (2026): https://time.com/7362401/ai-stargate-data-center-abilene-housing-crisis/ Quotes:
  "would bring in over $22 million each year for the next 20 years" and "up to a third of the City
  of Abilene's budgeted property tax revenue for the fiscal year of 2025."
- County: $4M to $4.5M a year once the first two buildings are occupied, $18M with all eight,
  nothing before FY2027. KTAB/KRBC via Yahoo Finance (2025).
  https://finance.yahoo.com/news/taylor-county-estimated-see-18-222915156.html Quote: "Taylor County
  is estimated to see a windfall of $18 million a year".
- County, 2025 roll: "more than half the county's new property value this year came from Lancium";
  about $3 million of county tax from Lancium properties. Business Insider via AOL (2025), URL
  above. KTAB via Yahoo Finance (2025):
  https://finance.yahoo.com/news/tenant-challenges-lancium-ai-facility-233043823.html Quote: "the
  initial new property value came in at $930 million" and "$560 million of that was based on the
  Lancium property".
- City tax base: council told the tax base grows more than 25% in one year. KTXS (2026).
  https://ktxs.com/news/local/story/data-centers-in-abilene-a-community-conversation Quote (George
  P. Bush): "The tax base will grow by over 25% in one year." City FY2027 release: "New property is
  expected to account for $16.8 million of the $18.3 million increase in total property tax
  revenue." (City of Abilene, 2026, URL above; "new property" is not only the datacenter.)
- **Sales tax is the bigger near-term number.** City of Abilene (2026), URL above. Quote: "a $19.3
  million one-time sales tax surplus the City expects from data center construction". A KTAB report
  (2026, via search summary; page returned 403) says FY2026 sales tax is forecast above $67M against
  a $48.5M budget:
  https://www.bigcountryhomepage.com/news/how-datacenter-activity-is-impacting-the-city-of-abilenes-fy-2027-budget/
  **est.** $19.3M ÷ $48.5M = 40% over budget. Time (2026) quotes the Chamber CEO: "the city's sales
  tax revenue increased 40% compared to the average of the previous four years". The city treats it
  as one-time money.
- **Schools get nothing extra.** Abilene ISD has no abatement, but Texas school finance claws the
  gain back. KTAB (2026), via search summary; page returned 403:
  https://www.bigcountryhomepage.com/news/the-data-center-equals-no-new-revenue-for-us-aisd-superintendent-talks-district-revenue/
  Quote (headline): "The data center equals no new revenue for us". Abilene ISD August 2026 board
  recap (via search summary): the district "has officially entered recapture under Chapter 49 due to
  the increase in local property values", recapture payment "approximately $1.2 million".
  https://www.abileneisd.org/o/crms/article/3097861 (An earlier DCOA quote from the superintendent
  said the projects "could reduce the average school taxes while also generating the bond capacity
  needed to modernize our schools.")

#### Jobs vs local employment

- Construction: "The project created 9,000 immediate construction jobs" (Oracle, via KUT 2026, URL
  above); "There's 6,000 workers here, give or take" (Texas Standard, 2026,
  https://texasstandard.org/stories/stargate-data-center-abilene-texas-construction-ai-artificial-intelligence/);
  "More than 3,000 construction workers are already on-site daily, with that number expected to rise
  to nearly 5,000" (DCOA, 2025).
- Permanent: 357 required by the abatement at a $57,600 minimum salary (Business Insider 2025,
  secondary quote: "create 357 new full-time jobs with minimum salaries of $57,600"); "more than 400
  new direct jobs" (DCOA 2025); "1,000 long-term jobs once it's completed" (Oracle via KUT 2026);
  "about 300 permanent jobs" (Texas Standard 2026); Texas Tribune (2026) cites ConstructConnect:
  "the approximately 100 required to operate it once complete"
  https://www.texastribune.org/2026/02/13/texas-data-centers-local-governments-power/
- **est.** 6,000 construction workers ÷ 81,000 MSA payroll jobs = 7.4%. 9,000 ÷ 81,000 = 11%. 6,000
  ÷ 131,588 residents = 4.6% of the city's population.
- **est.** Permanent jobs: 357 ÷ 81,000 = 0.44% of MSA payroll jobs; 400 → 0.49%; 1,000 → 1.2%.
- MSA payroll employment rose only 1,000 (80.0K to 81.0K) from Oct 2024 to Oct 2026 (FRED/BLS
  above). Most construction workers are out-of-state contractors who don't show up in local payroll
  counts; that inference is mine.

### 1.4 Incentives

- **City of Abilene: 85% property tax abatement.** KTAB via Yahoo (2025).
  https://www.yahoo.com/news/abilene-city-council-weighs-large-005212844.html Quote (City Manager
  Robert Hanna): "On the tax abatement side, it's 15% of their tax liability. So, we're abating 85%,
  and we get 15%." Same article: the second reinvestment zone covers 940.89 acres; Hanna on the
  first agreement: "we're talking 70, 80, $90 million worth of return to the taxpayers of Abilene in
  revenue"; and "if they're required to pay their full tax burden, there's no way they could build
  the property."
- **Council votes:** approved Feb 13, 2025 (KTXS, 2025,
  https://ktxs.com/news/local/abilene-city-council-discusses-multiple-largely-talked-about-items-in-meeting).
  On Aug 28, 2025 Resolution 171-2025 split the abatement by building, approved 6-0 with one absent
  (Compute Atlas tracker citing council minutes, 2026,
  https://www.compute-atlas.com/facilities/stargate-abilene-tx; minutes at
  https://abilenetx.api.civicclerk.com/v1/Meetings/GetMeetingFileStream(fileId=4729,plainText=false),
  not opened).
- **Taylor County: 80% for 10 years** per KTAB (2025),
  https://finance.yahoo.com/news/taylor-county-estimated-see-18-222915156.html (paraphrase in my
  fetch: Lancium "would not pay taxes on 80% of its property value for 10 years"; commissioners
  "agreed to amend a tax abatement for the Lancium project", meeting of Feb 25, 2025).
- **Duration is reported inconsistently.** 10 years (Texas Standard 2026: "85% of the property taxes
  over 10 years"; UT Law clinic 2026), "a 20-year property tax abatement" from the county (KACU
  2026,
  https://radio.kttz.org/2026-09-04/panel-tackles-persistent-concerns-around-abilenes-ai-boom), and
  DCOA's "each year for 20 years". Texas Tax Code ch. 312 caps one abatement at 10 years; trackers
  describe the deal as two consecutive 10-year terms (Measured AI via search summary). I could not
  open the contract. Treat "85% city / 80% county, 10 years per building, phased over about 20
  years" as the best reading, not a confirmed fact.
- **What the company promised in return:** at least $2.4B of investment and 357 full-time jobs at
  $57,600+ (Business Insider 2025, secondary). DCOA (2025): "at least 50 direct jobs per building".
  Soft pledges: "Crusoe and Lancium have both pledged to support Science, Technology, Engineering,
  and Math initiatives, scholarships, and community nonprofit programs." (DCOA 2025). No cash
  community fund, road fund or water payment was found in any source. Lancium said it would build
  its own truck road (KTAB via Yahoo 2025,
  https://www.yahoo.com/news/prisoners-own-homes-traffic-rules-003842652.html).
- **Land:** Lancium annexed 800+ acres into the city in 2021. DCOA (2025). Quote: "facilitate
  Lancium's annexation of over 800 acres into the city limits." This matters for section 1.6: the
  site is inside city limits, so city zoning and city utilities apply.
- **Oracle then asked for more.** Oracle protested the ~$200M 2025 appraisal while holding the 85%
  abatement. Business Insider via AOL (2025). Quote: "Oracle is disputing the property valuation of
  its Stargate data center site in Abilene, Texas". Outcome of the protest: not found.
- **State sales tax exemption for datacenters** (Texas Tax Code 151.359): see state section.
- **School district:** no abatement (KTAB 2025, URL above: Abilene ISD "does not have an abatement
  agreement").

### 1.5 How residents feel

**Polls:** no Abilene or Taylor County poll found (searched "Abilene data center poll", UT Texas
Politics Project, Texas Tribune). Statewide Texas polling is in the state section.

**Turnout / early indifference:**

- "In Abilene, the data center project was not subject to much public scrutiny ... only one person
  testified in opposition to the generous tax abatement given to Stargate." UT School of Law
  Environmental Clinic blog (2026).
  https://sites.utexas.edu/texasenvironmentallaw/can-a-small-texas-town-say-no-to-ai/
- Feb 4-5, 2025 special council meeting: residents Samuel Garcia and Tammy Fogle asked about water,
  power and what the company contributes. KTAB via Yahoo (2025), URL above. Quote (Fogle): "Are they
  going to be contributing something since they're going to be expanding the need for the
  resources?" (Fogle later ran for council Place 4 in May 2026 and lost the June 13 runoff to
  Benjamin Bailey, 75% to 25%, per KTXS results via search summary. No source ties that race to the
  datacenter.)
- Feb 11, 2025 county commissioners meeting: one resident, Dr. Mark Teague, raised groundwater and
  energy concerns; Judge Crowley said the county wanted more citizen input. KTXS (2025).
  https://ktxs.com/news/local/taylor-county-residents-raise-concerns-on-lancium-tax-breaks-at-commissioners-meeting

**Complaints, with dates:**

- **Traffic (Mar 11, 2025):** Taylor County commissioners put up "No Thru Trucks" signs and a 45 mph
  limit after residents complained. KTAB via Yahoo (2025).
  https://www.yahoo.com/news/prisoners-own-homes-traffic-rules-003842652.html Quote (resident Cheryl
  Davis): "we kind of feel like prisoners in our own homes"; a resident counted "more than 72 trucks
  passing in front of their home" in 12 hours; Davis said two home sales fell through.
- **Housing (the main one, 2026):**
  - Time (Feb 4, 2026): https://time.com/7362401/ai-stargate-data-center-abilene-housing-crisis/
    Quotes: "the Abilene average rent per month is $2,395, up $1,000 from a year ago"; "a housing
    shortage of about 5,600 units" before the datacenter; council approved "two more RV parks to
    hold thousands of residents"; bail bondsman Vicki Morris: "Nobody can find a place to live".
  - KUT (Aug 12, 2026):
    https://www.kut.org/energy-environment/2026-08-12/abilene-tx-stargate-ai-data-center-economy-housing-crisis
    Quotes: "The average rent in Abilene is almost $2,600 a month" (up nearly 50% in a year, per
    Zillow); "it's cheaper to rent in Austin right now than it is in Abilene"; Abilene Christian
    University: "more than 100 of its incoming students did not have a place to live"; rehousing a
    homeless family: "Now, it can take up to six months."; neighbor Lexi Smith: "We got taken, we
    got robbed".
  - KACU (Sep 4, 2026): "Rents have doubled and even tripled across the area."
    https://radio.kttz.org/2026-09-04/panel-tackles-persistent-concerns-around-abilenes-ai-boom
- **Water:** the city says the closed-loop system takes an initial 8 million gallons against 22
  million gallons of daily city use. Texas Tribune (2025).
  https://www.texastribune.org/2025/09/25/texas-data-center-water-use/ Quote: "The data center will
  initially use 8 million gallons of Abilene city water to fill the cooling system." Mayor Weldon
  Hurt (KTXS 2025): "they're going to be using less than 1% of the water consumption in Abilene over
  that period each day".
- **Power and air:** the campus has ten on-site gas turbines rated 360.5 MW under a TCEQ standard
  permit (Compute Atlas tracker citing TCEQ, 2026, secondary). Residents at the Feb 2025 hearing
  invoked the 2021 freeze.
- **Transparency:** residents near the site complained at a Planning and Zoning Commission meeting
  about not being told of changes, including an on-site gas plant (KTAB 2025, via search summary;
  page 403/404:
  https://www.bigcountryhomepage.com/news/residents-demand-transparency-in-abilene-ai-data-center-project/).

**Organized opposition:**

- **Protest at the Texas Tribune / Chamber of Commerce town hall, Aug 26, 2026** (Heritage Square;
  date from KTXS's same-day story,
  https://ktxs.com/news/local/story/data-centers-in-abilene-a-community-conversation). KACU
  (published Sept 2, 2026; KTTZ reprint Sept 4),
  https://www.kacu.org/local-news/2026-09-02/panel-tackles-persistent-concerns-around-abilenes-ai-boom
  . Crowley also said: "But if people want counties that have control over data centers, you have to
  have an abatement". Quotes: resident Molly Cedillo's sign read "No More Backroom Data Center
  Deals."; "a group of demonstrators who showed up at the panel" with "concerns about water,
  affordability and local government transparency."; County Judge Phil Crowley: "I understand
  abatements are unpopular." When Google's representative said the company gave $50,000 for
  homelessness, the audience reaction showed "the sum falls far short of the need." Turnout number:
  not reported. The Reporter-News ran "See Judge Crowley hear residents' complaints after Abilene
  data center forum" (2026-08-28); I could not open it.
- **Change.org petition** "Stop the building and expansion of data centers in Abilene, TX", created
  April 14, 2026 by Jamil Whelan: 210 signatures when I fetched it (goal 500).
  https://www.change.org/p/stop-the-building-and-expansion-of-data-centers-in-abilene-tx That is
  0.16% of the city's population (**est.**).
- **Save Abilene** (https://saveabilene.com/), a satirical site, "a project of the American
  Superhero Coalition", that told people to vote in the Nov 3, 2026 election and named three
  candidates (Riley Rodriquez, Diana Luna, Kyle Rable) as wanting datacenters to "pay their share".
  Not a membership group as far as I can tell.
- **Riley Rodriquez**, an Abilene resident who lives near the campus, spoke at a Public Citizen
  press conference on Oct 20, 2026. Texas Tribune (2026).
  https://www.texastribune.org/2026/10/20/data-center-permits-tceq-abbott-texas-pause/ Quote: "The
  people in this area have had enough, and we're fed up. We want real policy around this, not
  rhetoric".
- **Lawsuits against the Abilene campus:** none found. suedatacenters.org lists none "as of November
  4, 2026" (secondary).

**Elections:**

- **May 2, 2026 city election:** Mayor Weldon Hurt and Place 3's Jay Patterson ran unopposed. KTXS /
  KTAB (2026), via search summary: "Mayor Weldon Hurt and Place 3 council member Jay Patterson, both
  of whom ran unopposed, were officially sworn into office."
  https://ktxs.com/news/local/abilene-city-council-certifies-may-2-election-results No local race
  visibly turned on the datacenter.
- **Nov 3, 2026, Texas House District 71 (Abilene):** Republican Jay Hardaway beat Democrat Diana
  Luna (who campaigned on the datacenter's effects) with 73.7%. KTXS (2026).
  https://ktxs.com/news/local/jay-hardaway-projected-to-win-texas-house-district-71-seat Hardaway
  after winning: "reforms on the data center front, it's my hope that there are Democrats that are
  enthusiastic about that".
- **Statewide, the same night:** Greg Abbott lost; Governor-elect Gina Hinojosa campaigned on a
  datacenter moratorium; Democrats took the Texas House. Bloomberg via Insurance Journal (Nov 19,
  2026). https://www.insurancejournal.com/news/southcentral/2026/11/19/893149.htm Quote: her
  campaign included "repeated calls for a moratorium on new data centers." and data centers "emerged
  as a key issue in the midterm elections." So Abilene itself voted Republican by 3 to 1 while the
  state turned.

**Supporters' case:**

- Mayor Hurt (Jan 2025, KTAB via Yahoo): "It does put Abilene on the national map." and "it's a win
  for Abilene, but it's a win for this whole region."
  https://www.yahoo.com/news/locals-weigh-stargate-benefits-abilene-161920913.html
- Council member Brian Yates (Time 2026): "The choice is not between $12 million or $4 million. It's
  between $4 million or zero".
- DCOA CEO Misty Mayo (KUT 2026): "New tax revenue funds new roads." Time (2026): Abilene has "$110
  million worth of street repairs needed, but only $7 million to spend on those projects in its
  latest budget."
- George P. Bush at the Aug 2026 forum (KTXS): "it's unprecedented economic development."
- Counter-view from economist Timothy Bartik on the jobs claims (Time 2026): "the industry is vastly
  overstating them".

### 1.6 Exposure to local rules

**Who has leverage:**

- **Abilene City Council.** The campus was annexed into the city, so council controls zoning, the
  reinvestment zone and the abatement, and city water. Texas Tribune (2026).
  https://www.texastribune.org/2026/02/13/texas-data-centers-local-governments-power/ Quotes:
  "Cities can control what happens within their limits through land use and utility control"; cities
  "have a right to impose conditions for approval on a new heavy water user"; but a government
  "can't say no, just for the sake of saying no or because it's controversial."
- **Taylor County Commissioners Court.** Abatement and county roads only. Same article: "Counties
  have no zoning authority and typically don't operate utility systems." and any other safeguard
  "would have to be through a tax abatement agreement with the developer." Crowley made the same
  point at the Aug 2026 forum (KACU): counties need abatements to have any say.
- **Taylor Central Appraisal District / Appraisal Review Board.** Sets the taxable value Oracle is
  contesting.
- **Abilene ISD.** No lever; no abatement, revenue recaptured by the state.
- **State bodies with more power than any local one:** ERCOT and the PUC (SB 6, large-load
  interconnection), TCEQ (air permit for the on-site gas turbines), the Legislature (convenes Jan
  12, 2027 with a Democratic House and a governor who ran on a moratorium).

**What has actually been proposed or passed locally since approval:**

- Moratorium in Abilene or Taylor County: **none found.** Rezoning denial: none found. Abatement
  clawback: none found (the only move on the tax deal went the other way, with Oracle protesting its
  appraisal in 2025). New datacenter ordinance: none found. Searched: "Abilene data center
  moratorium/ordinance/zoning 2026", "Taylor County commissioners data center 2026", Abilene council
  coverage on KTXS/KTAB/KACU.
- Passed: county truck-route and speed rules (Mar 11, 2025); council approvals of RV parks for
  workers (Time 2026); the Aug 28, 2025 re-split of the abatement by building.
- Elsewhere in Texas, county moratoria have been fragile: Hood County voted one down in Feb 2026
  after a state senator threatened legal action; Hill County passed a one-year pause 3-2 in May 2026
  , was sued by a developer for $100 million and later rescinded it (Texas Tribune 2026,
  https://www.texastribune.org/2026/05/12/texas-hill-county-approves-data-center-construction-pause-ai/,
  via search summary).

**Do later phases still need local approval?**

- The original eight buildings are already covered by the approved abatements, are built or nearly
  built, and need nothing more from the city that I could find. Crusoe "is still completing six more
  buildings for OpenAI and Oracle due to be completed by the end of this year" (Data Center Dynamics
  2026, via search summary).
- The planned 600 MW expansion past 1.2 GW was dropped by Oracle and OpenAI in March 2026 for
  commercial reasons, not local ones. Bloomberg (2026).
  https://bloomberg.com/news/articles/2026-03-06/oracle-and-openai-end-plans-to-expand-flagship-data-center
- Crusoe then announced a separate ~900 MW campus next door for Microsoft (Mar 27, 2026) with its
  own on-site power plant. Fortune (2026).
  https://fortune.com/2026/03/27/microsoft-texas-data-center-open-ai-former-partner-cloud-provider/
  Whether that campus has its own abatement or needs a rezoning: **not found.** One tracker says an
  application is "filed" and undecided, but it cites no local record
  (https://isadatacentercoming.com/projects/crusoe-microsoft-abilene-expansion-taylor-tx). A new
  abatement for it would need fresh votes from council and commissioners, which is the one place the
  2026 mood could bite.

---

## 2. NEW CARLISLE, INDIANA (AWS "Project Rainier", used by Anthropic)

The campus is not inside the town. It sits in unincorporated Olive Township in the county's Indiana
Enterprise Center, just east of New Carlisle. St. Joseph County, not the town, negotiated the deal
and holds the zoning power. The town supplies the water.

### 2.1 Population

| Geography                         | Figure                                                                                                                                              | Source                                                                                                                                                                                                                                |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New Carlisle town                 | 1,884 (July 1, 2025 estimate)                                                                                                                       | citypopulation.de, republishing U.S. Census Bureau (2025). https://www.citypopulation.de/en/usa/indiana/18141__st_joseph Quote: "New Carlisle (Town) ... 1,884"                                                                       |
| New Carlisle town, 2020 census    | 1,891                                                                                                                                               | Wikipedia citing the 2020 census. https://en.wikipedia.org/wiki/New_Carlisle,_Indiana (citypopulation.de shows 1,899 after rebasing)                                                                                                  |
| St. Joseph County                 | about 272,900 (2025)                                                                                                                                | USAFacts, from Census Population Estimates Program (2026). https://usafacts.org/answers/how-many-people-live-in-the-us/county/st-joseph-county-in/ Quote: "In 2025, there were about 272,900 people living in St. Joseph County, IN." |
| St. Joseph County (older vintage) | 273,744 (July 1, 2024)                                                                                                                              | Census Reporter, ACS 2024 1-year. https://censusreporter.org/profiles/05000US18141-st-joseph-county-in/                                                                                                                               |
| South Bend-Mishawaka IN-MI MSA    | not found (FRED series ID I tried returned 404; the MSA is St. Joseph County, IN plus Cass County, MI, roughly 325,000, from memory and unverified) |                                                                                                                                                                                                                                       |

### 2.2 Size of the local economy

- **St. Joseph County GDP, 2024: $19.49 billion.** BEA via FRED series GDPALL18141 (updated
  2026-02-05). https://fred.stlouisfed.org/data/GDPALL18141.txt Quote: "2024-01-01 | 19493411"
  (thousands of dollars).
- **South Bend-Mishawaka MSA GDP, 2023: $20.55 billion.** BEA via FRED series NGMP43780
  (discontinued). https://fred.stlouisfed.org/data/NGMP43780.txt Quote: "2023-01-01 | 20547.790".
- **Median household income:** St. Joseph County $63,504. Census Reporter, ACS 2024 1-year. Quote:
  "Median household income: $63,504". New Carlisle town: about $66,800 per aggregator sites quoting
  ACS 5-year data (secondary; Census Reporter's town page not reached).
- **Payroll jobs, South Bend-Mishawaka MSA: 139,100 (2025 annual average).** BLS via FRED series
  SMU18437800000000001A (2026). https://fred.stlouisfed.org/data/SMU18437800000000001A.txt Quote:
  "2025-01-01: 139.1".
- **Main employers before the datacenter:** University of Notre Dame (largest; about 5,600 employees
  per a dated study), Beacon Health System, Saint Joseph Health System, AM General, South Bend
  schools, the county itself. State of Indiana Hoosiers by the Numbers major-employers list
  (https://www.hoosierdata.in.gov/major_employers.asp?areaID=141) lists names without headcounts.
  Current headcounts: not found.
- **New Carlisle itself:** "a town of 1,900 people", farming roots, a historic downtown, post office
  since 1837. Peter Osnos, Substack (2025).
  https://peterosnos.substack.com/p/a-21st-century-colossus-and-a-188
- **Local government budgets, 2026** (Indiana Department of Local Government Finance, St. Joseph
  County 2026 Certified Budget Order, Jan 14, 2026):
  https://www.in.gov/dlgf/files/2026-reports/2026-budget-orders/St-Joseph-260114-2026-Budget-Order.pdf
  - St. Joseph County (county unit): certified budget $135,682,675; property tax levy $84,469,044;
    certified assessed value $14,611,493,562. Quote: "Unit Total: $135,682,675 ... $84,469,044 ...
    $0.5781".
  - New Carlisle Civil Town: budget $4,938,574; levy $2,079,421; assessed value $183,031,503.
  - New Prairie United School Corporation (St. Joseph County portion): levy $6,041,608.
  - Olive-New Carlisle-Hudson Fire Protection Territory: levy $2,234,531.
  - **est.** Sum of all 37 taxing units' levies in the order: $515.3 million.

### 2.3 How big the datacenter is relative to that economy

#### Capital investment vs GDP

- **$11 billion** announced April 2024, then the largest capital investment in state history. Inside
  Indiana Business (2024).
  https://www.insideindianabusiness.com/articles/incentives-approved-for-amazon-data-center-project
- Scale since: "Amazon plans to build and operate 30 data centers on roughly 1,200 acres" and "up to
  2.2 gigawatts". TheStatehouseFile.com via Indiana Citizen (2026).
  https://indianacitizen.org/uncertain-future-new-carlisle-offer-lessons-to-other-communities-as-data-centers-arrive/
  Osnos (2025): Amazon's forecast was $11B for sixteen buildings and it "now plans nearly double
  that". WVPE (2026) calls it "the then-$14 billion Amazon data center" at the Aug 2024 vote, which
  conflicts with the $11B everyone else reports.
- "$8.9 billion as of January 1, 2026" invested to date, including $1.7 billion of assessed real
  property; 18 buildings operating and 14 under construction. Measured AI, Substack (June 2026),
  https://measuredai.substack.com/p/aws-new-carlisle-data-center-campus (secondary; the post gives
  no URL for these, they appear to come from the county's June 2026 compliance review).

**est.** $11B ÷ $19.49B (county 2024 GDP) = **56% of one year of county GDP**. $8.9B already spent =
46%. If the build really doubles to ~$22B, about 1.1x.

**est.** $11B ÷ 1,884 town residents = $5.8 million per New Carlisle resident; ÷ 272,900 county
residents = $40,000 each.

#### Property tax vs local budgets

- First-year tax bill and abatement size. WVPE (Aug 10, 2026).
  https://www.wvpe.org/wvpe-news/2026-08-10/council-republicans-ask-amazon-to-give-back-some-data-center-tax-break
  Quote (Council member Amy Drake): "Amazon will pay about $12.6 million in property taxes the first
  year" while the abatement "will save them over $50 million for the year."
- WVPE (June 24, 2026): Amazon had "nearly $38 million in property taxes abated in the first half of
  this year".
  https://www.wvpe.org/wvpe-news/2026-06-24/council-members-asking-amazon-to-pay-despite-tax-abatement
- Lifetime: "$4 billion in property tax abatements over 35 years" (WVPE 2026,
  https://www.wvpe.org/wvpe-news/2026-03-31/amazon-declines-publicly-discussing-renegotiating-tax-break).
  In 2024 the county's economic development director put it differently: "a net savings of about
  $1.9 billion for the company" while it "will still pay more than $722 million in taxes over a
  35-year period" (Inside Indiana Business 2024, URL above). The two numbers differ because the
  project roughly doubled and the first one is a 2026 press figure; I could not reconcile them from
  a primary.
- Projected: about $12.5M in 2027 and "above $20 million a year once full, making Amazon the
  county's largest taxpayer" (Measured AI 2026, secondary).
- **est.** $12.6M ÷ $515.3M (all property tax levied in the county) = 2.4%. $12.6M ÷ $84.5M (county
  government's own levy) = 15%. $12.6M ÷ $4.94M = 2.6x the town of New Carlisle's whole budget.
  Caveat: Amazon's payment is split across overlapping units (county, township, school, library,
  fire) and the site is in a TIF allocation area, so none of these units actually receives the whole
  $12.6M. I did not find the split.
- **est.** Abated tax of $50M+ a year = 59% of the county government's levy, or about 10% of all
  property tax levied in the county. $38M in a half-year annualizes to $76M, which would be 90% of
  the county government's levy. $4B ÷ 35 years = $114M a year on average.
- **est.** $1.7B assessed (secondary) ÷ $14.6B county certified assessed value = 12%.

#### Jobs vs local employment

- Permanent: "As of December 2025, the AWS center had 935 full-time employees, about 80% of them
  Indiana residents"; average pay $40.99/hour, "about $77,070 a year"; the exemption requires 125%
  of the county average wage ($35.97/hour). TheStatehouseFile via Indiana Citizen (2026), URL above.
  Amazon's own figure: "they've hired over 900 people for the data center" (WVPE Mar 2026). Promised
  in 2024: "at least 1,000 jobs", of which 400 direct (Inside Indiana Business 2024). Council
  President Bryan Tanner (Aug 2026): Amazon projects "over 3,000 permanent high-paying jobs."
- Construction: "There are about four thousand workers on the site." (Osnos 2025, citing the New
  York Times, June 24, 2025). TheStatehouseFile (2026): at peak, more than twice the town's
  population in workers passed through daily.
- **est.** 935 ÷ 139,100 MSA payroll jobs = 0.67%. 4,000 construction workers ÷ 139,100 = 2.9%.
  4,000 ÷ 1,884 = 2.1 construction workers per town resident. 935 permanent jobs = half the town's
  population.

### 2.4 Incentives

Approved Aug 13, 2024 by the county Redevelopment Commission, Commissioners and Council; the council
vote was 7-2 with Mark Root and Amy Drake voting no. Inside Indiana Business (2024), URL above.

- **Real property:** "a 10-year, 50% real property tax abatement for three parcels of land totaling
  870 acres." (Inside Indiana Business 2024). WVPE (May 2024): each shell "will generate $2.3
  million worth of taxes per year" before abatement.
  https://www.wvpe.org/wvpe-news/2024-05-31/st-joseph-county-officials-eye-tax-breaks-for-massive-amazon-data-center
- **Equipment (the big one):** an 85% exemption on computing equipment for 35 years under Indiana's
  Enterprise Information Technology Equipment law. WVPE (2024): "possibly an 85% exemption for 35
  years". It lasts as long as AWS meets the wage test (TheStatehouseFile 2026).
- **State sales tax:** no state sales tax on servers, software or the electricity to run them, for
  50 years. Inside Indiana Business (2024): the IEDC is offering "data center sales tax exemptions
  for eligible capital investments over a 50-year term". Plus "nearly $150 million" of
  performance-based IEDC incentives.
- **What Amazon promised:**
  - A community enhancement agreement "worth about $143 million" (county economic development
    director Bill Schalliol, Inside Indiana Business 2024) covering parks, schools, fire
    departments, roads and utilities. Line items per Measured AI (2026, secondary): an $11.1M
    Fillmore Road water tower, a $7.9M Edison Road sewer, $7M toward the $50M State Road 2 /
    Larrison interchange, sheriff road patrols, and per-building fees for fire service, schools and
    parks. About $114M of AWS-funded water and sewer work in total (same secondary source).
  - Paid so far, per Amazon: "they've given over $7 million for road improvements around the
    complex" and "granted over $250,000 to 31 community projects" (WVPE Mar 2026). New York Times
    via Osnos (2025): "Amazon agreed to pay $120,000 to cover overtime for traffic enforcement and
    an additional $7 million for road improvements."
  - Water: a county cap of 24 million gallons a day for the whole Indiana Enterprise Center (Inside
    Indiana Business 2024). Critics note the cap is voluntary (Measured AI 2026).
  - Electricity: Indiana Michigan Power said "Local ratepayers will not cover added power costs"
    (Inside Indiana Business 2024, paraphrase).
- **For comparison:** Microsoft, building in Granger in the same county, "has said they are not
  asking for property tax abatements" and "even reopened negotiations with LaPorte County and gave
  back their tax break." (WVPE Mar 2026).

### 2.5 How residents feel

**Polls:** no St. Joseph County poll found. Statewide: an October 2026 poll of 839 likely Indiana
voters found "almost 70% strongly or somewhat opposed building new data centers in Indiana, with 18%
in support." Indiana Capital Chronicle (Oct 15, 2026), via search summary; page returned 403.
https://indianacapitalchronicle.com/2026/10/15/hoosiers-disapprove-of-trump-braun-and-data-centers

**Incidents, with dates:**

- **Apr 30, 2025, wetlands hearing** at New Prairie High School on Amazon's request to fill nearly
  10 acres of wetlands. WNDU (2025).
  https://www.wndu.com/2025/05/01/new-carlisle-residents-voice-concerns-about-amazons-plans-fill-wetlands/
  Quote: "not a single person spoke in support of filling in fragile wetlands." A tracker puts
  attendance at 100+ (secondary).
- **Aug 2025:** the state environmental agency (IDEM) cited Amazon for filling wetlands without
  authorization and ordered work in those areas stopped. ABC57 (Aug 13, 2025).
  https://www.abc57.com/news/new-carlisle-amazon-data-center-cited-by-idem-for-impacting-wetlands-without-authorization
  A new permit hearing was held July 8, 2026 (WSBT 2026,
  https://wsbt.com/news/local/idem-hosts-public-hearing-amazon-data-center-permit-water-quality-wetlands-new-carlisle).
  Quote (Jennifer Betts, South Bend-Elkhart Bird Alliance): "Amazon has already partially destroyed
  a wetland without a permit".
- **Wells, Dec 2025 to Nov 2026:** homeowners near the site say their wells lost pressure after
  construction dewatering (Amazon sought permission to pump up to about 35 million gallons a day out
  of the ground during construction). ABC57 (Nov 18, 2026).
  https://www.abc57.com/news/wheres-the-water-one-year-later-homeowners-still-deal-with-well-water-issues-near-amazon-data-center
  Quote (Yvette Van Lue, 62 years in her home): "It all added up, Amazon." The state DNR blamed
  drought; Amazon says it buys town water and doesn't pump wells for operations.
- **Oct 21, 2025:** New Carlisle Town Council voted 4-0 to oppose a second hyperscale datacenter on
  1,000+ acres of farmland next to town. WVPE (2025).
  https://www.wvpe.org/wvpe-news/2025-10-24/new-carlisle-council-opposes-second-data-center-nearby
  Town Council President Marcy Kauffman: "Our town cannot sustain another data center." (Inside
  Indiana Business / WIBC 2025, via search summary).
- **Dec 9-10, 2025:** the County Council rejected that rezoning 7-2 after an eight-to-ten-hour
  meeting that ended about 4 a.m. WVPE (2025).
  https://www.wvpe.org/wvpe-news/2025-12-10/council-denies-rezoning-for-data-center-near-new-carlisle
  Quotes: the developer ran a "high-dollar PR blitz"; Amy Drake to New Carlisle residents: "I think
  that you have been forgotten, ignored and taken advantage of in the past." At that meeting
  "multiple people, including some elected officials, said the county had needlessly given Amazon
  too many incentives." (WVPE Mar 2026).
- **Traffic:** "It was just a nightmare to get through there." (former mail carrier Daniel Caruso,
  TheStatehouseFile 2026). NYT via Osnos (2025): "there has been such an uptick in congestion and
  traffic accidents".
- **Noise:** no New Carlisle noise complaints found. Osnos (2025) observed "the noise level is low."
  Housing: no rent-spike reporting found; Osnos notes the median home price went from under $200,000
  to about $250,000.
- **Electricity bills:** raised by critics (Citizens Action Coalition) as a stranded-cost risk, not
  as an observed bill increase tied to this site. See state section for I&M.

**Organized opposition:** Open Space Agricultural Alliance (a local farmland group dating from about
a decade ago, per Osnos 2025), South Bend-Elkhart Bird Alliance, Just Transition Northwest Indiana
(wetlands hearing), Citizens Action Coalition (statewide, rates). **Lawsuits against the Amazon
campus: none found** (Measured AI 2026 mentions none; searched "Amazon New Carlisle lawsuit").

**Elections (Nov 3, 2026):** Democrats swept the county: the County Council went from 5-4 Republican
to 7-2 Democratic, and the Republican commission president Carl Baxmeyer, who had backed the second
datacenter's rezoning, lost 58.4% to 41.6%. WNDU (2026).
https://www.wndu.com/2026/11/04/st-joseph-county-republicans-concede-local-races-congratulate-projected-winners/
WSBT (2026): "The Council now sits at seven-two with a Democratic majority. Previously, it was
five-four with a Republican majority."
https://wsbt.com/news/local/st-joseph-county-democrats-celebrate-sweeping-midterm-election-2026-us-house-senate-clerk-assessor-council-commissioner-prosecutor-blue-wave
This did not "turn on" the datacenter in a clean way: both sides ran against more datacenters. The
Republicans who lost (Amy Drake, Joe Thomas) had sponsored the ban and the clawback letters; the
Democrats who beat them (Rohatgi, Hamann, Cervelli) stood with a ban supporter at an Aug 26 press
conference. Winner Ranjan Rohatgi: "I heard people talking about data centers." (WSBT 2026). It was
a national Democratic wave year.

**Supporters' case:**

- Council President Bryan Tanner (D): the abatement "was approved by a supermajority of the council
  as well as the commissioners"; Amazon projects "over 3,000 permanent high-paying jobs." (WVPE Aug
  2026).
- Chamber president Jeff Rea: "a two-year moratorium basically takes us out of the game forever,
  probably." (WVPE Aug 2026,
  https://www.wvpe.org/wvpe-news/2026-08-21/st-joseph-county-leaders-debate-two-year-data-center-moratorium).
- Commissioner Carl Baxmeyer: datacenters offset revenue lost to the state's 2025 property tax cuts
  (WVPE May 2026, paraphrase).
- Then-council president Dan Schaetzle on the economic development director: "He has brought in over
  $20 billion of investment, businesses that will pay taxes that replace our property taxes." (WVPE
  Oct 2025,
  https://www.wvpe.org/wvpe-news/2025-10-15/county-council-oks-2026-budget-with-directors-salary-increase).
- Osnos (2025): "Amazon workers and the activity around the project has given a boost to the town's
  economy."

### 2.6 Exposure to local rules

**Who has leverage:**

- **St. Joseph County Council** (9 members; 7-2 Democratic from January 2027): zoning, abatements,
  and an annual compliance review of every abatement (the June 2026 review is where the clawback
  push started).
- **County Commissioners, Redevelopment Commission, Area Plan Commission, Drainage Board** (the
  Drainage Board approves construction dewatering; it renewed Amazon's permit in May 2026 per
  Measured AI, secondary).
- **Town of New Carlisle:** no zoning power over the site, but its two municipal water plants supply
  the campus, and its council has become a vocal opponent of further sites.
- **State:** IDEM (wetlands, air permits for 878 backup generators), DNR (groundwater), IURC (I&M's
  rates and large-load tariff), the General Assembly (sales tax exemption; local-control
  preemption).

**Proposed or passed since approval:**

- **Clawback requests (all refused):**
  - March 2026: four of five council Republicans (Drake, Thomas, Figg, Rutten) asked Amazon to
    renegotiate. WVPE (2026).
    https://www.wvpe.org/wvpe-news/2026-03-30/council-members-ask-amazon-to-renegotiate-data-center-tax-break
    Quote: "The initial value of Amazon's abatement was $4 billion over 35 years."
  - June 2026: the same four asked Amazon to "voluntarily pay into a fund that would reduce property
    tax bills for homeowners."
  - August 2026: Drake asked for $7 million a year back, enough for a $100 credit for each of 71,000
    homeowners. Amazon officials told a closed-door meeting they "are not interested in revisiting
    the issue." (WVPE Aug 10, 2026).
  - These were requests. No source says the county can change the abatement unilaterally while
    Amazon meets its job and wage terms; whether the contract has a clawback clause: not found.
- **Two-year moratorium:** proposed by council Republicans the week of Aug 17, 2026 (WVPE Aug 21,
  2026). Not adopted.
- **Permanent ban on new hyperscale datacenters:**
  - Resolution filed Aug 27, 2026; council voted 6-3 on Sept 22, 2026 to direct the Area Plan
    Commission to write a zoning amendment. ABC57 (2026).
    https://www.abc57.com/news/st-joseph-county-council-advances-plan-to-ban-new-data-centers Quote:
    "The resolution directs the Area Plan Commission to amend the county's zoning ordinance". The
    county has "around 40 data center buildings either under construction or in development", all
    Amazon's or Microsoft's.
  - It is aimed at newcomers, not Amazon: it would "ban any more data centers once Amazon and
    Microsoft's centers are finished." (WVPE Aug 27, 2026,
    https://www.wvpe.org/wvpe-news/2026-08-27/new-data-center-ban-has-majority-st-joe-county-council-support).
  - Nov 17, 2026: the Area Plan Commission voted 7-0 to send it back with an unfavorable
    recommendation; the draft defines hyperscale as over 1 million square feet. WVPE (Nov 18, 2026).
    https://www.wvpe.org/wvpe-news/2026-11-18/planners-say-data-center-ban-too-vague-hurts-growth
    Council committee debate starts Dec 8; Tanner: "I would anticipate, given the amount of
    concerns, it will be held in committee for some period of time."
- **Rezoning denial:** the Dec 2025 7-2 rejection of the third datacenter (above).
- **Neighbors:** "Marshall and Cass counties both approved permanent data center bans in April" 2026
  (ABC57 2026). "Almost a third of Indiana counties have issued restrictions on data centers."
  (TheStatehouseFile 2026).
- **Amazon's own concession:** it "will no longer sign nondisclosure agreements with local
  governments" (ABC57, Oct 28, 2026,
  https://abc57.com/news/amazon-details-water-and-energy-usage-at-new-carlisle-data-center).

**Do later phases still need approval?**

- Yes, but mostly from the state. The 14-building expansion needs an IDEM wetlands (Section 401)
  certification, which Amazon was cited for jumping in Aug 2025 and re-applied for in mid-2026, and
  an IDEM air permit; decisions expected early 2027 (Measured AI 2026, secondary). Locally it needs
  Drainage Board dewatering renewals and continued compliance with the abatement's wage and job
  terms.
- The land is already zoned and inside the Indiana Enterprise Center, and the abatement parcels were
  approved in 2024. I found no pending county zoning vote that could stop the expansion. Whether the
  extra buildings beyond the original 16 shells each need a new abatement resolution: not found.
- A state bill preempting local zoning for datacenters (HB 1333) got through the Indiana House 56-43
  on Feb 2, 2026 and died in a Senate committee. Council President Tanner described it to WVPE
  (Aug 2026) as failing by a "slim margin"; the roll call does not support "slim". See state
  section.

---

## 3. STATE-LEVEL MOVES (Texas and Indiana)

Gathered by a second research agent; I re-opened and confirmed the SB 293 bill text, the Foley &
Lardner count, the Hinojosa quote, the Bloomberg resumption story and the UT poll. "[snippet]" means
the figure came from a search-result summary and the page was not opened. Quotes are clipped to
about 125 characters by the fetch tool.

### 3.1 Texas

**The big three, all from the last four months:**

1. **Governor-ordered pause, Aug to Nov 2026.** Abbott ordered an ERCOT/PUC audit of every
   datacenter in the interconnection queue on Aug 3, a water-reporting crackdown on Sep 14, and on
   Sep 21 told the environmental regulator (TCEQ) "to halt all permits sought by data centers until
   the Electric Reliability Council of Texas (ERCOT) completes its audit." Office of the Governor
   (2026), https://gov.texas.gov/news/post/governor-abbott-directs-tceq-to-halt-data-center-permits
   ; timeline from Willkie Farr & Gallagher (2026),
   https://www.willkie.com/publications/2026/10/texas-governor-halts-data-center-permits-pending-ercot-audit
   . TCEQ resumed Nov 16: "The agency has resumed its normal permit review process." Texas Tribune
   (2026), https://www.texastribune.org/2026/11/17/tceq-environmental-data-center-permits-resume/ .
   ERCOT's audit report is due Dec 10, PUC meeting Dec 17; energization of new large loads still
   appears paused.
2. **Abbott lost on Nov 3, 2026.** "Democrats won the governorship, the lieutenant governorship, and
   control of the Texas House" "while Republicans retained control of the Senate." Gibson Dunn
   (2026),
   https://www.gibsondunn.com/texas-data-center-critical-dates-and-procedures-following-the-2026-elections/
   . Hinojosa, Oct 22 video: "When I am governor I will issue a moratorium — a ban — on all data
   center approvals." Her term begins January 19. Texas Tribune (Nov 4, 2026),
   https://texastribune.org/2026/11/04/data-center-texas-pause-gina-hinojosa-governor-policies/ .
   Scope (new vs existing, permits vs grid) is not specified. The Legislature convenes Jan 12, 2027.
3. **Sales-tax exemption repeal filed with a Senate supermajority.** SB 293 (Huffman) repeals Tax
   Code 151.359 and 151.3595. Bill text: an existing exemption "on the effective date of this Act
   expires on that date"; pending applications are "considered to be denied"; effective immediately
   with two-thirds of each house, otherwise "takes effect September 1, 2027." Texas Legislature
   Online (2026), https://capitol.texas.gov/tlodocs/90R/billtext/html/SB00293I.htm . "Twenty-three
   of the Senate's 31 members and members-elect had signed on to her bill by Monday evening." Foley
   & Lardner (Nov 10, 2026), https://www.foley.com/?p=131063 . The House version, HB 167,
   grandfathers already-certified datacenters. Whether the Abilene campus holds a Comptroller
   certification: not found (the Comptroller refused the Tribune's facility-level records request).

**SB 6 (2025), large loads of 75 MW and up.** Signed June 20, 2025. Text:
https://capitol.texas.gov/tlodocs/89R/billtext/html/SB00006F.htm

- Threshold: "The commission shall establish a demand threshold of 75 megawatts".
- Fees: "The standards must set a flat study fee of at least $100,000"; the final PUC rule (Project
  58481, adopted Sep 18, 2026, effective Oct 8, 2026) sets security at $50,000 per MW (secondary:
  https://ailawsusa.com/protection/tx-puct-large-load-interconnection-rule-58481-2026/).
- Curtailment ("kill switch"): utilities must be able to cut the load "during firm load shed", but
  "This subsection applies only to a load interconnected after December 31, 2025".
- Backup generation: a disclosure duty plus an ERCOT right to order on-site backup to run, not a
  mandate to install it.
- Transmission cost allocation: the PUC must revisit the "four coincident peak" method and amend
  rules "not later than December 31, 2026"; the draft report floats "a minimum demand charge based
  on their contracted peak demand" "for a period of 10 to 15 years." K&L Gates (2026),
  https://www.klgates.com/Request-for-Comments-on-Texas-PUCT-Draft-Report-Regarding-Transmission-Cost-Recovery-in-the-ERCOT-Region-3-30-2026
- **Reach on Abilene (inference):** the interconnection and curtailment rules bind new or expanded
  load, so whatever was energized before Dec 31, 2025 is mostly outside them. The
  transmission-charge change is the piece most likely to reach an existing load.

**Sales-tax exemption today.** Terms (Texas Tribune, Apr 2026, paraphrased,
https://www.texastribune.org/2026/04/08/texas-data-centers-sales-tax-break-billion-dollars/): over
100,000 sq ft, 20 jobs and $200M over five years; over 250,000 sq ft, 40 jobs and $500M; up to 15 or
20 years (another source says 10 or 15; check the statute). Cost: "this year Texas is forgoing at
least $1.3 billion."; "$3.2 billion in sales tax revenue over the next two years" (Texas Tribune,
Jul 2026, https://www.texastribune.org/2026/07/27/texas-data-centers-sales-tax-break-audits/). Of
138 qualified datacenters, 20 were audited and six were in breach (same, paraphrased).

**Abatement law.** Chapter 312 abatements run "for a period not to exceed 10 years" (Tax Code
312.204(a), https://texas.public.law/statutes/tex._tax_code_section_312.204). That is why "20 years"
in Abilene coverage is best read as two phased 10-year terms or a 20-year revenue projection. JETI
(Chapter 403) does not list datacenters as eligible. SB 36 (Zaffirini, filed for 2027) would bar new
or renewed Chapter 312/380/381 deals for datacenters from Sept 1, 2027
(https://capitol.texas.gov/tlodocs/90R/billtext/html/SB00036I.htm); inference: that blocks new deals
for an Abilene expansion, not the existing agreements. SB 34 would give counties datacenter zoning
in unincorporated areas only, which doesn't reach the annexed Abilene site.

**County moratoria.** Hood County rejected one 3-2 on Feb 10, 2026 after Sen. Bettencourt wrote that
commissioners "cannot claim any powers unless it is expressly conferred by the Constitution or
statute." (Texas Tribune 2026,
https://www.texastribune.org/2026/02/10/texas-hood-county-rejects-data-center-development-pause-ai/).
Hill County "approved a one-year pause on the construction of new data centers in unincorporated
areas" on May 12, 2026 and later rescinded it after a $100 million developer lawsuit (Texas Tribune
2026,
https://www.texastribune.org/2026/05/12/texas-hill-county-approves-data-center-construction-pause-ai/;
rescission per the Tribune's Aug 3 story, paraphrased). An Attorney General opinion was requested
Feb 23, 2026; no issued opinion found.

**ERCOT queue.** "ERCOT is tracking more than 438,000 MW of large load requests, nearly 89 percent
from data centers alone." ERCOT (June 18, 2026),
https://www.ercot.com/news/release/06182026-puct-approves-ercots . The batch study is paused and "We
will not have the study done by April 9, 2027" (Utility Dive 2026,
https://utilitydive.com/news/ercot-texas-puc-data-center-audit/828472).

**Abilene's most concrete state touchpoint.** "Stargate's developers have already built 10
gas-powered turbines and 62 backup diesel generators" and "want to add 41 more turbines and 18 more
generators to the sprawling site." The first units went through minor permits; the expansion needs a
major air permit, pending. Floodlight via Texas Tribune (2026),
https://www.texastribune.org/2026/07/09/texas-data-centers-ai-power-plants-pollution-state-permits/
. Inference: that permit sat under the Sep 21 to Nov 16 halt and would sit under a Hinojosa
moratorium. Its current status: not found.

**Water reporting.** The Water Development Board's mandatory survey: "Only one-third of data centers
surveyed in 2024 responded and in 2025 only 17% responded"; the penalty is "a Class C misdemeanor
with a maximum fine of $500." Texas Tribune (2026),
https://www.texastribune.org/2026/06/23/texas-data-centers-puc-water-survey/ . Whether Abilene's
operators answered: not found.

**Texas polls.**

| Poll                          | Dates           | Sample                  | Result                                                                                       |
| ----------------------------- | --------------- | ----------------------- | -------------------------------------------------------------------------------------------- |
| UT / Texas Politics Project   | June 5-12, 2026 | 1,200 registered voters | 56% oppose a datacenter in their community, 29% support; Republicans 44% oppose, 42% support |
| UT / Texas Politics Project   | Aug 5-13, 2026  | 1,200 registered voters | 57% oppose, 30% support                                                                      |
| Univ. of Houston Hobby School | Oct 10-14, 2026 | 2,000 likely voters     | 79% support limiting the number of datacenters built in Texas                                |

Sources: Texas Tribune (2026),
https://www.texastribune.org/2026/06/23/texans-oppose-data-centers-poll/ Quote: "56% of those
surveyed by the UT poll said they oppose the construction of a data center in their community.";
Texas Politics Project (2026),
https://texaspolitics.utexas.edu/blog/june-poll-finds-a-competitive-u-s-senate-race-in-texas-amid-continuing-economic-concerns-data-center-backlash
; Hobby School (2026), https://uh.edu/hobby/texas2026/centers.pdf Quote: "79% of Texas likely voters
support a policy that would limit the number of data centers that can be built in Texas".

### 3.2 Indiana

**Sales and use tax exemption (IC 6-2.5-15).** Up to 25 years under $750M of investment; "If the
investment exceeds $750 million, the IEDC may award an exemption for up to 50 years." IEDC (2026),
https://iedc.in.gov/incentives/data-center-sales-tax-exemption . The state has no cost estimate: "it
is not currently possible to estimate its fiscal or economic impact due to data limitations." (WFYI
2025,
https://www.wfyi.org/news/articles/data-center-tax-breaks-could-leave-indiana-22-billion-short). A
secondary site citing a WTHR / Good Jobs First investigation puts current exemptions at "more than
$655 million", "$561 million of that" to Amazon (unverified,
https://sales.tax/sales-tax-updates/indiana-data-center-sales-tax-exemption-655-million-amazon/).

- 2025: expanded, not cut (HB 1601).
- 2026: HB 1333 first contained a full repeal; "Lawmakers abruptly stripped bill language that would
  have eliminated state sales tax exemptions for data centers" (Indianapolis Star via Yahoo, Jan
  2026,
  https://www.yahoo.com/news/articles/indiana-lawmakers-axe-proposal-eliminate-110644839.html). What
  became law is HB 1210, signed March 12, 2026: a local payment of at most one penny per dollar of
  exempted purchases, only for datacenters "gaining local approval after June 30." (Indiana Capital
  Chronicle via WFIU 2026,
  https://www.ipm.org/news/2026-03-26/that-1-incentive-to-encourage-data-center-approvals-final-deal-watered-it-down).
  Inference: it does not reach Amazon's New Carlisle certificate.
- 2027 repeal bills: not found.

**Local control.** HB 1333 would have made datacenters a permitted use on lower-quality farmland:
"This bill would allow data centers on agriculturally zoned land, which would eliminate that public
process"; "The bill passed the House 56-43"; "That description fits about 31% of all farmable
acreage in St. Joseph County." WVPE (Feb 3, 2026),
https://www.wvpe.org/wvpe-news/2026-02-03/data-center-bill-would-share-tax-money-remove-public-process
. It died in the Senate Utilities Committee (WFYI, Mar 2, 2026,
https://www.wfyi.org/news/articles/data-center-legislation-indiana-general-assembly-2026). No state
moratorium proposed; "at least 17 counties have temporary moratoriums on data centers" (Indiana
Capital Chronicle via WFIU, Jul 2026,
https://www.ipm.org/news/2026-07-23/indiana-governor-signs-trump-data-center-ratepayer-protection-pledge).

**IURC and I&M.**

- Large-load tariff, approved Feb 19, 2025; parties were the state consumer counselor, AWS,
  Microsoft, Google, the Data Center Coalition and Citizens Action Coalition. AEP (2025),
  https://www.aep.com/news/stories/view/10037/ . Terms: "Initial contracts between I&M and the load
  must be for at least 12 years."; customers may cut contracted capacity by up to 20% after five
  years, more only with an exit fee; applies at 70 MW or more. Utility Dive (2024),
  https://www.utilitydive.com/news/indiana-michigan-power-aep-amazon-google-microsoft-data-center-interconnect/733850/
  . The "80% minimum billing demand" and "exit fee above $1 billion" that Measured AI reports could
  not be confirmed in these sources.
- "I&M expects peak load in Indiana will jump to more than 7,000 MW by 2030 from 2,800 MW" (Utility
  Dive 2025,
  https://www.utilitydive.com/news/indiana-iurc-large-load-interconnection-data-center-aep-amazon-google/740452/).
- Rates: no base-rate increase in 2025-2026. On Aug 26, 2026 I&M filed for a cut: "help a
  residential customer in Indiana using 1,000 kWh a month save an estimated $100 per year",
  crediting "increased revenue from large customers including data centers." AEP (2026),
  https://aep-q.aep.com/news/stories/view/12206/ . Decision expected June 2027.
- New generation: an 870 MW gas plant in Oregon, Ohio (bought; AEP 2025,
  https://www.aep.com/news/stories/view/10588/), a 1,520 MW gas plant at Rockport (filed July 2026;
  AEP 2026, https://aep-q.aep.com/news/stories/view/12100/), a 918 MW gas acquisition [snippet], and
  an expedited plan that Citizens Action Coalition calls "a more than $7 billion blank check" with
  "at least 39% of EGR Plan costs will fall to other customers in 2030" (Earthjustice 2025,
  https://earthjustice.org/press/2025/indiana-utility-im-proposes-more-than-7-billion-generation-plan-for-amazon-and-google-ai-data-centers).
- HB 1007 (signed May 6, 2025): large-load customers must reimburse "at least 80% of the project
  costs" of generation built for them; the IURC must rule on expedited plans "within 90 days". Taft
  (2025),
  https://www.taftlaw.com/news-events/law-bulletins/indiana-enacts-new-laws-supporting-smr-manufacturing-utility-smr-development-and-new-generation-resources-to-support-large-load-economic-development/

**Water.** The state DNR investigated residential wells near the Amazon and GM sites in June 2025
and found three "consistent with historic levels."; its Division of Water "has the power to
temporarily halt dewatering". Inside Indiana Business (2025),
https://www.insideindianabusiness.com/articles/state-investigates-groundwater-issues-near-amazon-gm-projects-in-st-joseph-county
. The 24-million-gallon cap is a county agreement, not state law. Two 2026 bills to permit
datacenter water use (HB 1043, HB 1297) died without hearings (Indianapolis Star via Yahoo 2026,
https://www.yahoo.com/news/articles/crackdowns-pfas-water-air-pollution-101817915.html).

**Governor Braun.** Signed Trump's ratepayer-protection pledge July 23, 2026; "encourages locals to
evaluate whether tax abatements are necessary" but won't "tell local communities what to do." (Bond
Buyer, Sep 2026,
https://www.bondbuyer.com/news/indiana-counties-response-to-data-centers-reflects-broader-political-risk).
No moratorium, no endorsement of repeal found.

**Indiana poll.** Bellwether Research for Free Press Indiana, Oct 8-11, 2026, 839 likely voters:
"Almost 70% strongly or somewhat oppose building new data centers in Indiana, with 18% in support".
Indiana Capital Chronicle (Oct 15, 2026),
https://indianacapitalchronicle.com/2026/10/15/hoosiers-disapprove-of-trump-braun-and-data-centers
[snippet; page returned 403].

### 3.3 Net read (inference)

- **Abilene** is exposed mostly to the state, and to changes that reach existing facilities:
  sales-tax repeal with no grandfathering (SB 293), the transmission-charge rewrite due Dec 31,
  2026, the pending major air permit for 41 more turbines, and whatever Hinojosa's moratorium covers
  after Jan 19, 2027. Locally nothing has been proposed against it.
- **New Carlisle** is the reverse: the state has declined to touch Amazon (no repeal, no preemption,
  the one new law exempts existing certificates), while the county is the active front (three
  clawback requests, a rejected rezoning, a pending ban), though all of it is aimed at the next
  datacenter and not at Amazon's approved campus.

---

## 4. Not found (and what I searched)

- A poll of Abilene / Taylor County or New Carlisle / St. Joseph County residents. Searched local
  outlets plus UT, UH and Bellwether polls.
- Any lawsuit against either campus. Searched "Stargate Abilene lawsuit", "Amazon New Carlisle
  lawsuit", tracker sites.
- The outcome of Oracle's 2025 appraisal protest, and the campus's 2026 certified taxable value from
  the Taylor Central Appraisal District itself (only a tracker's reading of the roll).
- The actual abatement contracts for either site (duration and clawback clauses). Business Insider
  obtained Abilene's by records request; I could not open that article.
- Whether the Microsoft/Crusoe 900 MW campus beside Stargate has, or needs, its own abatement or
  rezoning.
- How Amazon's $12.6M first-year tax bill splits between the county, township, school district,
  library, fire territory and the TIF area.
- Current headcounts for the pre-datacenter employers in either place.
- South Bend-Mishawaka MSA population (latest).
- New Carlisle noise complaints or rent increases; Abilene noise complaints with a date.
- Abilene Reporter-News and South Bend Tribune articles specifically (pages blocked); their
  reporting is represented only where syndicated.

---

# Part: Power Sources and Other Physical Facts

## Giant datacenters: physical, engineering and environmental facts

Researched 2026-11-22. Two sites: AWS Project Rainier, New Carlisle, Indiana (Anthropic, Trainium)
and Stargate Abilene, Texas (Crusoe / Oracle / OpenAI, Nvidia).

Conventions: quotes are verbatim from the page I fetched unless marked "(search excerpt)", which
means the page itself returned 403 and I only saw the search tool's excerpt. "Single source" means I
found the number in one place only. "est." means the source itself is estimating (satellite imagery,
modelling).

Pages I could not open (403): Bloomberg and The Information originals on the Abilene outage, Data
Center Dynamics, Argus, S&P Global, Indiana Capital Chronicle, Oracle's safety blog post, R&D World.
Where a fact rests on one of those I say so.

---

### Section A. Where the power comes from

#### New Carlisle

**A1. Supplier: the grid, through Indiana Michigan Power (I&M), an AEP utility inside the PJM
market. No on-site generation except backup diesel.**

- Measured AI (Corey Trinetti, Substack), 2026-06-16,
  https://measuredai.substack.com/p/aws-new-carlisle-data-center-campus : utility is I&M within PJM;
  "all operating power comes from the grid"; on-site generation is backup diesel only. Grid draw
  2.25 GW at full build-out against about 1.96 GW IT (est.). Single source for the detailed
  breakdown.
- New York Times (Karen Weise, Cade Metz), 2025-06-24, read via reprint
  https://thenightly.com.au/business/the-new-york-times-at-amazons-biggest-data-centre-everything-is-supersized-for-ai-c-19309860
  : the facility will draw 2.2 GW, "enough to power 1 million homes."
- Backup diesel: ABC57 (Jordan Tolbert), 2026-07-10,
  https://abc57.com/news/the-real-story-backup-diesel-generators-at-aws-data-center-campuses-in-new-carlisle
  : Amazon says it submitted permit applications for 911 generators across the two New Carlisle
  campuses, "running on average, about ten hours per year". Measured AI counts 878 "critical" units
  at 2.75 MW each, about 2.4 GW of standby (single source, est.). So the diesel fleet's nameplate is
  about the size of the grid draw.

**A2. What I&M's fleet is today: nuclear and coal, with a little wind, solar and hydro.**

- I&M 2024 Indiana Integrated Resource Plan summary (filed 2025-03-28),
  https://secure.in.gov/iurc/files/IndMich_2024-IN-IRP-Summary_032825.pdf , Table 2, Indiana's share
  of capacity as of September 2024: Cook 1 nuclear 830 MW, Cook 2 nuclear 956 MW (1,786 MW
  together), Rockport 1 coal 1,079 MW, two old OVEC coal shares 62 + 61 MW, hydro about 16 MW, plus
  wind and solar contracts; total 4,974 MW including contracts not yet started.
- Same document: "I&M is forecasting electric load growth by the end of 2030 that will more than
  double I&M's peak load from its 2023 levels." And: "By the end of 2030, HSL customers are
  forecasted to represent approximately 60% of I&M's Indiana Jurisdiction peak load." (HSL =
  hyperscale load.)
- AEP news release, 2025-11-19, https://www.aep.com/news/stories/view/10588/ : Indiana peak demand
  projected to rise from about 2,800 MW in 2024 to more than 7,000 MW around 2030.
- NYT 2025 (reprint above): Amazon's campus accounts for about half of that growth, and AEP expects
  natural gas plants to supply about three-quarters of the additional power needed by 2030
  (paraphrase from the fetch, not a verbatim quote).
- The electrons are PJM grid power. I did not get a clean 2025 PJM generation-share table. PJM's
  capacity auction cleared mix (July 2025) was "45% natural gas, 21% nuclear, 22% coal, 4% hydro, 3%
  wind and 1% solar" (search excerpt of a PJM release; that is capacity, not energy).

**A3. New generation bought, ordered or proposed because of the load: almost all gas, 3,626 MW named
so far.**

| Resource                                                                                     | MW                          | Fuel                   | Status                                                                                    | Source                                                                                                                                        |
| -------------------------------------------------------------------------------------------- | --------------------------- | ---------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Oregon Clean Energy Center, Oregon, Ohio (existing plant, bought)                            | 870                         | gas combined cycle     | IURC approved 2025-11-19; ownership March 2026                                            | AEP 2025, https://www.aep.com/news/stories/view/10588/                                                                                        |
| Big Sandy peaker, Kenova, West Virginia (existing, bought)                                   | 318 (220 to 240 accredited) | gas combustion turbine | IURC approved 2026-09-02                                                                  | IURC order, Cause 46301 GRS-1, https://www.in.gov/iurc/files/ord_46301GRS1_090226.pdf                                                         |
| Sycamore Riverside Energy Center, Sullivan County, Indiana (new, Invenergy builds, I&M buys) | 918                         | gas combustion turbine | filed April 2026; IURC decision "by the end of 2026"; ownership "in March of 2029"        | Invenergy 2026-04-10, https://www.invenergy.com/news/invenergy-advances-918-mw-natural-gas-project-with-offtake-agreement-in-indiana          |
| Rockport Energy Center, Rockport, Indiana (new build on the coal site)                       | 1,520                       | gas combined cycle     | filed 2026-07-20; decision early 2027; "expected to be operational in the summer of 2030" | APPA 2026-07-21, https://www.publicpower.org/periodical/article/approval-sought-construction-1520-mw-natural-gas-combined-cycle-plant-indiana |
| Lawrenceburg + Montpelier capacity contracts (replace Rockport coal, not new build)          | 1,000                       | gas                    | approved earlier                                                                          | IURC staff report 2026-07-29 (below)                                                                                                          |

- The September 2026 IURC order records I&M's witness: "serving 4,200 MW of new load will require
  substantially more new generation resources on a nameplate capacity or ICAP basis" and "it is
  reasonable to assume that 7,000 – 10,000 MW of new generation ICAP capacity may be required".
  Also: "I&M currently has executed ESAs for approximately 4,200 MW of new load" (Amazon plus Google
  and others). The plan's gas need "grows to 3,600 MW (ICAP)" of combined cycle and "1,690 MW
  (ICAP)" of combustion turbines in 2030.
- The umbrella is I&M's Expedited Generation Resource plan (Cause 46301, approved by settlement
  January 2026). Earthjustice / Citizens Action Coalition, 2025-11-10,
  https://earthjustice.org/press/2025/indiana-utility-im-proposes-more-than-7-billion-generation-plan-for-amazon-and-google-ai-data-centers
  : a "more than $7 billion blank check", gas would "generate 85% of the electricity under the EGR
  Plan", and "at least 39% of EGR Plan costs will fall to other customers in 2030." Advocacy source;
  estimates.

**A4. Coal: none built, none kept open for this site. The opposite elsewhere in Indiana.**

- IURC staff report on Rockport Unit 1, 2026-07-29,
  https://secure.in.gov/iurc/files/IURC-Staff-Report_IC-8-1-8.5-13s_IM-Rockport-1.pdf : "I&M has an
  obligation to retire Unit 1 by December 31, 2028, pursuant to a Federal Consent Decree." Unit 1
  "provides 1,079 MW of nameplate capacity to serve Indiana." Staff: "absent a judicial release from
  it, staff must conclude that any retirement reasonableness recommendation other than meeting this
  legal obligation is without support." Replacement: gas capacity contracts "totaling 1,000 MW", 19
  MW wind, 48 MW solar, and "a 1,520 MW natural gas facility that it expects to be in service in
  2030."
- Elsewhere in Indiana coal retirements were delayed with data centers cited. E&E News (Benjamin
  Storrow, Hannah Northey), 2025-12-24,
  https://www.eenews.net/articles/doe-orders-2-indiana-coal-plants-to-continue-operating/ : the
  Department of Energy ordered NIPSCO's 800 MW R.M. Schahfer plant and a 14 MW CenterPoint unit at
  F.B. Culley to keep running past their end-of-December-2025 retirement; the Energy Secretary tied
  it to rising consumption from data center construction; a NIPSCO executive said the company plans
  2,600 MW of gas on the Schahfer site to serve Amazon data centers (those are Amazon's other
  northern Indiana campuses in NIPSCO territory, not New Carlisle). Indiana Capital Chronicle,
  2026-09-21,
  https://indianacapitalchronicle.com/2026/09/21/indiana-coal-retirements-delayed-again-as-utilities-seek-to-recover-costs/
  : orders renewed, "three coal units to remain available through Dec. 18, nearly a year beyond
  their planned retirement" (search excerpt; page 403).

**A5. Renewables and nuclear: the "100% renewable" figure is accounting, not delivery.**

- Amazon, 2025-06-24 (updated 2025-10-29),
  https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster/ :
  electricity for Amazon's operations was matched with 100% renewable energy in 2023 and 2024. This
  is annual matching across the company (contracts with wind and solar farms elsewhere plus
  certificates), not hourly supply to the site. A search excerpt of Amazon's own wording: the goal
  was met by "matching 100% of the electricity consumed across its global operations" including
  through renewable energy certificates.
- AWS Indiana fact sheet (PDF dated 2026-06-22),
  https://sustainability.aboutamazon.com/aws-sustainability-fact-sheets/aws-fact-sheet-indiana.pdf :
  Amazon has "invested in over 700 carbon-free energy projects in 28 countries". Nothing in it ties
  a specific wind or solar farm to New Carlisle.
- I&M's own plan (IRP summary above): relicense Cook nuclear "from 2034 and 2037 to 2054 and 2057";
  "SMRs were included in the Preferred Portfolio in 2036 and 2037, reflecting a total 600 MW of
  nameplate capacity" at Rockport; "wind and solar resources provide approximately 25% of the energy
  generated from 2034 to 2044 and nuclear resources provide approximately 28%". Wind/solar contracts
  on I&M's books total a few hundred MW (Table 2).

#### Abilene

**A6. Supplier: the Texas grid (ERCOT), through a 1.2 GW interconnection arranged by the landowner
Lancium on AEP transmission, plus Crusoe's own gas plant.**

- Crusoe, 2025-03-18,
  https://www.crusoe.ai/resources/newsroom/crusoe-expands-ai-data-center-campus-in-abilene-to-1-2-gigawatts
  : Lancium's plan includes a "1.2 GW grid interconnection" and "large-scale behind-the-meter
  battery storage and solar resources"; the data center will "feature natural gas turbines to power
  its back-up power supply."
- Mortenson (the substation contractor), project page read 2026-11,
  https://mortenson.com/projects/abilene-data-center-development : a 200 MW, 138 kV substation
  started May 2022 and expanded 2024; then "Constructed a 12.5-acre, 1 GW, 345 kV greenfield
  substation beginning of Q2 2025." "Achieved first transformer energization by December 19, 2025,
  only nine months after construction start." Fully energized March 10, 2026 using three temporary
  transformers because of procurement delays; swaps to permanent units expected by October 2026.
  Utility named: AEP.
- Grid Status (Tim Ennis, Connor Waldoch), 2026-03-11,
  https://blog.gridstatus.io/hype-or-hyperscale/ : the site is "located in ERCOT's West weather load
  zone", ties into the Mulberry Creek 345 kV network, and will "utilize both power from the ERCOT
  grid and on-site gas generation." Their model has on-site generation meeting about a quarter of
  demand (est.).
- Epoch AI (Elliot Stewart, Ben Cottier), 2026-04-17,
  https://epoch.ai/blog/openai-stargate-where-the-us-sites-stand : "Power is currently supplied by a
  mix of on-site natural gas and grid power".

**A7. On-site generation actually built: a 360 MW simple-cycle gas plant and 62 diesel generators.**

- Floodlight (Evan Simon), 2026-07-09, co-published with WIRED and the Texas Tribune,
  https://floodlightnews.org/ai-data-centers-texas-pollution-loophole/ : "Stargate's fleet of 10
  turbines and 62 backup diesel generators" may emit more than 1.6 million tons of greenhouse gases
  and about 1,000 tons of other pollutants a year under its permits. Crusoe "told Floodlight that
  the turbines will only be used for backup power." Thermal imagery showed one turbine running in
  late March 2026. No run-hour or measured-emissions data exists publicly.
- Why it was built: ENR (Bruce Buckley), 2025-08-04,
  https://www.enr.com/articles/61133-project-team-pushes-limits-on-abilene-data-center-job :
  "Although there was a 200-MW substation in the area, it would not be enough." A 340 MW gas turbine
  plant was added to scope, with turbines being procured within weeks. (ENR says 340 MW; the permit
  and Floodlight say 360 MW; Grid Status computes about 368 MW from ten LM2500XPRESS at 36.8 MW
  each.)
- Turbine models: GE Vernova LM2500XPRESS aeroderivatives; Business Insider (2025) reported a 360.5
  MW plant split between GE Vernova and Solar Turbines (via Glenn Lockwood's notes,
  https://www.glennklockwood.com/garden/Stargate ). Sources disagree on whether all ten are GE.
- Backup diesel: Infrastructure Research (Yair Titelboim, Substack), 2026-05-27,
  https://infrastructureresearch.substack.com/p/the-shadow-grid-is-real-and-its-filed : the
  operating permit lists "62 emergency backup generators" and "170 MW of total backup capacity."
  Single source for the 170 MW.
- Crusoe's own framing (blog dated 2025-08-05,
  https://www.crusoe.ai/blog/an-inside-look-at-the-abilene-ai-data-center ): "The Abilene data
  center connects directly to the ERCOT grid"; the turbines produce "90% lower emissions than
  traditional gas or diesel powered reciprocating engines"; eventually backup, replacing diesel
  generators.

**A8. More gas ordered and permitted.**

- Distilled (Michael Thomas, using Cleanview data), 2026-06-17,
  https://www.distilled.earth/p/openais-stargate-data-centers-are : Crusoe ordered 10 GE Vernova
  turbines in December 2024 and 19 more in June 2025, together over 1 GW; the 360 MW permit was
  approved six days after filing; aeroderivatives were chosen because combined-cycle lead times had
  reached as long as seven years. Not all 29 are confirmed for Abilene.
- Floodlight 2026: the year after the minor permits, the developers "filed their first major air
  permit—for 41 more turbines and 18 more generators." "If approved, the expansion would make
  Stargate one of the largest fossil fuel power plants in the state — capable of powering more than
  1 million homes and emitting more annual greenhouse gases than nearly 2 million cars." It would be
  "a gas plant that could power every home in Abilene more than 20 times over" (that phrase refers
  to the full build-out, not the existing 360 MW).
- TCEQ plain-language summary, application 182126 (PDF created 2025-11-19),
  https://www.tceq.texas.gov/downloads/permitting/air/bilingual/pending-permit-notices/182126-pls-english.pdf
  : Crusoe Energy Systems, "Longhorn Data Center", "additional power generation equipment for onsite
  consumption in data center buildings". Proposed tons per year: NOx 760.33, CO 870.07, VOC 815.59,
  PM10 451.10, PM2.5 313.20, SO2 233.90, HAPs 49.77. I did not confirm whether it has been issued.
  This expansion is tied to the buildings OpenAI dropped and Microsoft took over.
- Efficiency: IEEE Spectrum (Matthew S. Smith), 2026-03-24,
  https://spectrum.ieee.org/5gw-data-center : combined-cycle plants exceed 60% efficiency against
  about 40% for simple-cycle turbines; both Abilene and xAI's Colossus 2 use simple-cycle.

**A9. The fuel mix on the grid, and what "renewable" means here.**

- EIA, 2025-10-24, https://www.eia.gov/todayinenergy/detail.php?id=66464 : in January to September
  2025 gas averaged 43% of ERCOT generation and "wind and solar generation met 36% of ERCOT's
  electricity demand"; wind 87 TWh, solar 45 TWh; demand up 5%.
- FactSet (Matthew Hoza), 2025-02-25,
  https://insight.factset.com/ercot-curtailments-persist-as-load-rises : in 2024 the West zone had
  "3.1 TWh of wind and 2.2 TWh of solar generation curtailed" because "wind and solar facilities
  frequently outstrip the available transmission capacity to the rest of ERCOT."
- Crusoe's claim is locational: the site can "primarily draw from the region's robust and growing
  supply of renewable energy" (Oracle fact sheet, 2025-09-23,
  https://arrington.house.gov/UploadedFiles/FINAL_Oracle_OAI_Data_Center_Fact_Sheet_092225b.pdf ). I
  found no named wind or solar power purchase agreement and no renewable-certificate claim for the
  campus. Being a flat 24/7 load in a wind-curtailed zone does soak up some otherwise-wasted wind,
  but when the wind is low the marginal supply is gas (grid or on-site).
- Batteries and solar: Grid Status 2026: Lancium's May 2025 presentation showed a planned 1000 MW /
  4000 MWh battery south of the last two buildings. Not confirmed built; Epoch's satellite notes
  mention no battery. The Microsoft expansion next door is described as having on-site power and a
  battery system (search excerpt, Converge Digest).
- No coal or nuclear tied to the site. ERCOT's coal share fell from 19% to 13% over 2021 to 2025
  (search excerpt of a later EIA note).

---

### Section B. Other physical, engineering and environmental facts, ranked

**B1. Abilene went dark for days in its first winter.** Winter weather disrupted liquid-cooling
equipment and "took several buildings offline" in "a multi-day winter weather outage." Reported by
Bloomberg on 2026-03-06 alongside the news that Oracle and OpenAI dropped a 600 MW expansion; Oracle
called the coverage "false and incorrect."

- Tom's Hardware (Luke James), 2026-03-10,
  https://www.tomshardware.com/tech-industry/oracle-and-openai-scrap-planned-600mw-abilene-expansion
  (secondary; Bloomberg original is paywalled).
- Distilled 2026 (URL above), citing The Information: the site went offline for days at a time over
  power and cooling equipment problems; an OpenAI engineer said Crusoe's "fail and iterate" strategy
  "has definitely not been cheap."
- The specific mechanism (glycol concentration, ice in external pipes) appears only in low-quality
  aggregator sites. Do not use. Date within the winter is not given anywhere reliable ("early 2026"
  per Measured AI).

**B2. The Indiana site is a drained marsh, and keeping the foundations dry takes more water than a
city uses.**

- NYT 2025 (reprint URL above): one permit application sought to "pump 2.2 million gallons an hour,
  for 730 days." The site "was an empty cornfield" a year earlier.
- WVPE (Jeff Parrott), 2026-03-03,
  https://www.wvpe.org/wvpe-news/2026-03-03/farmers-worry-amazons-next-site-dewatering-will-flood-ditch
  : for the next phase Amazon asked to "pump 35 million gallons of water a day from the aquifer for
  546 days", discharged to the Niespodziany Ditch and on to the Kankakee River. A farmer: "The
  Niespodziany is not made to handle 35 million." "The board decided to indefinitely table the
  request." Measured AI says a trimmed renewal (1.3 million gallons an hour) was approved in May
  2026 (single source; I could not confirm).
- For scale: Abilene's entire city uses an "average daily use of 22 million gallons" (Texas Tribune,
  Alejandra Martinez, 2025-09-25,
  https://www.texastribune.org/2025/09/25/texas-data-center-water-use/ ). The comparison is mine.
- Hoosier Environmental Council, 2026-08-05,
  https://www.hecweb.org/2026/08/05/amazons-data-center-on-grand-kankakee-marsh/ (advocacy): the
  Grand Kankakee Marsh "once encompassed over 500,000 acres", "the largest wetland in the contiguous
  United States at its prime", nicknamed the "Everglades of the North". Part of the third-campus
  land is "currently used to cultivate mint (a wetland plant)."
- The county rerouted more than a mile of the Niespodziany Ditch, nearly 12,000 cubic yards of fill,
  nearly $1 million, to make room (Hometown News Now, 2025-12-22,
  https://hometownnewsnow.com/local-news/895519/ditch-realignment-for-amazon-project-nears-completion
  ).
- Wells: the state investigated dry residential wells near the site; for three wells near Hudson
  Lake it found levels "consistent with historic levels"; three more east of town were under formal
  investigation (Inside INdiana Business / IBJ, Marek Mazurek, 2025-06-06,
  https://www.insideindianabusiness.com/articles/state-investigates-groundwater-issues-near-amazon-gm-projects-in-st-joseph-county
  ). County official: "They've had smaller projects where they haven't had water to this level."
  Outcome of the investigation not found.

**B3. The two sites made opposite cooling choices, and neither drinks much.**

- Abilene: sealed water loop, heat dumped to air. Crusoe blog (2025): "The initial fill for the
  closed-loop system in each of the eight buildings requires one million gallons of water"; eight
  million gallons is about a year's use for a 200,000 square foot office building; the design is
  "typically not deployed at this scale due to increased lifecycle and maintenance costs." Texas
  Tribune 2025 confirms the 8 million gallons from the city water utility, whose official said: "We
  may be the white elephant of all the other AI centers out there."
- Annual top-up is disputed between two company documents: Oracle's fact sheet (2025-09-23) says
  "approximately 12,625 gallons per building per year"; Crusoe's blog as fetched in November 2026
  says "approximately 50,000 gallons per building per year." A household uses about 100,000.
- Epoch AI, page updated 2026-11-01,
  https://epoch.ai/data/ai-data-centers/directory/openai-stargate-abilene : 640 Airedale OptiChill
  air-cooled chillers, 1,125.4 MW of cooling capacity (est. from imagery).
- New Carlisle: outside air. Amazon 2025: "From October to March the data centers won't use any
  water for cooling at all"; April to September, a few hours a day. NYT 2025: air comes through
  "handlers the size of cargo containers." Epoch: the site "forgoes external cooling infrastructure
  in favor of direct air-based cooling."
- AWS Indiana fact sheet 2026: "In 2025, AWS withdrew 24,229,979 gallons (91,720,448 liters) of
  water in Indiana." That is all AWS sites in the state for the year, about one day of Abilene's
  city use.
- The site-level figure is secret: the projects "have their water usage protected under a
  nondisclosure agreement" (TheStatehouseFile / Indiana Citizen, Arianna Hunt, 2026-07-10,
  https://indianacitizen.org/uncertain-future-new-carlisle-offer-lessons-to-other-communities-as-data-centers-arrive/
  ). Measured AI: Phase 1's discharge permit allows "up to 1.58 million gallons per day" (single
  source).

**B4. Same order of megawatts per square foot, but a four-to-five-fold difference per rack.**

- Abilene (ENR 2025): each "474,000-sq-ft, single-story building" has four 106,000 sq ft data halls;
  each hall holds 500 racks and up to 25 MW, so 100 MW a building; each building takes up to 50,000
  Nvidia GB200s. An Nvidia GB200 NVL72 rack draws about 120 kW and weighs up to 1,553 kg (IEEE
  Spectrum 2026). Liquid cooled to the chip.
- New Carlisle (Measured AI 2026, single source): phase 1 buildings about 216,000 sq ft, "about 65
  MW apiece"; each Trainium2 rack "roughly 27 kW", two 16-chip servers per rack, air cooled. 32
  buildings at full build-out, about 6.5 million sq ft. Epoch's independent estimate is 398 MW IT
  for the first seven buildings, about 57 MW each.
- Why: NYT 2025, Amazon's Gadi Hutt: "why choose to make a lot of exotic engineering choices that
  will just slow us down and cause delays?" Amazon is "packing twice as many of these simpler chips
  into each data centre." An AWS executive has said Trainium2 does not need liquid cooling but
  Trainium3 will (search excerpt); Measured AI says the third campus adds direct-to-chip liquid
  cooling and two-story buildings.
- My arithmetic, not a sourced claim: 100 MW / 474,000 sq ft is about 210 W per sq ft at Abilene; 57
  to 65 MW / 216,000 sq ft is about 260 to 300 W per sq ft at New Carlisle. The low-density racks
  are packed into less ancillary space, so floor-area density comes out similar.

**B5. Construction speed.**

- Abilene, ENR 2025: "Each building was enclosed in less than eight weeks." "Each hall takes the
  team roughly 10 months from start to energizing." Only four panel types; 672 prefabricated wall
  panels per building; steel on site within three months. A potential 154-day delay from an
  equipment swap was cut to 28 days. Six months in, the job grew from two buildings to eight. 2,785
  workers on site in July 2025; Oracle's fact sheet later said "more than 6,400 construction workers
  on site every day."
- Crusoe (2025-09-30,
  https://crusoe.ai/resources/newsroom/crusoe-announces-flagship-abilene-data-center-is-live ):
  "Construction of the multi-building campus began in June 2024." "Within a year, the first two
  buildings were energized".
- IEEE Spectrum 2026: Crusoe reports delivering in "about 12 months" against 30 to 36 months before.
- It slipped later. Epoch timeline: buildings 3 and 4 were due March 2026 and were estimated
  operational late May; Oracle said on 2026-09-10 "6 of the 8 campus buildings, representing 618
  megawatts and 75% of total capacity have now been delivered"; buildings 7 and 8 est.
  November 2026.
- New Carlisle: land clearing February 2024; seven buildings by June 2025 (NYT; Epoch); 16 buildings
  and 910 MW IT by March 2026, 18 buildings and 1,037 MW IT by October 2026 (Epoch, est.,
  https://epoch.ai/data/data-centers/satellite-explorer/AnthropicAmazonProjectRainierNewCarlisleIndiana
  ). Distilled 2026: it passed 1 GW in March 2026 and grid power, not turbines, delivered the first
  gigawatt-scale data center.
- Bottlenecks: transformers (Abilene's 1 GW substation ran on three temporary ones, Mortenson);
  turbines (GE Vernova "is taking reservations for 2031 deliveries now", Utility Dive, Brian
  Martucci, 2026-07-23,
  https://www.utilitydive.com/news/ge-vernova-gas-turbine-backlog-climbs-to-116-gw/826039/ ;
  aeroderivatives cost about $1,800/kW against $950/kW for big combined-cycle, analyst est. in the
  same article).

**B6. Abilene's power plant was permitted like a dry cleaner.** Floodlight 2026: the first ten
turbines and 62 generators were authorized through minor permits, "the kind more commonly associated
with dry cleaners and autobody shops", yet may emit more than 1.6 million tons of greenhouse gases a
year. A former EPA enforcement chief: "All of this should have been rolled into one permit." The
plant is about 500 yards from one resident's house; she says of the night lighting: "The lights are
insane. It's as if we're in a stadium," Details of the pending major permit are in A8.

**B7. Nine hundred diesel engines in a field.** ABC57 2026: Amazon confirmed permit applications for
911 backup generators across the two New Carlisle campuses. WVPE (Jeff Parrott), 2026-06-16,
https://www.wvpe.org/wvpe-news/2026-06-16/amazon-data-center-violates-air-permits-in-multiple-ways :
the state found Amazon installed two generators rated 1,600 kW when it "had only been approved to
install 1,500-kilowatt generators", skipped a required affidavit, and had exhaust temperature
sensors fail on four dates; no legal action. (Generator size differs between sources: 1,500 to 1,600
kW here, 2.75 MW for the "critical" units in Measured AI. Probably two classes of unit.)

**B8. Injuries, one death under investigation, and a fire.**

- TIME (Andrew R. Chow), 2026-06-25,
  https://time.com/article/2026/06/24/ai-data-center-stargate-abilene-texas-injuries/ : OSHA records
  show three leg-fracture incidents at Abilene in 2025 (a worker pinned under a mini excavator on
  May 23; three glass panels weighing 1,400 pounds falling on a leg about a week later; a ladder
  incident July 28). 911 was called from the first site 14 times since December 2024. On October 1,
  2025 a 61-year-old worker was found dead in a portable toilet; police said a "medical event was
  suspected"; OSHA said it was "not aware" of the fatality. Workers described July heat near 110°F
  and 60-hour weeks. Oracle says 8,000 people have worked 20 million hours with incident rates
  "approximately 2.5x lower than industry norms" and declined to share the data.
- New Carlisle: a fire on 2025-04-24 (date inferred) filled a building with smoke; two workers "had
  to be airlifted from the scene" (Baxtel, 2025-04-26,
  https://baxtel.com/news/fire-at-aws-construction-site-in-indiana-leaves-two-hospitalized , citing
  WNDU). No worker deaths found at New Carlisle.

**B9. An unpermitted wetland fill and a stop-work order in Indiana.** WVPE (Michael Gallenberger),
2025-08-14,
https://www.wvpe.org/wvpe-news/2025-08-14/amazon-looking-to-resubmit-idem-application-after-contractors-unauthorized-wetland-impact
: contractor Walbridge impacted "almost an acre of emergent wetland north of the project location
without Amazon's knowledge"; the state "ordered it to stop working in state-regulated water." Amazon
had wanted to fill almost 10 acres; NYT 2025 quotes Amazon calling it "a small, shallow wetland, not
a major nature preserve." HEC 2026: the refiled permits cover permanent loss of 4.51 acres of
wetland and 3,986 feet of streams on a third campus of nearly 820 acres; "A decision has yet to be
issued on the permits" (August 2026).

**B10. The Abilene site was laid out for Bitcoin.** Lancium announced it in 2021 as a data center
and Bitcoin campus on about 800 acres of former ranchland around Spinks Road and Summerhill Road
(search excerpts: Commercial Search, "The property initially was set to be a bitcoin farm"; AOL /
Abilene Reporter-News, "an 800-acre tract of former ranchland"; Lancium 2021 release at
https://developabilene.com/wp-content/uploads/2021_12_Project_Artemis_Press_Release_Final.pdf ). The
200 MW substation that let Crusoe start fast in 2024 was built in 2022 for that plan (Mortenson). I
did not fetch these pages directly. No archaeology or wildlife findings turned up for Abilene.

**B11. Electricity prices: the Indiana utility has filed to cut rates and credits data centers.**
WVPE (Jeff Parrott), 2026-08-26,
https://www.wvpe.org/wvpe-news/2026-08-26/i-m-announces-electric-rate-cut-plan-enabled-by-data-centers
: I&M filed for a $79 million a year reduction, about $100 a year for a typical household, plus a
three-year freeze, "made possible by increased revenue paid by large customers including data
centers." Decision expected by June 2027. The counterweight is the advocates' estimate in A3 that
39% of new-generation costs fall on other customers by 2030. Under the 2024 large-load settlement,
big customers sign contracts of at least 12 years and "monthly billing demand can't go under 80% of
the large load customer's contract capacity" (Indiana Capital Chronicle via Route Fifty, 2024-11-27,
https://www.route-fifty.com/digital-government/2024/11/ratepayer-advocates-hail-landmark-settlement-data-centers-utility-company/401342/
). I found nothing solid on price effects around Abilene.

**B12. Scale comparisons that check out.**

- Abilene: "eight buildings on 1,100 acres, with up to approximately 4 million square feet" (Oracle
  fact sheet 2025). Central Park is 843 acres, so the site is 1.3 Central Parks; the floor area is
  about 92 acres (my arithmetic).
- New Carlisle: about 1,200 acres (NYT); about 882 acres mapped and 6.5 million sq ft at 32
  buildings (Measured AI, single source). Each early building is "larger than a football stadium"
  (NYT).
- One customer versus a utility: New Carlisle's 2.2 GW against I&M's whole Indiana peak of about
  2,800 MW in 2024.
- Abilene's proposed full gas build-out "could power every home in Abilene more than 20 times over"
  (Floodlight 2026).
- NYT: the Indiana complex will hold "hundreds of thousands of miles of fibre" (paraphrase in my
  fetch).

**B13. What comes next.**

- New Carlisle: 32 buildings and 1,925 MW of IT power by March 2028, with Trainium3 (Epoch, est.).
  The 14 new buildings include six two-story ones and liquid cooling (Measured AI).
- Abilene: OpenAI and Oracle dropped the expansion; Microsoft took it. Two buildings of 336 MW IT
  each, due September and November 2027 (Epoch,
  https://epoch.ai/data/ai-data-centers/directory/crusoe-abilene-expansion , est.). Each is more
  than three times an OpenAI building.
- Stargate elsewhere: "Together, the seven sites add up to over 9 GW of planned capacity" (Epoch,
  2026-04-17). Shackelford County, Texas ordered more than 670 reciprocating engines for 2.58 GW
  (Distilled 2026). Doña Ana County, New Mexico: 2.2 GW (Epoch) to 4.5 GW (Measured AI), on gas
  microgrids.
- Meta Hyperion, Louisiana: 5 GW, 11 buildings, a site "about a quarter the area of Manhattan";
  three new gas plants that "will generate a combined 2.26 GW" (IEEE Spectrum 2026).
- Anthropic and Amazon: "up to 5 gigawatts (GW) of capacity" and "nearly 1GW total of Trainium2 and
  Trainium3 capacity coming online by the end of 2026" (Anthropic, 2026-04-20,
  https://www.anthropic.com/news/anthropic-amazon-compute ).

---

### Things I looked for and did not find

- Any worker death at New Carlisle, or an OSHA-recorded fatality at Abilene.
- Archaeological or wildlife findings at either site (beyond the wetland material).
- Named wind, solar or nuclear contracts tied to either campus.
- Whether Abilene's battery and solar were built.
- Measured run hours or emissions for Abilene's turbines.
- A reliable account of what physically failed in the Abilene winter outage.
- Electricity price effects near Abilene; steel or concrete tonnage for either site.

### Discrepancies worth knowing

- Abilene annual cooling water per building: 12,625 gallons (Oracle 2025) vs about 50,000 (Crusoe
  blog as of November 2026).
- Abilene gas plant: 340 MW (ENR), 360 MW (permit, Floodlight), 360.5 MW (Business Insider), about
  368 MW (Grid Status arithmetic).
- Abilene acreage: 1,100 (Oracle), 825 (Infrastructure Research), 800 (2021 plan).
- New Carlisle generator count: 911 (Amazon via ABC57), 878 (Measured AI).
- New Carlisle dewatering: 2.2 million gallons an hour for 730 days (NYT, earlier permit) vs 35
  million gallons a day for 546 days (WVPE, 2026 request). Different applications.
- New Carlisle buildings: "around 30" (NYT 2025) vs 32 (Epoch, Measured AI 2026).

---

# Part: Money, Strategy, History, Security

## Giant datacenters: money, strategy, history, security

Research date: 2026-11-22. Scope: New Carlisle, Indiana (AWS Project Rainier, Anthropic) and
Abilene, Texas (Crusoe / Oracle / OpenAI Stargate). Basic stats, town politics, cost breakdown and
the physical/engineering side are other researchers' lanes and are left out except where a number is
needed for a comparison.

Conventions: "H100e" = H100-equivalents. "est." = an outside estimate (mostly Epoch AI, from
satellite imagery and filings). "reported" = anonymous-source journalism. "derived" = my arithmetic
on someone else's numbers. Quotes are verbatim; quotes from pages I could only read through a
summarizing fetch are kept short.

Things I could not read directly: Anthropic's S-1 on EDGAR (SEC blocks undeclared automated clients;
the file is over 10 MB), the Bloomberg Businessweek Abilene feature, The Information's originals,
the FT original, the NYT New Carlisle piece. Those are cited through the secondary source named in
each entry.

---

### Ranked facts

#### 1. Aschenbrenner's trillion-dollar cluster is his ~2030 row. His ~2026 row is what got built, and he hit all three columns

The forecast table in "IIIa. Racing to the Trillion-Dollar Cluster" (June 2024), copied from the
page:

| Year  | OOMs           | H100s-equivalent | Cost              | Power  | Power reference class                      |
| ----- | -------------- | ---------------- | ----------------- | ------ | ------------------------------------------ |
| 2022  | ~GPT-4 cluster | ~10k             | ~$500M            | ~10 MW | ~10,000 average homes                      |
| ~2024 | +1 OOM         | ~100k            | $billions         | ~100MW | ~100,000 homes                             |
| ~2026 | +2 OOMs        | ~1M              | $10s of billions  | ~1 GW  | The Hoover Dam, or a large nuclear reactor |
| ~2028 | +3 OOMs        | ~10M             | $100s of billions | ~10 GW | A small/medium US state                    |
| ~2030 | +4 OOMs        | ~100M            | $1T+              | ~100GW | >20% of US electricity production          |

Caption: "Scaling the largest training clusters, rough back-of-the-envelope calculations."

Key passages, verbatim:

- "By the end of the decade, we are headed to $1T+ individual training clusters, requiring power
  equivalent to >20% of US electricity production. Trillions of dollars of capex will churn out 100s
  of millions of GPUs per year overall."
- "The trillion-dollar cluster—+4 OOMs from the GPT-4 cluster, the ~2030 training cluster on the
  current trend—will be a truly extraordinary effort. The 100GW of power it'll require is equivalent
  to >20% of US electricity production; imagine not just a simple warehouse with GPUs, but hundreds
  of power plants. Perhaps it will take a national consortium."
- "We're on the path to individual training clusters costing $100s of billions by 2028—clusters
  requiring power equivalent to a small/medium US state and more expensive than the International
  Space Station."
- The hedge most people forget: "(Note that I think it's pretty likely we'll only need a ~$100B
  cluster, or less, for AGI. The $1T cluster might be what we'll train and run superintelligence on,
  or what we'll use for AGI if AGI is harder than expected.)"
- "'Where do I find 10GW?' (power for the $100B+, trend 2028 cluster) is a favorite topic of
  conversation in SF."
- Method: "The OpenAI GPT-4 tech report stated that GPT-4 finished training in August 2022.
  Thereafter we play forward the rough ~0.5 OOMs/year trend."

So the answer to the post's "in 202x" blank is **~2030, ~100 GW, $1T+, ~100M H100-equivalents**.

Reality against the ~2026 row (Epoch AI estimates, pages updated Oct 19 and Nov 1, 2026):

| Site         | IT power | Compute      | Capital cost | Forecast row (~2026)         |
| ------------ | -------- | ------------ | ------------ | ---------------------------- |
| New Carlisle | 1,037 MW | 818k H100e   | $39.3B       | ~1 GW, ~1M, $10s of billions |
| Abilene      | 824 MW   | 1,019k H100e | $31.2B       | ~1 GW, ~1M, $10s of billions |

Caveats: all six numbers are Epoch estimates. Abilene's last two buildings are counted as
operational on a projection (Oracle confirmed six of eight, 618 MW, on Sept 10, 2026, and said
"nearly complete" on Nov 20). Aschenbrenner's table is for a single training cluster; neither site
is necessarily one training run (Epoch: "A whole data center is not necessarily devoted to a single
AI training run").

His second table, total AI investment: ~$150B in 2024, ~$500B in ~2026, ~$2T in ~2028, ~$8T in
~2030. For 2026 The Register (2026) cites eight hyperscalers expected to spend a collective $710
billion; Amazon alone guided to about $220B.

- Source: https://situational-awareness.ai/racing-to-the-trillion-dollar-cluster/ (Leopold
  Aschenbrenner, Situational Awareness, 2024). Primary, read directly.
- Source: https://epoch.ai/data/ai-data-centers/directory/anthropic-amazon-new-carlisle and
  https://epoch.ai/data/ai-data-centers/directory/openai-stargate-abilene (Epoch AI, 2026).
  Estimates.

#### 2. Abilene was a bitcoin site, then Musk's site, then Altman's. Musk's replacement cluster is now rented to Anthropic

- 2021–22: the city annexed land for Lancium's "Clean Campus", pitched for bitcoin mining and
  flexible load. Fortune (2026): the site "was originally planned as a cryptocurrency mining
  facility". CNBC (2024), on the Lancium-Crusoe deal of July 18, 2024: Lancium president Ali Fenn
  said "Lancium's original vision was to bring large-scale loads to locations with the best,
  abundant renewable energy". Crusoe itself started as a company mining bitcoin on flared gas.
- Mid-2024, reported (The Information, Jan 2025, by Aaron Holmes, Anissa Gardizy and Amir Efrati,
  quoted in Spyglass): "Musk had previously talked to Oracle and a small data center developer,
  Crusoe, about designing a site in Abilene, Texas, for xAI, code-named Project Ludicrous, a
  reference from the film 'Space Balls.'" Then: "After Musk suddenly opted to build his own data
  center instead of working with Oracle, Altman pounced" and "Starting in June, Oracle began working
  with Crusoe on developing the site for OpenAI instead." Single outlet, anonymous sources ("three
  people who worked on the deal"). One other note-taker (Glenn Lockwood) describes Project Ludicrous
  as the Crusoe/Oracle build generally, so the code name's exact referent is unsettled.
- July 2024, on the record: Musk posted that xAI was building its 100k H100 system itself "for
  fastest time to completion"; The Information reported the Oracle expansion talks (reported $10B)
  ended because Oracle could not meet his timeline. That system became Colossus in Memphis.
- At the time, Oracle's Abilene capacity was routed to OpenAI through Microsoft: DCD, citing The
  Information (2024), says Oracle's Crusoe deal was "part of its deal to rent 100,000 advanced GPUs
  to Microsoft for OpenAI's use". NYT (Feb 2025, via Spyglass): after the Nov 2023 board crisis "Mr.
  Nadella was spooked and decided not to put in the money for Stargate."
- Jan 21–22, 2025: hours after the White House Stargate announcement Musk posted "They don't
  actually have the money" and "SoftBank has well under $10B secured. I have that on good
  authority." Altman: "Wrong, as you surely know," with an invitation to visit Abilene.
- May 6, 2026: SpaceX (which absorbed xAI) rented all of Colossus 1 to Anthropic: "Colossus 1
  features over 220,000 NVIDIA GPUs". Reported capacity over 300 MW. Reported reason Musk was fine
  with it: training had moved to Colossus 2 (Tom's Hardware, 2026).

Sources:

- https://spyglass.org/from-space-balls-to-stargate/ (Spyglass quoting The Information, 2025).
  Reported, single source.
- https://fortune.com/2026/03/27/microsoft-texas-data-center-open-ai-former-partner-cloud-provider/
  (Fortune / AP, 2026)
- https://www.nbcnews.com/tech/tech-news/bye-bye-bitcoin-hello-ai-texas-miners-leave-crypto-new-wave-rcna162573
  (CNBC via NBC News, 2024)
- https://techcrunch.com/2025/01/22/elon-musk-and-sam-altman-take-to-social-media-to-fight-over-stargate
  (TechCrunch, 2025)
- https://x.ai/news/anthropic-compute-partnership (SpaceX/xAI, 2026). Primary.
- https://spyglass.org/the-500b-phone-call/ (Spyglass quoting NYT, 2025)

#### 3. Aschenbrenner warned against building in the Gulf. Iran then bombed AWS there and named Stargate UAE as a target; the UAE is reportedly redesigning it underground

What he wrote (2024): "Do we really want the infrastructure for the Manhattan Project to be
controlled by some capricious Middle Eastern dictatorship?" and "it risks the AGI weights getting
stolen (and perhaps be shipped to China) (more later); it risks these dictatorships physically
seizing the datacenters (to build and run AGI themselves) when the AGI race gets hot". He did not
list the risk that materialized: a third country's missiles.

What happened:

- May 2025: OpenAI, G42, Oracle, Nvidia, SoftBank and Cisco announced Stargate UAE, a 1 GW cluster
  in a planned 5 GW Abu Dhabi campus. Reuters (2026): the UAE got Nvidia chips and "in return, it
  agreed to cut AI ties with China and invest in the Stargate initiative's American data centers".
  G42 is controlled by Sheikh Tahnoun, the UAE's national security adviser.
- March 1, 2026: Iranian drones hit two AWS data centers in the UAE and damaged a third in Bahrain.
  Iran's Fars agency said the Bahrain site was "deliberately targeted". TNW's characterization: "the
  first instance in recorded history of a state deliberately targeting commercial data centres"
  (their claim, not independently checked). Fortune (2026) quotes Carnegie's Sam Winter-Levy: "If
  you knock out some of the chillers you can take them fully offline."
- April 3, 2026: an IRGC video threatened Stargate UAE by name. Reuters: it showed a map of the site
  with the caption "Nothing stays hidden from our sight."
- Sept 11, 2026 (Reuters exclusive, four sources): the single 5 GW campus will likely become "a
  network of data centers spread across the UAE"; "Air defense systems are being incorporated into
  the redesign"; some facilities may go underground. Phase one is valued at $30 billion with 200 MW
  due in 2026. G42: "The project's specifics are subject to continuous review."

Sources:

- https://www.al-monitor.com/originals/2026/09/exclusive-uae-revises-ai-data-center-plan-after-iranian-attacks-sources-say
  (Reuters via Al-Monitor, 2026). Redesign is reported, anonymous sources.
- https://thenextweb.com/news/iran-threatens-stargate-openai-abu-dhabi (The Next Web, 2026)
- https://fortune.com/2026/03/09/irans-attacks-on-amazon-data-centers-in-uae-bahrain-signal-a-new-kind-of-war-as-ai-plays-an-increasingly-strategic-role-analysts-say/
  (Fortune, 2026)

No comparable incident found at the two US sites. Searches for sabotage, espionage, drones or FBI
involvement at Abilene or New Carlisle returned only: a ransomware attack on the City of Abilene
(2025, no evidence of a Stargate link), police-blotter items, and TIME's worker-safety reporting
(2026).

#### 4. Abilene's risk sits in four layers, and the thinnest balance sheet is at the bottom

1. **Buildings**: owned by a joint venture of Crusoe, Blue Owl and Primary Digital. Crusoe (2025):
   "the second phase of a $15 billion joint-venture to fund the 1.2 gigawatt AI data center in
   Abilene, Texas". (Phase one was a $3.4B JV, Oct 2024.)
2. **Construction debt**: Reuters citing FT (2025): "JPMorgan has provided a bulk of the debt
   financing across two loans totaling $9.6 billion" and the owners "have invested around $5 billion
   in cash". Bloomberg reported the two loans separately as $2.3B (Jan 2025) and $7.1B (May 2025),
   which sum to $9.4B; the $9.6B figure is the FT's.
3. **Tenant and chip owner**: Oracle. Reuters/FT (2025): "Oracle has agreed to lease the site for 15
   years" and "Oracle will spend around $40 billion on Nvidia's higher-performance chips", about
   400,000 GB200s, then "lease the computing power to OpenAI". Reported; note Epoch's whole-site
   capital cost estimate is $31.2B, lower than the FT's chips-only number, so one of them is off.
4. **End customer**: OpenAI, under a contract Reuters (Dec 2025) calls "The $300 billion OpenAI
   data-center contract", which Bernstein's Mark Moerdler said gives Oracle "unprecedented single
   customer revenue exposure". The Register (2025): OpenAI had "$1.4 trillion in commitments over
   the next eight years".

Signs of strain on Oracle: CNBC (March 2026) says Oracle is "carrying over $100 billion on its books
while free cash flow has gone negative", and that it is the only hyperscaler funding the buildout
mainly with debt. Its CDS "shot to record highs" (Reuters, Dec 2025). On Nov 20, 2026, one minute
after the close, Oracle posted: "Oracle has secured all the funding we need to fulfill our contract
with OpenAI" and "Any media reports that will come out and say the contrary are incorrect and
wrong", after a $20B raise ($10B stock, $10B debt). It targets positive free cash flow in the second
half of FY2028.

Government as lender of last resort was floated and shot down. Nov 5, 2025, OpenAI CFO Sarah Friar
at a WSJ event: "the backstop, the guarantee that allows the financing to happen"; asked if she
meant a federal backstop for chip investors: "Exactly". She retracted that evening ("I used the word
'backstop' and it muddied the point"). White House AI czar David Sacks: "There will be no federal
bailout for AI." Aschenbrenner's version (2024): "Perhaps it will take a national consortium."

Sources:

- https://www.crusoe.ai/resources/newsroom/crusoe-blue-owl-capital-and-primary-digital-infrastructure-enter-joint-venture
  (Crusoe, 2025). Primary.
- https://gvwire.com/?p=192577 (Reuters citing FT, via GV Wire, 2025). Reported.
- https://www.khaleejtimes.com/business/tech/oracles-openai-reliance-faces-scrutiny-as-debt-fuelled-ai-buildout-raises-worries
  (Reuters via Khaleej Times, 2025)
- https://www.cnbc.com/2026/03/09/oracle-is-building-yesterdays-data-centers-with-tomorrows-debt.html
  (CNBC, 2026)
- https://thenextweb.com/news/oracle-openai-contract-fully-funded-20bn-raise (The Next Web, 2026);
  https://thestar.com.my/tech/tech-news/2026/11/21/oracle-says-openai-infrastructure-deal-is-fully-funded-after-final-capital-raise
  (Reuters via The Star, 2026)
- https://www.theregister.com/2025/11/06/openai_cfo_walks_back_remarks/ (The Register, 2025)

#### 5. New Carlisle's money loop: Amazon put in about $18B, got a $110B purchase commitment back, and marks its stake at about $98B

From Anthropic's S-1 as reported by TechCrunch (Oct 27, 2026):

- Amazon invested "$8 billion in convertible notes from 2023 through 2025" plus $10 billion of
  nonvoting preferred in 2026: about $18B. The April 2026 deal allows up to $25B more in total ($5B
  immediately, up to $20B on milestones), i.e. up to $33B.
- Anthropic committed to spend "at least $110 billion on AWS over the next 10 years". Anthropic's
  own April 2026 post: "We are committing more than $100 billion over the next ten years to AWS
  technologies, securing up to 5GW of new capacity to train and run Claude."
- Amazon's own filings valued its Anthropic notes at $97.9 billion as of June 30, 2026. Its
  ownership is capped at 12% of the partially diluted share count (it can waive the cap).
- Anthropic booked a non-cash $72.4 billion charge in H1 2026 for the change in fair value of
  convertible notes and similar instruments.

What the S-1 does not say (Strauss and O'Reilly, Tech Policy Press, Nov 3, 2026): how much Anthropic
actually pays Amazon. It discloses that 44% of revenue in the first nine months of 2026 came through
the Amazon, Google and Microsoft marketplaces, booked "at the full customer price" with distribution
fees paid to the clouds, and that leases and purchase commitments total $895 billion against $4.5
billion of lease liabilities on the balance sheet. The compute contracts themselves were not filed
as exhibits.

Other S-1 figures via Dealroom summarizing The Information (Oct 26, 2026): H1 2026 revenue $16.3B;
compute spend $8.9B, up 3.8x; commitments of $110B AWS, $114.5B Google Cloud, $44.9B Microsoft,
$120.5B SpaceX (mostly cancellable on 90 days' notice). The Google figure is $121.3B in Tech Policy
Press; the two secondaries disagree.

Amazon's side: Q3 2026 AWS revenue $46B, up 39%; 2026 capex guidance about $220B;
trailing-twelve-month free cash flow negative $42.4 billion versus positive $14.7B a year earlier
(Constellation Research, Oct 29, 2026). In Q3 2025 Amazon booked a $9.5 billion pre-tax gain on
Anthropic in non-operating income, which is why Q3 2026 net income fell year on year. Unlike Oracle,
Amazon funds this from an operating business; the "risk" is on its own balance sheet.

Sources:

- https://techcrunch.com/2026/10/27/vcs-will-make-billions-on-anthropics-ipo-but-amazon-is-set-to-make-much-much-more/
  (TechCrunch, 2026)
- https://asimovaddendum.substack.com/p/anthropics-missing-s-1-disclosures (Strauss and O'Reilly,
  Tech Policy Press / Asimov's Addendum, 2026)
- https://dealroom.co/news/info-1sghj5n-anthropics-s-1-takeaways-from-giant-compute-commitments-to-complex-lock/
  (Dealroom summarizing The Information, 2026)
- https://www.anthropic.com/news/anthropic-amazon-compute (Anthropic, 2026). Primary, read directly.
- https://www.constellationr.com/insights/news/aws-q3-revenue-growth-surges-39-capex-stings-amazons-cash-flow
  (Constellation Research, 2026)
- S-1 itself:
  https://www.sec.gov/Archives/edgar/data/0002130357/000162828026067168/anthropicpbc-sx1.htm (not
  read; SEC blocked the fetch)

#### 6. Chips are written off in five or six years; Oracle's lease is fifteen; and the Abilene expansion reportedly died because Blackwell was already last year's chip

- Amazon FY2025 10-K (via Hudson Labs): it "changed our estimate of the useful lives of a subset of
  our servers and networking equipment from six years to five years", effective Jan 1, 2025, "due to
  the increased pace of technology development, particularly in the area of artificial intelligence
  and machine learning". Effect: "an increase in depreciation and amortization expense of $1.4
  billion and a reduction in net income of $1.0 billion". This reversed a 2024 change from five to
  six years that had added $2.5B to net income.
- Michael Burry (Nov 2025) estimated the big hyperscalers will understate depreciation by a
  cumulative $176 billion over 2026–2028 by using five-to-six-year lives; he argues two to three
  years is realistic. Disputed by Nvidia and CoreWeave.
- CNBC (March 2026): "Artificial intelligence chips are getting upgraded more quickly than data
  centers can be built." Nvidia moved to an annual cadence; Vera Rubin "delivers five times the
  inference performance of Blackwell". "The current Abilene site is expected to use Nvidia's
  Blackwell processors."
- March 6, 2026 (Bloomberg): Oracle and OpenAI dropped a tentative lease on "expanding the facility
  from 1.2 gigawatts to about 2.0 gigawatts", over "financing and OpenAI's changing needs". The
  Information (via CNBC) reported OpenAI wanted newer Nvidia generations at a new campus. OpenAI's
  Sachin Katti: "We considered expanding it further, but ultimately chose to put that additional
  capacity in other locations." Bloomberg also reported "Nvidia paid a $150 million deposit to
  Crusoe and began helping court Meta as a tenant for the expansion", to keep AMD out.
- March 27, 2026: Microsoft took it. Crusoe: a 900 MW campus with two buildings of 336 MW critical
  IT load each and its own 900 MW on-site power plant; "the first building expected to be energized
  in mid-2027"; "the full site is expected to reach approximately 2.1 GW of total capacity". So the
  company that reportedly declined to fund Stargate now sits next door to it.
- Satya Nadella on Dwarkesh (Nov 12, 2025), explaining why he paces builds: "I didn't want to go get
  stuck for four or five years of depreciation on one generation."
- New Carlisle faces the same turnover: Epoch models buildings 1–18 on Trainium2 and buildings 19–32
  (by est. March 2028) on Trainium3, taking the site to 1,925 MW, 1,746k H100e and $72.9B.

What the site is worth after generation one: no source gives a number. The structural answer is that
the 15-year lease, the substation and the grid/gas interconnect outlive the chips by about three
chip generations, and the lease is Oracle's obligation whether or not OpenAI still wants
Blackwell-era halls. Compare Meta's Hyperion leases, which have "an initial four-year term with
options to extend".

Sources:

- https://hudson-labs.com/research/amazon-server-depreciation-amzn (Hudson Labs quoting Amazon
  10-Ks, 2026)
- https://www.cnbc.com/2026/03/09/oracle-is-building-yesterdays-data-centers-with-tomorrows-debt.html
  (CNBC, 2026)
- https://www.insurancejournal.com/news/southcentral/2026/03/10/861213.htm (Bloomberg via Insurance
  Journal, 2026)
- https://crusoe.ai/resources/newsroom/crusoe-announces-new-900-mw-ai-factory-campus-in-abilene-texas-to-support-microsoft-ai-infrastructure
  (Crusoe, 2026). Primary.
- https://www.dwarkesh.com/p/satya-nadella-2 (Dwarkesh Podcast, 2025)
- https://www.fool.com/investing/2025/11/11/michael-burrys-latest-warning-could-be-bad-news-fo
  (Motley Fool on Burry, 2025). Burry's number is his own estimate.

#### 7. What the labs say the sites are for

- OpenAI (April 29, 2026): "Our latest and smartest model yet, GPT‑5.5, was trained at our flagship
  Stargate site in Abilene, Texas." The site "operates on Oracle Cloud Infrastructure and runs
  NVIDIA GB200 systems". In Sept 2025 it said Abilene was already running "early training and
  inference workloads".
- Oracle (Nov 20, 2026, X post as quoted by The Next Web): "Our Abilene campus, where Astra-6 was
  trained, is nearly complete." Reuters renders the model name as "GPT-6 Astra". I found no OpenAI
  statement confirming this, so treat the model name as Oracle's claim.
- Crusoe's press release describes each Abilene building as up to 50,000 GB200s "on a single
  integrated network fabric".
- Anthropic (April 20, 2026): "Together we launched Project Rainier, one of the largest compute
  clusters in the world, and we currently use over one million Trainium2 chips to train and serve
  Claude." and "We continue to choose AWS as our primary training and cloud provider for
  mission-critical workloads." The one million chips are across all of Rainier, not New Carlisle
  alone (AWS said about 500,000 Trainium2 in Indiana in Oct 2025).
- NYT (June 2025, via The Batch): "Anthropic may use all of New Carlisle's processing power to build
  a single system", attributed to co-founder Tom Brown. Seven buildings then, "up to 30 on the
  drawing board".
- AWS (Oct 2025): Rainier provides "more than five times the compute power Anthropic used to train
  its previous AI models".
- Andy Jassy, Q3 2026 call: "inference already accounts for well over half of AWS' AI revenue and
  growing."
- No named Claude model has been publicly attributed to New Carlisle. Anthropic's wording is always
  "train and serve" / "train and run". This neither confirms nor rules out the draft's guess that
  frontier pretraining happens on TPUs; the only on-record statement that cuts against it is
  "primary training ... provider".

Sources:

- https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age/ (OpenAI,
  2026). Primary.
- https://www.anthropic.com/news/anthropic-amazon-compute (Anthropic, 2026). Primary.
- https://thenextweb.com/news/oracle-openai-contract-fully-funded-20bn-raise (The Next Web, 2026)
- https://www.deeplearning.ai/the-batch/amazon-plans-to-spend-tens-of-billions-on-ai-infrastructure-with-project-rainier
  (The Batch summarizing NYT, 2025)

#### 8. Two addresses hold about 5% of the world's deployed AI compute (derived estimate)

Epoch AI, page updated Nov 18, 2026: 96 tracked AI data centers hold 15.8M H100e and 15.1 GW of IT
power, and "coverage of global deployed AI computing capacity" is 43% (90% CI 29% to 77%).

- Implied world total: about 36.7M H100e (derived; 20M to 54M across the CI).
- Abilene plus New Carlisle: 1,837k H100e, so about 5% of the world total (derived; roughly 3% to
  9%), 12% of what Epoch tracks, and 1.86 GW of the tracked 15.1 GW.
- Add Colossus 2 (1,112k H100e) and three sites hold about 8%.
- Rankings: "The largest known AI data center by IT power is Anthropic-Amazon New Carlisle" (1,037
  MW), then Colossus 2 (946 MW), then Abilene (824 MW), then Microsoft Fairwater Atlanta (636 MW).
  By compute: Colossus 2, Abilene, New Carlisle.
- For scale, Epoch compares the biggest sites to San Diego's average draw of about 800 MW.
- Lab-level concentration (Epoch, Josh You, May 2026, end-2025 figures): OpenAI had "around 10% to
  15% of the world's operational AI compute supply"; Anthropic plus OpenAI "probably made up
  15–20%"; the five frontier labs together "probably had access to less than half of global AI
  compute". "Much of Anthropic's compute is housed in Amazon's Project Rainier campus in Indiana."

Sources:

- https://epoch.ai/data/data-centers (Epoch AI, 2026). Estimates.
- https://epoch.ai/graphs/largest-ai-data-centers-by-power-capacity (Epoch AI, 2026)
- https://epoch.ai/gradient-updates/frontier-labs-dont-use-most-ai-compute (Epoch AI, 2026)

#### 9. Nothing under construction reaches his ~2028 row (10 GW in one cluster). The biggest tracked 2028 sites are about 2 GW; the biggest announcement is 8 GW by 2032 on a former uranium enrichment plant

Epoch's largest planned sites (Nov 19, 2026), projected IT power:

| Site                          | Projected IT power | Est. completion |
| ----------------------------- | ------------------ | --------------- |
| Microsoft Fairwater Wisconsin | 2,263 MW           | 2028            |
| Anthropic-Amazon New Carlisle | 1,925 MW           | 2028            |
| OpenAI Stargate New Mexico    | 1,750 MW           | 2028            |
| Meta Hyperion (Louisiana)     | 1,632 MW           | 2028            |
| Colossus 2 (Memphis)          | 1,531 MW           | 2027            |

Against the forecast's ~10 GW / ~10M H100e / $100s of billions for ~2028, single sites are running
roughly 5x short on power. New Carlisle's own 2028 projection is 1,746k H100e and $72.9B. Lab-level
totals are closer to trend: OpenAI said in April 2026 it had "already surpassed" its goal of "10GW
of AI infrastructure in the United States by 2029", and The Information (via The Decoder, 2026)
reported Anthropic had locked in at least 14.8 GW since Oct 2025 in contracts worth up to $517B.

Announced successors:

- **OpenAI PORTS-Pike, Ohio** (Aug 17, 2026): "approximately 8 gigawatts-IT" with SB Energy, Nvidia
  and the Department of Energy, on "remediated land controlled by the Department of Energy at the
  former Portsmouth Gaseous Diffusion Plant", a Cold War uranium enrichment site. "six-year buildout
  through 2032"; "The first 800 megawatts are expected to become available in 2028"; "SB Energy will
  build, own, and operate the data center under a 20-year lease to OpenAI". Circularity in one
  sentence: "NVIDIA will invest $1.5 billion in SB Energy and will provide credit support for the
  land, power, and shell buildout associated with the initial 4.25 IT-GW." No total cost given.
- **Anthropic–Amazon**: up to 5 GW, more than $100B over ten years (April 2026).
- **Anthropic–Google–Broadcom**: about 3.5 GW of TPUs from 2027 (April 2026, figure from a Broadcom
  filing per press reports).
- **Meta Hyperion**: Meta has said it scales to 5 GW; financed off Meta's balance sheet by a $27B
  joint venture, Blue Owl funds 80% and Meta 20%, with Pimco anchoring the bonds (Oct 2025).
- **Oracle/OpenAI Shackelford County, Texas**: "our next gigawatt-scale campus, is fully permitted",
  first Vera Rubin racks due within weeks (Nov 2026). Oracle and OpenAI plan 4.5 GW beyond Abilene.
- **Microsoft at Abilene**: 900 MW (see fact 6).
- Altman's stated ambition (Fortune, Sept 2025): "In several years, I think this could be something
  like a gigawatt per week", and a reported internal target of 250 GW by 2033.

Sources:

- https://epoch.ai/graphs/largest-ai-data-centers-by-power-capacity (Epoch AI, 2026). Estimates.
- https://openai.com/index/openai-joins-ports-pike-project/ (OpenAI, 2026). Primary, read directly.
- https://www.bisnow.com/news/national/data-center-capital-markets/meta-pushes-its-largest-data-center-project-off-its-books-with-27b-joint-venture-131490
  (Bisnow, 2025)
- https://the-decoder.com/anthropic-reportedly-signs-517-billion-in-compute-deals-after-dario-amodei-warned-rivals-about-reckless-risk/
  (The Decoder on The Information, 2026). Reported.
- https://finance.yahoo.com/news/met-sam-altman-texas-turning-162949844.html (Fortune via
  Yahoo, 2025)

#### 10. Aschenbrenner runs a hedge fund on this thesis, and its last widely reported 13F shows $1.07B notional of puts on Oracle

Situational Awareness LP's 13F for March 31, 2026: "a $5.52 billion U.S. equity portfolio", 29
positions. Longs: Bloom Energy $879M, Sandisk $724M, CoreWeave $556M, IREN $401M, Core Scientific
$389M, Applied Digital $320M (several are bitcoin miners turned AI landlords, the Crusoe/Lancium
path). Put notional "roughly $8.7 billion": VanEck Semiconductor ETF $2.04B, Nvidia $1.57B, Oracle
$1.07B, Broadcom $1.01B, AMD $969M.

Caveats: 13F notional overstates what the puts cost and shows no strikes or expiries; the puts may
hedge the longs. A 13F "does not capture the full portfolio, including cash, swaps, short sales, or
private holdings." A Stocktwits item claims the June 30, 2026 filing showed about $20B of reportable
holdings; single source, not verified. WSJ (via Forklog) reported a 47% net return for H1 2025.

- Source:
  https://finance.yahoo.com/markets/options/articles/situational-awareness-lp-discloses-5-155553432.html
  (Blockspace via Yahoo Finance, 2026)

#### 11. Anthropic's off-balance-sheet compute commitments: $895B disclosed, $4.5B on the balance sheet

Covered under fact 5. Standalone because the ratio is the "huh": Tech Policy Press (2026) says the
S-1 puts leases and purchase commitments at $895 billion while showing $4.5 billion in lease
liabilities, that about $214B more is cancellable or conditional, and that "The Google and Amazon
agreements require minimum payments through 2033 and 2036, respectively." New Carlisle is one
physical instance of the Amazon line.

- Source: https://asimovaddendum.substack.com/p/anthropics-missing-s-1-disclosures (Tech Policy
  Press, 2026)

#### 12. Why these two places

- Abilene: Crusoe (2025): "The availability of abundant, low-cost wind energy in Abilene factored
  heavily into site selection". Lancium's thesis was to put flexible load next to stranded West
  Texas wind in ERCOT's competitive market; a 200 MW substation existed by 2022 and a 1 GW
  substation was nearly complete in Jan 2026 (Epoch). Argus (2026) adds proximity to West Texas gas.
  In practice the first phase leaned on on-site gas turbines; Altman in Abilene (2025, via Fortune
  2026): "We're burning gas to run this data center".
- New Carlisle: a pre-assembled county megasite. The campus sits in the Indiana Enterprise Center,
  "a master-planned development in St. Joseph County that spans nearly 3,000 acres". A shell
  company, Razor5, bought more than 600 acres of farmland the year before the April 2024
  announcement. The state offered a sales-tax exemption "over a 50-year term" and the county package
  was put at about $1.9 billion of net savings (Inside Indiana Business / IBJ, 2024). Amazon's
  announced figure was $11B; Epoch's cost estimate for what is there now is $39.3B.
- I found no on-record statement from Amazon explaining why New Carlisle over other sites. Single
  aggregator claims about "transmission-line access" exist but I would not cite them.

Sources:

- https://www.crusoe.ai/resources/newsroom/crusoe-blue-owl-capital-and-primary-digital-infrastructure-enter-joint-venture
  (Crusoe, 2025)
- https://www.insideindianabusiness.com/articles/amazon-web-services-plans-11b-data-center-campus-near-south-bend
  (Inside Indiana Business, 2024)
- https://www.ibj.com/articles/amazon-web-services-to-build-11-billion-data-center-campus-near-south-bend
  (IBJ, 2024)

#### 13. Abilene's financier already backed away once elsewhere

CNBC (March 2026): "Blue Owl, an Oracle partner, is declining to fund an additional facility."
(Reported in Dec 2025 by the FT as Oracle's Michigan site.) Blue Owl is the same firm that owns most
of Abilene and 80% of Meta's Hyperion vehicle, so one alternative asset manager is the landlord of
record for a large share of frontier compute.

- Source:
  https://www.cnbc.com/2026/03/09/oracle-is-building-yesterdays-data-centers-with-tomorrows-debt.html
  (CNBC, 2026)

---

### Quotes worth having

- Aschenbrenner (2024): "Perhaps the wildest part is that willingness-to-spend doesn't even seem to
  be the binding constraint at the moment, at least for training clusters. It's finding the
  infrastructure itself"
- Aschenbrenner (2024): "The clusters that are being planned today may well be the clusters AGI and
  superintelligence are trained and run on, not just the 'cool-big-tech-product clusters.'"
- Aschenbrenner (2024): "If American business is unshackled, America can build like none other (at
  least in red states)." Both sites are in red states.
- Musk (Jan 2025): "They don't actually have the money"
- Altman (Sept 2025, Abilene): "What you saw today is just a small fraction of what this site will
  eventually be". Six months later OpenAI declined the expansion.
- Altman, internal Slack (2025, reported by Alex Heath via Fortune): "The mission is simple: create
  and deliver massive usable compute as fast as physics allows, to power us through ASI"
- CNBC headline (2026): "Oracle is building yesterday's data centers with tomorrow's debt"
- Nadella (2025): "I didn't want to go get stuck for four or five years of depreciation on one
  generation."
- David Sacks (2025): "There will be no federal bailout for AI."
- Jassy (Q3 2026): "We're installing an AI accelerator about every 14 seconds"
- The Register (2026) on Crusoe: "Bitcoin farmer turned bit barn builder"

### Open questions / things to check before publishing

- The Abilene compute and cost figures are Epoch estimates with the last two buildings projected,
  and they conflict with the FT's $40B chips-only figure.
- "Astra-6" / "GPT-6 Astra" trained at Abilene rests on an Oracle X post as relayed by Reuters and
  The Next Web.
- All Anthropic S-1 numbers here are second-hand; the two secondaries disagree on the Google
  commitment ($114.5B vs $121.3B) and on marketplace share (48% of H1 vs 44% of nine months, which
  may both be right).
- The 5% share of world compute is my division of Epoch's numbers, with Epoch's own CI spanning 29%
  to 77% coverage.
- The Musk "Project Ludicrous" story is The Information only.
- The draft's line "The cluster is ~x% of Anthropic's total compute" appears under Abilene too; that
  one should be OpenAI's.

---

# Part: Who Built and Runs Abilene

### Who built and runs Stargate Abilene (research notes, 2026-11-22)

Question from the draft: "research to what extent Abilene site is built by Oracle etc?"

**Headline answer.** Oracle built none of the campus and owns neither the land nor the buildings.
Oracle is the tenant and the computer owner: it leases all eight buildings for 15 years, buys the
Nvidia systems, installs and runs them as Oracle Cloud Infrastructure, and rents the output to
OpenAI. On the capital, Oracle's hardware is roughly 60% to 75% of the money (estimate, section 4).
The land and grid connection are Lancium's. The buildings, cooling, gas plant and day-to-day
facility are Crusoe's, owned through a joint venture with Blue Owl and Primary Digital
Infrastructure and financed mostly by JPMorgan loans. The people who physically built it work for
DPR Construction, Rosendin, Southland and about 90 subcontractors. OpenAI owns nothing there and no
OpenAI, SoftBank, MGX or Microsoft money in the site has been reported.

How the quotes were checked. Labels:

- **[PDF]** = I read the document text directly (Oracle fact sheet, extracted with pdftotext).
- **[FETCHED]** = I fetched the page; the quote was extracted by the fetch tool's summarizer model,
  so check the wording on the page before putting it in quotation marks in the post.
- **[SNIPPET]** = seen only in a search result; the page itself returned 403 or was not opened.
  Treat as unverified wording.
- **[MY ARITHMETIC]** = computed here.

Pages that refused the fetch (403): every oracle.com and blogs.oracle.com page, every
datacenterdynamics.com page, energynow.com (the syndicated copy of Bloomberg's May 2025 feature).
Bloomberg, FT, WSJ and The Information originals are paywalled; they are cited through the outlet
that relayed them.

Builds on POST_RESEARCH.md, part "Abilene (Stargate, OpenAI) and the Power Chart Reference Numbers"
section 7, and part "Money, Strategy, History, Security" item 4. What I re-verified from those: the
$15B joint venture (Crusoe 2025), the 15-year lease, $40B of chips, $9.6B of loans and $5B of cash
(Reuters via GV Wire 2025), Mortenson's substation scope, the Oracle fact sheet's 6,400 workers and
1,100 acres, Oracle's "6 of the 8 campus buildings" statement (Sep 2026 call), the Nvidia $150M
deposit (Tom's Hardware 2026). All held. One correction to section 7: it says Crusoe "operates the
data centers"; the sources split on that (section 1, "who operates").

---

#### 1. Role-by-role breakdown

| Role                                                                          | Who                                                                                                                                          | Confidence                  |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| Found the site, owns the land, holds the grid connection                      | Lancium                                                                                                                                      | Primary sources             |
| Built the two substations                                                     | Mortenson, for Lancium; transmission by AEP                                                                                                  | Primary                     |
| Developer, designer of record for the campus, builder, owner of the buildings | Crusoe                                                                                                                                       | Primary                     |
| Co-owners of the buildings                                                    | Joint venture of Crusoe, Blue Owl Capital funds and Primary Digital Infrastructure. Split not public.                                        | Primary for the parties     |
| Construction lenders                                                          | JPMorgan led both loans                                                                                                                      | Reported                    |
| Lead contractor                                                               | DPR Construction                                                                                                                             | Trade press                 |
| Electrical (design-build)                                                     | Rosendin                                                                                                                                     | Trade press                 |
| Mechanical (design-build)                                                     | Southland Industries (Southland Brandt in ENR)                                                                                               | Trade press                 |
| Architect                                                                     | Alfatech                                                                                                                                     | Trade press, one source     |
| Employers of the 6,400 workers                                                | DPR, Rosendin, Southland and about 90 subcontractors. Not Oracle, OpenAI or (mostly) Crusoe.                                                 | Trade press                 |
| Gas plant                                                                     | Crusoe owns and permits it; turbines from GE Vernova and Caterpillar's Solar Turbines                                                        | Reported (permit)           |
| Switchboards                                                                  | Crusoe's own factory (Crusoe Industries)                                                                                                     | Trade press                 |
| Chillers, transformers                                                        | Makers not public                                                                                                                            | Not found                   |
| GPUs                                                                          | Bought by Oracle from Nvidia                                                                                                                 | Reported (FT)               |
| Racks and servers                                                             | Not disclosed for Abilene. Foxconn is Oracle's largest AI-server supplier.                                                                   | Reported, not site-specific |
| Installing the racks                                                          | Oracle ("delivered" by Oracle; Oracle hires the technicians)                                                                                 | Primary, thin               |
| Running the building day to day                                               | Split: Crusoe runs the power plant and facility plant, Oracle runs the data halls. The line between them is not public and sources conflict. | Conflicting                 |
| Running the cluster and its software                                          | Oracle (Oracle Cloud Infrastructure)                                                                                                         | Primary                     |
| Paying customer                                                               | OpenAI. Controls the workloads and accepts each delivery; owns nothing on site.                                                              | Primary                     |

##### Land and grid connection: Lancium

- Lancium is the landowner and master developer and leases ground to Crusoe. Development Corporation
  of Abilene, 2025 [FETCHED]: "As the owner and master developer of the Lancium Clean Campus";
  "Crusoe is the first specialty developer at the Lancium Clean Campus."
  https://developabilene.com/2025/03/18/the-development-corporation-of-abilene-city-of-abilene-and-taylor-county-announce-expansion-on-the-lancium-clean-campus-with-project-radiance/
- Taylor County's auditor calls Lancium "the company that owns the land underneath the Stargate data
  center". Business Insider via AOL, 2025 [FETCHED].
  https://www.aol.com/oracle-got-big-tax-breaks-090001667.html
- The buildings sit on a ground lease from Lancium, about 90 acres for the first phase. Bisnow, 2025
  [FETCHED] (ground lease, paraphrased by the summarizer); Texas EDC member news, 2024 [SNIPPET] (90
  acres).
  https://www.bisnow.com/national/news/data-center/primary-digital-infrastructure-emerges-as-key-player-in-texas-stargate-data-center-campus-129519
- What Lancium supplies. Crusoe, 2025 [FETCHED]: "Lancium's end-to-end solutions include land
  acquisition, grid interconnect, site engineering"; the release also gives the 1.2 GW grid
  connection.
  https://www.crusoe.ai/resources/newsroom/crusoe-expands-ai-data-center-campus-in-abilene-to-1-2-gigawatts
- The substations were built for Lancium, not for Crusoe or Oracle, and the first one predates the
  data center by two years. Mortenson, 2026 [FETCHED]: "Customer: Lancium"; work on the original 200
  MW, 138 kV substation began May 2022; the 1 GW, 345 kV substation was fully energized March 10,
  2026 on temporary transformers; five main power transformers, maker not named; AEP coordinated
  transmission and interconnection. https://mortenson.com/projects/abilene-data-center-development
- Cost of the land and substations, and Lancium's ground rent: **not public.**

##### Developer, designer, owner of the buildings: Crusoe and its joint venture

- Crusoe's own claim. Crusoe, 2024 [FETCHED]: the first two buildings are "being designed, built,
  and operated by Crusoe", "100% long-term leased to a Fortune 100 hyperscale tenant" (unnamed; it
  is Oracle).
  https://www.crusoe.ai/resources/newsroom/crusoe-blue-owl-capital-primary-digital-joint-venture
- Crusoe, 2025 [FETCHED]: "Designed and built by Crusoe at the Lancium Clean Campus". Construction
  began June 2024, seven months before the Stargate announcement.
  https://www.crusoe.ai/resources/newsroom/crusoe-expands-ai-data-center-campus-in-abilene-to-1-2-gigawatts
- Ownership vehicle. Crusoe, 2025 [FETCHED]: "second phase of a $15 billion joint-venture to fund
  the 1.2 gigawatt AI data center in Abilene, Texas"; the three partners "jointly sponsor the
  construction of six new buildings."
  https://www.crusoe.ai/resources/newsroom/crusoe-blue-owl-capital-and-primary-digital-infrastructure-enter-joint-venture
- State building filings name the owner of buildings 3 to 8 as "Data Center 3-8 Hold Co, LLC" and of
  building 2 as "Crusoe Energy Systems", project name "Project Plaid". Texas Department of Licensing
  and Regulation, 2025 [FETCHED]. Each filing answers "Are the private funds provided by the
  tenant?" with "No", including the fit-out ("Tenant Improvement") filings. So the landlord, not
  Oracle, pays for the shell and the data-hall fit-out; Oracle pays it back as rent.
  - Shell: "Crusoe Building 7", $292,000,000, owner "Data Center 3-8 Hold Co, LLC".
    https://www.tdlr.texas.gov/TABS/Search/Project/TABS2025016966
  - Fit-out: "Crusoe Building 7 Tenant Improvement (TI)", $384,000,000, "build-out an office and
    data hall Tenant Improvement into an existing 484,960 SF shell building", tenant funds "No".
    https://www.tdlr.texas.gov/TABS/Search/Project/TABS2025019019
  - Fit-out: "Crusoe Building 3 TI", $384,000,000, tenant funds "No".
    https://www.tdlr.texas.gov/TABS/Search/Project/TABS2025015061
  - Shell, building 2: owner "Crusoe Energy Systems", $292,000,000.
    https://www.tdlr.texas.gov/TABS/Search/Project/TABS2025011917
- Equity split inside the joint venture: **not public.** Bisnow, 2025 [FETCHED] says of Primary
  Digital: "its capital contribution to the joint venture is comparatively small". Reuters/FT call
  "Crusoe and U.S. investment firm Blue Owl Capital" "the site's owners".
- Crusoe holds the 85% property-tax abatement and committed to 357 full-time jobs and up to $3.5B of
  spending; Oracle benefits as Crusoe's sub-lessee. Business Insider via AOL, 2025 [FETCHED] (URL
  above).

##### Construction: DPR, Rosendin, Southland, and whose workers they are

- ENR, 2025 [FETCHED]: DPR "operates like a CM/GC, running schedule, safety and logistics"; "prime
  contractors Rosendin Electric and Southland Brandt are delivering their scopes using
  design-build"; "DPR manages 60 subcontractors with another 30 subcontractors under the other prime
  partners"; "the customer, Crusoe Energy Systems". Rosendin had more than 1,200 people on site,
  rising toward 1,600, and "committed 180 supervisors"; Southland expected to "exceed 900 with about
  200 field supervisors"; "2,785 total crew members on site" in late July 2025. DPR's engineering
  arm GPLA did structural design; its affiliate Digital Building Components did prefabricated wall
  panels. https://www.enr.com/articles/61133-project-team-pushes-limits-on-abilene-data-center-job
- Construction Digest, 2026 [FETCHED]: "Owner: Crusoe Energy, Denver, Colorado"; "Prime Contractors:
  DPR Construction, Santa Clara, California"; "Electrical Contractor: Rosendin"; "Mechanical
  Contractor: Southland Industries"; "Architect: Alfatech, San Jose, California"; "a multi-prime
  approach that reports directly to the owner". Rosendin's subsidiary Modular Power Solutions built
  60% of the electrical infrastructure off site. The partner list covers Crusoe's West Texas jobs
  generally, not only Abilene.
  https://acppubs.com/CD/article/14CD82BE-crusoe-energy-s-west-texas-data-center-projects-showcase-speed-scale-and-collaboration
- TIME, 2026 [FETCHED]: workers "are managed by a complicated web of contractors and
  subcontractors"; names "DPR Construction, a lead contractor at the site", "Kiewit Corporation,
  whose subsidiary The Industrial Company is constructing the site, and MMR Group", and
  subcontractors Abilene Glass & Mirror and Ruiz-Boyter Construction & Supplies; "some 8,000 people
  have worked 20 million hours at Stargate's first Abilene campus, according to Oracle".
  https://time.com/article/2026/06/24/ai-data-center-stargate-abilene-texas-injuries/
  - **Conflict/unclear:** ENR and Construction Digest name DPR as the lead and never mention Kiewit;
    TIME says Kiewit's subsidiary "is constructing the site". Kiewit's scope (the gas plant, later
    buildings, or the Microsoft campus next door) is not stated anywhere I found.
- The 6,400. Oracle fact sheet, 2025 [PDF]: "There are more than 6,400 construction workers on site
  every day". Crusoe, 2025 [FETCHED] said "more than 5,600 construction workers on-site every day" a
  month earlier (https://www.crusoe.ai/resources/blog/an-inside-look-at-the-abilene-ai-data-center).
  No source gives a headcount by employer. The contractor figures above (Rosendin 1,200+, Southland
  900+, plus DPR and its 60 subcontractors) account for the bulk. I found no Oracle or OpenAI
  employees in the construction count.
- Oracle nonetheless speaks for the site's safety record (TIME 2026: Oracle said its incident rate
  is "approximately 2.5x lower than industry norms") and publishes the worker totals, even though it
  employs none of them.

##### Power plant, turbines, transformers, cooling

- Gas plant: 10 simple-cycle turbines, 360.5 MW, half GE Vernova LM2500 and half Solar Turbines
  Titan 350 (Caterpillar). Citrini Research, 2025 [FETCHED]: "Stargate Abilene is using simple cycle
  gas turbines from GEV and CAT." Business Insider, 2025, relayed in Glenn Lockwood's notes, 2026
  [FETCHED]: "GE Vernova and Solar Turbines are each providing half of the turbines."
  https://www.citriniresearch.com/p/stargate-a-citrini-field-trip-bde and
  https://www.glennklockwood.com/garden/Stargate
- Oracle's fact sheet, 2025 [PDF] credits only one vendor: "Advanced natural gas turbines from GE
  Vernova".
- The plant is Crusoe's: ENR 2025 says Crusoe "offered to build a natural gas power plant on site";
  Crusoe advertises turbine-plant operator and maintenance jobs in Abilene (job boards, 2026
  [SNIPPET]). Gas is delivered by Atmos (Citrini 2025).
- Who built the plant (the engineering contractor): **not found.** Primoris is described as
  "involved" by Citrini; Kiewit's subsidiary is named by TIME without a scope.
- Switchboards: Light Reading, 2026 [FETCHED]: Crusoe's Tulsa factories supplied "more than 2,500
  switchboards supplied to Crusoe's flagship Stargate Project site in Abilene, Texas."
  https://www.lightreading.com/ai-machine-learning/crusoe-opens-second-tulsa-manufacturing-facility
- Medium-voltage cable: Prysmian, $118M contract (Citrini 2025, single source).
- **Chiller maker: not found.** Citrini 2025 guesses Vertiv or Schneider ("likely"); nothing
  confirms it. Southland designed and installed the mechanical systems (ENR 2025).
- **Transformer maker: not found** (Mortenson names none).
- Cooling design: closed-loop liquid with air-cooled chillers; Crusoe, 2025 [FETCHED]: "we're
  constructing this facility" and "purposely selected this system".

##### GPUs, racks, installation

- Buyer of the chips: Oracle. Reuters relaying the Financial Times, via GV Wire, 2025 [FETCHED]:
  "Oracle will spend around $40 billion on Nvidia's higher-performance chips"; "will purchase around
  400,000 of Nvidia's most powerful GB200 chips" and lease the computing power to OpenAI.
  https://gvwire.com/?p=192577
- Epoch AI, 2026 [FETCHED]: "an operational AI data center with AI chips owned by Oracle and used by
  OpenAI". https://epoch.ai/data/ai-data-centers/directory/openai-stargate-abilene
- Delivery/installation: OpenAI, 2025 [FETCHED]: "Oracle began delivering the first NVIDIA GB200
  racks in June." https://openai.com/index/five-new-stargate-sites/ . Oracle, Q1 FY2027 call, Sep
  2026 [FETCHED]: "We delivered 131 thousand GPUs there in Q1"; "6 of the 8 campus buildings,
  representing 618 megawatts and 75% of total capacity have now been delivered to the customer."
  https://www.fool.com/earnings/call-transcripts/2026/09/11/oracle-orcl-q1-2027-earnings-call-transcript/
- Who assembles the racks: **not disclosed for Abilene.** Digitimes, 2025 [FETCHED]: "Foxconn is
  Oracle's largest AI-server supplier", with Quanta a competitor
  (https://www.digitimes.com/news/a20251113VL211.html). A March 2025 Taiwanese report (Economic
  Daily News via TrendForce [FETCHED]) said "Foxconn will secure the exclusive contract for AI
  server manufacturing under the Stargate Project"; never confirmed
  (https://www.trendforce.com/news/2025/03/03/news-foxconn-reportedly-lands-exclusive-ai-server-orders-for-u-s-stargate-ai-project/).
  I found no source tying Supermicro or Dell to Abilene; Dell's Stargate-adjacent orders in the
  press are xAI's.
- Who physically racks them: Oracle hires the on-site technicians (next subsection). Whether Oracle
  also uses a contractor for rack installation is **not public.**
- Networking: Oracle's own Ethernet design (already in the post). Switch vendor at Abilene not
  public; HPE Juniper supplies Oracle's AI data centers generally (w.media, 2026 [SNIPPET]).

##### Who operates what

- The cluster: Oracle. OpenAI, 2026 [FETCHED]: "The site operates on Oracle Cloud Infrastructure and
  runs NVIDIA GB200 systems."
  https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age/
- OpenAI told Bloomberg in March 2025 it was working with Oracle on the design and delivery of the
  Abilene data center, but that Oracle was in charge of sourcing and operating the supercomputer.
  This is DCD's paraphrase of the Bloomberg piece [SNIPPET, identical wording in two search results;
  DCD page 403].
  https://datacenterdynamics.com/en/news/openai-and-oracle-to-deploy-64000-gb200-gpus-at-stargate-abilene-data-center-by-2026-report
- The building: **sources conflict.**
  - Crusoe 2024: "designed, built, and operated by Crusoe". The Register, 2025 [FETCHED] calls
    Crusoe the "datacenter operator" (https://www.theregister.com/2025/05/27/oracle_openai_40b/). A
    2026 report on Oracle layoffs describes Oracle staff "supporting the Crusoe-operated facility"
    (Analytics Insight, 2026 [FETCHED], unnamed employees, weak source).
  - But Crusoe's own Abilene community page, read Nov 2026 [FETCHED]: "The data center will be
    operated by the customer to which we lease the site, or by Crusoe for our Cloud service."
    https://www.crusoe.ai/about/communities/abilene
  - DCD, 2025 [SNIPPET]: under Stargate "SoftBank has financial responsibility and OpenAI has
    operational responsibility", "but this data center appears to be run by Oracle".
  - TechRepublic, 2025 [SNIPPET] says "OpenAI will operate the center"; that is the January 2025
    announcement's language, not what happened at Abilene.
  - Reading them together: Crusoe runs the landlord side (gas plant, electrical yard, chilled-water
    plant, grounds, security) and Oracle runs the data halls and everything in the racks. The exact
    demarcation is **not public.**

##### The customer: OpenAI

- Sole user. Bisnow, 2025 [FETCHED]: OpenAI and Oracle "will be the end user and tenant,
  respectively, of the Abilene data centers."
- What it controls: the workloads (GPT-5.5 was trained there, OpenAI 2026) and acceptance of each
  delivery. Oracle, Sep 2026 call [FETCHED]: "Customer acceptance has compressed to only 24 hours".
- What it owns on site: nothing reported (section 3).

---

#### 2. Oracle's part

**Paid for.** The computers: reported about $40B for about 400,000 GB200 (FT via Reuters via GV Wire
2025); Epoch models the installed compute at $21.5B (2025 USD, estimate). Plus rent on a 15-year
lease of the whole campus. Reuters/FT 2025 [FETCHED]: "Oracle has agreed to lease the site for 15
years". Lease price **not public.** Oracle's company-wide lease commitments were $248B in its
December 2025 10-Q, with terms of 15 to 19 years, not broken out by site (CoStar / Bloomberg via
Advisor Perspectives, 2025 [SNIPPET],
https://www.costar.com/article/606433792/oracle-on-the-hook-for-248-billion-in-data-center-leases-a-move-some-analysts-call-risky).

**Owns.** The chips, servers, networking and storage in the halls. Not the land, shells, cooling
plant, gas plant or substations.

**Designed.** Oracle's cluster and network architecture, and by its own account some of the
building. Oracle, Sep 2026 call [FETCHED], Clay Magouyrk describing what Oracle invests in: "from
data center design through supply chain and manufacturing to installation and operations"
(transcript is machine-assisted; check wording). The Information, 2025, via Spyglass [in
POST_RESEARCH.md]: "Starting in June, Oracle began working with Crusoe on developing the site for
OpenAI". How the building design was divided between Crusoe (which claims "designed") and Oracle is
**not public**; the design-build engineers of record were Rosendin and Southland.

**Operates.** The cluster, as Oracle Cloud Infrastructure, and the data halls.

**Staff on site: not published.** What exists:

- DCD, 2025 [SNIPPET, page 403]: Oracle was hiring "a senior manager of data center operations for
  the site, alongside three data center site leads" and had "at least 35 open positions for data
  center technicians, alongside several more for night technicians".
  https://datacenterdynamics.com/en/news/oracle-hiring-for-abilene-texas-stargate-data-center-roles
- An Oracle job ad for Abilene (Dice, 2026 [SNIPPET, listing now gone]): a support manager "managing
  15-20 Data Center Technicians".
- Oracle's Abilene page (oracle.com, read via search snippet 2026 [SNIPPET]): "more than 9,000
  construction jobs, as well as 1,000 ongoing project-supported jobs within the first two years
  after construction is complete". "Project-supported" is not Oracle headcount.
- Oracle fact sheet, 2025 [PDF]: "Ongoing, the campus and nearby expansion will provide nearly 1,700
  jobs onsite". Includes the expansion Oracle later dropped.
- Crusoe's side: 357 full-time jobs promised under the tax deal (Business Insider 2025); Crusoe told
  Bloomberg in January 2025 it expected "more than 100 full-time jobs" (Bloomberg Línea, 2025
  [FETCHED],
  https://www.bloomberglinea.com/mundo/estados-unidos/asi-es-el-primer-centro-de-datos-de-stargate-en-texas-tiene-el-tamano-de-central-park/).
- Oracle layoffs on September 14, 2026 reportedly reached Abilene hardware-support staff (Analytics
  Insight 2026, unnamed employees, no count).

**What Oracle itself says it "built".** Oracle does not claim to have constructed the campus. Its
fact sheet, 2025 [PDF] lists under Abilene "Data Center Development Partners: Crusoe" and says "The
campus in Abilene, Texas is already up and running on Oracle Cloud Infrastructure (OCI)". On
earnings calls it says "our site in Abilene", "We delivered 131 thousand GPUs there", buildings
"delivered to the customer". On X in April 2026 (quoted second-hand in Ed Zitron's newsletter
[SNIPPET]): "in Abilene, 200MW is already operational, and delivery of the eight-building campus
remains on schedule". Oracle's verb is "deliver".

**What Oracle did not do.** Find or own the land (Lancium). Arrange the grid connection or build the
substations (Lancium, Mortenson, AEP). Own or finance the buildings (the Crusoe / Blue Owl / Primary
Digital venture, JPMorgan). Pay directly for the shells or hall fit-out (state filings: tenant funds
"No"). Manage construction or employ the 6,400 (DPR, Rosendin, Southland). Build or run the gas
plant (Crusoe). Make the chips (Nvidia) or, as far as is public, assemble the racks (contract
manufacturers). Train the models (OpenAI).

**Origin.** Oracle's Abilene lease predates Stargate and was first aimed at Microsoft. DCD, 2024,
relaying The Information [SNIPPET, page 403]: "As part of its deal to rent 100,000 advanced GPUs to
Microsoft for OpenAI's use, Oracle is nearing an agreement with Crusoe in Abilene, Texas"; "Crusoe
is expected to operate the data center that Oracle will lease. Then Oracle will put GPUs in that
facility and rent the servers to Microsoft, which will give those chips to OpenAI."
https://datacenterdynamics.com/en/news/oracle-to-lease-texas-data-center-from-cryptomining-and-ai-firm-crusoe-report

---

#### 3. OpenAI's part

- **Money put into the site: none reported.** FT, 2025, quoted by Spyglass [FETCHED]: "Stargate,
  which incorporated earlier this year, has not invested in the site."
  https://spyglass.org/the-stargate-data-center-layer-cake/ . I found no later report of OpenAI
  capital in the Abilene land, buildings or chips. OpenAI pays Oracle for the compute as it is
  delivered.
- **What it pays: not public for Abilene.** The widely quoted $300B is the later 4.5 GW contract,
  which excludes Abilene. Oracle's October 2026 investor day gave generic economics for one roughly
  1 GW AI contract: about $80B of contracted revenue over about five years, about $16B a year at
  full ramp, about $37B of Oracle capital spending (CryptoBriefing, 2026 [FETCHED], single outlet,
  not tied to Abilene by the source).
  https://cryptobriefing.com/oracle-80b-ai-infrastructure-investor-day/
- **Why it doesn't own it.** The Information, 2026, via Tom's Hardware [FETCHED]: OpenAI "couldn't
  secure financing on competitive terms", and lenders "offered materially better terms when a more
  creditworthy tenant, like Oracle, signed the lease."
  https://www.tomshardware.com/tech-industry/openai-couldnt-finance-its-data-centers-so-it-took-control-of-hardware-instead
- **Design input.** Some, through Oracle: the March 2025 statement to Bloomberg above (design and
  delivery with Oracle; Oracle sources and operates). The fuller design control OpenAI now has
  ("cluster architecture, cooling systems, rack configs, and power infrastructure", The Information
  via Tom's Hardware 2026) is for later sites such as Milam County, where "SoftBank builds and owns
  the project, while OpenAI controls design". Not Abilene.
- **Staff on site: a handful, number not public.** SDxCentral, 2026 [FETCHED]: in September 2026
  OpenAI advertised for a senior networking technician to lead network bring-up on a "large
  partner-operated campus", on site in Texas five days a week.
  https://www.sdxcentral.com/news/openai-seeks-technician-to-lead-network-buildout-for-unidentified-partner-campus-at-stargate-abilene/
  . DCD, 2026 [SNIPPET]: a former Google data center program manager joined OpenAI's Stargate team
  "starting in Abilene, Texas". An OpenAI hardware-operations ad says the role will "Collaborate
  with Cloud Service Provider operations teams and OEM vendors to coordinate repairs" [FETCHED via
  Khosla job board]; so repairs go through Oracle's people.
- **Owns: nothing on site** that any source reports. Tom's Hardware 2026 says of OpenAI's model
  generally that it does not own the land or building.

---

#### 4. Rough split of the capital

Inputs:

| Layer                                                                  | Who pays                                               | Amount      | Type                         | Source                                                   |
| ---------------------------------------------------------------------- | ------------------------------------------------------ | ----------- | ---------------------------- | -------------------------------------------------------- |
| Buildings, cooling, electrical, gas plant ("the facility")             | Crusoe / Blue Owl / Primary Digital joint venture      | $15B        | Primary                      | Crusoe 2025                                              |
| of which loans                                                         | JPMorgan-led lenders                                   | $9.6B       | Reported                     | FT via Reuters 2025 (Bloomberg's two loans sum to $9.4B) |
| of which owners' cash                                                  | Blue Owl funds mainly, Crusoe, Primary Digital (small) | about $5B   | Reported                     | FT via Reuters 2025                                      |
| Computers (chips, servers, networking)                                 | Oracle                                                 | $40B        | Reported, single origin (FT) | Reuters via GV Wire 2025                                 |
| same, modelled                                                         | Oracle                                                 | $21.5B      | Estimate                     | Epoch AI 2026                                            |
| same, Bloomberg / Cushman & Wakefield at $17B of chips per GW × 1.2 GW | Oracle                                                 | $20.4B      | Estimate, MY ARITHMETIC      | Bloomberg via AI Weekly 2026                             |
| Land, two substations                                                  | Lancium                                                | not public  | —                            | —                                                        |
| OpenAI, SoftBank, MGX, Microsoft, Stargate LLC                         | —                                                      | $0 reported | Reported                     | FT via Spyglass 2025                                     |

Arithmetic [MY ARITHMETIC]:

- $9.6B + $5B = $14.6B, against the $15B headline; the $0.4B gap is rounding in the press figures.
- Low case (Epoch hardware): $15B + $21.5B = **$36.5B**. Oracle 21.5 / 36.5 = **59%**. Lenders 9.6 /
  36.5 = 26%. Building owners' cash 5 / 36.5 = 14%.
- High case (FT hardware): $15B + $40B = **$55B**. Oracle 40 / 55 = **73%**. Lenders 9.6 / 55 = 17%.
  Building owners' cash 5 / 55 = 9%.
- So: Oracle about 60% to 75%, JPMorgan-led lenders about 15% to 25%, the building owners' own cash
  about 10% to 15%, everyone named at the White House other than Oracle 0%. Estimate.

Caveats:

- Oracle's share is itself mostly borrowed at the corporate level: Oracle raised about $43B of debt
  and $5B of equity in fiscal 2026 (The Next Web, 2026 [FETCHED],
  https://thenextweb.com/news/oracle-q4-fy2026-capex-55-billion-ai-data-center-openai). Not
  attributable to one site.
- Over 15 years Oracle also pays for the buildings through rent, so on a whole-life basis nearly all
  the money is Oracle's, and behind Oracle, OpenAI's. Rent **not public.**
- Cross-check on the $15B: state filings give $292M shell + $384M fit-out = $676M per building, × 8
  = $5.4B [MY ARITHMETIC; building 1's fit-out was filed lower, $140M, per Business Insider via
  Lockwood]. The gas plant was permitted at up to $500M (DCD [SNIPPET]). The remaining roughly $9B
  would be owner-furnished electrical and mechanical equipment, site work, interest during
  construction and fees; no source itemizes it. Crusoe's CEO reportedly expected Crusoe's cost to
  build Abilene "to reach about $12 billion" (Bloomberg, May 2025 [SNIPPET only, not verified]).
- The low and high hardware figures can't both be right; POST_RESEARCH.md already flags this.
- Epoch's own all-in is $31.2B ($21.5B compute + $9.7B construction), lower on both lines than the
  financing figures; with Epoch's split Oracle is 69%.

---

#### 5. SoftBank, Microsoft, Nvidia, MGX at this site

What the announcement said. OpenAI, January 21, 2025 [FETCHED]: "The initial equity funders in
Stargate are SoftBank, OpenAI, Oracle, and MGX." SoftBank has "financial responsibility" and OpenAI
"operational responsibility". "Arm, Microsoft, NVIDIA, Oracle, and OpenAI are the key initial
technology partners" (paraphrased by the summarizer). "The buildout is currently underway, starting
in Texas." https://openai.com/index/announcing-the-stargate-project/

What happened at Abilene:

- **SoftBank: nothing found.** Construction started June 2024; Oracle's lease and the first $3.4B of
  financing (October 2024) predate the announcement. FT, May 2025, via Spyglass: Stargate "has not
  invested in the site." Bisnow's May 2025 account of the financing names Primary, Crusoe, Blue Owl,
  JPMorgan and Newmark, and not SoftBank. SoftBank's Stargate work is elsewhere: OpenAI, 2025
  [FETCHED] assigns Lordstown, Ohio and Milam County, Texas to SoftBank and the Abilene campus to
  Oracle ("already up and running on Oracle Cloud Infrastructure"). Indirectly, SoftBank is OpenAI's
  largest recent investor, so some of what OpenAI pays Oracle is SoftBank's money; that is inference
  (Spyglass 2025 makes the same one), not a sourced flow.
- **MGX: nothing found.** No report of MGX money in the Abilene land, buildings or chips. Crusoe's
  own investors include Mubadala Capital, a different Abu Dhabi fund (TechCrunch, 2026 [FETCHED]:
  round "co-led by Atreides Management, Mubadala Capital, and Valor Equity Partners").
  https://techcrunch.com/2026/09/17/crusoe-raises-3-9b-to-build-massive-data-centers-and-small-modular-ai-factories/
- **Microsoft: not in this campus, though it nearly was, twice.** In 2024 Oracle's Abilene capacity
  was reportedly to be rented to Microsoft for OpenAI's use (DCD relaying The Information, 2024
  [SNIPPET], above). Microsoft stepped back (NYT 2025 via Spyglass, in POST_RESEARCH.md: Nadella
  "decided not to put in the money for Stargate"). In March 2026 Microsoft took the adjacent 900 MW
  expansion that Oracle and OpenAI dropped; that is a separate campus (Crusoe 2026, already in the
  post).
- **Nvidia: supplier, not owner.** It sold Oracle the GB200 systems. It holds no stake in the
  campus. It is a shareholder in Crusoe the company (TechCrunch 2026: "Founders Fund, GIC, Nvidia,
  Qatar Investment Authority (QIA), Radical Ventures, and TPG also participated"). For the dropped
  expansion, Bloomberg via Tom's Hardware, 2026 [FETCHED]: "Nvidia paid a $150 million deposit to
  Crusoe to secure that space."
  https://www.tomshardware.com/tech-industry/oracle-and-openai-scrap-planned-600mw-abilene-expansion
- **Arm:** nothing site-specific found (the GB200's Grace CPUs are Arm designs; that is the extent
  of it).

So of the four "initial equity funders", only Oracle has visible money in Abilene, and it is there
as a tenant and hardware buyer under a deal struck before Stargate existed, not as an equity funder
of a Stargate entity.

---

#### 6. How New Carlisle differs

Amazon does in-house almost everything that six companies split at Abilene. It bought the land
itself (NYT via The Nightly, 2025 [FETCHED]: "By early 2024, Amazon owned the land"), builds on its
own balance sheet with no developer, landlord or construction lender, designs the data center, the
servers, the network and the Trainium2 chip (Amazon, 2025 [FETCHED]: control from the chip "to the
complete design of the data center itself"; "This vertical integration gives AWS a significant
advantage"), and operates the site with its own staff. What it contracts out is construction labor
(NYT 2025: "Amazon hired four general contractors to work simultaneously", unnamed; one contractor,
Walbridge, is named in WVPE 2025), grid power (Indiana Michigan Power) and chip fabrication.
Anthropic's position matches OpenAI's: it rents.

- https://thenightly.com.au/business/the-new-york-times-at-amazons-biggest-data-centre-everything-is-supersized-for-ai-c-19309860
- https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster

---

#### Where sources conflict

- **Who operates the building:** Crusoe says "operated by Crusoe" (2024) and also that the data
  center "will be operated by the customer to which we lease the site" (community page, 2026). DCD
  says it "appears to be run by Oracle". Most likely both, on either side of a line nobody has
  published.
- **Who "is constructing the site":** DPR (ENR, Construction Digest) versus Kiewit's subsidiary
  (TIME). Probably different scopes.
- **Chip spend:** $40B (FT) versus $21.5B (Epoch) versus about $20B (Bloomberg / Cushman &
  Wakefield).
- **Loans:** $9.6B (FT) versus $9.4B (sum of Bloomberg's two).
- **Lease scope:** "the site" (FT) versus "a significant portion of the Abilene campus" (WSJ via
  Yahoo, 2025). Bloomberg, March 2025 [FETCHED via Yahoo]: "Oracle has already agreed to use the
  Abilene location's full build for Stargate". Later statements all treat the eight buildings as
  Oracle's.
- **Construction headcount:** 5,600 (Crusoe, Aug 2025), 6,400 (Oracle, Sep 2025), 8,000 cumulative
  (Oracle, 2026), "more than 9,000 construction jobs" (Oracle's Abilene page).

#### Not public / not found

- Oracle's on-site headcount; OpenAI's on-site headcount.
- The lease price, and what OpenAI pays Oracle for Abilene.
- The equity split among Crusoe, Blue Owl and Primary Digital.
- Lancium's land cost, ground rent and who paid for the substations.
- The makers of the chillers and transformers; the contractor that built the gas plant.
- Which manufacturer assembled Abilene's racks, and whether a contractor installs them.
- Any SoftBank or MGX money in the site.
- Whether any Abilene capacity was ever actually billed through Microsoft (the 2024 plan), or
  whether OpenAI contracted with Oracle directly from the start.
- The publication dates of the two DCD articles cited as 2025 and 2024 (pages returned 403; years
  inferred from their content and from when the underlying Bloomberg and The Information reports
  ran).
- An unverifiable figure I did not use: an AI-generated Sacra summary gives first-year base rent of
  "$2.475M per data hall plus $297K for each building network core" with 3% yearly increases, with
  no period (month or year) and no source document.

---

# Part: Power Comparisons for the Chart

## Power comparisons for the giant-datacenter log-scale chart

Researched 2026-11-22. Conversion everywhere: average GW = annual TWh / 8.76.

### Summary table

| #   | Item                                                         |                    Avg GW | Year                                 | Basis                                                                          | Source                                                                         |
| --- | ------------------------------------------------------------ | ------------------------: | ------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| 1   | All datacenters, world (IEA)                                 |                        55 | 2025                                 | 485 TWh, estimate                                                              | IEA, Key Questions on Energy and AI (2026)                                     |
| 1   | All datacenters, world (IEA)                                 |                        47 | 2024                                 | 415 TWh, estimate                                                              | IEA, Energy and AI (2025)                                                      |
| 1   | All datacenters, world (Energy Institute / S&P, wider scope) |                        90 | 2025                                 | 787.8 TWh, estimate                                                            | Energy Institute Statistical Review 2026, via Carbon Brief and OilPrice (2026) |
| 2   | All US datacenters (LBNL)                                    |                        22 | 2024                                 | 192 TWh, estimate, excludes crypto                                             | LBNL, US Data Center Energy Usage Report: 2025 Update (2026)                   |
| 2   | All US datacenters (LBNL, older)                             |                        20 | 2023                                 | 176 TWh, estimate                                                              | LBNL 2024 report (2024)                                                        |
| 2   | All US datacenters (Energy Institute / S&P)                  |                        36 | 2025                                 | 312.6 TWh, estimate, secondary source                                          | OilPrice citing EI Statistical Review 2026                                     |
| 3a  | All US light-duty vehicles, fuel energy (thermal)            |                       500 | 2024/2025                            | 124.8 bn gal x 120,214 Btu/gal = 4,397 TWh thermal                             | FHWA Table VM-1 (2026); EIA (2026)                                             |
| 3b  | Same miles driven by EVs (hypothetical, electric)            |                       100 | 2024 miles                           | 2.924 trillion mi x 0.3 kWh/mi = 877 TWh; 83 to 134 GW for 0.25 to 0.40 kWh/mi | FHWA Table VM-1 (2026) x assumption                                            |
| 3c  | US EVs today, actual electricity                             |                       2.7 | 2025                                 | 23.5 TWh, modeled estimate                                                     | EIA Monthly Energy Review Table 7.6 (2026)                                     |
| 4   | Total US electricity consumption                             |                       479 | 2025                                 | 4,195 TWh = 4,058 retail sales + 137 direct use                                | EIA Monthly Energy Review Table 7.6 (2026)                                     |
| 5   | Total world electricity demand                               |                     3,628 | 2025                                 | 31,779 TWh                                                                     | Ember, Global Electricity Review 2026 (2026)                                   |
| 6   | New York City                                                |                       5.7 | 2025                                 | 50,104 GWh, NYISO Zone J                                                       | NYISO 2026 Gold Book, Table I-2 (2026)                                         |
| 7   | San Francisco                                                |                      0.58 | 2022                                 | 5,121 GWh, SF County                                                           | California Energy Commission ECDMS (latest year in database)                   |
| 8   | One average US nuclear reactor                               |                      0.95 | 2025                                 | 784.8 TWh / 94 reactors = 8.35 TWh each                                        | EIA Monthly Energy Review Table 8.1 (2026)                                     |
| 8   | Vogtle (largest US plant, 4 reactors)                        |                       4.2 | 2025                                 | 37.14 TWh net generation                                                       | EIA Form EIA-923, 2025 final (2026)                                            |
| 8   | Palo Verde (3 reactors)                                      |                       3.6 | 2025                                 | 31.32 TWh net generation                                                       | EIA Form EIA-923, 2025 final (2026)                                            |
| 9   | Bitcoin mining, world                                        |       21.5 (10.9 to 44.5) | 2025 avg                             | 188.7 TWh, model estimate with bounds                                          | Cambridge CBECI data download (2026)                                           |
| 9   | Bitcoin mining, world, latest                                |       18.8 (10.2 to 33.0) | 21 Nov 2026                          | 164.7 TWh annualised                                                           | Cambridge CBECI data download (2026)                                           |
| 10  | Three Gorges Dam                                             |                      10.9 | 2025                                 | 95.7 TWh generation                                                            | China Yangtze Power announcement 2026-001 (2026)                               |
| 11  | Aschenbrenner cluster forecast                               | 0.01 / 0.1 / 1 / 10 / 100 | 2022 / ~2024 / ~2026 / ~2028 / ~2030 | Forecast, single largest training cluster                                      | Situational Awareness (2024)                                                   |
| 12  | Texas (whole state)                                          |                        61 | 2025                                 | 533.3 TWh retail sales                                                         | EIA Form EIA-861M (2026)                                                       |
| 12  | United Kingdom                                               |                        37 | 2025                                 | 323.0 TWh demand                                                               | DESNZ, DUKES 2026 Chapter 5 (2026)                                             |
| 12  | Grand Coulee Dam (largest US plant by capacity)              |                       1.8 | 2025                                 | 16.15 TWh net generation                                                       | EIA Form EIA-923, 2025 final (2026)                                            |
| 12  | Arizona / Washington (a "small/medium US state" near 10 GW)  |               10.5 / 10.3 | 2025                                 | 92.1 / 90.1 TWh retail sales                                                   | EIA Form EIA-861M (2026)                                                       |
| 12  | California (whole state)                                     |                        28 | 2025                                 | 243.0 TWh retail sales (excludes rooftop-solar self-use)                       | EIA Form EIA-861M (2026)                                                       |
| ref | Hoover Dam, 2025 actual                                      |                      0.31 | 2025                                 | 2.735 TWh (NV 1.808 + AZ 0.927)                                                | EIA Form EIA-923, 2025 final (2026)                                            |
| ref | All US homes, cross-check                                    |                       173 | 2025                                 | 1,519.15 TWh residential sales                                                 | EIA Form EIA-861M (2026); MER Table 7.6 says 1,515.0                           |

### How each quote was obtained

- "raw" = I read the number or sentence directly out of the downloaded PDF/CSV/XLSX/HTML.
- "relayed" = the page was read through a fetch tool that summarises pages with a small model, so
  the wording is very likely right but was not checked character by character. Re-open the URL
  before pasting a relayed quote into the post.

---

### 1. All datacenters globally

| Estimate                                                          |   TWh | Year |    GW | Status                      |
| ----------------------------------------------------------------- | ----: | ---- | ----: | --------------------------- |
| IEA, Energy and AI                                                |   415 | 2024 |  47.4 | estimate                    |
| IEA, Key Questions on Energy and AI                               |   485 | 2025 |  55.4 | estimate                    |
| IEA, same report                                                  |   950 | 2030 | 108.4 | forecast                    |
| Energy Institute Statistical Review 2026 (S&P Global Energy data) | 658.2 | 2024 |  75.1 | estimate, secondary-sourced |
| Energy Institute Statistical Review 2026                          | 787.8 | 2025 |  89.9 | estimate, secondary-sourced |

- IEA 2024: https://www.iea.org/reports/energy-and-ai/executive-summary , IEA, published April 2025.
  Quote (relayed): "Data centres accounted for around 1.5% of the world's electricity consumption in
  2024, or 415 terawatt-hours (TWh)."
- IEA 2025: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary , IEA,
  published 16 April 2026. Quote fragments (relayed): "from 485 TWh in 2025 to 950 TWh in 2030" and
  "grew by 17% in 2025". Press release,
  https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions
  : "Electricity demand from data centres soared by 17% in 2025". 415 x 1.17 = 485.6, so the two IEA
  figures are consistent.
- IEA Global Energy Review 2026,
  https://www.iea.org/reports/global-energy-review-2026/electricity-demand (relayed): "Data centres
  continued to grow strongly, with their electricity consumption increasing by around 17%." and
  "this 70 TWh increase compares with a total electricity demand increase of around 800 TWh."
- Energy Institute: the EI site returned HTTP 403, so this is from two secondary write-ups.
  - Carbon Brief, 29 June 2026,
    https://www.carbonbrief.org/six-charts-show-how-clean-power-was-worlds-largest-source-of-new-energy-in-2025
    (relayed): "data centres used 788TWh of electricity in 2025, up 130TWh on a year earlier."
  - OilPrice.com (Robert Rapier), 27 Aug 2026,
    https://oilprice.com/Energy/Energy-General/The-AI-Boom-Is-Driving-a-New-Era-of-US-Power-Demand.html
    (relayed): "worldwide data-center electricity demand reached 787.8 terawatt-hours in 2025, up
    from 658.2 TWh in 2024."
- 2026: no published full-year 2026 estimate found. My own interpolation of the IEA path (485 in
  2025 to 950 in 2030 is 14.4% a year) gives about 555 TWh, 63 GW, for 2026. That is my arithmetic,
  not a source figure.
- Range: 55 GW (IEA) to 90 GW (Energy Institute/S&P) for 2025. The gap is scope and method (the EI
  series is new in the 2026 edition and counts more than IEA's bottom-up model does), not year. IEA
  is the figure most people cite.

### 2. All US datacenters

| Estimate                                            |   TWh | Year |                  GW | Status                    |
| --------------------------------------------------- | ----: | ---- | ------------------: | ------------------------- |
| LBNL 2024 report                                    |   176 | 2023 |                20.1 | estimate, excludes crypto |
| LBNL 2025 Update                                    |   192 | 2024 |                21.9 | estimate, excludes crypto |
| IEA (45% of 415; Pew quotes 183)                    |   183 | 2024 |                20.9 | estimate                  |
| Energy Institute / S&P via OilPrice                 | 249.0 | 2024 |                28.4 | estimate, secondary       |
| Energy Institute / S&P via OilPrice                 | 312.6 | 2025 |                35.7 | estimate, secondary       |
| LBNL 2025 Update, reference case                    |   464 | 2028 |                53.0 | forecast                  |
| LBNL 2025 Update, reference case (range 521 to 843) |   649 | 2030 | 74.1 (59.5 to 96.2) | forecast                  |

- LBNL 2024 report:
  https://eta-publications.lbl.gov/sites/default/files/2024-12/us_data_center_energy_usage_report_lbnl-2001637.pdf
  , Lawrence Berkeley National Laboratory, December 2024. Quote (raw): "reaching 176 TWh by 2023,
  representing 4.4% of total U.S. electricity consumption." Also (raw): "with the low and high end
  of roughly 325 and 580 TWh in 2028".
- LBNL 2025 Update: https://escholarship.org/uc/item/33m6w3x0 (also
  https://www.energy.gov/documents/united-states-data-center-energy-usage-report-2025-update ),
  LBNL, publication date 2026-06-18. Quotes (raw): "The updated estimate of data center electricity
  use in 2024 is 192 terawatt-hours (TWh), accounting for 4.7% of total U.S. electricity
  consumption." and "the energy use of cryptocurrency mining is not included in the scope of this
  report." and "The Reference Case estimate for 2030 data center electricity use is 649 TWh,
  representing 11.8% of forecasted 2030 U.S. electricity use". The report says 2024 is its last
  historical year; it gives no 2025 number in text.
- IEA: https://www.iea.org/reports/energy-and-ai/executive-summary (relayed): "The United States
  accounted for the largest share of global data centre electricity consumption in 2024 (45%)". Pew
  Research, 24 Oct 2025,
  https://www.pewresearch.org/short-reads/2025/10/24/what-we-know-about-energy-use-at-us-data-centers-amid-the-ai-boom/
  (relayed): "U.S. data centers consumed 183 terawatt-hours (TWh) of electricity in 2024, according
  to IEA estimates."
- OilPrice.com, 27 Aug 2026 (relayed): "U.S. consumption increased from 249.0 TWh in 2024 to 312.6
  TWh in 2025, a gain of 63.5 TWh."
- 2025 on the IEA/LBNL basis: no published number found. Rough derivation: IEA's Global Energy
  Review 2026 says US data centres "alone contributed around half of the country's entire increase
  in electricity consumption" (relayed); US end use rose 84.7 TWh in 2025 (EIA), so about +42 TWh on
  183 to 192, roughly 225 to 235 TWh, about 26 GW. Mine, not a source figure.
- EIA publishes no US datacenter consumption series.
- Range for the chart: about 22 GW (LBNL, 2024) up to 36 GW (EI/S&P, 2025).

### 3. All US car use (light-duty vehicles: cars, SUVs, vans, pickups)

#### (a) Fuel chemical energy as average thermal power: about 500 GW

- FHWA Highway Statistics 2024, Table VM-1, "Updated: February 2026":
  https://www.fhwa.dot.gov/policyinformation/statistics/2024/pdf/vm1.pdf , Federal Highway
  Administration, 2026. Raw table values for the "ALL LIGHT DUTY VEHICLES" column, 2024: travel
  2,924,107 million vehicle-miles; fuel consumed 124,798,269 thousand gallons; 23.4 miles per
  gallon; 271,085,742 vehicles registered.
- EIA heat content: https://www.eia.gov/energyexplained/units-and-calculators/ (relayed): "1
  gallon=120,214 Btu" for motor gasoline; "1 kilowatthour=3,412 Btu".
- Arithmetic: 124.798 bn gal x 120,214 Btu = 15.00 quadrillion Btu = 4,397 TWh thermal = 501.9 GW
  thermal (2024).
- Cross-check from EIA gasoline, 2025:
  https://www.eia.gov/energyexplained/gasoline/use-of-gasoline.php , EIA, 2026 (relayed): "In 2025,
  Americans used about 136.72 billion gallons of gasoline", "136.53 billion gallons of finished
  motor gasoline", and "Light-duty vehicles (cars, sport utility vehicles, and small trucks) account
  for about 91%" "of all gasoline consumption in the United States." 136.53 x 0.91 = 124.2 bn gal =
  14.94 quads = 4,377 TWh = 499.7 GW thermal.
- Cross-check from Transportation Energy Data Book, Edition 40 (Oak Ridge National Laboratory,
  2022), Table 2.8, https://afdc.energy.gov/files/u/publication/TEDB_Ed_40.pdf (raw): "Light
  vehicles 15,225.9 15,164.2" trillion Btu for 2018 and 2019. 15,164 trillion Btu = 4,444 TWh = 507
  GW thermal (2019). Old, but agrees.
- This is heat content of fuel burned, not electricity. It is not directly comparable to the
  electrical bars; the FHWA fuel column also includes a little diesel, treated here at gasoline heat
  content.

#### (b) Electricity if the same miles were driven by EVs: about 100 GW (hypothetical)

- 2,924,107 million miles (FHWA VM-1, 2024) x 0.3 kWh/mile = 877 TWh a year = 100.1 GW.
- Sensitivity: 0.25 kWh/mi gives 731 TWh, 83 GW; 0.35 gives 1,023 TWh, 117 GW; 0.40 gives 1,170 TWh,
  134 GW. The 0.3 kWh/mile is the assumption given in the brief, not a sourced fleet average. EPA's
  2025 Automotive Trends Report (EPA-420-R-26-001, February 2026,
  https://www.epa.gov/system/files/documents/2026-02/420r26001.pdf ) plots BEV consumption between
  roughly 20 and 40+ kWh per 100 miles depending on weight and notes (raw) "Pickups and truck SUVs
  represent the heaviest BEVs and are somewhat less efficient than other vehicle types". The US
  fleet is truck-heavy, so 0.3 is on the low side for a like-for-like swap.
- Implied: gasoline cars use about 1.5 kWh of fuel heat per mile, five times the 0.3 kWh of
  electricity.

#### (c) Electricity actually used by US EVs today: 2.7 GW

- EIA Monthly Energy Review (October 2026 edition), Table 7.6 "Electricity End Use and Electric
  Vehicle Use": https://www.eia.gov/totalenergy/data/browser/?tbl=T07.06 , EIA, 2026. Raw CSV rows:
  "Electric Vehicle Use" 2025 = 23,532.855 million kWh; 2024 = 17,800.214 million kWh. 23.53 TWh =
  2.69 GW; 2024 was 2.03 GW. Modeled estimate, light-duty on-road EVs.
- EIA Today in Energy, 30 Sept 2026, https://www.eia.gov/todayinenergy/detail.php?id=68224
  (relayed): "more than doubled since 1H23, totaling nearly 14 billion kilowatthours in 1H26." My
  sum of the monthly CSV values for Jan to Jun 2026 is 13.67 TWh, so the 2026 run rate is about 3.1
  GW.

### 4. Total US electricity consumption

- 4,195.085 TWh in 2025 = 478.9 GW. That is 4,058.007 retail sales + 137.077 direct use (raw CSV,
  MER Table 7.6, https://www.eia.gov/totalenergy/data/browser/?tbl=T07.06 , EIA, October 2026
  edition).
- Quote, https://www.eia.gov/energyexplained/electricity/use-of-electricity.php , EIA, 2026
  (relayed): "Total U.S. electricity consumption in 2025 was about 4.20 trillion kWh, the highest
  recorded".
- Vintage mismatch to know about: the Form EIA-861M file
  (https://www.eia.gov/electricity/data/eia861m/ , sales_revenue.xlsx, status "Final") sums to
  4,079.9 TWh retail sales for 2025 with residential 1,519.15 TWh, which matches the 1,519 TWh the
  chart already uses for homes. MER Table 7.6 has residential at 1,514.99 TWh. Using 861M sales plus
  MER direct use gives 4,217 TWh, 481 GW. Either way the bar is about 480 GW.
- Net generation for comparison: 4,429.5 TWh in 2025 = 505.7 GW (MER Table 7.1, raw).
  Aschenbrenner's "about 4,250 TWh" is production, not consumption.

### 5. Total world electricity

- 31,779 TWh demand in 2025 = 3,628 GW. Ember, Global Electricity Review 2026, published 21 April
  2026,
  https://ember-energy.org/latest-insights/global-electricity-review-2026/electricity-demand-and-supply-trends/
  . Quote (relayed): "Global electricity demand increased by 2.8% (+849 TWh) in 2025, to a new
  record high of 31,779 TWh."
- Ember's "demand" is generation-based (it includes grid losses), so it is the right comparator for
  US net generation (506 GW), slightly generous against US end use (479 GW).
- IEA's Global Energy Review 2026 gives growth only ("around 3%", "around 800 TWh"), no level, on
  the page I read.

### 6. New York City

- 50,104 GWh in 2025 = 5.72 GW. NYISO 2026 Load & Capacity Data report ("Gold Book"), April 2026,
  Table I-2 "Baseline Annual Energy, Historical & Forecast", "Annual Energy by Zone - GWh",
  https://www.nyiso.com/documents/20142/2226333/2026-Gold-Book-Public.pdf . Raw row: "2025 15,160
  9,377 14,760 5,267 7,315 11,590 9,513 2,698 5,853 50,104 19,957 151,594" where column J (New York
  City) is 50,104 and the last column is the whole state (NYCA).
- Zone J is the five boroughs. Whole New York grid: 151,594 GWh = 17.3 GW. Earlier Zone J years:
  49,703 (2024), 48,280 (2023), 53,653 (2016).
- This is grid-delivered energy, net of behind-the-meter solar.

### 7. San Francisco

- 5,120.6 GWh in 2022 = 0.585 GW. California Energy Commission, Energy Consumption Data Management
  System, "Electricity Consumption by County", https://ecdms.energy.ca.gov/elecbycounty.aspx (query:
  County = SAN FRANCISCO, Sector = Total). Raw rows returned, with header note "All Usage Expressed
  in Millions of kWh (GWh)":
  - Total: 2022 5120.585617; 2021 4990.150570; 2020 5032.031362; 2019 5631.344589; 2018 5626.631924
  - Residential 2022: 1514.882206; Non-Residential 2022: 3605.703411
- 2022 is the latest year this database serves. The CEC's newer consumption dashboard (Tableau) may
  have 2023 and 2024 but I could not read it by machine. Pre-pandemic the city ran at 0.64 GW
  (2019). Call it 0.6 GW.

### 8. Nuclear

- One average US reactor: 784,781 GWh net generation in 2025 / 94 operable units = 8.35 TWh each =
  0.953 GW. Fleet capacity 96.88 GW net summer (1,031 MW per reactor) at a 91.0% capacity factor.
  All raw from MER Table 8.1, https://www.eia.gov/totalenergy/data/browser/?tbl=T08.01 , EIA,
  October 2026 edition.
- Quotes, https://www.eia.gov/energyexplained/nuclear/us-nuclear-industry.php , EIA, 2026 (relayed):
  "As of March 2026, the United States had 94 operating commercial nuclear reactors at 54 nuclear
  power plants in 28 states." and "Vogtle is the largest nuclear power plant in the United States,
  with four reactors" ... "a total 4,530 MW net summer electricity generation capacity." The same
  page gives fleet capacity as 98,441 MW, which differs from MER's 96.88 GW; I used MER.
- Vogtle (Georgia), whole plant: 37,144,415 MWh in 2025 = 4.24 GW average (93.6% of 4,530 MW).
- Palo Verde (Arizona), whole plant: 31,321,808 MWh in 2025 = 3.58 GW average.
- Source for both: Form EIA-923, 2025 final file (EIA923_Schedules_2_3_4_5_M_12_2025_Final.xlsx,
  dated 11 Sept 2026), https://www.eia.gov/electricity/data/eia923/ , summed over plant IDs 649 and
  6008 (raw). Vogtle and Palo Verde were the top two US plants of any kind by 2025 net generation in
  that file; Browns Ferry third at 29.67 TWh.

### 9. Bitcoin mining worldwide

- Cambridge Bitcoin Electricity Consumption Index (Cambridge Centre for Alternative Finance), data
  download https://ccaf.io/cbeci/api/v1.5.0/download/data?price=0.05 (index page
  https://ccaf.io/cbnsi/cbeci ), pulled 2026-11-22. Model estimate with theoretical lower and upper
  bounds; header line (raw): "Average electricity cost assumption: 0.05 USD/kWh".
- Calendar 2025 mean of daily "power GUESS, GW": 21.5 GW (mean annualised 188.7 TWh). Bounds: 10.9
  to 44.5 GW.
- 2026 year to date (325 days): 18.2 GW mean, bounds 9.5 to 32.2 GW.
- Latest row (raw, 2026-11-21): power MAX 32.98, MIN 10.15, GUESS 18.78 GW; annualised GUESS 164.66
  TWh.
- Spot values: 20.6 GW on 2025-01-01, 22.5 GW on 2025-12-31, 17.1 GW on 2026-07-01.
- No prose quote exists; the site is a live chart. Secondary coverage reported "about 190
  terawatt-hours ... on an annualized basis in December" 2025, which matches the CSV.

### 10. Three Gorges Dam

- 95.715 TWh in 2025 = 10.93 GW. China Yangtze Power Co. (the listed operator, a China Three Gorges
  Corporation subsidiary), "2025 年发电量完成情况公告" (Announcement on 2025 electricity
  generation), No. 2026-001, dated 5 January 2026,
  https://pdf.dfcfw.com/pdf/H2_AN202601051815378174_1.pdf . Raw table row: "三峡电站 256.95 78.78
  957.15 15.44", meaning Three Gorges station: Q4 25.695 bn kWh (+78.78%), full year 95.715 bn kWh
  (+15.44% year on year). Preliminary company statistics.
- Implied 2024: 82.9 TWh = 9.5 GW. So 9.5 to 10.9 GW depending on the water year.
- Secondary (search snippets, not opened): design output 88.2 TWh a year (10.1 GW); record 111.8 TWh
  in 2020 (12.8 GW). Installed capacity is commonly given as 22.5 GW (not verified here), so it runs
  at under half of nameplate.

### 11. Aschenbrenner, "Situational Awareness" (June 2024), chapter IIIa "Racing to the Trillion-Dollar Cluster"

URL: https://situational-awareness.ai/racing-to-the-trillion-dollar-cluster/ . Table extracted raw
from the page HTML; caption: "Scaling the largest training clusters, rough back-of-the-envelope
calculations."

| Year  | OOMs           | # of H100s-equivalent | Cost              | Power  | Power reference class                      |
| ----- | -------------- | --------------------- | ----------------- | ------ | ------------------------------------------ |
| 2022  | ~GPT-4 cluster | ~10k                  | ~$500M            | ~10 MW | ~10,000 average homes                      |
| ~2024 | +1 OOM         | ~100k                 | $billions         | ~100MW | ~100,000 homes                             |
| ~2026 | +2 OOMs        | ~1M                   | $10s of billions  | ~1 GW  | The Hoover Dam, or a large nuclear reactor |
| ~2028 | +3 OOMs        | ~10M                  | $100s of billions | ~10 GW | A small/medium US state                    |
| ~2030 | +4 OOMs        | ~100M                 | $1T+              | ~100GW | >20% of US electricity production          |

Spacing is his: "~10 MW", "~100MW", "~1 GW", "~10 GW", "~100GW". These rows are for the single
largest training cluster, not all AI.

Supporting sentences (raw):

- "A 10GW cluster run continuously for a year is 87.6 TWh."
- "A 100GW cluster run continuously for a year is 876 TWh, while total annual US electricity
  production is about 4,250 TWh."
- "The 100GW of power it’ll require is equivalent to >20% of US electricity production; imagine not
  just a simple warehouse with GPUs, but hundreds of power plants."
- "We’re on the path to individual training clusters costing $100s of billions by 2028—clusters
  requiring power equivalent to a small/medium US state and more expensive than the International
  Space Station."

A second table on the same page covers total AI, not one cluster. Its column "Power as % of US
electricity production" reads: 2024 "1-2%"; ~2026 "5%"; ~2028 "20%"; ~2030 "100%". Against 4,250 TWh
(485 GW) that is roughly 5 to 10 GW, 24 GW, 97 GW and 485 GW.

Checks on his reference classes against the numbers above:

- "~10,000 average homes" for 10 MW implies 1 kW per home. The US average is about 1.2 kW (EIA:
  1,519 TWh over 146.4 million residential customers = 10,370 kWh a year), so that holds.
- "The Hoover Dam" for 1 GW is nameplate thinking. Hoover averaged 0.31 GW in 2025 (0.37 GW in the
  chart). "A large nuclear reactor" is right: 0.95 GW average.
- "A small/medium US state" for 10 GW: Arizona 10.5 GW, Washington 10.3 GW, Alabama 10.1 GW (2025
  retail sales). Those rank 15th to 17th of 51, so "medium", not small.
- ">20% of US electricity production": 100 GW / 505.7 GW = 19.8% of 2025 net generation, 20.9% of
  2025 end use.

### 12. More comparisons

- Texas: 533.26 TWh retail sales in 2025 = 60.9 GW, the largest state by a factor of two. Form
  EIA-861M, sales_revenue.xlsx, sheet "Monthly-States", 12 months summed, status "Final",
  https://www.eia.gov/electricity/data/eia861m/ , EIA, 2026 (raw). ERCOT alone (about 90% of Texas
  load): 488 TWh = 55.7 GW; ERCOT 2025 Annual Report, March 2026,
  https://www.ercot.com/files/docs/2026/03/19/2025-ERCOT-Annual-Report-Final-Single-Pages-March-19-2026.pdf
  , quote (raw): "customers consumed more than 488 million megawatt-hours (MWh) of electricity in
  2025 – about a 5.7 percent increase over 2024."
- United Kingdom: 323.0 TWh demand in 2025 = 36.9 GW. Department for Energy Security and Net Zero,
  Digest of UK Energy Statistics (DUKES) 2026, Chapter 5, 2026 (month not checked),
  https://assets.publishing.service.gov.uk/media/6aba96e8997a4b2950ccf02c/DUKES_2026_Chapter_5.pdf .
  Quote (raw): "Electricity demand was higher in 2025 at 323.0 TWh, up 1.2 per cent compared to
  2024." Final consumption was 275.5 TWh (31.4 GW); "demand" includes losses and the energy
  industry's own use.
- Grand Coulee Dam, the largest US power plant by installed capacity (commonly given as 6,809 MW,
  not verified here): 16,151,147 MWh in 2025 = 1.84 GW average. Form EIA-923, 2025 final, plant ID
  6163 (raw). A clean way to show nameplate versus average: one 1.2 GW campus running flat out uses
  two thirds of what the country's biggest power station delivers.
- A state at Aschenbrenner's 10 GW: Arizona 92.08 TWh = 10.5 GW; Washington 90.12 TWh = 10.3 GW
  (EIA-861M, 2025, raw).
- California: 242.97 TWh retail sales = 27.7 GW (EIA-861M, 2025, raw). Understates true use because
  rooftop-solar self-consumption is not a retail sale. New York State: 143.76 TWh = 16.4 GW.
  Florida: 259.08 TWh = 29.6 GW.

### Caveats

1. Unlike quantities. 3a is fuel heat (thermal); everything else is electricity. Label it or leave
   it off an electricity chart; 3b (100 GW) is the like-for-like bar but is hypothetical and rests
   on an assumed 0.3 kWh/mile.
2. Average versus capacity. Every bar is annual energy / 8,760 h. If "about 1.2 GW" for the campuses
   is nameplate or contracted capacity, their average draw is lower (LBNL converts energy to
   capacity assuming 50% utilisation in its 2024 report; AI training sites run much higher).
3. Datacenter totals are estimates and the sources disagree by 60%: IEA 485 TWh versus Energy
   Institute/S&P 788 TWh for world 2025; LBNL 192 TWh (2024) versus EI/S&P 313 TWh (2025) for the
   US. The EI figures here are secondary-sourced. LBNL excludes crypto mining.
4. Consumption versus generation. US 479 GW is end use; world 3,628 GW is generation-based demand;
   state and city figures are retail sales or grid load. Differences of 5 to 8% from losses.
5. San Francisco is 2022 data. Bitcoin is a model with a 4x spread between bounds. Three Gorges and
   Hoover swing 15 to 20% with the water year.
6. Quotes marked "relayed" came through a summarising fetch tool; verify wording at the URL before
   quoting in the post.

---

# Part: Cost Breakdown for the Chart

## Cost breakdown for the two sites (research for the log-scale dollar chart)

Compiled 2026-11-22. Basis labels: REPORTED (a company, regulator or filing said it), ESTIMATE
(third-party model), ARITHMETIC (computed here, inputs shown in the sections below). "Today" means
18 buildings at New Carlisle (1,037 MW IT, 1,244 MW at the meter, Epoch AI 2026) and 8 buildings at
Abilene (824 MW IT, 1,154 MW peak at the meter, Epoch AI 2026).

"Chips" below means whole servers and racks (accelerators plus boards, chassis, in-rack cabling and
power shelves). It excludes the switches, optics and fiber between racks, which are the "networking"
row, so the two rows do not overlap.

### Summary table

| Site         | Category                                              | Best figure                           | Range                                                                      | Basis                                                                                                                                                                                                              | Source                                                                                                                                                                                                                                                                     |
| ------------ | ----------------------------------------------------- | ------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New Carlisle | Chips (whole servers and racks)                       | $8B                                   | $4.9B (bare accelerators) to $22B (Epoch's Nvidia-priced servers)          | ARITHMETIC: 1,044,976 Trainium2 x ~$7,000 per chip installed + 104,067 Trainium3 x ~$10,000. The $7,000 is $4,000 per bare chip + ~$1,100 cabling (both SemiAnalysis) + ~$2,000 assumed for the rest of the server | Epoch AI chip table, 2026, https://epoch.ai/data/ai_chip_sales_chip_types.csv ; SemiAnalysis, 2024, https://newsletter.semianalysis.com/p/amazons-ai-self-sufficiency-trainium2-architecture-networking                                                                    |
| New Carlisle | Networking                                            | $1.4B                                 | $1.2B to $5.1B                                                             | ESTIMATE: Epoch's 13% share x Amazon's $11B announced campus budget. The high end is Epoch's $4.9B per GW x 1.037 GW, calibrated on Nvidia clusters, which overstates AWS's in-house gear                          | Epoch AI, 2026, https://epoch.ai/data-insights/ai-datacenter-cost-breakdown ; IEDC, 2024 (the $11B)                                                                                                                                                                        |
| New Carlisle | Storage                                               | $0.3B                                 | $0.11B to $0.59B                                                           | ESTIMATE: Bernstein's 1 to 1.5% of capex. Low end x $11B, high end x Epoch's $39.3B; best is the middle                                                                                                            | Bernstein via Investing.com, 2025, https://www.investing.com/news/stock-market-news/how-much-does-a-gw-of-data-center-capacity-actually-cost-4314046                                                                                                                       |
| New Carlisle | Buildings (shell + mechanical and electrical fit-out) | $5B (shells $1.7B + fit-out ~$3.3B)   | $1.7B (shells only) to $11.9B (Epoch model)                                | Shells REPORTED (assessed real property, 1 Jan 2026). Fit-out ARITHMETIC, scaled from Abilene's state filings per MW and capped by Amazon's $8.9B reported total                                                   | Measured AI, 2026, https://measuredai.substack.com/p/aws-new-carlisle-data-center-campus ; Epoch AI, 2026                                                                                                                                                                  |
| New Carlisle | New power capacity                                    | $0.8B                                 | $0.19B (substations only) to $1.4B (substations + both gas plants in full) | $185M of substations REPORTED; gas plants: Big Sandy $299.5M REPORTED, Oregon Clean Energy Center ~$880M ARITHMETIC (price is sealed); site share 54% ARITHMETIC. Paid by the utility, recovered in rates          | PJM, 2024, https://pjm.com/-/media/committees-groups/committees/teac/2024/20241008/20241008-item-06---aep-supplemental-projects.ashx ; IURC, 2025, https://www.in.gov/iurc/files/ord_46217_111925.pdf ; IURC, 2026, https://www.in.gov/iurc/files/ord_46301GRS1_090226.pdf |
| New Carlisle | Land                                                  | $70M                                  | $48M to $100M                                                              | ARITHMETIC: no recorded price found. 870 to 1,200 acres x $55,000 to $83,000 per acre from two local comps                                                                                                         | WNDU, 2020, https://www.wndu.com/content/news/Next-steps-announced-for-Indiana-Enterprise-Center-571137531.html ; ABC57, 2024, https://www.abc57.com/news/microsoft-buys-st-joe-farm-property                                                                              |
| New Carlisle | Annual power spend (today's load)                     | $0.6B per year                        | $0.5B to $0.7B                                                             | ARITHMETIC: 1,244 MW x 0.9 x 8,760 h = 9.8 TWh x 6.1 cents/kWh (I&M Tariff I.P., transmission voltage, with riders)                                                                                                | Indiana Michigan Power tariff book, 2026, https://www.indianamichiganpower.com/lib/docs/ratesandtariffs/Indiana/IM_IN_TB_20_10-28-2026v1.pdf                                                                                                                               |
| Abilene      | Chips (whole servers and racks)                       | $17.5B                                | $16.7B to $40B (the Financial Times figure)                                | ESTIMATE: Epoch's $21.2B of servers per GW x 0.824 GW. Matches 5,600 NVL72 racks x $3.1M (SemiAnalysis) = $17.4B                                                                                                   | Epoch AI, 2026, https://epoch.ai/data-insights/ai-datacenter-cost-breakdown ; SemiAnalysis, 2025, https://newsletter.semianalysis.com/p/h100-vs-gb200-nvl72-training-benchmarks ; FT via The Register, 2025, https://www.theregister.com/2025/05/27/oracle_openai_40b/     |
| Abilene      | Networking                                            | $4.1B                                 | $2.4B to $7.2B                                                             | ESTIMATE: Epoch's $4.9B per GW (13%) x 0.824 GW. Low end is optics only (Nvidia's $6,000 per GPU); high end is 13% x the $55B built from the FT chip figure                                                        | Epoch AI, 2026 (same page)                                                                                                                                                                                                                                                 |
| Abilene      | Storage                                               | $0.4B                                 | $0.3B to $0.8B                                                             | ESTIMATE: Bernstein's 1 to 1.5% x Epoch's $31.2B site total = $0.31B to $0.47B; high end is 1.5% x $55B                                                                                                            | Bernstein via Investing.com, 2025 (URL above)                                                                                                                                                                                                                              |
| Abilene      | Buildings (shell + mechanical and electrical fit-out) | $9.4B (shells $2.3B + fit-out ~$7.1B) | $5.2B (state filings) to $14.5B (money raised, less the gas plant)         | Shells REPORTED ($292M x 8, Texas filings). Total ESTIMATE (Epoch's $11.4B per GW x 0.824)                                                                                                                         | TDLR, 2025, https://www.tdlr.texas.gov/TABS/Search/Project/TABS2025016966 ; Epoch AI, 2026 ; Crusoe, 2025 (the $15B)                                                                                                                                                       |
| Abilene      | New power capacity                                    | $0.65B                                | $0.5B to $0.7B                                                             | Gas plant up to $500M REPORTED (permit filing); two substations ~$150M ARITHMETIC (no public cost). Paid by Crusoe's joint venture and Lancium                                                                     | DCD, 2025, https://datacenterdynamics.com/en/news/natural-gas-plant-planned-for-stargate-ai-data-center-campus-report ; Epoch AI, 2026                                                                                                                                     |
| Abilene      | Land                                                  | $7M                                   | $4M to $11M                                                                | ARITHMETIC: no recorded price (Texas does not record sale prices). 1,100 acres x $3,487 to $10,000 per acre from 2026 listings next to the site                                                                    | Barnett & Hill listing, 2026, https://barnettandhill.com/tay/ ; Land.com listing, 2026, https://www.land.com/property/91.04-acres-in-taylor-county-texas/24775433                                                                                                          |
| Abilene      | Annual power spend (today's load)                     | $0.4B per year                        | $0.28B to $0.50B                                                           | ARITHMETIC: 1,154 MW x 0.8 x 8,760 h = 8.1 TWh x $46 to $53/MWh (ERCOT West zone wholesale + transmission and fees)                                                                                                | Potomac Economics, 2026, https://www.potomaceconomics.com/wp-content/uploads/2026/10/2026-09_Nodal_Monthly_Report.pdf ; NRG, 2025, https://www.nrg.com/assets/documents/energy-policy/ercot-transmission-costs-and-rate-design-remarks-on-feb-25-2025.pdf                  |

Sum of the capital rows: Abilene $32B (Epoch's site total is $31.2B; financing-based total is $55B).
New Carlisle $15.5B (Amazon reported $8.9B invested at 1 Jan 2026 with about 11 of 18 buildings
running; Epoch's Nvidia-priced total is $39.3B).

### How I read the sources

Read from raw text (quotes exact): Epoch AI's CSVs, the two IURC orders, the I&M tariff book, the
PJM slide decks, the Potomac Economics monthly reports, the NRG note. Everything else came through a
summarising fetch tool or search snippets, so check wording before quoting.

Could not get: the Oregon Clean Energy Center price (sealed by the IURC; SEC EDGAR blocks scripts
and the 10-Q text did not come through), any deed or sales-disclosure price for Amazon's land
(Indiana's sales-disclosure search needs a captcha), Taylor County appraisal records (the search
site refused the session), a cost for the Abilene substations, a Trainium3 unit cost, a Trainium
server price.

### 1. Chips

#### New Carlisle

Counts (Epoch AI, 2026): 1,044,976 Trainium2 in buildings 1 to 16, 104,067 Trainium3 in buildings 17
and 18.

Bare accelerators:

- Epoch's chip table prices Trainium2 at $4,000: "Unit cost per standalone chip approximately $4k,
  per SemiAnalysis". This is Amazon's cost, with no vendor margin.
  https://epoch.ai/data/ai_chip_sales_chip_types.csv
- 1,044,976 x $4,000 = $4.18B.
- Trainium3: Epoch's table has no cost and I found none. Assuming $7,000 (my assumption, 1.75x
  Trainium2): 104,067 x $7,000 = $0.73B.
- Bare total: about $4.9B.

Whole servers and racks:

- SemiAnalysis, 2024 (free part of the article): "the total networking connector and cabling cost
  will come up to nearly $1,000 per chip" for the 64-chip configuration and "~$1.2k per chip" for
  the 16-chip one. That is the in-server and in-rack cabling.
- Board, chassis, power, head-node CPUs: no source. I assumed about $2,000 per chip. So about $7,000
  per installed Trainium2.
- 1,044,976 x $7,000 = $7.3B. Trainium3 at an assumed $10,000 installed: $1.0B. Total $8.4B, call it
  $8B.
- Check against Amazon's own number: the county's compliance review says $8.9B was invested by 1 Jan
  2026, of which $1.7B was assessed real property (Measured AI, 2026). That leaves $7.2B of
  equipment. Epoch has 11 buildings running on 2025-12-23 (718,000 chips) and 16 by 2026-03-23.
  $7.2B / 718,000 = $10,000 per chip; $7.2B / 1,044,976 = $6,900. That equipment figure also holds
  cooling and electrical gear, so $7,000 to $10,000 is a ceiling on the per-chip server cost. $7,000
  fits.

Epoch's site model (Nvidia prices): compute $27.08B for 1,037 MW IT, of which servers 1.037 x
$21.19B = $22.0B and networking $5.1B. This is what the same wattage of Nvidia GB200 racks would
cost.

Paid by Amazon.

#### Abilene

- Epoch: servers $21,188M per GW of IT x 0.824 = $17.46B. Epoch's "compute cost" for the site,
  $21.52B, is this plus $4.06B of networking.
- SemiAnalysis, 2025: "the rack scale server alone costs $3.1M for a typical hyperscaler. Including
  networking, storage and other items, all in cost comes up to about $3.9M per rack." 403,200 GPUs /
  72 = 5,600 racks x $3.1M = $17.4B.
- Epoch's chip table: B200 $37,000, B300 $43,000 (these are system prices per GPU, not bare chips).
  100,800 x $37,000 + 302,400 x $43,000 = $16.7B.
- Financial Times via The Register, 2025: about $40B for about 400,000 GB200. That is $100,000 per
  GPU, twice what the other three sources give. It may cover networking and storage too, or a
  different period; unresolved.
- No bare-chip figure exists for Abilene: Nvidia sells these as racks.

Paid by Oracle.

### 2. Networking (estimate, no site-specific figures exist)

Shares: Epoch AI 2026 has "network infrastructure" at $4,925M of $37.9B per GW of IT (13.0%),
separate from servers. Bernstein 2025 has networking at about 13% of $35B per GW, but its 13%
includes DPUs, NICs and copper cabling that sit inside the Nvidia rack, so it partly overlaps a
whole-rack chips figure. I used Epoch's split.

Abilene:

- $4,925M x 0.824 = $4.06B (same as 13% x Epoch's $31.2B site total).
- Cross-checks: SemiAnalysis's $0.8M per rack for "networking, storage and other items" x 5,600
  racks = $4.5B. Nvidia's rule of about $6,000 of transceivers per GPU x 403,200 = $2.4B for optics
  alone. 13% x $55B (the $15B facility + $40B FT chip figure) = $7.2B.

New Carlisle:

- 13% x $11B (Amazon's announced campus budget, the only Amazon-reported total) = $1.43B. 13% x
  $8.9B (invested by 1 Jan 2026) = $1.16B.
- Epoch's Nvidia-calibrated figure: $4,925M x 1.037 = $5.1B. This overstates it for three reasons:
  AWS designs its own switches and network cards and books them at cost; each Trainium2 gets 200
  Gb/s of network against 400 to 800 Gb/s per GPU at Abilene (The Register, 2025); and chips inside
  a server are wired to each other with direct cables that are already in the chips row.
- A port-count sanity check (1.15M accelerators x roughly $2,000 of switch ports and optics each, my
  assumption) gives about $2B, inside the range.

### 3. Storage (estimate, no site-specific figures exist)

Bernstein 2025: storage is about 1 to 1.5% of capex, $350M to $500M per GW at $35B per GW. Epoch has
no storage line.

- Abilene: 1 to 1.5% x $31.2B = $0.31B to $0.47B. Per GW of IT: $350M to $500M x 0.824 = $0.29B to
  $0.41B. 1.5% x $55B = $0.83B.
- New Carlisle: 1 to 1.5% x $11B = $0.11B to $0.17B. 1 to 1.5% x Epoch's $39.3B = $0.39B to $0.59B.
  Storage need follows the size of the cluster more than the price of its chips, so the per-GW
  reading (1.037 x $350M to $500M = $0.36B to $0.52B) is as defensible as the share of Amazon's
  budget. Best $0.3B.

### 4. Buildings

#### Abilene

- Shells: Texas Department of Licensing and Regulation filings, 2025, $292,000,000 per 484,960 sq ft
  shell ($602 per sq ft). x 8 = $2.34B.
  https://www.tdlr.texas.gov/TABS/Search/Project/TABS2025016966 and
  https://www.tdlr.texas.gov/TABS/Search/Project/TABS2025011917
- Fit-out as filed: $384,000,000 per building "Tenant Improvement"
  (https://www.tdlr.texas.gov/TABS/Search/Project/TABS2025019019), building 1 filed at $140M. 7 x
  $384M + $140M = $2.83B. That is $3.7M per MW of IT.
- Shell + filed fit-out: $5.16B. These filings give construction contract values and leave out
  owner-supplied equipment (chillers, generators, switchgear; Crusoe makes its own switchboards), so
  they are a floor.
- Epoch model: facility $11,433M per GW x 0.824 = $9.42B (its "construction cost" of $9.70B adds
  land and utility works).
- Financing: the Crusoe / Blue Owl / Primary Digital joint venture raised $15B "to fund the 1.2
  gigawatt AI data center" (Crusoe, 2025). Less the gas plant ($0.5B) = $14.5B. Includes interest
  during construction, fees and contingency, so it is a ceiling.
- Bloomberg / Cushman & Wakefield, 2026 (via AI Weekly): shell and construction $2.4B per GW, power
  infrastructure $3B per GW.
- Best: $9.4B, of which shells $2.3B and mechanical and electrical fit-out about $7.1B.

Paid by the joint venture (Crusoe, Blue Owl, Primary Digital), mostly with JPMorgan-led loans;
Oracle pays it back as rent.

#### New Carlisle

- Shells: $1.7B of assessed real property at 1 Jan 2026, when all 18 buildings were construction
  complete (Measured AI, 2026, single secondary source). About $94M per building. Consistent with
  WVPE, 2024: each shell "will generate $2.3 million worth of taxes per year" before abatement.
- Fit-out: no source. Abilene's filed $3.7M per MW x 1,037 MW = $3.9B. Abilene's $792 per sq ft x
  3.89M sq ft = $3.1B.
- Ceiling from Amazon's own total: $8.9B invested by 1 Jan 2026 less $1.7B of real property less
  about $5B of servers then installed (718,000 x $7,000) leaves about $2.2B for other equipment. So
  fit-out is probably $2B to $4B. I used $3.3B.
- Epoch model: $11,433M per GW x 1.037 = $11.9B. Calibrated on liquid-cooled Nvidia sites; New
  Carlisle is mostly air-cooled at about 27 kW per rack (SemiAnalysis, 2024) and Amazon's reported
  total rules this out.
- Best: about $5B.

Paid by Amazon.

### 5. New power capacity

#### New Carlisle

Substations and transmission (REPORTED, primary):

- PJM, AEP supplemental project AEP-2023-IM023, solution meeting 2024-10-08: "A customer has
  requested new service for 1100MW of load in New Carlisle, IN area. Initial service is requested by
  12/15/2026." Larrison Drive 345 kV station $70.38M, New Prairie 345 kV station $79.53M, Olive
  station $29.287M, remote-end work and a sag study $5.78M. "Transmission Cost Estimate: $155.69 M
  $184.977M" (the first figure is the June 2024 estimate).
- A second request, AEP-2024-IM016 (PJM, AEP Local Plan 2026): "437MW of load in the New Carlisle,
  IN area", Navistar 345 kV station, "Estimated Cost: $50.364 M", in service 2027-03-15. The
  customer is not named; it is probably the same campus's expansion.
  https://www.pjm.com/-/media/DotCom/committees-groups/committees/teac/2026/20261006/20261006-informational-only---aep-local-plan-submission-of-the-supplemental-projects-for-2026.pdf
- Who paid: AEP's transmission companies build these as supplemental projects and recover them
  through AEP-zone transmission rates, which every customer in the zone pays, Amazon included.

Gas plants bought by Indiana Michigan Power (I&M):

- Oregon Clean Energy Center, 870 MW, owned since 2026-03-03. Price sealed: the order calls it "the
  confidential best estimate" and the Journal Gazette, 2026, reports terms undisclosed. Inference:
  the order says disallowing the return "would result in a disallowance of approximately $55 million
  of annual after-tax carrying costs" and "this represents nearly 50% of the $116 million annual
  non-fuel revenue requirement associated with Oregon." $55M / 6.25% (my assumption for I&M's
  after-tax weighted cost of capital; 6% to 7% gives $790M to $920M) = about $880M, or $1,010 per
  kW. I&M's 2026 note prospectus says a $650M issue would "fund a portion of the purchase price".
  https://www.in.gov/iurc/files/ord_46217_111925.pdf
- Big Sandy peaker, 318 MW: "the purchase price of $299,525,000", "$1,014/kilowatt". IURC, 2026.
  https://www.in.gov/iurc/files/ord_46301GRS1_090226.pdf
- Bought so far: about $1.18B for 1,188 MW, close to the site's present 1.2 GW draw.
- Pending, prices not found: Sycamore Riverside (918 MW, new, I&M to own from March 2029) and
  Rockport Energy Center (1,520 MW, new, summer 2030). Citizens Action Coalition puts the whole plan
  at "more than $7 billion" (Earthjustice, 2025; advocacy estimate).

Site share: I&M has "executed ESAs for approximately 4,200 MW of new load" (IURC, 2026). Amazon's
filing is 2,250 MW at full buildout (The Times via GovTech, 2025). 2,250 / 4,200 = 54%.

- Best: $185M + 54% x $1.18B = $0.82B.
- Low: $0.19B (substations only, the part built physically for the site). High: $185M + $50M +
  $1.18B = $1.4B. At full buildout, 54% of the $7B plan would be $3.8B.

Who paid: I&M buys the plants and puts them in its rate base. Amazon pays through Tariff I.P.
(12-year contract, minimum bill at 80% of contract capacity). Under the settlement I&M nets
large-load revenue against the plant costs; I&M says revenue growth exceeds Oregon's $116M a year.
Citizens Action Coalition estimates at least 39% of the plan's costs fall on other customers
in 2030.

#### Abilene

- Gas plant: 360.5 MW, ten simple-cycle turbines, "expected to cost up to $500 million" per the
  permit filing (DCD and Business Insider, 2025, read as search snippets). About $1,390 per kW.
  Built and owned by Crusoe's side.
- Substations: a 200 MW, 138 kV substation (2022, expanded 2024) and a 1 GW, 345 kV substation
  (energized March 2026), built by Mortenson for Lancium. Cost not public. Estimate: Epoch's utility
  works at $164M per GW x 0.824 = $135M; New Carlisle's PJM figure of $185M for 1.1 GW of 345 kV
  stations gives $170M per GW. I used $150M.
- Transmission lines to the site: AEP Texas; cost not found; recovered from all ERCOT load through
  the transmission charge.
- Battery (1,000 MW / 4,000 MWh in a May 2025 Lancium plan): not confirmed built, not included.
- Best: $0.5B + $0.15B = $0.65B.

### 6. Land

#### New Carlisle

No purchase price found. Amazon bought through Razor5 LLC; WVPE, 2023 and 2024, reports only a $1
million payment for survey access, with "a sale price will have to be negotiated later." Acreage:
870 (abatement parcels) to 1,200 (NYT, 2025).

Local comps:

- Indiana Enterprise Center, the same industrial area: "Two families that collectively own 732 acres
  of farmland have signed agreements" giving the county options "at a price of $55,000 per acre", "a
  grand total of more than $40 million" (WNDU, 2020).
- Microsoft, Granger, same county: 929 acres for $77.5M, from the county recorder's deed (ABC57 and
  South Bend Tribune, 2024). $83,400 per acre.
- Farm value for scale: Indiana top-quality farmland averaged $14,826 per acre (Purdue, 2025). 870
  acres at farm value would be $13M.

Arithmetic: 870 x $55,000 = $48M; 870 x $83,400 = $73M; 1,200 x $55,000 = $66M; 1,200 x $83,400 =
$100M. Best $70M.

#### Abilene

Lancium owns the 1,100 acres and leases ground to Crusoe (about 90 acres for phase 1); the rent is
not public. Texas does not record sale prices. 2026 asking prices: 648 acres including tracts
"adjacent to the Stargate / Lancium / Crusoe facility" at "$3487/ac" (Barnett & Hill), and a 91-acre
tract near the site at $10,000 per acre (Land.com). Lancium bought in 2021, before the boom, so the
low end is more likely.

Arithmetic: 1,100 x $3,487 = $3.8M; 1,100 x $10,000 = $11M. Best $7M.

For both sites Epoch's model books land at $172M per GW of IT ($178M and $142M). That is a generic
allowance, far above what raw land costs at either place.

### 7. Annual power spend, today's load

#### New Carlisle

Tariff I.P., transmission voltage (I&M tariff book, I.U.R.C. No. 20, 2026): demand $10.194 per
kW-month; energy 5.058 cents for the first 410 kWh per kW and 1.286 cents above. Riders for the I.P.
class per kW-month: fuel 0.549, environmental 0.378, PJM 7.316, resource adequacy 0.242, solar
0.045, phase-in -0.343, tax 0.952. Riders per kWh in cents: fuel -0.1219, environmental 0.0407, PJM
-0.4297, solar 0.0013, phase-in -0.0003, demand-side (opt-out) 0.0218.

At a 90% load factor (Amazon's own figure in its IURC filing), per kW-month: 657 kWh; demand $19.33;
energy $23.91; kWh riders -$3.21; total $40.04 = 6.09 cents per kWh. At 80% it is 6.76 cents; at
100%, 5.56 cents.

- 1,244 MW x 0.9 x 8,760 h = 9.81 TWh x 6.09 cents = $598M. With 1,200 MW: 9.46 TWh, $577M.
- Because half the bill is demand charges, the total barely moves with load factor: $589M at 80%,
  $606M at 100%.
- Amazon's contract terms are not public and may differ from the published tariff. Epoch's model has
  energy at about $0.6B a year per GW of IT, which gives $0.62B.

#### Abilene

Wholesale: ERCOT West load zone monthly average real-time prices (Potomac Economics, 2026): calendar
2025 $41.38/MWh (day-ahead $42.31); October 2025 to September 2026 $34.18 (day-ahead $35.96);
January to September 2026 $31.64. Simple averages of monthly figures.

Delivery and fees: "ERCOT's transmission rate is currently $66.76 per kilowatt-year" (NRG, 2025),
charged on demand at the four summer peaks. 1,150 MW x $66.76 = $77M a year, or $9.50/MWh over 8.1
TWh. Ancillary services and ERCOT fees: about $2.50/MWh (my allowance). So about $12/MWh on top of
wholesale.

- Load: 1,154 MW peak at the meter assumes a peak power usage effectiveness of 1.4; the yearly
  average is lower. I used a 0.8 load factor: 8.09 TWh.
- 8.09 TWh x ($34.18 + $12) = $372M. With 2025 prices ($41.38 + $12): $429M. Best $0.4B.
- Low: energy only at the last-12-month price, 8.09 x $34.18 = $277M. High: 1,200 MW x 0.9 = 9.46
  TWh x $53 = $501M.
- Some power comes from the on-site turbines (Grid Status, 2026, models about a quarter; Crusoe says
  backup only). Fuel for a simple-cycle turbine at West Texas gas prices costs about the same as
  grid power or less, so it does not move the total much.
- Epoch's model gives about $0.49B for energy at this site.

### Not found

- Oregon Clean Energy Center purchase price (sealed).
- Sycamore Riverside and Rockport Energy Center costs.
- Deed or sales-disclosure price for Amazon's New Carlisle land.
- Lancium's land price, Crusoe's ground rent, and the cost of the Abilene substations and
  transmission lines.
- A published Trainium3 unit cost or Trainium server price.
- Any site-specific networking or storage spend.
- Amazon's actual contract rate with I&M and Oracle's or Crusoe's actual power contract at Abilene.
