# Image prompts

Working file, ignored by the build. One section per AI-generated image in `gen/`, with the model,
any source photo and the exact prompts in order, so each can be regenerated. How the generation
works is in `docs/ai-images.md`. All generated 2026-11-22.

The two real photos shown are `gen/hunters-point-real.jpg` and `gen/sutro-baths-real.jpg` (sources
below) and `gen/kelp-real.jpg`: "CINMS fish in kelp forest (50199042878).jpg" by Robert Schwemmer /
NOAA (Channel Islands National Marine Sanctuary), Public domain,
https://commons.wikimedia.org/wiki/File:CINMS_fish_in_kelp_forest_(50199042878).jpg.

## redwood-climbing.jpg

Model: Nano Banana 2.1 (google/gemini-nano-banana-2.1 on OpenRouter).

Text only:

```text
Create a photograph of this scene in San Francisco. Looking up in a foggy redwood grove in Golden Gate Park. Three tall coast redwoods stand close together as public climbing routes, each with an orange auto-belay device bolted to the trunk 18 metres up and a strap running down to a climber. Left tree: a child in a helmet climbing branches like a ladder. Middle tree: a woman on small brown footholds bolted into the bark. Right tree: a strong climber jamming hands into the deep cracks of the bark. People in harnesses wait on the wood-chip ground. Photorealistic photograph. No added text, no captions, no watermark, no borders.
```

Then, with that output attached:

```text
Edit this image. Zoom out a little so more of the redwood grove and more of the trees' height is in frame. Remove every person except one: keep a single climber on a single tree, partway up, clipped to the orange auto-belay strap that hangs from the device bolted high on that trunk. There are no other people anywhere in the picture: nobody on the other trees, nobody on the ground. Keep the same three redwoods, the same foggy light and the same photographic style. Photorealistic photograph, no text, no borders.
```

## water-polo.jpg

Model: GPT Image 2 (through the Codex CLI's built-in image tool).

Text only:

```text
Create a photograph of this scene in San Francisco. A Sunday water polo match in China Basin (McCovey Cove) beside the brick Giants ballpark in San Francisco: a floating pitch marked by lane ropes with two floating goals, two teams in dark blue and white numbered caps, a player rising out of the water mid-shot with a yellow ball, spray flying, spectators along the promenade railing and on kayaks and paddleboards. Clean blue-green water, sunny afternoon, downtown towers behind. Photorealistic photograph. No added text, no captions, no watermark, no borders.
```

## blue-heron-sailing.jpg

Model: GPT Image 2 (through the Codex CLI's built-in image tool).

Text only:

```text
Create a photograph of this scene in San Francisco. A children's sailing lesson on Blue Heron Lake (Stow Lake) in Golden Gate Park: a dozen El Toro dinghies, tiny 8-foot pram-bowed boats each with one white sail and one child in a life jacket, tacking around orange buoys. Behind, the wooded slope of Strawberry Hill with a long bright-blue water slide winding down through the trees and splashing into the lake. Sunny summer day. Photorealistic photograph. No added text, no captions, no watermark, no borders.
```

Then, with that output attached:

```text
Edit this image. Keep the lake, the trees and the light exactly as they are. Reduce the boats to only two small El Toro sailing dinghies, each with one child in a life jacket, both fairly small in the frame, and remove all the other boats and the buoys. Replace the blue plastic water slide with a natural rock water slide: a smooth, water-polished chute of bare grey granite running down the hillside between the trees, with a thin sheet of water flowing over it into the lake, like the natural rock slides on the Yuba River or in Yosemite. It must look completely natural, with no plastic, no rails and no built structure. One kid is sliding down it and one is climbing back up the rocks beside it. Photorealistic photograph, no text, no borders.
```

## hunters-point.jpg

Model: GPT Image 2 (through the Codex CLI's built-in image tool).

Edited from `hunters-point-real.jpg`: "Hunters Point Naval Shipyard 38" by Christopher Michel
(2020), CC BY-SA 4.0, https://commons.wikimedia.org/wiki/File:Hunters_Point_Naval_Shipyard_38.jpg

With the photo attached:

```text
Edit this aerial photograph of the abandoned Hunters Point Naval Shipyard in San Francisco to show the same place from exactly the same camera position, years after it became a glorious public orchard and garden.

Scale matters. This view is about a kilometre across and the gantry crane towers over everything, so every tree looks tiny from up here: fruit trees are small dots a few metres tall, planted by the thousand in groves, and even a full-grown oak reaches barely a fifth of the crane's height.

Replace all the pavement and warehouses with an English landscape garden in the style of Capability Brown: broad sweeping lawns, groves of apricot, persimmon and pomegranate trees, oaks and plane trees scattered between the groves, winding gravel paths.

Be bold with the old structures. The giant steel gantry crane is now a hanging garden, smothered in purple wisteria and climbing roses, with vines trailing from its arms. The flooded dry dock is now a turquoise public swimming lagoon with a sandy beach at its rounded end, lily pads, swimmers and little rowing boats. The old barge floating in it is now a floating glass greenhouse cafe.

Keep the shoreline, the piers, the bay, the sky and the haze where they are. Soft morning light. Photorealistic photograph. No added text, no captions, no watermark, no borders.
```

## chase-tag.jpg

Model: GPT Image 2 (through the Codex CLI's built-in image tool).

Text only:

```text
Create a photograph of this scene in San Francisco. An outdoor parkour chase-tag arena in the Panhandle park in San Francisco, beside the basketball courts, under tall eucalyptus trees with Victorian houses behind: a 12-metre square of black matting filled with a jungle of steel scaffold bars, rails, angled boxes and platforms. Two athletes mid-chase, one vaulting a bar, the other diving under a rail reaching to tag. A line of people waits along the edge, others watch from the grass, bikes on the lawn. Golden evening light. Photorealistic photograph. No added text, no captions, no watermark, no borders.
```

## sutro-tower.jpg

Model: GPT Image 2 (through the Codex CLI's built-in image tool).

Reference photo of the tower: "Sutro Tower, San Francisco, California LCCN2013630723.tif" by Carol
M. Highsmith, Public domain,
https://commons.wikimedia.org/wiki/File:Sutro_Tower,_San_Francisco,_California_LCCN2013630723.tif

With the photo attached:

```text
Create a photograph of a via ferrata climbing route on Sutro Tower, the giant red-and-white three-legged steel TV tower on the hill above San Francisco. The attached photo shows the real tower; keep its real shape and colours.

The view is from partway up one of the lattice legs. A guided group of five people in helmets and harnesses, each clipped by two lanyards to a steel safety cable, climbs iron rungs fixed to the steelwork and crosses a narrow hanging footbridge strung between two legs of the tower. Far below them the city grid, Golden Gate Park and the Pacific Ocean spread out, with a blanket of fog rolling in over the hills at sunset. Dizzying but joyful. Photorealistic photograph. No added text, no captions, no watermark, no borders.
```

Then, with that output attached:

```text
Edit this image. Remove only the three climbers nearest the camera, the ones on the iron rungs of the right-hand tower leg, and show the bare red steel, rungs and safety cable where they were. Keep exactly the two small people who are crossing the hanging footbridge far away in the background: they must still be there, small and distant. Keep the tower, the footbridge, the view of the city below, the fog and the sunset light exactly as they are. Photorealistic photograph, no text, no borders.
```

## alamo-elk.jpg

Model: Nano Banana 2.1 (google/gemini-nano-banana-2.1 on OpenRouter).

Text only:

```text
Create a photograph of this scene in San Francisco. Alamo Square in San Francisco: the row of pastel Victorian 'Painted Ladies' houses with the downtown skyline behind, and on the sloping lawn in front a small herd grazing calmly: three tule elk (a bull with big antlers and two cows) and five black-tailed deer with a fawn. Long wild grass with wildflowers, no cars on the street, two kids playing ball, a couple on a picnic blanket. Golden late-afternoon light. Photorealistic photograph. No added text, no captions, no watermark, no borders.
```

Then, with that output attached:

```text
Edit this image. Keep the houses, the skyline, the lawn, the people and the light exactly as they are. Halve the number of animals so it looks believable: leave about half as many elk and deer as there are now (for example one elk and two or three deer), spaced naturally on the grass, and remove the rest, filling in grass where they stood. Photorealistic photograph, no text, no borders.
```

## stonestown-waterfall.jpg

Model: GPT Image 2 (through the Codex CLI's built-in image tool).

Reference photos: two of Robbie's own waterfall photos from Bali (IMG_1280, IMG_1254), not in the
repo.

With both photos attached:

```text
Create a photograph of this scene in San Francisco. An artificial nature preserve built on a former shopping-mall parking lot: a 15-metre curtain waterfall pouring over a curved wall of dark hand-laid stone into a deep green plunge pool, tree ferns, bamboo, young redwoods, sunbeams through mist. A person in mid-air swan-diving from a ledge beside the falls, others swimming and waiting on the rocks. Peeking over the treetops in a top corner: the boxy beige facade of the Stonestown Galleria mall. The waterfall should look and feel like the one in the attached photos: use them for the rock, the falling water and the light only, and do not include the man. Photorealistic photograph. No added text, no captions, no watermark, no borders.
```

## sutro-baths.jpg

Model: GPT Image 2 (through the Codex CLI's built-in image tool).

Edited from `sutro-baths-real.jpg`: "Lands End - Sutro Baths - March 2018 (4866).jpg" by Gregory
Varnum, CC BY-SA 4.0,
https://commons.wikimedia.org/wiki/File:Lands_End_-_Sutro_Baths_-_March_2018_(4866).jpg

With the photo attached:

```text
Edit this photograph of the ruins of Sutro Baths at Lands End in San Francisco, keeping the camera position, the cliffs, the ocean, the rocks offshore and the horizon exactly as they are.

The baths have been rebuilt on their old foundations as a vast modern bathhouse: a soaring greenhouse of glass and pale timber arches in the spirit of the 1896 original, open on the ocean side. Inside it and on terraces outside are a chain of steaming seawater pools at different temperatures, cedar barrel saunas with people stepping out wrapped in towels, a cold plunge fed by the surf, and hanging plants everywhere. Hundreds of bathers: people floating, a yoga class on a deck, a few meditating beside a big brass gong. It is dusk, with warm lantern light inside against a cool blue sky and steam drifting off the water. Photorealistic photograph. No added text, no captions, no watermark, no borders.
```

## strawberry-treehouse.jpg

Model: GPT Image 2 (through the Codex CLI's built-in image tool).

Reference photo of the hill: "Strawberry Hill (San Francisco) 4 2023-04-24.jpeg" by FASTILY, CC
BY-SA 4.0, https://commons.wikimedia.org/wiki/File:Strawberry_Hill_(San_Francisco)_4_2023-04-24.jpeg

With the photo attached:

```text
Create a photograph of a huge, wind-sculpted Monterey cypress standing at the summit of Strawberry Hill, the wooded island in the middle of Blue Heron Lake in Golden Gate Park, San Francisco. If a photo is attached, use it as a reference for the place.

Halfway up the tree, cradled in its massive spreading limbs, is a hand-built wooden treehouse: a shingled cabin with a round window, a wraparound deck with a rope railing, a spiral staircase winding around the trunk and a rope bridge to a second, smaller platform. A few people sit on the deck with their legs dangling, watching the sun set over the Pacific Ocean beyond the western half of the park and the low houses of the Sunset district. The sky is orange and pink. Photorealistic photograph. No added text, no captions, no watermark, no borders.
```

Then, with that output attached:

```text
Edit this image to make it much more subtle. Zoom out and make the Monterey cypress smaller and less prominent in the frame: it is one tree on the wooded hilltop, not a giant filling the picture. Replace the treehouse with a very small, simple one, about a third of its current size: a tiny plain wooden platform with a little shingled hut tucked into the branches, easy to miss at first glance. Remove every staircase, spiral stair, rope bridge and second platform. The only way up is one thin rope ladder hanging from the platform to the ground. At most one or two small figures sitting on the platform. Keep the sunset over the ocean, the park and the light as they are. Photorealistic photograph, no text, no borders.
```

Then, with that output attached:

```text
Edit this image. Keep the tree, the tiny treehouse, the rope ladder, the hillside and the view exactly as they are. Change only the sky: make the sunset a little less spectacular. A calmer, more ordinary clear evening, with softer, more muted colours and fewer dramatic clouds, the kind of pleasant sunset San Francisco gets on a normal day. Photorealistic photograph, no text, no borders.
```

## peninsula-redwoods.jpg

Model: GPT Image 2 (through the Codex CLI's built-in image tool).

Edited from a photo not shown in the post: "Golden Gate Bridge from the Presidio (TK2).JPG" by
Tobias Kleinlercher / Wikipedia, CC BY-SA 3.0,
https://commons.wikimedia.org/wiki/File:Golden_Gate_Bridge_from_the_Presidio_(TK2).JPG

With the photo attached:

```text
Edit this photograph, taken in the Presidio of San Francisco looking across Crissy Field to the Golden Gate Bridge. Keep the camera position, the bridge, the Marin Headlands, the water and the sky exactly as they are.

The flat lawn, the road, the parked cars and the buildings in the foreground and middle distance are now a mature coast redwood forest: tall straight trunks with reddish bark and dark green crowns, ferns and sorrel on the forest floor, and one dirt trail winding in from the bottom of the frame. The forest runs down to the beach. The trees are arranged so the view stays open in the middle: the bridge's two towers and its span are still clearly visible beyond and above the treetops. Photorealistic photograph, same daylight, no text, no borders.
```

## milky-way-dolores.jpg

Model: Nano Banana 2.1 (google/gemini-nano-banana-2.1 on OpenRouter).

Edited from a photo not shown in the post: "View from top of Mission Dolores Park, SF (July
2017).jpg" by Mélanie Lacroix (mlle_farfalle), CC0,
https://commons.wikimedia.org/wiki/File:View_from_top_of_Mission_Dolores_Park,_SF_(July_2017).jpg

With the photo attached:

```text
Turn this daytime photograph into a night photograph of exactly the same scene. Same camera position, same framing, same park, same palm trees, same buildings in the same places. Add nothing and remove nothing: no new people, no telescope, no blankets, no new objects.

It is a clear, moonless night in a city that has strict light-pollution rules. The buildings are dark shapes with a modest number of small, dim, warm window lights. There is no skyglow, no streetlight glare and no car lights. The park is dark, with only faint detail in the grass.

The sky must be subtle and believable, the way a single real long exposure from a truly dark place looks straight out of the camera: a deep blue-black sky with many small pinpoint stars, and the Milky Way as a soft, pale, low-contrast band rising at an angle above the skyline. No vivid purple, orange or teal, no glowing nebula clouds, no painted or HDR look, no oversized stars. A little natural sensor grain. It should pass for a real photograph. No text, no borders.
```
