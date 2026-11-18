# 07: Bay Fill in San Francisco: What Was Done, and What If We Did More

Research notes, compiled 2026-11-17. Estimates I built myself are labeled "my arithmetic" with
inputs linked. Conversions: 1 sq mi = 640 acres = 2.59 km²; 1 ha = 2.471 acres; S$1 = US$0.75;
HK$7.8 = US$1; DKK 7 = US$1.

## Headline Findings

- **What % of SF's land is reclaimed? About 18%.** USGS mapping
  ([Knudsen et al., 2000](https://pubs.usgs.gov/of/2000/of00-444/)) classifies 5,284 acres (8.3 sq
  mi) of the city's 29,823 acres of land as "artificial fill over Bay mud": ground that was open
  Bay, mudflat or tidal marsh before the 1850s. That is 17.7% with Treasure Island, 16.5% without. I
  computed it from the USGS shapefile because nobody seems to have published it;
  [National Geographic (2017)](https://www.nationalgeographic.com/news/2017/06/Boston-landfill-maps-history/)
  says San Francisco's "landfill hasn't been comprehensively totaled".
- **The Bay shrank by about a third, mostly by diking, not filling.** BCDC:
  [787 sq mi of open water and bordering wetlands in 1849, 548 sq mi by mid-20th century](https://arccadigest.org/?p=39433),
  a 30% loss. The
  [1999 Baylands Goals report](https://www.waterboards.ca.gov/waterrights/water_issues/programs/bay_delta/docs/cmnt081712/sldmwa/goalsproject1999.pdf)
  counts roughly 137,000-139,000 acres diked against 50,000 filled. Tidal marsh fell from 190,000
  acres to 40,000.
- **Gold miners put far more material into the Bay than San Francisco did.** Gilbert (1917)
  estimated
  [1.146 billion cubic yards](https://www.waterboards.ca.gov/waterrights/water_issues/programs/bay_delta/deltaflow/docs/exhibits/swrcb/swrcb_krone1979.pdf)
  of hydraulic mining debris settled in the bays by 1914, about 75 times the
  [11.7 million m³](https://pubs.usgs.gov/circ/2004/c1259/c1259_tagged.pdf) of fill behind San
  Francisco's whole waterfront (my arithmetic: 876 / 11.7).
- **The trend has reversed.** Since 1969 the Bay has
  [grown by 23,637 acres](https://vitalsigns.mtc.ca.gov/indicators/bay-restoration), mostly salt
  ponds reopened to the tide.
- **Making land is cheap next to SF land prices; making a neighborhood is not.** My estimate for
  engineered fill in 2 m of water is $2-3 million per acre. Residential land in San Francisco was
  worth [$24.3 million per acre in 2022](https://www.fhfa.gov/research/papers/wp1901). With streets,
  utilities and transit the cost is about $7 million per gross acre against about $12 million of
  saleable value. It pencils in San Francisco proper, roughly breaks even at Bayview prices and
  loses money at East Bay prices.
- **Zoning is the binding constraint.** San Francisco at Paris density would hold 1.6 million homes,
  1.2 million more than today, on existing land. Getting 1.2 million homes from fill at Paris
  density takes about 22,000 acres, more than the Reber Plan proposed.
- **The old "smaller Bay, hotter summers" claim came from a real study:** BCDC's meteorologist
  estimated in 1967 that filling 25% of the Bay would raise San Jose's average July maximum by
  [at least 5°F](https://www.bcdc.ca.gov/wp-content/uploads/sites/354/2024/05/SFBayPlanSupplement1969.pdf).
  No modern model has checked it.
- **The legal wall is specific.** State law allows Bay fill only for "water-oriented uses", and
  [Mein v. BCDC (1990)](https://law.justia.com/cases/california/court-of-appeal/3d/218/727.html)
  held that housing is not one.
- **People are proposing it again:** [Kaufman (2019)](https://www.jefftk.com/p/make-more-land), 50
  sq mi south of the Dumbarton Bridge;
  [Arena Magazine (2026)](https://arenamag.com/articles/build-your-own-frontier); a
  [2025 concept](https://urbanize.beehiiv.com/p/out-of-land-is-san-francisco-ready-to-reclaim-the-bay)
  for 700 acres and 20,000 homes at Hunters Point.

## Part 1: What Has Been Done

### How Much of San Francisco Is Fill

Method. The USGS nine-county Quaternary deposits database
([Knudsen et al., 2000, Open-File Report 00-444](https://pubs.usgs.gov/of/2000/of00-444/)) tags
every surface polygon with a deposit type and a liquefaction class. I clipped it to the city limits
(county line at 37.708°N, plus Treasure Island and Yerba Buena Island), projected to UTM and summed
areas. The clipped land area is 46.6 sq mi against the Census figure of 46.9. The newer
[Witter et al. (2006)](https://pubs.usgs.gov/of/2006/1037/) revision omits the San Francisco North
quadrangle, so it cannot answer the question.

| Unit                                                 | Acres  | Share of SF land |
| ---------------------------------------------------- | ------ | ---------------- |
| Artificial fill over Bay mud                         | 5,284  | 17.7%            |
| Other artificial fill (filled ravines, graded dunes) | 949    | 3.2%             |
| Dune sand                                            | 8,875  | 29.8%            |
| Bedrock                                              | 7,957  | 26.7%            |
| Older alluvium and other                             | 6,758  | 22.7%            |
| Total land                                           | 29,823 | 100%             |

What it is measured against: the landward edge of Bay mud, which is the pre-development limit of the
tides. That counts filled marsh and mudflat, not only open water. Against the open-water line on the
1852 Coast Survey chart the share would be lower, because the Islais Creek and Mission Creek marshes
were wet ground, not water. The mapping is "preliminary", so read it as "about 18%".

| Stretch of shoreline           | Acres of fill over Bay mud | What is there                                                               |
| ------------------------------ | -------------------------- | --------------------------------------------------------------------------- |
| Marina and Crissy Field        | 401                        | Filled for the 1915 Panama-Pacific Exposition                               |
| Aquatic Park to Telegraph Hill | 351                        | Fisherman's Wharf, northern piers                                           |
| Broadway to 16th Street        | 1,764                      | Yerba Buena Cove (Financial District east of Montgomery), SoMa, Mission Bay |
| 16th Street to Islais Creek    | 1,198                      | Dogpatch, Islais Creek basin, Piers 80-96                                   |
| India Basin and Hunters Point  | 647                        | Shipyard                                                                    |
| Candlestick                    | 404                        | Candlestick Point                                                           |
| Treasure Island                | 448                        | Built 1936-39                                                               |
| Elsewhere                      | 70                         |                                                                             |

Cross-checks from [Dow's 1973 thesis](https://semspub.epa.gov/work/09/1137835.pdf), the standard
history: Yerba Buena Cove covered about 336 acres in 1846; Mission Bay was about 260 acres of water
ringed by 330 acres of salt marsh; the fill at Market and Spear is 31 feet deep. SFO and Foster City
are in San Mateo County and are not in the city's number. Foster City is
[2,600 acres raised with more than 14 million cubic yards of sand pumped from San Bruno Shoal](https://fostercity.org/community/page/creation-foster-city-land)
in the 1960s. For comparison, Boston has
[more than 5,000 acres of made land](https://www.nationalgeographic.com/news/2017/06/Boston-landfill-maps-history/).

### How Much of the Bay Was Lost

| Measure                            | Before           | After                                  | Source                                                                                                                                         |
| ---------------------------------- | ---------------- | -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Open water plus bordering wetlands | 787 sq mi (1849) | 548 sq mi (mid-1900s)                  | [BCDC](https://arccadigest.org/?p=39433)                                                                                                       |
| Tidal marsh                        | 190,000 acres    | 40,000 acres, of which 16,000 original | [Goals Project (1999)](https://www.waterboards.ca.gov/waterrights/water_issues/programs/bay_delta/docs/cmnt081712/sldmwa/goalsproject1999.pdf) |
| Tidal flat                         | 50,000 acres     | 29,000 acres                           | [Goals Project (1999)](https://southbayrestoration.org/news/articles/article19.html)                                                           |
| Vegetated tidal wetland            | 190,135 acres    | 85% lost                               | [NOAA (2019)](https://www.fisheries.noaa.gov/feature-story/new-mapping-reveals-lost-west-coast-estuary-habitat)                                |

The "80-90% of tidal marsh" figure holds: 79% by area, 92% counting only original marsh, 85% in the
2019 remapping. The "one third" is BCDC's 239 sq mi out of 787, and most of it is marsh that was
diked off for salt ponds, hay fields and duck clubs, not open water that was filled. The Goals
Project's split is about 137,000-139,000 acres diked and 50,000 filled (the two sources draw the
boundary differently, so the totals do not match). BCDC's summary rate is
[four square miles a year for 110 years](https://www.bcdc.ca.gov/what-we-do/our-story/).

Hydraulic mining did the rest. Miners in the Sierra washed hillsides through sluices with water
cannons, and the tailings moved down the Sacramento into the Bay. Gilbert's 1917 USGS study
estimated
[1.146 billion cubic yards](https://www.waterboards.ca.gov/waterrights/water_issues/programs/bay_delta/deltaflow/docs/exhibits/swrcb/swrcb_krone1979.pdf)
deposited in the bays through 1914. San Pablo Bay took
[about 300 million m³, shallowing it about a meter on average](https://www.waterboards.ca.gov/waterrights/water_issues/programs/bay_delta/docs/cmnt091412/sldmwa/jaffe_et_al_1998.pdf)
(Jaffe et al., 1998). The mud built new flats and marsh at the margins, which were then easy to
dike. The shallowness that made the Bay look fillable in 1959 was partly a Gold Rush artifact.

### How Filling Worked

1. **Wharf and dump (1850s).** The city sold underwater "water lots" in Yerba Buena Cove. Owners
   built wharves over the mud, then
   [paid crews to haul sand from the dunes and dump it](https://www.kqed.org/news/11799297/large-parts-of-the-bay-area-are-built-on-fill-why-and-where)
   between them. From 1859 a steam shovel on rails leveled the sand hills south of Market and
   [made 450 acres of ground in Mission Bay in fourteen years](https://semspub.epa.gov/work/09/1137835.pdf).
2. **Seawall and backfill (from about
   [1878](https://geoprac.net/2018/06/san-franciscos-embarcadero-seawall-at-risk-from-earthquakes-sea-level-rise/)).**
   A rock-and-concrete wall along today's Embarcadero, filled behind. A wall gives a fixed edge with
   deep water at the pier face.
3. **Rubble and garbage.** 1906 earthquake debris and decades of city refuse went into the margins.
4. **Hydraulic dredge fill (1912 on).** A suction dredge pumps sand slurry from the Bay floor
   through a pipe; the sand settles and the water runs off. This made the Marina and Treasure
   Island. Treasure Island was a ring of
   [287,000 tons of quarried rock on the Yerba Buena Shoals with about 29 million cubic yards of dredged sand pumped inside](https://en.wikipedia.org/wiki/Treasure_Island,_San_Francisco).
   Hydraulic fill is fast and cheap, and it leaves loose, uniform, saturated sand.

### The Catch: Liquefaction

Mechanism. Loose saturated sand stands up because the grains bear on each other. Shaking makes the
grains try to pack tighter, but the water between them cannot escape fast enough, so the water
carries the load, grain contact is lost, and the ground acts like a heavy liquid for tens of
seconds. Buildings tilt, buried pipes float and snap, and ground near a shoreline slides sideways.
Soft Bay mud underneath amplifies the shaking.

- **1906.** Lateral spreading on filled ground was the most damaging ground failure
  ([Youd and Hoose, USGS Professional Paper 993, 1978](https://pubs.usgs.gov/pp/1978/pp0993)), and
  [broken water mains in those zones cut the supply needed to fight the fire](https://ascelibrary.com/doi/10.1061/AJGEB6.0000267)
  (1976).
- **1989.** Loma Prieta was 60 miles away. In the Marina,
  [most liquefaction fell inside the footprint of the 1915 hydraulic fill](https://pubs.usgs.gov/of/1990/0253/report.pdf)
  (USGS, 1990) and
  [35 buildings were destroyed](https://conservation.ca.gov/cgs/Documents/Melange/Marina%20Poster.pdf).
  Regionally,
  [83% of liquefaction occurrences were in artificial fill](https://earthquake.usgs.gov/cfusion/external_grants/reports/07HQGR0078.pdf).
- **The USGS picture.** In the same 2000 database, 5,631 acres of San Francisco rate "very high"
  susceptibility and 455 "high": 20% of the city's land, almost exactly the fill (my computation).
  The Sunset's dune sand rates "moderate"; the hills "very low".
- **Millennium Tower.** A 58-story tower on fill whose piles stopped in sand short of bedrock. By
  2016 it had
  [settled about 18 inches and leaned about 24](https://www.enr.com/articles/61679-project-of-the-year-finalist-norcal-best-specialty-construction-301-mission-perimeter-pile-upgrade).
  Eighteen new piles to bedrock, finished in 2025, cost a reported $75 million.
- **Treasure Island.** To put 8,000 homes on 1930s hydraulic fill, the developer is
  [vibro-compacting the sand and using wick drains and surcharge on the mud below](https://www.engeo.com.au/our-projects/treasure-island-yerba-buena-island-redevelopment/).
  Infrastructure and site improvement are put at
  [$1.9 billion](https://en.wikipedia.org/wiki/Treasure_Island_Development), of which geotechnical
  stabilization was estimated at $137 million in 2011.
- **Embarcadero seawall.** It sits on Bay mud and is expected to slide bayward in a big quake.
  Estimates rose from
  [$2-3 billion (2016)](https://capradio.org/articles/2016/04/18/san-francisco-3-billion-to-secure-embarcadero-in-quake)
  to ["up to $5 billion"](https://sfport.com/wrp/embarcadero-seawall-program) to the Army Corps
  draft plan of [$13.5 billion for 7.5 miles of waterfront](https://sfport.com/wrp/draft-plan)
  (2024): $1.8 billion per mile to defend land that was nearly free to make.
- **SFO.** The airport is fill. Its program to rebuild
  [7.6 miles of perimeter as sheet-pile and concrete wall](https://www.bcdc.ca.gov/wp-content/uploads/sites/354/2024/01/2024-09-25-SFO-Shoreline-protection-program-Item-3.pdf)
  went from
  [$58 million to $587 million between 2015 and 2019](https://planetizen.com/news/2019/09/106249-waters-rise-toward-san-francisco-international-airport-so-do-costs-staying-dry).

### Why It Stopped

**The Reber Plan** (full story under Best Anecdotes). From 1929 a theatrical producer campaigned for
two earth dams that would turn the north and south Bay into freshwater lakes, with 20,000 acres of
fill between them. The Army Corps built the Bay Model in Sausalito in 1957 to test it, and in 1963
called it
["infeasible by any frame of reference"](https://www.foundsf.org/index.php?title=John_Reber:_The_Man_Who_Helped_Save_the_Bay_by_Trying_to_Destroy_It).

**The 1959 report and the map.** "Future Development of the San Francisco Bay Area 1960-2020" was a
federal land-demand projection. BCDC attributes it in one place to the
[U.S. Department of Commerce](https://www.bcdc.ca.gov/what-we-do/our-story/) and in another to
[the Army Corps](https://arccadigest.org/?p=39433); both say it identified about 325 more square
miles as fillable, 59% of the 548 then remaining. Its map ran in the Oakland Tribune
([April 1961 per KQED](https://www.kqed.org/news/11991017/transcript-how-environmental-activism-that-saved-the-bay);
other accounts say December 1959) with the line that by 2020 the Bay "could be little more than a
wide river". It reflected real plans: Berkeley alone intended to fill more than 2,000 acres and
double its size.

**Save the Bay.** Kay Kerr, Sylvia McLaughlin and Esther Gulick founded the Save San Francisco Bay
Association in 1961. Of their first 700 letters, about 600 came back with support. Berkeley
rescinded its plan in 1963.

**McAteer-Petris and BCDC.** The 1965 McAteer-Petris Act created the Bay Conservation and
Development Commission as a temporary agency with permit power over fill and a mandate to write a
plan. The Bay Plan was adopted in 1968 and BCDC became permanent in 1969 under Governor Reagan. Any
fill, including a pier on piles, needs its permit.

### Since Then

BCDC's ledger shows the Bay
[23,637 acres larger in 2025 than in 1969](https://vitalsigns.mtc.ca.gov/indicators/bay-restoration),
86% of that added between 2001 and 2018. The largest piece is the South Bay Salt Pond Restoration
Project:
[15,100 acres bought from Cargill in 2003](https://esassoc.com/projects/south-bay-salt-ponds-restoration/),
of which
[just over 3,700 have been restored](https://www.sierraclub.org/sierra/one-most-ambitious-nature-based-solutions-sea-level-rise).
The regional goal is 100,000 acres of tidal marsh. The last big fill proposal, SFO's 1998 plan to
push runways into the Bay, was [the largest since the 1960s](https://cp-dr.com/articles/node-1555)
and was shelved; in 2008 the city
[prohibited Bay fill for SFO runways](https://sfbos.org/index.aspx?page=3918).

## Part 2: What If We Did It Anyway

### Bathymetry: How Much Is Shallow

The "average depth of 12-14 feet" line describes the median, not the mean. From the
[USGS bathymetry summary](https://www.usgs.gov/centers/pcmsc/science/san-francisco-bay-bathymetry):

| Datum                  | Surface area          | Mean depth    | Median depth  |
| ---------------------- | --------------------- | ------------- | ------------- |
| Mean lower low water   | 1,138 km² (439 sq mi) | 6.3 m (21 ft) | 2.8 m (9 ft)  |
| Mean sea level         | 1,219 km²             | 6.9 m         | 3.6 m (12 ft) |
| Mean higher high water | 1,244 km² (480 sq mi) | 7.7 m         | 4.4 m         |

Half the Bay, about 140,000 acres, is under 2.8 m deep at low tide. The share under 5 m is 69% in
the South Bay, 82% in San Pablo Bay, 57% in Suisun and 32% in the Central Bay: 60% Bay-wide (my
arithmetic: 720 of 1,196 km²). BCDC says
["about two thirds of it is less than 18 feet deep"](https://www.bcdc.ca.gov/what-we-do/our-story/).
No published figure for "under 2 m"; interpolating gives 35-45% of the Bay, 100,000-125,000 acres
(unverified). The Central Bay off San Francisco's own waterfront is the deep part. The city's
shallow water is south of Hunters Point.

### Cost per Acre to Create vs. Value per Acre Created

| Project                                                  | Cost                                                                                                                                                                                          | Area           | US$ per acre | Notes                                               |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------ | --------------------------------------------------- |
| Singapore, projects completed 2013-22                    | [S$270-850 per m²](https://leaderoftheopposition.sg/2023/01/10/cost-of-land-reclamation-over-last-10-years)                                                                                   | n/a            | $0.8-2.6M    | Government range                                    |
| Singapore, all projects 2000-2023                        | [S$13 billion](https://www.mnd.gov.sg/newsroom/speeches/view/written-answer-by-ministry-of-national-development-on-cost-of-land-reclamation-project-and-proceeds-from-sale-of-reclaimed-land) | 74.5 km²       | $0.5M        | Nominal                                             |
| Singapore, Tuas Phase 2                                  | [S$1.46 billion](https://gcaptain.com/singapore-awards-1-1-billion-contract-for-phase-2-of-tuas-mega-port-project)                                                                            | 387 ha         | $1.1M        | Includes caisson seawall                            |
| Hong Kong, Kau Yi Chau, reclamation only                 | [HK$140 billion](https://hongkongfp.com/2019/03/19/hong-kongs-lantau-development-projects-cost-least-hk624bn-says-govt/) (2018 prices)                                                        | 1,000 ha       | $7.3M        | Deep water, thick marine mud                        |
| Hong Kong, same, with infrastructure and transport links | [HK$580 billion](https://www.legco.gov.hk/yr2022/english/panels/dev/minutes/dev20221229.pdf) (2022)                                                                                           | 1,000 ha       | $30M         | About half is transport                             |
| Copenhagen, Lynetteholm, perimeter phases 1-2            | [DKK 2.5 billion](https://cphpost.dk/2022-02-09/news/copenhagens-artificial-island-construction-off-to-rocky-start)                                                                           | 275 ha         | $0.5M        | Fill is surplus soil builders pay to dump           |
| Copenhagen, Lynetteholm, all-in                          | [DKK 20 billion](https://www.euronews.com/2018/10/09/copenhagen-new-island-settlement-to-house-35-000-people-and-shore-up-sea-defence)                                                        | 275 ha         | $4.2M        | Includes metro and harbor tunnel                    |
| Netherlands, Marker Wadden phase 1                       | [€75 million](https://www.natuurmonumenten.nl/marker-wadden/english/collaboration-and-planning)                                                                                               | about 1,000 ha | $0.03M       | Silt habitat islands, not buildable                 |
| Treasure Island, making old fill buildable               | [$1.9 billion](https://en.wikipedia.org/wiki/Treasure_Island_Development)                                                                                                                     | 405 acres      | $4.7M        | Ground improvement, streets, utilities; no new land |

Sample arithmetic: HK$140 billion / 1,000 ha = HK$140M per ha = US$17.9M per ha; / 2.471 = US$7.3M
per acre.

My bottom-up estimate for San Francisco Bay, per acre, in 2 m of water:

- **Fill volume.** Floor at 2 m below low water, finished grade about 5 m above it (see sea level,
  below), plus 1.5 m to make up for the mud compressing: 8.5 m x 4,047 m² = 34,400 m³ = 45,000 cubic
  yards.
- **Fill cost.** Placing dredged material at the Hamilton and Montezuma wetland sites costs
  [about $30 per cubic yard](https://www.pressreader.com/usa/the-mercury-news/20210413/281505049039695)
  (2021). 45,000 x $30 = $1.35M.
- **Ground improvement.** Treasure Island's $137M over 405 acres is $0.34M per acre in 2011 dollars;
  call it $0.5M.
- **Perimeter.** SFO's $587M for about 8 miles is $73M per mile. A 700-acre block needs about 2.5
  miles of seaward edge: $0.26M per acre.
- **Raw land: about $2.1M per acre; call it $2-3M.** Between Singapore and Hong Kong, as expected.
- **Serviced land: about $7M per gross acre** after adding Treasure Island's $4.7M for streets,
  utilities, parks and transit. Habitat mitigation is extra and could dominate: SFO offered
  [15 acres of restored wetland per acre filled](https://cp-dr.com/articles/node-1555).

Value side. FHFA's land price dataset
([Davis, Larson, Oliner and Shui, working paper 19-01, 2019; June 2024 data release](https://www.fhfa.gov/research/papers/wp1901))
estimates the land component of single-family home appraisals. 2022 values:

| Location                     | Land value per net acre | Per gross acre (x 0.5) | Minus $7M serviced cost |
| ---------------------------- | ----------------------- | ---------------------- | ----------------------- |
| Mission (94110)              | $29.5M                  | $14.8M                 | +$7.8M                  |
| San Francisco County average | $24.3M                  | $12.2M                 | +$5.2M                  |
| Sunset (94122)               | $22.1M                  | $11.0M                 | +$4.0M                  |
| Bayview (94124)              | $12.5M                  | $6.2M                  | -$0.8M                  |
| Foster City (94404)          | $10.6M                  | $5.3M                  | -$1.7M                  |
| San Mateo County average     | $7.9M                   | $4.0M                  | -$3.0M                  |
| Alameda County average       | $4.8M                   | $2.4M                  | -$4.6M                  |

The x 0.5 is my assumption that half of a new district is streets, parks and schools. Reading: raw
fill is worth four to ten times its cost anywhere on the inner Bay. After paying to make it a
neighborhood, the margin survives only at San Francisco prices, and new fill would sit next to
Bayview and Brisbane, not the Mission. Two caveats cut further. These are prices for scarce land,
and tens of thousands of new acres would lower them. And most of that $24M is the price of
permission: a legislature able to authorize Bay fill could authorize apartments on existing land
with a shorter bill.

### How Much Housing

Densities in homes per gross acre: Sunset about 10 (FHFA's average lot there is about 2,800 sq ft,
so 15 per net acre, less a third for streets); Mission about 20
([44,541 people on 1.48 sq mi](https://en.wikipedia.org/wiki/Mission_District,_San_Francisco) at
[2.24 per household](https://www.census.gov/quickfacts/fact/table/sanfranciscocountycalifornia/));
Paris about 54 ([1,402,024 homes](https://www.insee.fr/fr/statistiques/2011101?geo=COM-75056) on
105.4 km²).

| Scenario                            | Acres   | Sunset density | Mission density | Paris density |
| ----------------------------------- | ------- | -------------- | --------------- | ------------- |
| Hunters Point concept (2025)        | 700     | 7,000          | 14,000          | 38,000        |
| Reber Plan's fill (1940s)           | 20,000  | 200,000        | 400,000         | 1.1M          |
| Kaufman, south of Dumbarton (2019)  | 32,000  | 320,000        | 640,000         | 1.7M          |
| Everything under 2.8 m at low tide  | 140,000 | 1.4M           | 2.8M            | 7.6M          |
| The 1959 report in full (325 sq mi) | 208,000 | 2.1M           | 4.2M            | 11.2M         |

For scale, the Bay Area's state housing target is
[about 440,000 homes by 2031](https://urbanize.beehiiv.com/p/out-of-land-is-san-francisco-ready-to-reclaim-the-bay).

The comparison that matters: San Francisco has
[421,342 homes](https://www.census.gov/quickfacts/fact/table/sanfranciscocountycalifornia/) on
30,000 acres, 14 per gross acre. At Mission density it would have 600,000 (+180,000); at Paris
density, 1.6 million (+1.2 million). The city's 2025 rezoning was sized for
[36,200 homes](https://sfplanning.org/sites/default/files/documents/citywide/FZP-Factsheet-Capacity-Calculations.pdf),
and the city's economist projected it would yield
[about 14,600 over 20 years](https://www.planetizen.com/news/2025/11/136292-report-shows-san-franciscos-family-zoning-plan-would-produce-less-half-needed).
Physical capacity on dry land is two orders of magnitude above what the politics deliver. Fill does
not escape that politics. It adds BCDC, the Corps and the Endangered Species Act.

### Has Anyone Seriously Proposed It

- **Jeff Kaufman, "Make more land" (2019).**
  [Fill about 50 sq mi south of the Dumbarton Bridge](https://www.jefftk.com/p/make-more-land) and
  house 2-4 million people. No cost estimate. "Is this a serious proposal? Yes. We should do this."
  What is south of Dumbarton is mostly salt ponds already diked off, the ones bought for restoration
  in 2003, so the plan is closer to "develop the salt ponds" than "fill open water".
- **Farrell Gregory, Arena Magazine (2026).**
  [Fill the shoals](https://arenamag.com/articles/build-your-own-frontier); cites Singapore at
  $0.86-2.7M per acre against SF land at $5.7M per acre averaged citywide, and says BCDC took "the
  wrong lesson" from Reber.
- **Hunters Point concept (Planetizen feature, 2025).**
  [700 acres of new elevated land, up to 20,000 homes](https://urbanize.beehiiv.com/p/out-of-land-is-san-francisco-ready-to-reclaim-the-bay),
  pitched as flood defense that pays for itself, with a dozen such zones meeting most of the
  regional target. That is 29 homes per gross acre.
- **Redwood City Saltworks (2009-).** The one with a real applicant: Cargill and developer DMB filed
  for
  [up to 12,000 homes on 1,436 acres of salt ponds](https://www.kqed.org/science/1939188/in-redwood-city-a-renewed-battle-brews-over-developing-cargill-land),
  withdrew in 2012, and revived it when the EPA ruled in 2019 that the site was outside the Clean
  Water Act. Unbuilt.
- **Golden Gate barrier.**
  [SPUR's 2009 review](https://www.spur.org/publications/urbanist-article/2009-11-01/strategies-managing-sea-level-rise)
  listed a barrage as a sea-level option and reported BCDC's 2007 staff analysis: two to three times
  the cost of Three Gorges Dam, far more than levees, with changes to salinity, sedimentation and
  wetlands. The design was
  [two miles long and 500 feet tall from the Bay floor](https://legacy.xconomy.com/2013/08/30/sea-level-rise-time-for-a-barrage-of-new-ideas/2).
  A wall that holds the ocean out also holds the Sacramento River in. When the idea resurfaced in
  2021 the regional agencies called it a nonstarter, though a former staffer described the original
  analysis as
  ["a smart intern looking at this for four weeks"](https://www.sfchronicle.com/climate/article/San-Francisco-Bay-s-tides-are-going-to-rise-16386134.php).

### The Case Against, Quantified

**Tidal prism and the shipping channel.** The tidal prism is the water that moves in and out each
tide: 9,570 - 7,142 = 2,428 million m³
([USGS](https://www.usgs.gov/centers/pcmsc/science/san-francisco-bay-bathymetry)), about 2 m over
the whole Bay. That flow scours the Golden Gate to 113 m and keeps channels open. Inlets size
themselves to their prism, so less prism means a shallower throat. It has happened once: filling,
diking and mining silt cut the prism an estimated 9%, and from 1873 to 2005 the bar outside the Gate
[lost about 100 million m³ of sand and contracted about 1 km](https://pubs.usgs.gov/publication/70034106)
(Dallas and Barnard, 2011). Each km² of shallows filled removes about 2 million m³. My arithmetic:
700 acres removes 0.2% of the prism; 32,000 acres of open shallows, 11%; the full 1959 map, about
70%.

**Mudflats and the Pacific Flyway.** Single-day spring counts found
[589,000 to 932,000 shorebirds](https://sora.unm.edu/sites/default/files/journals/wb/v33n02/p0069-p0098.pdf),
more in every season than any other wetland on the U.S. Pacific coast outside Alaska (Stenzel et
al., 2002). They feed on 29,000 acres of tidal flat, already down from 50,000. Any scenario above
700 acres comes out of that and the shallows next to it.

**Climate and air quality.** BCDC's 1967 "Smog and Weather" report, summarized in the
[Bay Plan Supplement (1969)](https://www.bcdc.ca.gov/wp-content/uploads/sites/354/2024/05/SFBayPlanSupplement1969.pdf):
filling 25% of the Bay would raise San Jose's average July maximum by at least 5°F (to 86°F), lower
winter minimums by 2-3°F, slow the South Bay sea breeze and add fog and smog. The smog mechanism:
overnight inversions that trap pollution form more often over land than water, so converting water
to land adds inversions even before anyone builds. Is it real? The direction is sound. The number
came from analogy with other coastal valleys, not a model, and I found no modern simulation. Smog
fell after 1970 because of tailpipe rules, so emissions dominate. My read: negligible for hundreds
of acres, plausible in the South Bay for tens of thousands.

**Seismic.** New fill can be compacted, drained or cement-mixed; that is the $0.5M per acre. It
still sits on soft mud that amplifies shaking, and the bill for the last generation's fill is still
arriving.

**Sea level.** California's 2024 guidance projects
[0.8 ft by 2050 and a likely 1.6 to 3.1 ft by 2100](https://opc.ca.gov/2024/06/for-immediate-release-ocean-protection-council-adopts-updated-guidance-to-help-california-prepare-for-and-adapt-to-rising-seas/),
with a high planning scenario of
[6.6 ft](https://www.ppic.org/publication/sea-level-rise-in-california/). New land needs finished
grade several feet above today's 100-year tide plus that allowance, about 15-17 ft above low water,
the 5 m used above (my estimate). Proponents call this a feature: land built high in front of the
old shore is a levee you can sell. It also stands where a marsh would need to migrate.

**Law.** Four locks. (1)
[Government Code 66605](https://california.public.law/codes/government_code_section_66605): fill
only for water-oriented uses such as ports, airports and bridges, only with no upland alternative,
only the minimum needed;
[Mein v. BCDC (1990)](https://law.justia.com/cases/california/court-of-appeal/3d/218/727.html)
confirmed housing does not qualify. (2) The public trust doctrine: the state holds tidelands for
navigation, fisheries and public use. (3) Clean Water Act section 404: no fill permit where a
practicable alternative exists, and for uses that need not be on water, alternatives are presumed.
(4) The Endangered Species Act: Ridgway's rail and the salt marsh harvest mouse in the marsh;
salmon, sturgeon and smelt in the water. Changing this takes the Legislature and probably Congress.

**Material.** 32,000 acres at 45,000 cubic yards per acre is 1.4 billion cubic yards, about what the
Gold Rush washed into the bays. The marshes and mudflats that exist need
[450-650 million cubic yards by 2100](https://www.sfei.org/projects/sediment-survival) to keep up
with sea level (SFEI, 2021), and natural supply falls short. A big fill program competes with the
marshes for mud, or imports sand by ship as Singapore does.

### The Middle Path

- **Horizontal levees.** A wide, gently sloped marsh in front of a low levee. The marsh knocks down
  waves, so the levee can be shorter:
  [over $12 million per mile for a conventional levee over 50 years, under $7 million with a marsh in front](https://archive.estuarynews.org/estuary-news/the-laid-back-levee/)
  (Bay Institute, 2013). The
  [Oro Loma pilot](https://orolomasanitarydistrict.ca.gov/files/ecb2c02f9/STB-Oro-Loma-Report_11.13.17.pdf)
  cost $9.1 million (2017). This is fill placed in the Bay that BCDC likes.
- **Fill for habitat.** In 2019 BCDC amended the Bay Plan to
  [permit larger fills for habitat and shoreline adaptation](https://www.bcdc.ca.gov/wp-content/uploads/sites/354/2024/05/20190524ChangingBay.pdf).
  The agency founded to stop fill now has a policy for adding it.
- **Dredged sediment reuse.** Dumping channel dredgings at Alcatraz costs about $10 per cubic yard,
  hauling to sea $20, placing in a restoration site
  [$30](https://www.pressreader.com/usa/the-mercury-news/20210413/281505049039695). Hamilton
  Wetlands took [5.9 million cubic yards from 2008 to 2013](https://ewn.erdc.dren.mil/?p=19897). The
  fight is over who pays the difference.
- **Build on the fill we have.** Treasure Island's
  [8,000 homes](https://www.sfcta.org/blogs/affordable-housing-transportation-improvements-coming-treasure-island),
  the Hunters Point shipyard and the Brisbane Baylands are existing fill, raised and compacted to
  modern standards as they are built.

Is any version of "more land" compatible with a healthier Bay? Narrowly, yes: thicken and raise the
existing edge, with marsh on the water side and denser building on the land side. That yields
hundreds of acres, not tens of thousands.

### Verdict (My Judgment)

Engineering is not the obstacle; Singapore and Hong Kong do harder versions routinely. The economics
are real but narrower than the headline ratio: the tenfold gap between fill cost and land price
shrinks to under twofold after infrastructure in the best locations and turns negative in the likely
ones, before mitigation. The decisive point is substitution. Bay Area land is expensive because of
what you may build on it, and the legislative act that could authorize fill could instead authorize
four more stories on 30,000 existing acres: more homes, lower cost, no tidal, seismic or habitat
bill. Large-scale fill is a dominated way to get housing. The 700-acre class of proposal is the
interesting margin: small enough that prism, climate and sediment effects are negligible, and it
turns a flood-defense liability into an asset. I expect it to lose anyway on Mein and section 404.
The better trade is the one underway, where the Bay gets bigger and the existing fill gets taller.

## Best Anecdotes

**John Reber, the showman who wanted to dam the Bay.** From
[Wollenberg (2014)](https://www.foundsf.org/index.php?title=John_Reber:_The_Man_Who_Helped_Save_the_Bay_by_Trying_to_Destroy_It).
Reber came from Ohio in 1907 at age 20, wrote screenplays for Mack Sennett (his method: write a
tragedy, then "throw in a couple of custard pies") and staged more than 300 community pageants in
sixty California towns with casts of up to 5,000. "What is master planning but stage managing an
area?" He called the Bay "a geographic mistake". The plan, first floated in 1929: a 2,000-foot-wide
earth dam south of the Bay Bridge carrying 32 lanes of traffic plus rail, a second near today's
Richmond-San Rafael Bridge, two freshwater lakes holding 10 million acre-feet (twice Lake Shasta),
20,000 acres of fill off Berkeley and Richmond, a twelve-mile canal between the lakes, and ship
locks. About 15% of the Bay would have stayed tidal. Later versions added naval bases, bombproof
hangars in the quarries and atomic evacuation routes. He had a high school education and no staff,
and gave over a thousand speeches. Herbert Hoover endorsed it in 1933; San Francisco's supervisors
in 1942. Oakland, whose port would have sat behind a lock, called it "Hitler tactics". An admiral
said it had "no merit", then retired and joined the campaign. At the 1949 Senate hearing Reber
testified for two hours and proposed fixing the sturgeon problem with eggs from the Volga "if we can
get on friendly terms with Stalin". Congress gave the Army Corps $2.5 million to study it. It failed
on water balance. A 1951 state study found too little river flow in summer to keep the lakes full,
so the locks would let salt water in; too much in winter, so the Delta would flood; and still lakes
that would turn into polluted evaporation ponds. A Dutch engineer priced it at $1.4 billion against
Reber's $250 million. In 1957 the Corps built its hydraulic model in a Sausalito shipyard warehouse:
an acre and a half of concrete Bay at
[1:1,000 horizontal and 1:100 vertical scale, running a day of tides in fifteen minutes](https://en.wikipedia.org/wiki/U.S._Army_Corps_of_Engineers_Bay_Model).
Reber, asthmatic, told reporters God had promised him five more years and he would see construction
start. He died on 16 October 1960, the year the model began testing his plan. The 1963 verdict:
"infeasible by any frame of reference". Nobody killed it for environmental reasons; the Sierra Club
never took a position. The model is still open to visitors.

**The ships under the Financial District.** In 1849-50 crews abandoned their ships in Yerba Buena
Cove to go to the mines. A water-lot claim was stronger with something sitting on it, so speculators
hauled hulks onto their lots; some became hotels and warehouses and were then buried in sand.
Excavations downtown keep
[hitting them](https://sfpuc.gov/construction-contracts/lands-rights-of-way/historical-discoveries/two-buried-ships/san-franciscos).

**1906 built the ground that failed in 1989.** After the earthquake the city wanted a world's fair
to show it was back. The site was a tidal lagoon, pumped full of dredged sand in 1912 for the 1915
exposition and then sold off as the Marina. In 1989 the liquefaction
[matched the outline of that fill](https://pubs.usgs.gov/of/1990/0253/report.pdf).

**Three women and a newspaper map.** After the Tribune ran the federal map, Kerr, McLaughlin and
Gulick went to the established conservation groups, were told the groups had other priorities (the
Sierra Club's David Brower said wilderness came first) and were given the mailing lists instead.
[About 600 of the first 700 letters](https://www.kqed.org/news/11991017/transcript-how-environmental-activism-that-saved-the-bay)
drew pledges. Four years later California had the first coastal regulatory agency in the country.

**Treasure Island's name.** The sand dredged for it in 1936 included Sierra sediment washed down by
hydraulic mining, so the island was said to be
[made of gold-bearing dirt](https://en.wikipedia.org/wiki/Treasure_Island,_San_Francisco):
deliberate fill built from accidental fill.

## Could Not Verify

- **The 18% figure has no published counterpart.** It is my GIS computation. The mapping is
  preliminary, the unit includes filled marsh as well as filled water, and my city-limit clip is
  approximate (it matches Census land area within 1%).
- **Who wrote the 1959 report** (Commerce, the Corps, or Commerce for the Corps) and when the map
  ran in the Tribune (December 1959 or April 1961). Popular "70%" and "90%" fillable figures do not
  match 325 sq mi.
- **Share of the Bay under 2 m and under 4 m.** Only the median and under-5 m shares are published;
  an exact answer needs the USGS grid.
- **Deaths in the Marina in 1989** and the number of ships buried downtown: not confirmed, so not
  stated.
- **Treasure Island's $137 million geotechnical estimate** came from a search summary of a news
  report, not the city document.
- **Hong Kong's 2022 split** (about 30% reclamation, 20% island infrastructure, 50% transport) is
  from LegCo minutes via a search summary; the table uses the 2018 reclamation figure.
- **Costs for IJburg, Boston and Singapore's Long Island:** none found. Singapore has published no
  figure for Long Island.
- **Cargill Saltworks after 2019:** a court ruled against the EPA determination in 2020; later
  history not confirmed.
- **The 2007 BCDC barrage analysis** and the 2025 Hunters Point feature: known only through
  secondary summaries (SPUR, Xconomy, the Chronicle; a digest of the Planetizen piece).
- **Half of the flyway's diving ducks winter on the Bay:** widely repeated; I did not open the
  source page, so it is left out above.
- **Legal points 2 and 3** (public trust, section 404 presumption) are from general knowledge, not
  retrieved cases.
- **Design elevations.** The 15-17 ft finished grade is my estimate, not a design figure.
- **The $30 per cubic yard fill price** is for placing dredged mud at restoration sites. Engineered
  sand fill at the scale of thousands of acres has no local price and could cost more.
