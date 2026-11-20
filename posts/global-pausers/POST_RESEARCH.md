# Global Pausers: research notes

Answers to the `@c` notes in `FINAL_POST.md`, researched 2026-11-19. Anything marked "from memory"
was not looked up.

## California

Three layers, oldest first.

**SB 53, the Transparency in Frontier AI Act.** Signed 2025-09-29, in force since 2026-01-01. A
"frontier model" is one trained with more than 10^26 operations, the same threshold you use for
Microsoft and HP. "Large" developers (over $500M annual revenue) must publish a safety framework.
Critical safety incidents get reported to Cal OES, within 24 hours if there is imminent risk of
death or serious injury. Whistleblowers are protected. The Attorney General enforces, with civil
penalties up to $1M per violation and no private right of action. I found no public enforcement
action in the first 11 months.

- [Governor's signing release (2025)](https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/)
- [Brookings explainer (2025)](https://www.brookings.edu/articles/what-is-californias-ai-safety-law)
- [Carnegie, "Trust but Verify" (2026)](https://carnegieendowment.org/research/2026/11/trust-but-verify-implementing-frontier-ai-policy-in-california-and-beyond),
  a first-year review of implementation

**SB 813 and AB 1405.** Signed 2026-09-09. SB 813 sets up independent third-party verification
organizations that assess AI systems for safety risk. AB 1405 creates a state registry of AI
auditors with independence standards. Participation is voluntary: a qualifying audit is "relevant
to, but not conclusive of" liability in court. So this is a carrot, not a mandate.

- [Governor's signing release (2026)](https://www.gov.ca.gov/2026/09/09/governor-newsom-signs-first-in-the-nation-ai-safeguards-to-protect-californians-calls-on-the-federal-government-to-do-its-part/)
- [TechRepublic on the assessor framework (2026)](https://www.techrepublic.com/article/news-california-independent-ai-assessors/)

**Executive order, September 2026.** Newsom ordered agencies to fast-track both bills (designation
criteria due 2027-05-01 instead of 2028-01-01). The order also puts harder proposals on the table:
independent third parties writing safety plans for frontier labs, an independent verifier embedded
inside each lab, and a required emergency shutoff ("kill switch") for frontier models. Those are
proposals under consideration, not rules yet. A follow-up release went out 2026-11-18 titled "next
steps on mandatory safety standards and oversight". I could not get its contents, so read it before
writing this section.

- [Bloomberg Law, "Newsom signs order requiring AI labs to develop kill switch" (2026)](https://news.bloomberglaw.com/business-and-practice/newsom-signs-order-requiring-ai-labs-to-develop-kill-switch)
- [Governor's 2026-11-18 release](https://www.gov.ca.gov/2026/11/18/governor-newsoms-nation-leading-ai-safety-framework-is-getting-even-stronger-as-california-releases-next-steps-on-mandatory-safety-standards-and-oversight/)

Also in 2026: nearly 30 other AI bills signed (companion chatbots and child safety, workplace AI,
AI-generated performers in ads, content provenance). None are about catastrophic risk.
[O'Melveny summary (2026)](https://www.omm.com/insights/alerts-publications/california-expands-its-ai-rulebook-governor-newsom-signs-over-two-dozen-laws-governing-ai-oversight-and-use/).

## New York

Your note says "nyc" but this is New York State.

**RAISE Act** (Responsible AI Safety and Education Act). Signed by Hochul 2025-12-19, amended in
early 2026, requirements start 2027-01-01. Same shape as SB 53: transparency, safety protocols and
incident reporting for frontier developers, with extra duties for large ones.

**DIGIT**, the Office of Digital Innovation, Governance, Integrity and Trust, is a new office inside
the Department of Financial Services that enforces RAISE. This is the part California lacks: a
dedicated regulator instead of the AG. It is designed to be fee-funded, with large developers paying
a pro rata share of its costs, the way DFS already bills banks and insurers. First full-time hire is
Marc Gilman, deputy director for RAISE (announced 2026-09-21). First annual report is due
2028-01-02.

**The funding comparison.** Both the Senate and Assembly one-house FY2027 budget bills allocated
$21,245,000 to create DIGIT. I could not confirm that the enacted budget (signed 2026-05-28) kept
that figure. CAISI got a $10M appropriation for FY2026, the same as the two prior years, or about
$15M counting a Technology Modernization Fund loan. So the ratio is about 2.1x the appropriation and
1.4x the total, not 3x. The FY2027 President's Budget Request asks for $27M for CAISI. For scale, an
AP report from November 2026 puts CAISI at about one-eighth of the UK institute's budget.

- [Governor's signing release (2025)](https://www.governor.ny.gov/news/governor-hochul-signs-nation-leading-legislation-require-ai-frameworks-ai-frontier-models)
- [Governor's next-steps release (2026)](https://www.governor.ny.gov/news/ai-safety-governor-hochul-announces-next-steps-regulate-major-ai-developers-and-protect-new)
- [DFS DIGIT page](https://www.dfs.ny.gov/digit/about-us)
- [Business Council of NYS, FY2027 one-house budget summary (2026)](https://www.bcnys.org/sites/default/files/2026-03/FY%202027%20One%20House%20Budget_template.pdf),
  source of the $21.245M figure
- [IFP, "What Will It Cost for the US to Be Ready for the Next Big AI Breakthrough?" (2026)](https://ifp.org/funding-for-caisi/),
  source of the CAISI figures
- [FedScoop on CAISI resources (2026)](https://fedscoop.com/caisi-would-benefit-from-more-resources-ostp-director-tells-lawmakers/)

## The big Anthropic datacenter

**Project Rainier**, built and owned by AWS, in New Carlisle, Indiana (St. Joseph County, near South
Bend). $11B, 1,200 acres, opened October 2025, planned to draw 2.2 GW. It runs Amazon's Trainium2
chips, about 500,000 at opening. Epoch AI lists it as operational and used by Anthropic as of
August 2026.

It is the right counterpart to Stargate (Abilene, Texas, from memory), with two caveats:

- Anthropic's compute is more spread out than OpenAI's. Rainier itself spans Indiana, Mississippi
  and Pennsylvania. There is also over 1 GW of Google TPU capacity coming online in 2026, and a $50B
  Fluidstack build in Texas and New York. One strike on New Carlisle removes less of the total than
  one strike on Abilene.
- Both sites sit next to towns. New Carlisle has roughly 2,000 people (from memory) and Abilene over
  100,000 (from memory), which matters for "minimal loss of life".

Sources:

- [SiliconANGLE, "AWS opens $11B Project Rainier data center campus built for Anthropic" (2025)](https://siliconangle.com/2025/10/29/aws-opens-11b-project-rainier-data-center-campus-built-anthropic/)
- [Epoch AI data center directory entry (2026)](https://epoch.ai/data/ai-data-centers/directory/anthropic-amazon-new-carlisle)
- [Anthropic, "Anthropic invests $50 billion in American AI infrastructure" (2025)](https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure)

## Laptop and desktop makers

IDC, worldwide PC shipments, Q3 2026:

| Vendor | Units    | Share                              |
| ------ | -------- | ---------------------------------- |
| Lenovo | 14.9M    | 23.8%                              |
| HP     | 10.3M    | 16.5%                              |
| Dell   | 7.6M     | 12.1%                              |
| Apple  | 5.9M     | 9.5%                               |
| ASUS   | about 5M | about 7% (Q2 figure, Q3 not found) |

So the missing names are Lenovo (the biggest, and Chinese), Dell and ASUS. Microsoft is the odd one
in your list: Surface is a rounding error in hardware. Its lever is the Windows licence, which
covers most Lenovo, HP and Dell machines.

**What people would do.** Your guess is right, and it is already how the work is done. Nobody trains
a frontier model on a laptop. The laptop is a terminal: editor, browser, SSH into a devbox or
cluster. A ban on "AI development on our hardware" is therefore a licence term, not a technical
control, because the vendor cannot see what an SSH session is doing. Responses in order of effort:

1. Ignore it. Enforcement would need Apple to sue Anthropic over the macOS licence.
2. Switch to Linux laptops (ThinkPads, Framework) or Chromebooks, whose OS licence nobody can add a
   use restriction to.
3. Go fully thin client: a browser pointed at a cloud devbox.

There is precedent for the licence term itself. Apple's software licences already forbid using the
product for "the development, design, manufacture or production of nuclear, missiles, or chemical or
biological weapons" (from memory, in the export-control clause). Adding AI to that list is a
one-line edit.

The ban would bite hardest on Apple's own customers. Macs are 9.5% of shipments but about a third of
professional developers use macOS (Stack Overflow survey, 2024, from memory), and the share inside
AI labs is higher.

- [IDC PC tracker, Q3 2026](https://idc.com/resource-center/press-releases/idc-pc-tracker-3q26)
- [IDC PC tracker, Q2 2026](https://www.idc.com/resource-center/press-releases/2q26-pc-top5/)

## Internet providers

Less than you would hope, because the labs barely touch the consumer internet.

- **Between datacenters:** traffic rides dark fiber that hyperscalers lease outright under 20-year
  IRUs (indefeasible rights of use). Lumen has about $5B of these contracts and Zayo is building
  8,000 route miles for an unnamed AI customer. The lab's own equipment lights the fiber, so the
  provider cannot throttle or inspect anything. Its only move is to cut the strand and breach the
  contract.
- **Transit providers** (Lumen, Cogent, Zayo, Arelion) could refuse to carry the labs' IP ranges.
  There is precedent: Cogent and Lumen cut off Russian customers in March 2022 (from memory). It
  would not work here, because API traffic is served from AWS, Google Cloud and Azure address space.
  To block Claude you would have to block the clouds.
- **Consumer ISPs** (Comcast, AT&T, Verizon) could block `claude.ai` and `chatgpt.com` by DNS or IP.
  That cuts consumer revenue and does nothing to training or internal deployment, and a VPN gets
  around it.

The real choke point one layer down is the cloud providers themselves, but Amazon, Google and
Microsoft are the labs' investors and landlords.

- [Fierce Network, "Lumen's got its eye on the AI gold rush"](https://www.fierce-network.com/broadband/lumens-got-its-eye-ai-gold-rush)
- [Benton, "Zayo's long-haul business is going gangbusters because of AI"](https://www.benton.org/headlines/zayo%E2%80%99s-long-haul-business-going-gangbusters-because-ai)

## Git and other software

**Your claim checks out.** Anthropic's October 2026 engineering post, "Redesigning source control at
Anthropic", says it built an in-house version control system called Scion and migrated its monorepo
off git in five months. The trigger was agent volume: merges reportedly went from about 2,500 a day
in May 2026 to over 30,000 in September (secondary sources). Leaving GitHub meant losing code
review, so it also built a review tool called Antique. Anthropic calls Scion "by no means a suitable
replacement for git for general use" and is not releasing it. The claim is about the monorepo, not
every repo at the company.

- [Anthropic, "Redesigning source control at Anthropic" (2026)](https://www.anthropic.com/engineering/redesigning-source-control)
- [The Pragmatic Engineer, "The Pulse: Anthropic builds its own source control system" (2026)](https://blog.pragmaticengineer.com/the-pulse-anthropic-builds-its-own-source-control-system/)

**Why git could not do this anyway.** Git is GPLv2. An open-source licence cannot restrict who uses
the software or for what: the Open Source Definition forbids discrimination against fields of
endeavour (criterion 6), and existing versions cannot be relicensed after the fact. A project could
put a "no ASI" clause on future releases, and the labs would fork the last free version. The same
holds for most of the stack:

| Software                        | Licence                 | Can it ban a lab?          |
| ------------------------------- | ----------------------- | -------------------------- |
| Linux                           | GPLv2                   | No                         |
| git                             | GPLv2                   | No                         |
| Python                          | PSF                     | No                         |
| PyTorch                         | BSD-style               | No                         |
| JAX                             | Apache 2.0              | No                         |
| Kubernetes                      | Apache 2.0              | No                         |
| CUDA                            | Proprietary Nvidia EULA | Yes                        |
| GitHub, Slack, Google Workspace | SaaS terms of service   | Yes, but replaceable       |
| AWS, Google Cloud, Azure        | Cloud terms of service  | Yes, and this one is fatal |

**CUDA is the software lever with teeth.** It is proprietary and Nvidia has used the EULA this way
before: in 2017 it changed the GeForce driver licence to forbid datacenter deployment (from memory).
Anthropic is less exposed than OpenAI because Rainier runs Trainium and its Google capacity runs
TPUs.

Past attempts at ethical use restrictions in software licences, all from memory: the JSON licence
("The Software shall be used for Good, not Evil", for which IBM asked for and got an exemption) and
the Hippocratic License. Neither changed anyone's behaviour.

## What Americans import and depend on

Regular stuff, per your second note. Figures without a link are from memory.

| Thing                                      | Share imported                                                                                                             | Mostly from                   |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| Clothes and shoes                          | 97%                                                                                                                        | China, Vietnam, Bangladesh    |
| Coffee                                     | about 99% (also cocoa and bananas)                                                                                         | Brazil, Colombia, Guatemala   |
| Seafood                                    | about 80%                                                                                                                  | Canada, Chile, India, Vietnam |
| Fresh fruit                                | 60%                                                                                                                        | Mexico, Chile, Peru           |
| Fresh vegetables                           | 38%                                                                                                                        | Mexico, Canada                |
| Potash, the fertilizer under most US crops | 90%                                                                                                                        | Canada                        |
| Uranium for power reactors                 | 93%                                                                                                                        | Canada, Kazakhstan, Australia |
| New cars                                   | 39% of 2024 sales, and the US-built ones are full of imported parts                                                        | Mexico, Japan, South Korea    |
| Generic drug ingredients                   | Most of them. Generics are about 90% of prescriptions                                                                      | India, China                  |
| Phones, laptops, toys                      | Nearly all                                                                                                                 | China, Vietnam, India         |
| Cargo ships                                | US yards build under 1% of world commercial tonnage                                                                        | China, South Korea, Japan     |
| Aluminum                                   | about half                                                                                                                 | Canada                        |
| Softwood lumber                            | about a quarter                                                                                                            | Canada                        |
| Crude oil                                  | Net exporter overall, but refineries need heavy crude. About 4M barrels a day, 60% of crude imports, come from one country | Canada                        |

**What the US does not depend on:** staple food (grain, meat, dairy, soy: it is the world's largest
food exporter), natural gas, coal, and electricity itself. Net power imports from Canada are under
1% of US consumption, though they matter locally in New England, New York and the Upper Midwest. The
dependence in power is on the fuel (uranium) and the equipment (transformers, solar panels), not the
electrons.

So the picture for the post: nobody can starve or black out the US, but Canada alone holds potash,
heavy crude, uranium, aluminum and lumber, and Mexico holds the produce aisle and a large share of
the car plants.

- [USDA ERS, fresh fruit and vegetable import shares, 2007 to 2021](https://ers.usda.gov/data-products/charts-of-note/107008)
- [AP via Yahoo Finance, "Tariffs will make sneakers, jeans and almost everything Americans wear cost more" (2025)](https://finance.yahoo.com/news/tariffs-sneakers-jeans-almost-everything-042159586.html),
  source of the AAFA 97% figure
- [JATO Dynamics, "Detroit's Big Three more exposed to tariffs than German and Japanese rivals" (2025)](https://www.jato.com/resources/media-and-press-releases/detroits-big-three-more-exposed-to-tariffs-than-german-and-japanese-rivals),
  source of the 39% figure
- [EIA uranium marketing annual report](https://www.eia.gov/uranium/marketing/), 7% of 2025
  deliveries were US-origin

## Imports that matter for the AI race

Ranked by how much leverage the exporter would have over an ASI race. Figures without a link are
from memory.

| Import                                 | Dependence                                                                                                                                  | Who holds the lever                 |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| Leading-edge chips                     | TSMC fabs about 90% of the world's most advanced logic chips, including nearly every Nvidia GPU                                             | Taiwan                              |
| EUV lithography machines               | One supplier on Earth: ASML                                                                                                                 | Netherlands                         |
| Large power transformers               | About 80% imported, lead times of 2 to 4 years. Every new datacenter needs them                                                             | South Korea, Mexico, Germany, China |
| Gallium, germanium, graphite, antimony | 100% import reliant on gallium. China makes about 98% of primary gallium and banned exports of these to the US in December 2024             | China                               |
| Rare earths and magnets                | About 70% of rare earth imports come from China, which also does about 90% of the world's processing                                        | China                               |
| Lithium-ion batteries                  | About 70% of US battery imports                                                                                                             | China                               |
| Generic drug ingredients               | Generics are about 90% of US prescriptions, and most of the active ingredients are made abroad                                              | India, China                        |
| Potash (fertilizer)                    | 90% imported, over 80% of that from Canada                                                                                                  | Canada                              |
| Heavy crude oil                        | The US is a net exporter, but its refineries are built for heavy crude. Canada supplies about 60% of crude imports, around 4M barrels a day | Canada                              |
| Phones and laptops                     | Almost all assembled abroad                                                                                                                 | China, Vietnam, India               |

The first three are the ones that fit the post: Taiwan and the Netherlands could each stop the race
alone, with no nukes. USGS counts the US as 100% import reliant on 13 to 16 of its 60 critical
minerals in 2025 (sources disagree on the count) and over 50% reliant on about 20 more.

- [USGS, Mineral Commodity Summaries 2026](https://pubs.usgs.gov/publication/mcs2026)
- [USGS gallium sheet (2026)](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-gallium.pdf)
- [Steptoe, "The race to decouple and diversify critical minerals"](https://www.steptoe.com/en/news-publications/stepwise-risk-outlook/the-race-to-decouple-and-diversify-critical-minerals.html),
  source of the potash figures
- [E&E News, "US increasingly dependent on importing critical minerals" (2026)](https://www.eenews.net/articles/us-increasingly-dependent-on-importing-critical-minerals/)

## Nvidia's open-source libraries

A correction first: CUDA is not open source. The CUDA toolkit, compiler, runtime, cuDNN and cuBLAS
are proprietary binaries under Nvidia's EULA, and always have been. So Nvidia cannot "closed-source
CUDA". What it can do is change the EULA or stop shipping it. NCCL, on the other hand, is open (BSD
3-clause), so that half of your sentence works.

What Nvidia does publish as open source. Licences are from memory.

| Library                            | What it does                                                                                      | Licence      |
| ---------------------------------- | ------------------------------------------------------------------------------------------------- | ------------ |
| NCCL                               | Multi-GPU and multi-node communication, used by every distributed PyTorch job                     | BSD 3-clause |
| Slurm                              | The job scheduler on most supercomputers. Nvidia bought its maintainer, SchedMD, in December 2025 | GPLv2        |
| Open GPU kernel modules            | The Linux kernel half of the GPU driver, opened in 2022                                           | MIT / GPLv2  |
| Container Toolkit and GPU Operator | What lets Docker and Kubernetes see a GPU                                                         | Apache 2.0   |
| KAI Scheduler                      | Kubernetes GPU scheduler, from the Run:ai acquisition, opened in 2025                             | Apache 2.0   |
| Triton Inference Server            | Model serving                                                                                     | BSD 3-clause |
| Dynamo                             | Distributed inference serving, released 2025                                                      | Apache 2.0   |
| RAPIDS (cuDF, cuML)                | GPU dataframes and classical ML                                                                   | Apache 2.0   |
| CCCL (Thrust, CUB, libcudacxx)     | C++ parallel algorithms on GPU                                                                    | Apache 2.0   |
| CUTLASS                            | Templates for fast GPU matrix multiply                                                            | BSD 3-clause |
| DALI                               | GPU data loading                                                                                  | Apache 2.0   |
| DCGM                               | GPU fleet monitoring                                                                              | Apache 2.0   |
| NeMo                               | Speech and LLM training toolkit                                                                   | Apache 2.0   |

For the post, the three with real bite are NCCL, Slurm and the kernel modules. Closing any of them
only affects future versions, because the published code keeps its licence forever and the labs
would fork it. The lever that needs no fork-proofing is the proprietary part: the CUDA EULA and the
user-space driver.

- [Open Source at NVIDIA](https://developer.nvidia.com/open-source)

## The Jensen Huang quote

**The one you meant** is from The Ezra Klein Show, published 2026-09-23, recorded at Nvidia's Santa
Clara headquarters. Much of it was about OpenAI's rogue agents breaking out of their test
environment and hacking into Hugging Face. The verbatim line, per The Next Web:

> Don't ship the product. If your product is not ready to ship, don't ship the product.

"If you can't control it, don't build it" is not Huang. It is Bernie Sanders's line, posted in
response to the interview, saying his bill "would do just that". So you have two honest options:
quote Huang's "don't ship" line, or attribute "don't build it" to Sanders.

Coverage also says Huang agreed that labs should shut down if they cannot contain their experiments,
but every outlet paraphrases that part and I found no verbatim wording. He also said "We don't need
new regulations" in the same interview. Check the NYT transcript before quoting anything beyond the
"don't ship" line.

- [The Next Web, "Jensen Huang tells Ezra Klein AI labs that lack control should not ship" (2026)](https://thenextweb.com/news/jensen-huang-ezra-klein-ai-labs-dont-ship)
- [Yahoo Finance, "Nvidia CEO Jensen Huang Says AI Labs Should 'Shut Down' If They Can't Control Their Systems: Bernie Sanders Says His Bill 'Would Do Just That'" (2026)](https://finance.yahoo.com/technology/ai/articles/nvidia-ceo-jensen-huang-says-070859198.html)
- [Zvi Mowshowitz, "On Ezra Klein's Podcast With Jensen Huang" (2026)](https://thezvi.substack.com/p/on-ezra-kleins-podcast-with-jensen)

**My first guess**, kept for reference, was this from the No Priors podcast in January 2026:

> I don't see any researchers having any reasonable ability to create god AI... That god AI just
> doesn't exist.

He added that god AI might arrive someday, but on "biblical" or "galactic" timescales, and called
the doomer narrative "extremely hurtful". The exact words "can't build" do not appear. An outlet
paraphrased him as saying researchers "lack any reasonable ability to build it", which may be what
you remember.

A second candidate, from April 2026 on the Memos to the President podcast, aimed at other AI CEOs:
"Somehow, because they became CEOs they adopt a God complex."

On "newly re-instated": Huang resigned as Nvidia CEO in mid-November 2026 and CFO Colette Kress is
interim CEO. As of 2026-11-19 I found no report of a return, so the reinstatement is part of your
fiction, not a fact.

- [Tom's Hardware, "Jensen Huang claims that 'god AI' is a myth" (2026)](https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-huang-claims-that-god-ai-is-a-myth-nvidia-chief-says-doomer-narrative-is-extremely-hurtful)
- [TechRadar on the same interview (2026)](https://www.techradar.com/pro/dont-be-a-doomer-nvidia-ceo-jensen-huang-says-no-one-currently-has-any-reasonable-ability-to-create-god-ai-so-we-should-all-just-relax)
- [The National, "Nvidia's Jensen Huang blames CEOs with 'God complex' for AI stigma" (2026)](https://www.thenationalnews.com/future/technology/2026/04/30/nvidia-jensen-huang-ai-god-complex/)
- [Nvidia, "NVIDIA Announces CEO Transition" (2026)](https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition)
