---
title: Plastic Straws
subtitle: Stop Worrying About Your Consumption Habits
date: 2026-06-30
draft: false
---

Many people before me have dunked on the plastic-straw Nazis. From a utilitarian perspective, using
a paper straw is pointless. [^toxoplasma]

[^toxoplasma]:
    My plausible explanations are innumeracy or costly signaling/symbolism (see
    [The Toxoplasma of Rage](https://slatestarcodex.com/2014/12/17/the-toxoplasma-of-rage/)).

In the post-singularity utopia, we will price externalities, and no one (besides the
externality-pricers) will have to think about their consumption beyond its direct economic cost.
Today, I do think about some things, like how the food I eat affects animal welfare. This post is my
attempt to think about fewer of them: to convince myself that (for example) how much trash I create
is not (even remotely) important.

TLDR: These things matter:

- Eating meat
- Traveling long distances[^travel]
- Anything that costs a lot of money

Worth zero mental energy:

- Creating less trash, recycling, composting, buying fewer things
- Eating organic, eating local
- Water use, outside of that caused by food
- Any label that tries to convince me a product is ethical (aside from some animal welfare ones)

# I: Methodology

## Probably Approximately Correct

Claude found basically all of the numbers for this article. I _strongly_ believe in the power of
working with approximately correct numbers.

## Animal Welfare

See my thoughts [here](https://robbiewmthompson.com/blog/bobs-diet/).

## Global Warming

From my inside view, my carbon footprint is irrelevant. It's likely we get something
singularity-like in the next 20 years. Under this assumption, most attempts to reduce emissions are
cost efficient. Out of epistemic humility, I still try to reduce my carbon footprint.

This post uses GWP20 $\text{CO}_2\text{e}$. It measures how much warming something will cause over
the next 20 years, normalized to 1 ton of $\text{CO}_2$. You can then put other things on the same
scale: [a ton of methane is ~80 tons](@methane80) $\text{CO}_2\text{e}$,
[a flight from SF to NYC is ~2-3 tons](@flight) $\text{CO}_2\text{e}$.[^vortices]

[^vortices]:
    Much more than you'd think considering that only ~1 ton of $\text{CO}_2$ is emitted! Physicists
    think that atmospheric contrails caused by planes have a large warming effect.

It's convention to use GWP100. I am using GWP20[^methane] because interest rates are real and my
model of the world accounts for them.[^tbond]

[^tbond]: The price of treasuries suggests that \$1 today is worth 39¢ in 2046 and ~.6¢ in 2126.

[^methane]: Methane (from trash or cows) is ~3x less $\text{CO}_2\text{e}$ when using GWP100.

## Land Use, Water Use

These things matter, and I tried to quantify how your decisions affect each. But in my heart of
hearts, I don't think you should spend much energy optimizing for either. We should just make (a lot
more!) national parks and then price and tax land. [^Georgism]

[^Georgism]: Possible using [Georgist](https://en.wikipedia.org/wiki/Georgism) principles.

# II: You Can Safely Stop Worrying About...

## Buying Local

Shipping food in a container on a cargo ship is basically free, economically and from a carbon
perspective. In many cases it's much _more_ environmentally friendly to just ship stuff from where
it grows easily.[^flyin]

[^flyin]:
    Some supermarkets will fly in produce, but I don't know any heuristics for telling what has been
    flown (and not trucked or cargo-shipped). Avoid sashimi-grade fish from afar and berries with an
    insane price markup, I guess.

## Wasting Vegan Food

All of your food carbon footprint is in meat/dairy. Pound for pound, a loaf of bread is ~90× less
bad than a steak ([~1.4 vs ~120–200 kg](@foodghg) $\text{CO}_2\text{e}$/kg at GWP20). Buy fresh
loaves and toss them when they're stale.

## Reducing, Reusing, Recycling, Composting

Each year Americans send about [243 million cubic yards of trash to landfill](@landfill), which
means we must create ~1,500 acres of dumps (at 100 ft deep).

After 100 years a landfill gets covered and becomes a park, a golf course, a conservation area, or a
solar farm. Assume, conservatively[^generous], that one acre of new landfill is as bad as 100 acres
of farmland.

[^generous]:
    It's actually very generous to the anti-trash side to say that creating an acre of landfill is
    as bad as creating 100 acres of farmland: discount rates imply that one year of landfill in 2126
    is $0.95^{100} = 0.6\%$ as bad as one year of landfill in 2026. And farmland is fertile land
    that would counterfactually be biodiverse nature, which is not true of landfill.

The average American's annual landfill use is about 20 cubic feet, or $0.2\ \text{ft}^2$ of landfill
area. It takes ~[1,590 sq ft to create a 1-lb steak](@steak), so your year of trash is
$0.2 / 1590 \times
100 \approx \frac{1}{80}$ steaks, even after the 100x penalty.

No one has done a rigorous study showing that microplastics meaningfully impact health. Even if you
are worried about them, vanishingly little exposure comes from plastic that properly makes it to
landfill.

Warming is also negligible here: The average American's landfill methane emissions is ~0.53 t
$\text{CO}_2\text{e}$, or about 1/5 of SF↔NYC round-trip flights.[^capture]

If you do anything here, recycle your aluminum and cardboard (see [section III](#recycling)).

[^capture]: In the US, these methane emissions are captured anyway!

## Organic foods

I am not convinced that organic food creates fewer externalities than normal produce. It might be
worse:

- **Land:** [Organic yields run ~20-25% lower](@organicyield), so growing the same amount of food
  takes ~25-33% more farmland.
- **Banning GMOs makes the land problem worse:** Organic prohibits GMOs.
  [GM crops raise yields](@gmyield).[^gmyields]
- **Organic still uses pesticides:** Organic bans _synthetic_ pesticides but allows a long list of
  "natural" ones: copper (a heavy metal that never degrades and builds up in soil), sulfur, and
  pyrethrin (toxic to bees and fish).
- **More tillage:** No synthetic herbicides means more plowing for weeds, which causes erosion, and
  emissions (from tractors and directly from the soil).

[^gmyields]: Corn ~11%, soy ~5%, cotton ~19%.

I asked Claude for reasons why Organic farming is better, but it didn't come up with much:

- **Fewer synthetic pesticides sprayed**: Organic bans synthetic pesticides and synthetic nitrogen
  fertilizer outright (and [roughly halves cadmium](@cadmium)), cutting the synthetic load on soil
  and water. The catch is above: it leans on natural pesticides like copper and sulfur instead.
- **Farmworker pesticide exposure**: Conventional US farms spray
  [~1 billion lb of synthetic pesticides a year](@pesticidelb), and globally acute pesticide
  poisoning hits an estimated [hundreds of millions of farmworkers a year](@poisoning) (mostly
  poor-PPE, developing-world farms). Organic farming doesn't necessarily improve this situation.
  Sulfur, the primary organic fungicide, is
  [the top reported cause of pesticide illness in California](@sulfurca).
- **Biodiversity per acre**: Organic fields hold
  [~30% more species and ~50% more animals](@biodiversity). But they need ~30% more land per calorie
  grown, so you gain ~nothing.

## Most Labels On Consumables (eg no bycatch, FSC certified wood)

### Possibly Worthwhile:

- **Energy Star**: Its appliances [saved ~520 billion kWh in 2020](@energystar) (~400 Mt
  $\text{CO}_2\text{e,}$ the annual power of ~50M homes).
- **Certain Animal Welfare Labels**: Claude recommends **Animal Welfare Approved**, **Certified
  Humane**, **Global Animal Partnership**, and **USDA Organic**.[^welfare-labels] The tell is a
  third party auditing the farm: the Animal Welfare Institute found
  **[>80% of USDA-approved "animal-raising" claims had no supporting evidence](@awi)** beyond the
  producer's own word.
- **FSC wood**: [A 2024 _Nature_ study found more wildlife in FSC forests](@fsc), but
  [Greenpeace quit FSC in 2018](@greenpeace), calling it greenwashing.

[^welfare-labels]:
    **Animal Welfare Approved** is the gold standard — independent auditors visit every farm yearly,
    and it's the only label Consumer Reports rated "excellent." **Certified Humane** is 100%
    pass/fail, on-site audited. **Global Animal Partnership** is Whole Foods' 1–5+ steps (higher =
    better). **USDA Organic** means real audits and required outdoor access.

### Pointless:

- **Rainforest Alliance**: the premium that reaches the farmer is under a penny per chocolate bar
  (<1% of the cocoa price).
- **Fairtrade**: a little more ([~1–2¢/bar](@fairtrade)), but it goes to the co-op, not the farmer.
- **"No bycatch" / seafood labels in general**: each one fixes a single narrow thing and leaks the
  harm elsewhere.[^seafood-labels]
- **Many Animal Welfare Labels**: "Natural" on eggs / meat (meaningless); "No Hormones" on meat
  (this is banned anyway); "Vegetarian-fed poultry" (chickens are omnivores).

[^seafood-labels]:
    Dolphin-safe is the template: spare the cute mammal, push boats onto nets that kill sharks and
    juvenile tuna instead. "Sustainable" (MSC) only certifies that the target stock won't collapse —
    nothing about bycatch, a bottom-trawled seafloor, or the fish's suffering. "No bycatch,"
    "natural," and "eco" are unregulated marketing with no audit behind them. The only
    semi-trustworthy signal isn't a logo but **Seafood Watch** (Monterey Bay Aquarium): independent,
    and it rates the actual species, gear, and region you're buying.

# III: Too Much Data

## Price is a good proxy

Carbon costs correlate with dollar costs, r = 0.87. If you budget your spending, to some extent
you're already optimizing for reducing externalities.

![What you pay vs carbon footprint — log-log across ~5 orders of magnitude of price, r = 0.87](charts/dollar_vs_carbon.png)

This is also somewhat true of land and water use. Graphs for food in particular:

![Price per pound vs water use per pound — log-log, 21 groceries](charts/dollar_vs_food_water.png)

![Price per pound vs land use per pound — log-log, 21 groceries](charts/dollar_vs_food_land.png)

Looked at another way: carbon footprint per dollar spent does span two OOMs. This viewpoint is less
comforting.

![Carbon per dollar spent — linear scale; absolute footprint and per-dollar intensity rank almost oppositely](charts/bar_co2e_per_dollar.png)

## Quotidian Water Use

The only thing that matters here is what you eat. Definitely don't feel guilty about taking a long
shower.

![Quotidian water per item — linear scale](charts/bar_water_item.png)

Zoom out to the whole country and it's the same story. Agriculture is
[~80–90% of US water consumption](@agwater).[^water-consumption]

![US freshwater consumption by sector — agriculture dwarfs everything; power is a sliver](charts/bar_water_consumption.png)

[^water-consumption]:
    _Consumption_ is water withdrawn and not returned — evaporated by crops, cooling towers, and
    lawns — as opposed to _withdrawals_, most of which flow back to the river. Power is the headline
    case: ~46% of US withdrawals but only ~4% of consumption, because it borrows cooling water and
    returns ~97% of it. Irrigation and thermoelectric figures are USGS _Estimated Use of Water in
    the United States in 2015_ (Circular 1441); the other bars are estimated from withdrawals ×
    typical return rates, so read the small ones as order-of-magnitude. The data is stale by
    necessity: USGS reported consumption for every sector from 1960–1995, then dropped it after the
    1995 report due to budget and staffing cuts. Consumption can't be metered at a pipe the way a
    withdrawal can; it has to be _modeled_ from evapotranspiration and process losses. Only
    irrigation and power consumption were revived in 2015.

## Quotidian Power Use

There were no big surprises for me here. Driving is expensive. AI can use a lot of power, but only
if you're coding with it. Lightbulbs use small but nonzero energy.

![Quotidian power — carbon per action, GWP20, linear scale](charts/bar_power_co2e.png)

[^travel]:
    Cars and planes use a similar amount of carbon per human mile traveled, but certainly not per
    human hour spent traveling. Electric trains on a clean grid are approximately free (a French TGV
    is ~50× cleaner than driving solo); US Amtrak is mostly diesel and only ~2–3× better than a car.

## Recycling

People will actually pay for recycled cardboard and aluminum, whereas recycled plastic and glass is
mostly only used because of mandates or to please consumers.

![Total carbon lever if all landfilled material were recycled — linear scale](charts/bar_recycle_total.png)

**Per item:**

![Carbon saved by recycling one item — linear scale](charts/bar_recycle_item.png)

<!-- Source definitions (collected into the Sources section by cite.js; order here doesn't matter). -->

{@steak}: Beef land use ≈ 326 m²/kg live weight (~1,590 sq ft/lb), from Poore & Nemecek (2018),
"Reducing food's environmental impacts through producers and consumers," _Science_ 360(6392), via
Our World in Data. <https://ourworldindata.org/environmental-impacts-of-food>

{@methane80}: IPCC AR6 WGI (2021), Ch. 7 Table 7.15 — methane's 20-year GWP is ~80 (79.7–82.5× CO₂).
<https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-7/>

{@flight}: Per-passenger flight CO₂ is ~0.15–0.25 kg/km (Our World in Data, Ritchie 2023), so a
~4,100 km SF–NYC leg is ~0.6–1 t CO₂; contrail and non-CO₂ forcing add roughly 2–3× on a 20-year
horizon (Resources for the Future, "Contrails, Aviation, and Climate Change," 2023).
<https://ourworldindata.org/travel-carbon-footprint>
<https://www.rff.org/publications/issue-briefs/contrails-aviation-and-climate-change/>

{@foodghg}: Poore & Nemecek (2018), _Science_, via Our World in Data food-footprint data: beef ~60
kg CO₂e/kg (mean up to ~99) vs bread/wheat ~1.4–1.6 (GWP100; a GWP20 re-weighting of enteric methane
pushes beef higher). <https://ourworldindata.org/environmental-impacts-of-food>

{@landfill}: US EPA, "National Overview: Facts and Figures on Materials, Wastes and Recycling" (2018
data) — 146 million tons of MSW landfilled (the cubic-yard volume is derived from tonnage).
<https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/national-overview-facts-and-figures-materials>

{@organicyield}: Seufert, Ramankutty & Foley (2012), "Comparing the yields of organic and
conventional agriculture," _Nature_ 485:229–232 — organic yields ~25% lower (de Ponti et al. 2012
found ~20%). <https://www.nature.com/articles/nature11069>

{@gmyield}: Klümper & Qaim (2014), "A Meta-Analysis of the Impacts of Genetically Modified Crops,"
_PLOS ONE_ 9(11):e111629 — GM adoption raised crop yields ~22% on average.
<https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0111629>

{@cadmium}: Barański et al. (2014), "Higher antioxidant and lower cadmium concentrations… in
organically grown crops," _British Journal of Nutrition_ 112:794–811 — organic crops averaged ~48%
lower cadmium. <https://doi.org/10.1017/S0007114514001366>

{@pesticidelb}: US EPA, "Pesticides Industry Sales and Usage: 2008–2012 Market Estimates" — US
agriculture used ~0.9 billion lb of pesticide active ingredients (2012), of ~1.1 billion lb total
US.
<https://www.epa.gov/sites/default/files/2017-01/documents/pesticides-industry-sales-usage-2016_0.pdf>

{@poisoning}: Boedeker et al. (2020), "The global distribution of acute unintentional pesticide
poisoning," _BMC Public Health_ 20:1875 — estimated ~385 million cases/year worldwide (retracted by
the journal in 2024, but still the most-cited estimate).
<https://bmcpublichealth.biomedcentral.com/articles/10.1186/s12889-020-09939-0>

{@sulfurca}: Raanan et al. (2017), _Environmental Health Perspectives_ 125(8) — elemental sulfur is
California's most-used agricultural pesticide and is tied to more occupational-illness cases (1,698
in 1982–1995) than any other. <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5783654/>

{@biodiversity}: Tuck et al. (2014), "Land-use intensity and the effects of organic farming on
biodiversity," _Journal of Applied Ecology_ 51:746–755 (species richness ~30%); the ~50% greater
abundance is from Bengtsson et al. (2005).
<https://besjournals.onlinelibrary.wiley.com/doi/abs/10.1111/1365-2664.12219>

{@energystar}: US EPA/DOE, ENERGY STAR "Impacts" (2020 accomplishments) — 520 billion kWh saved and
400 million metric tons of GHG avoided in 2020. <https://www.energystar.gov/about/impacts>

{@awi}: Animal Welfare Institute, "Label Confusion" (Fall 2022 update) — 85% of reviewed
USDA-approved animal-raising label claims lacked meaningful substantiation.
<https://awionline.org/awi-quarterly/fall-2022/animal-welfare-label-claims-usda-does-little-deter-deception>

{@fsc}: Zwerts et al. (2024), "FSC-certified forest management benefits large mammals compared to
non-FSC," _Nature_ 628:563–568 — 2.5–2.7× more large mammals in FSC concessions (Gabon/Congo).
<https://www.nature.com/articles/s41586-024-07257-8>

{@greenpeace}: Greenpeace International (26 Mar 2018), "Greenpeace International to not renew FSC
membership."
<https://www.greenpeace.org/international/press-release/15589/greenpeace-international-to-not-renew-fsc-membership/>

{@fairtrade}: Fairtrade International cocoa Premium is US\$240/tonne (≈0.5–1.5¢ per bar), paid to
the producer co-op to invest collectively — not to the individual farmer.
<https://www.fairtrade.net/en/get-involved/news/new-fairtrade-minimum-price-for-cocoa-in-non-regulated-markets.html>

{@agwater}: USDA Economic Research Service, "Irrigation & Water Use" — agriculture is ~80–90% of US
consumptive water use.
<https://www.ers.usda.gov/topics/farm-practices-management/irrigation-water-use>
