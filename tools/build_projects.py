#!/usr/bin/env python3
"""Generate individual project pages.

One page per completed project, each targeting "<service> <city>" with content
no competitor can reproduce. The galleries they link from stay untouched.
"""
import os, json, re

SITE = "/Users/omershapan/Documents/Guild Builders Website/Construction-site"
URL = "https://guildbuildersgroup.com"
CSS = "style.css?v=90"
JS = "script.js?v=49"

CITIES = [("san-diego","San Diego"),("la-jolla","La Jolla"),("del-mar","Del Mar"),
  ("solana-beach","Solana Beach"),("rancho-santa-fe","Rancho Santa Fe"),("carmel-valley","Carmel Valley"),
  ("encinitas","Encinitas"),("carlsbad","Carlsbad"),("oceanside","Oceanside"),("vista","Vista"),
  ("san-marcos","San Marcos"),("escondido","Escondido"),("poway","Poway"),("fallbrook","Fallbrook"),
  ("el-cajon","El Cajon"),("la-mesa","La Mesa"),("chula-vista","Chula Vista")]
FOOTER = " &middot; ".join(f'<a href="{s}">{n}</a>' for s, n in CITIES)

PROJECTS = [
{
 "page": "kitchen-remodel-carmel-valley-kingsfield-court.html",
 "project": "Kingsfield Court",
 "city": "Carmel Valley", "city_page": "carmel-valley.html",
 "prefix": "kingsfield", "photos": range(1, 7),
 "anchor": "kitchens-cabinets.html#kitchen-kingsfield-court",
 "blurb": ("A full gut and rebuild of a Carmel Valley kitchen: appliances relocated, custom white oak "
           "cabinetry with a navy island and hood, quartzite counters, and 2,600 sq ft of hardwood flooring."),
 "hero_sub": ("Kingsfield Court &mdash; a full gut and rebuild with custom white oak cabinetry, a navy "
              "island and hood, quartzite counters, and new hardwood flooring throughout the home."),
 "specs": [("Location","Carmel Valley, San Diego County"),
           ("Timeline","8 weeks"),
           ("Scope","Full gut and rebuild, appliances relocated"),
           ("Cabinetry","Custom white oak, navy island and hood"),
           ("Counters","Quartzite"),
           ("Flooring","2,600 sq ft glued-down engineered hardwood")],
 "body": """
<p>This kitchen came to us as a full gut. Not a refresh, not new doors on old boxes — everything out, back to studs, and rebuilt around a layout that made sense for how the family actually uses the room.</p>

<h2>Moving the appliances</h2>

<p>The biggest change is the one you notice least. Relocating appliances means moving gas, water, waste and power, and it is the difference between a kitchen that works and one that merely looks better than it did.</p>

<p>With the range, refrigerator and ovens repositioned, the working zone stopped competing with the walkway. The island now sits clear of the traffic route between the kitchen and the living space beyond it, so people can gather at the counter without standing in the cook's path.</p>

<h2>Cabinetry</h2>

<p>Custom throughout, in white oak. Going custom here was not a luxury — the room has a long run of tall cabinetry, a chimney breast for the hood, and a ceiling carrying structural beams. Modular boxes would have left filler strips and a bulkhead. Built to the room, the cabinetry runs clean from floor to ceiling with no dead space.</p>

<p>The island and the hood are finished in navy. That was a deliberate decision rather than a colour preference: a room of unbroken white oak reads flat, and giving the two focal elements a deeper tone anchors the space. The hood and island now speak to each other across the room and the eye has somewhere to land.</p>

<h2>Counters</h2>

<p>Quartzite, in a pale grey-veined stone. Quartzite handles heat better than engineered surfaces and takes daily use without the fuss of marble, which matters on an island that doubles as homework desk and serving counter.</p>

<h2>Flooring throughout the house</h2>

<p>The job did not stop at the kitchen. We laid 2,600 square feet of engineered hardwood across the whole home, glued down rather than floated.</p>

<p>Glue-down matters more than it sounds. A floating floor moves slightly underfoot and can sound hollow over a large span; bonded directly to the slab, the floor feels solid and quiet across every room. Over the concrete slabs common in San Diego homes, engineered hardwood is also the more stable choice than solid timber, which reacts more to what the slab does underneath it.</p>

<p>Running one continuous floor through the entire house, with no thresholds breaking it at every doorway, is a large part of why the kitchen reads as connected to the living space rather than as a separate room that happens to adjoin it.</p>

<h2>The result</h2>

<p>An open kitchen that connects to the living space without surrendering to it. The working zones are separate from where people sit, storage runs to the ceiling instead of stopping short, and the finishes are ones that will still look considered in ten years. Eight weeks from demolition to final walkthrough.</p>
"""},
{
 "page": "kitchen-remodel-san-diego-miracle-drive.html",
 "project": "Miracle Drive",
 "city": "San Diego", "city_page": "san-diego.html",
 "prefix": "miracle", "photos": range(1, 9),
 "anchor": "kitchens-cabinets.html#kitchen-miracle-drive",
 "blurb": ("A full gut in San Diego: three windows relocated, every appliance repositioned, custom white "
           "oak cabinetry, a waterfall quartz island and a custom hood."),
 "hero_sub": ("Miracle Drive &mdash; a full gut with three windows moved, every appliance relocated, custom "
              "white oak cabinetry, a waterfall quartz island and a bespoke hood."),
 "specs": [("Location","San Diego"),
           ("Timeline","8 weeks"),
           ("Scope","Full gut, 3 windows relocated, all appliances repositioned"),
           ("Cabinetry","Custom white oak, integrated refrigerator panels"),
           ("Counters","Quartz, waterfall island"),
           ("Flooring","New tile throughout")],
 "body": """
<p>This was a full gut with an unusually ambitious brief: not just new cabinetry and surfaces, but a room reorganised from the structure outward. Three windows moved, every appliance relocated, and a custom hood and beam detail built specifically for the space.</p>

<h2>Moving three windows</h2>

<p>Relocating a window is structural work. Each opening means re-framing, new headers, and making the exterior watertight again — flashing and weather barrier detailed properly so the wall performs as well afterwards as it did before.</p>

<p>It is rarely done for appearance alone, and it was not here. Moving the three openings changed where daylight falls across the room and freed up wall that the old layout had wasted. The result is a kitchen that feels considerably larger without a single wall being removed.</p>

<h2>Every appliance repositioned</h2>

<p>With the windows resolved, the working layout was rebuilt from scratch. Gas, water, waste and power all moved to suit the new plan rather than the old one.</p>

<p>The refrigerator is fully integrated — built in and faced with custom cabinet panels so it disappears into the run of white oak. That only works when the surrounding cabinetry is built to the appliance's exact dimensions, which is a large part of why the cabinetry here is custom rather than modular.</p>

<h2>Cabinetry and the hood</h2>

<p>Custom white oak throughout, with glazed upper cabinets breaking up what would otherwise be an unbroken expanse of timber. The hood was designed for this room specifically rather than selected from a catalogue, which is what lets it sit in proportion with the cabinetry either side of it.</p>

<p>The ceiling beam is clad in solid wood. A beam cover is a small piece of joinery that changes the character of a whole room — it gives the ceiling weight and warmth, and ties back to the oak below it.</p>

<h2>Counters</h2>

<p>Quartz, with a waterfall return on the island. The waterfall detail is the reason the island reads as a single piece of stone rather than a counter sitting on a cabinet — the grain runs over the edge and down to the floor, and the join has to be mitred precisely for the effect to work.</p>

<p>Quartz was the right call for a household that wanted a surface needing no sealing and no particular care.</p>

<h2>The result</h2>

<p>A kitchen rebuilt from the framing out. New light from three relocated windows, an appliance layout designed around how the room is actually used, and joinery — hood, beam, integrated refrigerator — made for this space and no other. Eight weeks from demolition to final walkthrough.</p>
"""},
{
 "page": "kitchen-remodel-carlsbad-westwood-drive.html",
 "project": "Westwood Drive",
 "city": "Carlsbad", "city_page": "carlsbad.html",
 "prefix": "westwood", "photos": range(1, 9),
 "anchor": "kitchens-cabinets.html#kitchen-westwood-drive",
 "blurb": ("A full gut in Carlsbad with a load-bearing wall removed and opened into a breakfast bar, "
           "an exterior door and window relocated, custom cabinetry and quartz counters."),
 "hero_sub": ("Westwood Drive &mdash; a full gut with a load-bearing wall removed for a breakfast bar, "
              "an exterior door and window relocated, custom cabinetry and quartz counters."),
 "specs": [("Location","Carlsbad, San Diego County"),
           ("Timeline","8 weeks"),
           ("Scope","Full gut, load-bearing wall removed, exterior door and window relocated"),
           ("Cabinetry","Custom"),
           ("Counters","Quartz"),
           ("Flooring","Luxury vinyl plank")],
 "body": """
<p>This is the most structural of these projects. A load-bearing wall came out, an exterior door and a window moved, and the kitchen was rebuilt around an opening that did not exist before.</p>

<h2>Removing a load-bearing wall</h2>

<p>Taking out a wall that carries load is a different exercise from removing a partition. The weight above it has to go somewhere, which means a beam sized for the span and posts carrying that load down to something capable of taking it — often new footings, depending on what is beneath the floor.</p>

<p>It is engineered work, inspected work, and it is the reason a project like this takes planning before anyone swings a hammer. Done properly it is invisible: you see an opening where a wall used to be and nothing about the ceiling above it suggests anything changed.</p>

<h2>Opening it into a breakfast bar</h2>

<p>Rather than remove the wall entirely, we opened it to counter height and turned the remaining structure into a breakfast bar. That solves two problems at once — the kitchen gains the light and connection of an open plan, while the bar gives the opening a purpose and a place for people to sit.</p>

<p>It also keeps some separation. A fully open wall makes the kitchen part of the next room whether you want it to be or not; a bar height opening keeps the working side of the kitchen slightly its own space.</p>

<h2>Moving an exterior door and window</h2>

<p>Both openings changed position. Exterior work is unforgiving in a way interior work is not — every opening has to be re-framed, headed, flashed and sealed so the wall keeps water out as well as it did before. Get that detailing wrong and the failure shows up years later inside the wall.</p>

<p>Moving them freed up the run of wall the new layout needed and changed where daylight enters the room.</p>

<h2>Cabinetry, counters and floor</h2>

<p>Custom cabinetry built to the rebuilt room, quartz counters chosen for a surface that needs no sealing, and luxury vinyl plank flooring — fully waterproof, warm underfoot, and forgiving over a slab.</p>

<h2>The result</h2>

<p>A kitchen that reads as though the house was always laid out this way. The structural work is the part nobody will notice, which is exactly the point. Eight weeks from demolition to final walkthrough.</p>
"""},
{
 "page": "kitchen-remodel-san-marcos-reflection-street.html",
 "project": "Reflection Street",
 "city": "San Marcos", "city_page": "san-marcos.html",
 "prefix": "reflection", "photos": range(1, 8),
 "anchor": "kitchens-cabinets.html#kitchen-reflection-street",
 "blurb": ("A full gut in San Marcos with every appliance relocated, semi-custom white cabinetry and "
           "new quartzite counters, working around flooring the owners chose to keep."),
 "hero_sub": ("Reflection Street &mdash; a full gut with every appliance relocated, semi-custom white "
              "cabinetry and new quartzite counters, built around existing flooring that was kept."),
 "specs": [("Location","San Marcos, San Diego County"),
           ("Timeline","7 weeks"),
           ("Scope","Full gut, appliances relocated throughout"),
           ("Cabinetry","Semi-custom, white"),
           ("Counters","New quartzite"),
           ("Flooring","Existing floor retained")],
 "body": """
<p>A full gut in San Marcos with one deliberate exception: the flooring stayed. Everything else came out and the appliance layout was rebuilt from scratch.</p>

<h2>Keeping the floor</h2>

<p>The existing floor was in good condition and the owners liked it, so we worked around it rather than replacing it for the sake of a clean sweep.</p>

<p>That is a harder way to build, not an easier one. Protecting a finished floor through demolition and a full cabinetry installation takes real care, and the new cabinetry has to meet what is already there rather than the other way round. But replacing a floor that has years left in it is spending on something nobody asked to change, and it adds days to a schedule for no gain.</p>

<h2>Relocating the appliances</h2>

<p>Every appliance moved. That means gas, water, waste and power all rerouted to suit a plan built around how the room is actually used, rather than inheriting whatever the original builder found convenient.</p>

<p>It is the least photogenic part of any kitchen project and usually the one that decides whether the finished room works. Landing space beside the oven, a refrigerator door that does not block the walkway, a sink positioned so two people are not reaching across each other — all of it comes from where the services end up.</p>

<h2>Semi-custom cabinetry</h2>

<p>Semi-custom rather than full custom, and that was the right call for this room. Semi-custom is built to order from a defined range, with modifications available where they are needed — a depth adjusted here, a height changed there.</p>

<p>Where a room divides reasonably well into standard widths and has no unusual structure to work around, full custom buys flexibility you will not use. The tier should follow what the room demands. This one did not demand it, so the budget went into the counters and the layout instead.</p>

<p>Finished in white, which keeps a room bright and lets the counters carry the character.</p>

<h2>Quartzite counters</h2>

<p>New quartzite throughout. Quarried stone, so the slab is unique, and it takes heat in a way engineered surfaces do not — a pan straight off the burner will mark quartz but not this.</p>

<h2>The result</h2>

<p>A completely rebuilt kitchen that kept what was worth keeping. New layout, new cabinetry, new stone, on a floor that had plenty of life left in it. Seven weeks from demolition to final walkthrough.</p>
"""},
{
 "page": "kitchen-remodel-carmel-valley-arabian-crest-drive.html",
 "project": "Arabian Crest Drive",
 "city": "Carmel Valley", "city_page": "carmel-valley.html",
 "prefix": "arabiancrest", "photos": range(1, 5),
 "anchor": "kitchens-cabinets.html#kitchen-arabian-crest-drive",
 "blurb": ("A full gut in Carmel Valley with white oak cabinetry, quartz counters and a custom "
           "built-in glass wine cellar."),
 "hero_sub": ("Arabian Crest Drive &mdash; a full gut with white oak cabinetry, quartz counters and a "
              "custom built-in glass wine cellar."),
 "specs": [("Location","Carmel Valley, San Diego County"),
           ("Timeline","7 weeks"),
           ("Scope","Full gut and rebuild"),
           ("Cabinetry","White oak"),
           ("Counters","Quartz"),
           ("Feature","Custom built-in glass wine cellar")],
 "body": """
<p>A full gut in Carmel Valley, and the project on this list with the most distinctive single element: a glass-fronted wine cellar built into the kitchen rather than tucked away somewhere else in the house.</p>

<h2>The wine cellar</h2>

<p>Building a wine cellar into a kitchen is more involved than fitting a cabinet. Wine wants a stable temperature and it does not want the swings a kitchen produces — a room with a range in it is the least stable environment in the house.</p>

<p>That means the enclosure has to be built as its own sealed space: insulated, with glass specified for the job, and cooling that holds a set temperature rather than merely running cold. Glass fronts look effortless and are the hardest part to get right, because glazing is where a sealed enclosure most easily loses its temperature.</p>

<p>Done properly it becomes the focal point of the room. A lit run of bottles behind glass gives the kitchen something no cabinetry can — depth, and a reason for the eye to stop.</p>

<h2>Cabinetry</h2>

<p>White oak throughout. It takes a light finish without turning orange the way some oaks do, and the grain carries a large expanse without needing a second material to break it up. Against the glass and the bottles behind it, the timber keeps the room warm rather than clinical.</p>

<h2>Counters</h2>

<p>Quartz, for a household that wanted a surface needing no sealing and no particular thought. Engineered stone is consistent slab to slab, so what is specified is what arrives — useful where the cabinetry and the cellar are already doing the visual work.</p>

<h2>The result</h2>

<p>A kitchen with a genuine centrepiece. The wine cellar is the sort of thing that sounds like an indulgence and turns out to be the reason the room gets used — it makes the kitchen somewhere people gather rather than somewhere food is prepared. Seven weeks from demolition to final walkthrough.</p>
"""},
{
 "page": "kitchen-remodel-la-jolla-poole-street.html",
 "project": "Poole Street",
 "city": "La Jolla", "city_page": "la-jolla.html",
 "prefix": "poole", "photos": range(1, 9),
 "anchor": "kitchens-cabinets.html#kitchen-poole-street",
 "blurb": ("A full gut in La Jolla: every appliance relocated, custom two-tone cabinetry, a custom pantry, "
           "quartzite counters with tile and quartzite backsplashes, and new sliding doors."),
 "hero_sub": ("Poole Street &mdash; a full gut with every appliance relocated, custom two-tone cabinetry, "
              "a custom pantry, quartzite counters and new sliding doors."),
 "specs": [("Location","La Jolla, San Diego County"),
           ("Timeline","9 weeks"),
           ("Scope","Full gut and rebuild"),
           ("Layout","All appliances relocated, new sliding doors"),
           ("Cabinetry","Custom two-tone, custom pantry"),
           ("Counters","Quartzite"),
           ("Backsplash","Tile on one wall, quartzite on another"),
           ("Flooring","New luxury vinyl plank")],
 "body": """
<p>A full gut in La Jolla and one of the more involved kitchens on this list: every appliance moved, a purpose-built pantry, two cabinet finishes, and two different backsplash materials used deliberately on different walls.</p>

<h2>Relocating every appliance</h2>

<p>Nothing stayed where it was. Moving every appliance means rerouting gas, water, waste and power to suit a plan built from scratch rather than inheriting the one the house came with.</p>

<p>It is the least visible work in any kitchen and usually what decides whether the finished room actually functions — whether there is landing space beside the oven, whether the refrigerator door blocks the walkway, whether two people can work without reaching across each other.</p>

<h2>Two-tone cabinetry and a custom pantry</h2>

<p>Custom throughout, in two finishes. Two-tone gives a kitchen depth without introducing a second material, and it lets the working level of the room carry colour while the upper half stays light.</p>

<p>The pantry was built for the space rather than bought as a unit. A purpose-built pantry is one of the highest-return pieces of joinery in a kitchen: it takes the clutter that would otherwise live on the counter, and because it is built to the room it uses the full depth and height rather than leaving dead space above and behind.</p>

<h2>Two backsplashes, on purpose</h2>

<p>One wall is tile; another is quartzite run up from the counter. Using two materials in one room sounds like indecision and is the opposite when it is planned.</p>

<p>A full-height stone backsplash behind the range makes that wall the focal point — the veining continues from the counter up, so the two read as one piece. Tile on the second run keeps the rest of the room lighter and adds texture where a continuous slab would have been heavy. Each material is doing a job the other could not.</p>

<h2>Counters and flooring</h2>

<p>Quartzite throughout. Quarried stone, so every slab is unique, and it handles heat in a way engineered surfaces do not — a pan straight off the burner will mark quartz but not this.</p>

<p>Luxury vinyl plank on the floor: fully waterproof, warmer and quieter underfoot than tile, and forgiving over a slab.</p>

<h2>New sliding doors</h2>

<p>Replacing the sliders brought in more daylight and sealed the opening properly. Door replacement is exterior detailing as much as anything else — the opening has to be re-flashed and sealed, or a draught is simply traded for a leak.</p>

<h2>The result</h2>

<p>A kitchen rebuilt from the services out, with the joinery and stone doing genuinely different jobs in different parts of the room. Nine weeks from demolition to final walkthrough.</p>
"""},
{
 "page": "kitchen-remodel-san-diego-pipilo-street.html",
 "project": "Pipilo Street",
 "city": "San Diego", "city_page": "san-diego.html",
 "prefix": "pipilo", "photos": range(1, 9),
 "anchor": "kitchens-cabinets.html#kitchen-pipilo-street",
 "blurb": ("A full gut in San Diego that kept the appliance layout: custom white oak blended with white "
           "uppers, a custom hood, and quartzite counters carried up as the backsplash."),
 "hero_sub": ("Pipilo Street &mdash; a full gut that kept the appliance layout, with custom white oak "
              "blended with white uppers, a custom hood and quartzite counters and backsplash."),
 "specs": [("Location","San Diego"),
           ("Timeline","7 weeks"),
           ("Scope","Full gut and rebuild"),
           ("Layout","Appliance positions retained"),
           ("Cabinetry","Custom white oak with white uppers, custom hood"),
           ("Counters","Quartzite"),
           ("Backsplash","Quartzite, matched to the counters"),
           ("Flooring","New luxury vinyl plank")],
 "body": """
<p>A full gut in San Diego where the plumbing and gas stayed put. The appliances were already in sensible positions, so nothing was moved for the sake of it — the work went into cabinetry, stone and the hood.</p>

<p>That is worth being plain about. Relocating services is the most disruptive and least visible spend in any kitchen. Where the existing layout works, leaving it alone puts the budget into the parts of the room you look at every day.</p>

<h2>Blending two cabinet finishes</h2>

<p>White oak below, white above. This is a different move from a two-tone paint scheme, because one of the finishes is timber — the grain stays visible at the working level while the upper half of the room reads light and recedes.</p>

<p>It solves a problem that unbroken oak creates. A room finished entirely in timber can feel heavy and close, particularly where the uppers run to the ceiling. Keeping the top half white lifts the room without giving up the warmth where hands actually land.</p>

<h2>The hood</h2>

<p>Custom, built for the space. The hood sits alone above the range with nothing beside it to hide behind, which is why a catalogue unit so often looks chosen rather than designed. Built to the room, it holds proportion with the cabinetry either side and gives the wall a centre.</p>

<h2>Quartzite counters and backsplash</h2>

<p>The counters run up the wall as the backsplash. Carrying the same slab vertically is a deliberate detail and a demanding one — the veining has to be matched across the joint so the stone reads as continuous rather than as two separate pieces that happen to touch.</p>

<p>Done well, it removes the horizontal line a tile backsplash creates and makes the whole run read as one surface. It also removes grout from the wall behind the range, which is the part of a kitchen that takes the most splashing and the most cleaning.</p>

<p>Quartzite was the right stone for it. Quarried rather than engineered, so each slab is unique, and it takes heat in a way quartz does not.</p>

<h2>Flooring</h2>

<p>Luxury vinyl plank throughout. Fully waterproof, which is the argument for it in a kitchen, and warmer and quieter underfoot than tile. Over the concrete slabs common in San Diego homes it is also more forgiving than timber.</p>

<h2>The result</h2>

<p>A kitchen rebuilt entirely without moving a single service. Two cabinet finishes doing different jobs, a hood made for the room, and stone carried from counter to ceiling behind the range. Seven weeks from demolition to final walkthrough.</p>
"""},
{
 "page": "kitchen-remodel-carlsbad-unicornio-street.html",
 "project": "Unicornio Street",
 "city": "Carlsbad", "city_page": "carlsbad.html",
 "prefix": "unicornio", "photos": range(1, 6),
 "anchor": "kitchens-cabinets.html#kitchen-unicornio-street",
 "blurb": ("A full gut in Carlsbad that kept the appliance layout: custom cabinetry, quartzite counters "
           "carried up as the backsplash, and new LVP flooring. Six weeks."),
 "hero_sub": ("Unicornio Street &mdash; a full gut that kept the appliance layout, with custom cabinetry, "
              "quartzite counters and backsplash, and new LVP flooring."),
 "specs": [("Location","Carlsbad, San Diego County"),
           ("Timeline","6 weeks"),
           ("Scope","Full gut and rebuild"),
           ("Layout","Appliance positions retained"),
           ("Cabinetry","Custom"),
           ("Counters","Quartzite"),
           ("Backsplash","Quartzite, matched to the counters"),
           ("Flooring","New luxury vinyl plank")],
 "body": """
<p>The fastest of these projects at six weeks, and the reason is straightforward: the services stayed where they were. A full gut, everything stripped back, but no gas, water or waste rerouted.</p>

<p>That is the single biggest lever on a kitchen schedule. Moving appliances means rough-in, inspection, and waiting on trades in sequence. Leaving a working layout alone removes weeks from the calendar and puts the money into cabinetry and stone instead.</p>

<h2>Custom cabinetry</h2>

<p>Built for the room rather than assembled from standard widths. The advantage shows in the places you do not consciously notice — no filler strips where a run does not divide evenly, no dead space above the uppers, and cabinetry that meets walls which are rarely as square as they look.</p>

<h2>Quartzite, counter and wall</h2>

<p>Quartzite counters, with the same stone carried up the wall as the backsplash. Running the slab vertically is a deliberate detail and a demanding one: the veining has to be matched across the joint so the two read as one continuous piece rather than as separate slabs meeting at a corner.</p>

<p>It also removes grout from behind the range, which is the part of any kitchen that takes the most splashing and the most scrubbing. Fewer joints, less to clean, and a wall that reads as stone rather than as tile.</p>

<p>Quartzite is quarried, so each slab is unique and worth seeing in person before it is cut. It also handles a hot pan in a way engineered quartz does not.</p>

<h2>Flooring</h2>

<p>New luxury vinyl plank. Waterproof, which matters in a room where spills are routine, and warmer and quieter underfoot than tile.</p>

<h2>The result</h2>

<p>A complete rebuild inside the existing footprint, finished in six weeks because nothing needed relocating. The budget went where it shows: custom cabinetry and stone from counter to ceiling.</p>
"""},
{
 "page": "kitchen-remodel-carlsbad-luciernaga.html",
 "project": "Luciernaga",
 "city": "Carlsbad", "city_page": "carlsbad.html",
 "prefix": "luciernaga", "photos": range(1, 9),
 "anchor": "kitchens-cabinets.html#kitchen-luciernaga-street",
 "blurb": ("A full gut in Carlsbad with every appliance relocated, new white oak cabinetry, and quartz "
           "counters carried up as the backsplash, built around flooring the owners kept."),
 "hero_sub": ("Luciernaga &mdash; a full gut with every appliance relocated, new white oak cabinetry and "
              "quartz counters and backsplash, built around existing flooring that was kept."),
 "specs": [("Location","Carlsbad, San Diego County"),
           ("Timeline","8 weeks"),
           ("Scope","Full gut and rebuild"),
           ("Layout","Appliances relocated"),
           ("Cabinetry","New white oak"),
           ("Counters","Quartz"),
           ("Backsplash","Quartz, matched to the counters"),
           ("Flooring","Existing floor retained")],
 "body": """
<p>A full gut in Carlsbad with two decisions pulling in opposite directions: every appliance moved, and the existing floor kept. Both were the right call, and together they shaped how the job ran.</p>

<h2>Relocating the appliances</h2>

<p>Every appliance changed position, which means gas, water, waste and power all rerouted. It is the most disruptive part of a kitchen project and the part that decides whether the finished room works — landing space beside the oven, a refrigerator door clear of the walkway, a sink placed so two people are not reaching across each other.</p>

<p>None of it photographs. All of it is why the room functions.</p>

<h2>Working around the existing floor</h2>

<p>The floor was sound and the owners liked it, so it stayed. That is harder than replacing it, not easier.</p>

<p>Protecting a finished floor through demolition, plumbing and a full cabinetry installation takes genuine care, and the new cabinetry has to meet a datum that is already fixed rather than being set to suit. But tearing out a floor with years left in it is spending on something nobody asked to change — and with the services being rerouted anyway, the discipline was worth it.</p>

<h2>White oak cabinetry</h2>

<p>New throughout, in white oak. It takes a light finish without going orange the way some oaks do, and the grain carries a large expanse without needing a second material to break it up.</p>

<h2>Quartz, counter and wall</h2>

<p>Quartz counters with the same material carried up the wall as the backsplash. Running the slab vertically removes the horizontal break a tile backsplash creates, so the counter and wall read as one surface.</p>

<p>It also removes grout from behind the range — the part of a kitchen that takes the most splashing and the most cleaning. Quartz was the right choice for a household that wanted a surface needing no sealing and no thought, and being engineered rather than quarried, the slab that arrives matches the slab that was specified.</p>

<h2>The result</h2>

<p>A kitchen reorganised from the services outward, on a floor that never needed replacing. Eight weeks from demolition to final walkthrough.</p>
"""},
{
 "page": "kitchen-remodel-solana-beach-south-sierra-avenue.html",
 "project": "South Sierra Avenue",
 "city": "Solana Beach", "city_page": "solana-beach.html",
 "prefix": "southsierra", "photos": range(1, 13),
 "anchor": "kitchens-cabinets.html#kitchen-south-sierra-avenue",
 "blurb": ("A full gut in Solana Beach with semi-custom white cabinetry and a custom light green island "
           "built at 40 inches, concealing the washer and dryer behind a pocket door system."),
 "hero_sub": ("South Sierra Avenue &mdash; a full gut with semi-custom white cabinetry and a custom light "
              "green island built taller than standard, hiding the laundry behind pocket doors."),
 "specs": [("Location","Solana Beach, San Diego County"),
           ("Timeline","5 weeks"),
           ("Scope","Full gut and rebuild"),
           ("Layout","Laundry integrated into the island"),
           ("Cabinetry","Semi-custom white, custom light green island"),
           ("Island","40 in high, pocket door system"),
           ("Backsplash","Tile"),
           ("Flooring","New engineered hardwood")],
 "body": """
<p>The fastest project on this list at five weeks, and the one with the most unusual piece of joinery: the washer and dryer live inside the kitchen island, behind doors that slide away rather than swing.</p>

<h2>Laundry inside the island</h2>

<p>Putting a washer and dryer in a kitchen island solves a real problem in a house without room for a separate laundry. It also creates several.</p>

<p>The island has to carry plumbing and a drain, ventilation for the dryer, and enough structure to take appliances that vibrate under load. And the doors cannot swing — a hinged door standing open in the middle of a kitchen blocks the walkway and is exactly where someone walks into it.</p>

<p>Hence the pocket door system. The doors slide back into the cabinetry rather than opening into the room, so the appliances are reachable while nothing projects into the space. Closed, the island reads as an island. It is the sort of detail that only works when the piece is built for the purpose.</p>

<h2>An island at 40 inches</h2>

<p>Standard counter height is 36 inches. This island was built at 40.</p>

<p>Partly that is practical: the extra height accommodates the appliances underneath. But it changes the room as well. A taller island reads more like a bar than a work surface, screens the counter clutter from anyone in the adjoining space, and suits standing conversation rather than food preparation. It is a deliberate choice, not a compromise forced by the machines below.</p>

<h2>Two cabinet approaches in one room</h2>

<p>The perimeter is semi-custom in white; the island is custom in light green. That split follows the work rather than a style rule.</p>

<p>The perimeter runs divided sensibly into standard widths, so semi-custom did the job — full custom would have bought flexibility the walls did not require. The island could not be anything but custom: it is a non-standard height, holds two appliances, and carries a pocket door mechanism. Spending on custom where the room demands it and semi-custom where it does not is how a budget ends up in the right places.</p>

<p>The green also does something a single-finish kitchen cannot. It marks the island as a distinct object rather than another run of cabinetry, which matters when that object is doing several jobs at once.</p>

<h2>Backsplash and flooring</h2>

<p>Tile on the backsplash, which keeps the perimeter light and adds texture behind the working runs. New engineered hardwood on the floor — more stable than solid timber over a slab, and continuous through the space so the kitchen does not stop at a threshold.</p>

<h2>The result</h2>

<p>A kitchen that absorbed the laundry without looking like it had to. Five weeks from demolition to final walkthrough.</p>
"""},
{
 "page": "kitchen-remodel-pacific-beach-everts-street.html",
 "project": "Everts Street",
 "city": "Pacific Beach", "city_page": "san-diego.html",
 "prefix": "everts", "photos": range(1, 6),
 "anchor": "kitchens-cabinets.html#kitchen-everts-street",
 "blurb": ("A full gut in Pacific Beach that kept the appliance layout: two-tone semi-custom cabinetry in "
           "blue and white, quartzite counters and backsplash, and a ceiling-recessed custom hood."),
 "hero_sub": ("Everts Street &mdash; a full gut in Pacific Beach that kept the appliance layout, with "
              "two-tone blue and white cabinetry, quartzite counters and a ceiling-recessed custom hood."),
 "specs": [("Location","Pacific Beach, San Diego"),
           ("Timeline","6 weeks"),
           ("Scope","Full gut and rebuild"),
           ("Layout","Appliance positions retained"),
           ("Cabinetry","Semi-custom two-tone, blue and white"),
           ("Counters","Quartzite"),
           ("Backsplash","Quartzite, matched to the counters"),
           ("Flooring","New luxury vinyl plank")],
 "body": """
<p>A full gut in Pacific Beach, finished in six weeks. The appliances were already well placed, so nothing was rerouted — which is most of the reason the schedule was short.</p>

<h2>The ceiling-recessed hood</h2>

<p>The hood is custom and set into the ceiling rather than hung below it. That is a meaningfully different piece of work from fitting a chimney hood to a wall.</p>

<p>Recessing it means the ductwork and the housing sit within the ceiling structure, which has to be framed to take them and finished so the transition disappears. Done properly the hood reads as part of the ceiling rather than an appliance suspended from it, and the sightline across the kitchen stays unbroken — nothing hangs at eye level.</p>

<p>In a room this size that matters. A bulky wall hood would have dominated it; this one does the same job and gets out of the way.</p>

<h2>Two-tone cabinetry, semi-custom</h2>

<p>Blue and white, and semi-custom rather than full custom. Both decisions suited the room.</p>

<p>Semi-custom is built to order from a defined range with modifications where they are needed. Where a kitchen divides sensibly into standard widths and has no awkward structure to design around, full custom buys flexibility that goes unused — and the difference is better spent on stone or on a hood like this one.</p>

<p>The two tones give the room depth without a second material. Blue at the working level grounds the space; white above keeps the upper half light, which counts for a lot in a smaller kitchen.</p>

<h2>Quartzite, counter and wall</h2>

<p>Quartzite counters with the same slab carried up as the backsplash. Running the stone vertically removes the horizontal break a tile backsplash creates, so counter and wall read as one surface — and it takes grout off the wall behind the range, which is the hardest-working surface in any kitchen.</p>

<p>Quartzite is quarried, so each slab is unique, and it handles a hot pan in a way engineered quartz does not.</p>

<h2>Flooring</h2>

<p>Luxury vinyl plank throughout. Waterproof, warm and quiet underfoot, and forgiving over a slab — a sensible choice near the coast, where humidity is less kind to timber.</p>

<h2>The result</h2>

<p>A compact kitchen rebuilt entirely inside its existing footprint, with the ceiling doing work the walls did not have room for. Six weeks from demolition to final walkthrough.</p>
"""},
{
 "page": "kitchen-remodel-san-diego-north-star-drive.html",
 "project": "North Star Drive",
 "city": "San Diego", "city_page": "san-diego.html",
 "prefix": "northstar", "photos": range(1, 7),
 "anchor": "kitchens-cabinets.html#kitchen-north-star-drive",
 "blurb": ("A full gut in San Diego that kept the appliance layout: semi-custom grey cabinetry, quartz "
           "counters, a tile backsplash, new windows and LVP flooring."),
 "hero_sub": ("North Star Drive &mdash; a full gut that kept the appliance layout, with semi-custom grey "
              "cabinetry, quartz counters, new windows and LVP flooring."),
 "specs": [("Location","San Diego"),
           ("Timeline","6 weeks"),
           ("Scope","Full gut and rebuild"),
           ("Layout","Appliance positions retained, new windows"),
           ("Cabinetry","Semi-custom, grey"),
           ("Counters","Quartz"),
           ("Backsplash","Tile"),
           ("Flooring","New luxury vinyl plank")],
 "body": """
<p>A full gut finished in six weeks. The existing appliance layout was sound, so the services stayed where they were and the work went into cabinetry, surfaces, and the windows.</p>

<h2>New windows</h2>

<p>Replacing windows is exterior work as much as interior. Each opening has to be re-flashed and sealed so the wall keeps water out as reliably as it did before — get that detailing wrong and you have traded a draught for a problem that shows up inside the wall years later.</p>

<p>Done properly it changes a kitchen more than the specification suggests. New units bring in more daylight, seal considerably better than what they replace, and remove the cold edge an old window puts on the room beside it.</p>

<h2>Semi-custom grey cabinetry</h2>

<p>Semi-custom was the right tier here. It is built to order from a defined range, with modifications available where a room needs them — and where the runs divide sensibly into standard widths, full custom buys flexibility that goes unused.</p>

<p>Grey sits between the two easy choices. White can read cold in a room with a lot of daylight, and timber commits the kitchen to a warmth that not every house wants. A mid grey holds its own against both the quartz and the tile without competing with either.</p>

<h2>Counters and backsplash</h2>

<p>Quartz counters, chosen for a household that wanted a surface needing no sealing and no thought — being engineered rather than quarried, the slab that arrives matches the slab that was specified.</p>

<p>Tile on the backsplash rather than stone. Where the cabinetry is a single quiet colour, tile is the element that introduces texture, and it keeps the room from reading flat.</p>

<h2>Flooring</h2>

<p>New luxury vinyl plank. Waterproof, warmer and quieter underfoot than tile, and forgiving over a concrete slab.</p>

<h2>The result</h2>

<p>A kitchen rebuilt inside its own footprint, with the budget going into the windows and the finishes rather than into rerouting services that did not need moving. Six weeks from demolition to final walkthrough.</p>
"""},
{
 "page": "kitchen-remodel-carlsbad-brava-street.html",
 "project": "Brava Street",
 "city": "Carlsbad", "city_page": "carlsbad.html",
 "prefix": "brava", "photos": range(1, 8),
 "anchor": "kitchens-cabinets.html#kitchen-brava-street",
 "blurb": ("A full gut in Carlsbad with every appliance relocated, a curved custom island, a built-out bar "
           "area, and quartzite carried across counters, backsplash and the structural posts."),
 "hero_sub": ("Brava Street &mdash; a full gut with every appliance relocated, a curved custom island, a "
              "built-out bar area, and quartzite across counters, backsplash and posts."),
 "specs": [("Location","Carlsbad, San Diego County"),
           ("Timeline","8 weeks"),
           ("Scope","Full gut, bar area built out"),
           ("Layout","All appliances relocated"),
           ("Cabinetry","Custom island and bar, semi-custom white perimeter"),
           ("Counters","Quartzite, curved island"),
           ("Backsplash","Quartzite, and stone-clad posts"),
           ("Flooring","New luxury vinyl plank")],
 "body": """
<p>A full gut in Carlsbad that went beyond the kitchen. Every appliance moved, a bar area was built out alongside it, and quartzite was carried across three surfaces that are usually treated separately — counters, backsplash, and the structural posts.</p>

<h2>Custom where it counts, semi-custom where it does not</h2>

<p>The perimeter cabinetry is semi-custom in white; the island and the bar are custom. That split follows the work rather than a preference.</p>

<p>The perimeter runs divided sensibly into standard widths, so semi-custom did the job — full custom there would have bought flexibility the walls did not require. The island could not be anything but custom, because it is curved, and the bar area had to be built to a space that did not previously exist as one.</p>

<p>Putting custom money only where the room demands it is how a budget reaches further than it otherwise would.</p>

<h2>The curved island</h2>

<p>The island is cut to a curve rather than left square. That does real work: it opens the approach into the kitchen, removes the corner people walk into, and gives seating a natural arc to gather around instead of a straight line.</p>

<p>Curved stone is considerably more demanding to template and fabricate than a rectangle, and the cabinetry beneath has to be built to the same radius. It is a detail that reads as custom precisely because it could not have come off a shelf.</p>

<h2>Stone on the posts</h2>

<p>The structural posts are clad in the same quartzite as the counters. This is the detail that ties the room together and the one most likely to be skipped.</p>

<p>Posts are usually a nuisance — necessary structure standing in the middle of an open plan, boxed in drywall and painted to be ignored. Wrapping them in the counter stone turns them from an obstacle into part of the design. The room stops reading as a kitchen with columns in it and starts reading as one deliberate space.</p>

<p>It is fussy work. Stone on a vertical surface has to be supported and the joints have to line up with the horizontal runs nearby, or the eye catches it immediately.</p>

<h2>Quartzite throughout</h2>

<p>Counters, backsplash and posts in the same stone. Carrying one material across all three removes the visual breaks that separate materials create, so the eye travels the room without stopping.</p>

<p>Quartzite is quarried, so every slab is unique and worth seeing before it is cut — and it takes a hot pan in a way engineered quartz does not.</p>

<h2>The bar area</h2>

<p>Built out as part of the same project, in custom cabinetry matched to the island. Adding a bar is what turns a kitchen from somewhere food is made into somewhere people stay — and building it at the same time as the kitchen means the two are designed as one room rather than as a kitchen with something added later.</p>

<h2>The result</h2>

<p>A kitchen and bar that read as a single space, with the structure absorbed into the design rather than worked around. Eight weeks from demolition to final walkthrough.</p>
"""},
{
 "page": "kitchen-remodel-san-diego-canyon-drive.html",
 "project": "Canyon Drive",
 "city": "San Diego", "city_page": "san-diego.html",
 "prefix": "canyon", "photos": range(1, 5),
 "anchor": "kitchens-cabinets.html#kitchen-canyon-drive",
 "blurb": ("A full gut in San Diego where a load-bearing wall came down, every appliance moved, and a "
           "custom hood was built to the new layout."),
 "hero_sub": ("Canyon Drive &mdash; a full gut where a load-bearing wall came down, every appliance moved, "
              "and new windows changed how the room reads."),
 "specs": [("Location","San Diego"),
           ("Timeline","8 weeks"),
           ("Scope","Full gut, load-bearing wall removed"),
           ("Layout","All appliances relocated"),
           ("Cabinetry","Semi-custom, custom built hood"),
           ("Backsplash","Tile"),
           ("Windows","New throughout"),
           ("Flooring","New engineered hardwood")],
 "body": """
<p>This one started with a wall that could not simply be knocked out. Taking down a load-bearing wall is the difference between a kitchen that gets refreshed and a kitchen that gets rethought, and it is the single change that most often makes a house feel like a different house.</p>

<h2>Removing a load-bearing wall</h2>

<p>A load-bearing wall is holding up what is above it. It cannot be removed &mdash; only replaced. The load has to be picked up by a beam, and that beam has to carry down through posts to something that can take the weight, all the way to the foundation.</p>

<p>That means temporary shoring while the wall comes out, an engineered beam sized for the actual span, and inspection. It is permitted work and it should be. Contractors who open walls without that process leave homeowners with a problem that surfaces years later, usually when they try to sell.</p>

<p>Done properly, it is invisible. Nobody walking through afterwards can tell there was ever a wall there, which is exactly the point.</p>

<h2>New appliance locations</h2>

<p>With the wall gone, none of the old appliance positions made sense. Every one of them moved.</p>

<p>Relocating appliances means new gas, new electrical, new water lines and new venting run inside the walls and under the floor before anything closes up. It is work nobody ever sees, and it is the reason the finished kitchen works the way it does &mdash; the range where the cooking naturally happens, the refrigerator where it does not block the path through.</p>

<h2>Semi-custom cabinets with a custom hood</h2>

<p>The cabinetry is semi-custom, which fit the new runs well. The hood is custom, built on site.</p>

<p>That combination is deliberate. Semi-custom lines cover standard widths and standard depths, which is most of a kitchen. A hood is the exception &mdash; it sits at eye level in the middle of the wall, it has to reach a specific height, and it has to be sized to the range beneath it. Building it rather than ordering it means it fits the room instead of the room accommodating it.</p>

<h2>New windows</h2>

<p>New windows went in as part of the same project. In a kitchen this matters more than it sounds: a window over the sink is where you look for hours a week, and older units are usually smaller, single-pane, and framed heavier than they need to be.</p>

<p>Replacing them while the walls are already open is also considerably less disruptive than doing it later, when the finishes are in and every opening has to be protected.</p>

<h2>Engineered hardwood and tile</h2>

<p>New engineered hardwood throughout, with a tile backsplash. Engineered hardwood handles the humidity swings of a kitchen better than solid wood does, and it can run continuously from the kitchen into the adjoining rooms &mdash; which, with the wall gone, is now one space.</p>

<h2>The result</h2>

<p>An open kitchen where the structure was rebuilt rather than worked around, in eight weeks from demolition to final walkthrough.</p>
"""},
{
 "page": "kitchen-remodel-rancho-santa-fe-dalia-drive.html",
 "project": "Dalia Drive",
 "city": "Rancho Santa Fe", "city_page": "rancho-santa-fe.html",
 "prefix": "dalia", "photos": range(1, 9),
 "anchor": "kitchens-cabinets.html#kitchen-dalia-drive",
 "blurb": ("A full gut in Rancho Santa Fe with custom white cabinetry, a built-in hood, a panel-front "
           "integrated refrigerator, and every appliance in a new location."),
 "hero_sub": ("Dalia Drive &mdash; custom white cabinetry, a built-in hood, a panel-front integrated "
              "refrigerator, and every appliance relocated."),
 "specs": [("Location","Rancho Santa Fe, San Diego County"),
           ("Timeline","8 weeks"),
           ("Scope","Full gut, all appliances relocated"),
           ("Cabinetry","Custom white, built-in hood"),
           ("Refrigerator","Panel-front, integrated into the cabinetry"),
           ("Counters","Quartz"),
           ("Backsplash","Tile"),
           ("Flooring","New engineered hardwood")],
 "body": """
<p>A full gut in Rancho Santa Fe, built in custom white cabinetry with every appliance in a new location and a refrigerator you cannot pick out of the run.</p>

<h2>The panel-front refrigerator</h2>

<p>The refrigerator is fronted in the same custom cabinet panels as everything around it. From across the room it reads as tall cabinetry, not as an appliance.</p>

<p>This is one of the details that separates a custom kitchen from a very good semi-custom one, and it is not a finish choice &mdash; it is a construction one. A panel-ready refrigerator has to be specified before the cabinets are built, because the surrounding boxes are made to its exact dimensions and the panels are made to match the doors beside them. There is no retrofitting it afterwards.</p>

<p>What it buys is quiet. A stainless refrigerator is a large reflective rectangle that pulls the eye every time you walk in. Panelling it lets the room be about the room.</p>

<h2>The built-in hood</h2>

<p>The hood is built in and clad to match, so it belongs to the cabinetry rather than sitting in front of it.</p>

<p>Like the refrigerator, this has to be planned early. The venting has to be routed before anything closes up, the surround has to be framed to the insert's clearances, and the whole assembly has to land at a height that clears the cook without cutting the wall in half visually.</p>

<h2>Custom white cabinets</h2>

<p>Full custom throughout, in white. Custom earns its cost in a kitchen like this one, where the cabinetry has to absorb a refrigerator and a hood and still read as one continuous run &mdash; every box is built to the wall it sits against and to the appliance it surrounds.</p>

<p>White holds up because it is the least dated colour a kitchen can be. Cabinet colours cycle; white was in these kitchens before the current cycle and will be there after.</p>

<h2>Every appliance relocated</h2>

<p>Not one appliance stayed where it was. That meant gas, electrical, water and venting all rerun inside the walls and under the floor while everything was open.</p>

<p>Moving appliances is the part of a remodel homeowners tend to be talked out of, because it adds work that does not photograph. It is also the part that determines whether the kitchen is pleasant to cook in &mdash; where the range sits relative to the sink, whether the refrigerator door blocks the walkway, how far you carry a hot pan.</p>

<h2>Quartz, tile and hardwood</h2>

<p>Quartz counters, a tile backsplash, and new engineered hardwood. Quartz is the practical counter for a kitchen that gets used: non-porous, no sealing, and consistent across slabs, so a long run does not shift pattern halfway down.</p>

<h2>The result</h2>

<p>A custom white kitchen where the appliances disappear into the cabinetry and the layout was rebuilt around how the room is actually used. Eight weeks from demolition to final walkthrough.</p>
"""},
{
 "page": "kitchen-remodel-pacific-beach-dixie-drive.html",
 "project": "Dixie Drive",
 "city": "Pacific Beach", "city_page": "san-diego.html",
 "prefix": "dixie", "photos": range(1, 9),
 "anchor": "kitchens-cabinets.html#kitchen-dixie-drive",
 "blurb": ("A full gut in Pacific Beach with custom blue base cabinets under custom white uppers, "
           "quartzite counters and backsplash, and every appliance relocated."),
 "hero_sub": ("Dixie Drive &mdash; custom blue cabinets beneath custom white uppers, quartzite counters "
              "and backsplash, and every appliance in a new location."),
 "specs": [("Location","Pacific Beach, San Diego"),
           ("Timeline","7 weeks"),
           ("Scope","Full gut, all appliances relocated"),
           ("Cabinetry","Custom blue base, custom white uppers"),
           ("Counters","Quartzite"),
           ("Backsplash","Quartzite"),
           ("Windows","New throughout"),
           ("Flooring","New luxury vinyl plank")],
 "body": """
<p>A full gut in Pacific Beach, built in two-tone custom cabinetry with quartzite carried from the counters straight up the wall.</p>

<h2>Blue below, white above</h2>

<p>The base cabinets are a custom blue; the uppers are custom white. Both were built for the room rather than ordered from a line.</p>

<p>Two-tone is not only a colour decision &mdash; it changes how the kitchen sits. Darker cabinets below and lighter above give the room a base and let the top half recede, so the space reads taller and less closed in than an all-one-colour run. It is a useful move in beach houses, where kitchens are often smaller and ceilings lower than in newer inland construction.</p>

<p>Going custom on both halves matters here because the colours have to match each other in finish and sheen, not just in hue. Two different stock lines rarely do.</p>

<h2>Quartzite counters and backsplash</h2>

<p>The same quartzite runs across the counters and up the wall as the backsplash. Carrying one stone through both removes the horizontal seam where a counter usually stops and tile begins, so the surface reads as continuous.</p>

<p>Quartzite is a natural stone, quarried rather than manufactured, which means the slab you choose is the slab you get &mdash; worth seeing in person before it is cut. It is harder than marble and it will take a hot pan, which engineered quartz will not.</p>

<p>Against blue cabinetry it does something specific: the stone's movement is what carries the visual interest, so the cabinet colour can stay flat and calm underneath it.</p>

<h2>Every appliance relocated</h2>

<p>All of the appliances moved. That means gas, electrical, water and venting rerun inside the walls and under the floor before anything closed up.</p>

<p>In an older Pacific Beach house this is usually the right call. These kitchens were laid out for how people cooked decades ago, often in a smaller footprint with the refrigerator wherever it fit. Rebuilding the layout is what makes the finished room work.</p>

<h2>New windows and LVP flooring</h2>

<p>New windows went in throughout while the walls were open &mdash; far less disruptive than doing it after the finishes are in. Coastal houses take salt air on the frames, and older single-pane units are usually the weakest point in the whole envelope.</p>

<p>The floors are new luxury vinyl plank: fully waterproof, which is worth having a few blocks from the sand, and forgiving of the sand itself.</p>

<h2>The result</h2>

<p>A two-tone custom kitchen with quartzite running counter to ceiling, rebuilt from the layout up in seven weeks.</p>
"""},
{
 "page": "kitchen-remodel-encinitas-caminito-ocean-cove.html",
 "project": "Caminito Ocean Cove",
 "city": "Encinitas", "city_page": "encinitas.html",
 "prefix": "caminito", "photos": range(1, 9),
 "anchor": "kitchens-cabinets.html#kitchen-caminito-ocean-cove",
 "blurb": ("A full gut in Encinitas that kept the existing layout: dual-tone custom cabinetry with a "
           "stained island against painted white runs, a custom hood, quartz counters and new sliding doors."),
 "hero_sub": ("Caminito Ocean Cove &mdash; a full gut that kept the layout, with a stained island against "
              "painted white cabinetry, a custom hood, quartz counters and new sliding doors."),
 "specs": [("Location","Encinitas, San Diego County"),
           ("Timeline","6 weeks"),
           ("Scope","Full gut, existing layout retained"),
           ("Cabinetry","Custom dual-tone, stained island and painted white runs"),
           ("Counters","Quartz"),
           ("Flooring","1,100 sq ft luxury vinyl plank")],
 "body": """
<p>A full gut in Encinitas, taken back to studs and rebuilt without moving the plan. The existing layout worked, so the work went into cabinetry, surfaces and light rather than into relocating services.</p>

<h2>Dual-tone cabinetry</h2>

<p>The island is stained; the perimeter runs are painted white. Pairing a stained island against painted cabinetry is a different effect from two painted colours — the grain stays visible on the island, so it reads as a piece of furniture in timber rather than another run of joinery in a second shade.</p>

<p>It also ages differently, and better. Painted cabinetry shows wear at the points hands land, and can be touched up. A stained island wears in rather than out, which suits the piece that takes the most daily contact.</p>

<h2>The hood</h2>

<p>Custom, built for this room. A hood is the one element in most kitchens with nothing above or beside it to hide behind, which is why an off-the-shelf unit so often looks like it was chosen rather than designed. Building it to the room lets it sit in proportion with the cabinetry either side and carry the eye upward.</p>

<h2>New sliding doors</h2>

<p>Replacing the sliders changed the room as much as anything inside it. New units bring in more daylight, seal considerably better than what they replaced, and connect the kitchen to the outside — which in Encinitas is a space you use most of the year.</p>

<p>Door replacement is also structural detailing: the opening has to be flashed and sealed properly, or you have traded a draught for a leak.</p>

<h2>Counters and flooring</h2>

<p>Quartz throughout, chosen for a household that wanted a surface needing no sealing and no thought.</p>

<p>The floor is luxury vinyl plank, laid across 1,100 square feet. LVP is fully waterproof, which is the argument for it in a kitchen — a dishwasher leak or a dropped pan of water is a mopping job rather than a repair. It also sits warmer and quieter underfoot than tile, and over a concrete slab it is more forgiving than timber.</p>

<p>Running it continuously across the whole area means the kitchen reads as part of the rooms around it rather than stopping at a threshold.</p>

<h2>The result</h2>

<p>The same footprint, rebuilt completely. More daylight through new sliders, a stained island anchoring a room of white cabinetry, and a hood made for the space. Six weeks from demolition to final walkthrough.</p>
"""},
{
 "page": "kitchen-remodel-carmel-valley-baywind-point.html",
 "project": "Baywind Point",
 "city": "Carmel Valley", "city_page": "carmel-valley.html",
 "prefix": "baywind", "photos": range(1, 9),
 "anchor": "kitchens-cabinets.html#kitchen-baywind-point",
 "blurb": ("A full gut in Carmel Valley that kept the existing layout: two-tone custom cabinetry in soft "
           "green and white, two-tone counters, a curved island and a custom tile backsplash."),
 "hero_sub": ("Baywind Point &mdash; a full gut that kept the layout, with two-tone custom cabinetry, a "
              "curved island counter and a custom tile backsplash."),
 "specs": [("Location","Carmel Valley, San Diego County"),
           ("Timeline","8 weeks"),
           ("Scope","Full gut, existing layout retained"),
           ("Cabinetry","Custom two-tone, soft green and white"),
           ("Counters","Two-tone, curved island"),
           ("Flooring","New tile throughout")],
 "body": """
<p>Not every kitchen needs its walls moved. This was a full gut — everything out, back to studs — but the existing layout was genuinely working, so we kept it and spent the budget where it would show.</p>

<p>That decision is worth dwelling on. Moving plumbing and gas is the most disruptive part of any kitchen project, and doing it when the plan already functions is spending money on the parts nobody sees. Here the footprint stayed, and the room changed completely anyway.</p>

<h2>Two-tone cabinetry</h2>

<p>Custom throughout, in a soft green paired with white. Two-tone is one of the more reliable ways to give a kitchen depth without introducing a second material — the eye reads the lighter uppers as receding and the deeper base cabinets as grounding the room.</p>

<p>Running the green across the island and the lower runs, with white above, keeps the upper half of the room feeling open while the working level carries the colour. It is a scheme that will still look considered when a bolder choice would have dated.</p>

<h2>The curved island</h2>

<p>The island counter is cut to a half-moon on the seating side rather than left square. That curve does real work: it opens the approach into the kitchen, removes the sharp corner people walk into, and gives the stools a natural arc to sit around rather than a straight line.</p>

<p>Curved stone is more demanding to fabricate and template than a rectangle, and the cabinetry beneath has to be built to match the radius. It is the kind of detail that reads as custom precisely because it could not have come off a shelf.</p>

<h2>Two-tone counters</h2>

<p>The island carries a different stone from the perimeter runs. Pairing surfaces this way lets the island read as a separate piece of furniture within the room, which is the same idea as the two-tone cabinetry working on a second axis.</p>

<h2>Backsplash and flooring</h2>

<p>The backsplash is a custom tile layout rather than a standard field — it is the one place in this kitchen where pattern appears, so it carries the room's personality without competing with the cabinetry.</p>

<p>New tile flooring throughout, in a large format that keeps grout lines to a minimum and makes the floor read as one continuous surface.</p>

<h2>The result</h2>

<p>Proof that a full gut does not require moving a single wall. The layout that worked was kept, and everything the family actually touches — cabinetry, counters, tile, floor — was rebuilt. Eight weeks from demolition to final walkthrough.</p>
"""},
]


from bathroom_projects import BATHROOMS
from fullhome_projects import FULLHOMES
PROJECTS += BATHROOMS + FULLHOMES


def ld(o):
    return ('  <script type="application/ld+json">\n  '
            + json.dumps(o, indent=2, ensure_ascii=False).replace("\n", "\n  ")
            + '\n  </script>\n')


KIND = {
  "kitchen":  {"Label":"Kitchen Remodel", "Service":"Kitchen Remodeling",
               "thing":"kitchen", "things":"kitchens", "verb":"We design and build",
               "svc_page":"kitchen-remodeling.html", "svc_btn":"Kitchen Remodeling",
               "gallery_h2":"The Finished Kitchen", "back":"kitchen projects"},
  "bathroom": {"Label":"Bathroom Remodel", "Service":"Bathroom Remodeling",
               "thing":"bathroom", "things":"bathrooms", "verb":"We design and build",
               "svc_page":"bathroom-remodeling.html", "svc_btn":"Bathroom Remodeling",
               "gallery_h2":"The Finished Bathroom", "back":"bathroom projects"},
  "fullhome": {"Label":"Whole Home Renovation", "Service":"Home Renovation",
               "thing":"home renovation", "things":"whole homes", "verb":"We renovate",
               "svc_page":"home-renovation.html", "svc_btn":"Home Renovations",
               "gallery_h2":"The Finished Home", "back":"home renovation projects"},
}


def build(p):
    kind = p.get("kind", "kitchen")
    K = KIND[kind]
    noun = K["thing"]
    nums = list(p["photos"])
    # The first photo in the gallery set is not always the best lead image -
    # some sets open on the vanity when the page is about the shower.
    hero = f"{p['prefix']}{p.get('hero_photo', nums[0])}-1000.webp"
    photos = "\n".join(
        f'          <img src="{p["prefix"]}{n}-1000.webp" data-full="{p["prefix"]}{n}-2000.webp"'
        f' alt="{p["project"]} {noun} remodel in {p["city"]} — photo {i}"'
        f' class="gallery-image" loading="lazy" />' for i, n in enumerate(nums, 1))
    hero_style = (f' style="object-position: {p["hero_pos"]}"' if p.get("hero_pos") else "")
    related = ""
    if p.get("related"):
        links = " &nbsp;&middot;&nbsp; ".join(
            f'<a href="{pg[:-5]}">{label}</a>' for label, pg in p["related"])
        related = ('            <p class="project-related"><strong>Go deeper on this house:</strong> '
                   + links + '</p>')
    specs = "\n".join(
        f'            <div class="project-spec"><dt>{k}</dt><dd>{v}</dd></div>'
        for k, v in p["specs"])
    title = f"{K['Label']} in {p['city']} — {p['project']} | Guild Builders Inc."

    contractor = {
        "@context":"https://schema.org","@type":"GeneralContractor",
        "name":"Guild Builders Inc.","foundingDate":"2021",
        "image":f"{URL}/{hero}","logo":f"{URL}/favicon.png",
        "url":f"{URL}/{p['page'][:-5]}","telephone":"+1-619-763-2982",
        "email":"info@guildbuildersgroup.com","priceRange":"$$$",
        "description":p["blurb"],
        "address":{"@type":"PostalAddress","addressRegion":"CA","addressCountry":"US"},
        "areaServed":[{"@type":"City","name":f"{p['city']}, CA"},
                      {"@type":"AdministrativeArea","name":"San Diego County"}],
        "knowsAbout":["Kitchen Remodeling","Custom Cabinetry","Bathroom Remodeling","Home Renovation",
                      "Deck Building","Patio Covers","Hardscape","Exterior Renovation"],
        "sameAs":["https://g.page/r/CTjnAyM7sZDXEBM"],
    }
    service = {
        "@context":"https://schema.org","@type":"Service",
        "serviceType":K["Service"],"name":f"{K['Service']} in {p['city']}",
        "description":p["blurb"],"url":f"{URL}/{p['page'][:-5]}",
        "provider":{"@type":"GeneralContractor","name":"Guild Builders Inc.",
                    "url":f"{URL}/","telephone":"+1-619-763-2982"},
        "areaServed":[{"@type":"City","name":f"{p['city']}, CA"}],
    }

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
  new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  }})(window,document,'script','dataLayer','GTM-P526Z2L9');</script>
  <!-- End Google Tag Manager -->

  <link rel="preconnect" href="https://www.googletagmanager.com" />

  <title>{title}</title>
  <meta name="description" content="{p['blurb']}" />

  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=AW-18096983407"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag() {{ dataLayer.push(arguments); }}
    gtag('js', new Date());
    gtag('config', 'AW-18096983407');
    gtag('config', 'G-39ZPTZ73DK');
  </script>

  <link rel="preload" href="fonts/montserrat-latin.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="preload" href="fonts/cormorant-garamond-latin.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="stylesheet" href="fonts.css?v=1" />

  <link rel="stylesheet" href="{CSS}" />

  <link rel="icon" type="image/png" sizes="512x512" href="favicon.png?v=2" />
  <link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png?v=2" />
  <link rel="apple-touch-icon" href="apple-touch-icon.png?v=2" />

  <link rel="canonical" href="{URL}/{p['page'][:-5]}" />
  <meta property="og:type" content="article" />
  <meta property="og:site_name" content="Guild Builders Inc." />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{p['blurb']}" />
  <meta property="og:url" content="{URL}/{p['page'][:-5]}" />
  <meta property="og:image" content="{URL}/{hero}" />
  <meta name="twitter:card" content="summary_large_image" />

{ld(contractor)}{ld(service)}</head>

<body class="project-page">

  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-P526Z2L9"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->

  <div id="top"></div>

  <header class="site-header">
    <div class="container nav">
      <a href="/" class="logo">
        <img src="guild-logo-4.png" alt="Guild Builders Inc. logo" class="logo-image" />
      </a>
      <button class="menu-toggle" id="menu-toggle" aria-label="Open menu">☰</button>
      <nav class="site-nav" id="site-nav" aria-label="Main navigation">
        <a href="/">Home</a>
        <a href="about">About Us</a>
        <a href="services">Services</a>
        <a href="gallery">Gallery</a>
        <a href="/blog/">Blog</a>
        <a href="faq">FAQ</a>
        <a href="contact">Contact</a>
      </nav>
    </div>
  </header>

  <main>

    <section id="top" class="hero hero-small">
      <div class="container hero-content">
        <p class="eyebrow">Project &middot; {p['city']}</p>
        <h1>{K['Label']} in {p['city']}</h1>
        <p class="hero-text">{p['hero_sub']}</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="post-wrap">

          <img src="{hero}" alt="{p['project']} {noun} remodel in {p['city']}" class="post-hero-image"{hero_style} />

          <dl class="project-specs">
{specs}
          </dl>

          <div class="post-body">
{p['body'].strip()}
{related}
          </div>

        </div>
      </div>
    </section>

    <section class="section section-alt gallery-section">
      <div class="container">
        <p class="section-label">{p['project']}</p>
        <h2>{p.get('gallery_h2', K['gallery_h2'])}</h2>
        <div class="gallery-image-grid">
{photos}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="section-label">Planning Something Similar?</p>
        <h2>{K['Service']} in {p['city']}</h2>
        <p class="hero-text" style="max-width:700px;margin:0 auto;">
          {K['verb']} {K['things']} throughout {p['city']} and San Diego County, handling
          planning, permitting, materials and construction as one team.
        </p>
        <div class="hero-buttons" style="margin-top: 2rem;">
          <a href="contact" class="btn btn-primary">Request a Quote</a>
          <a href="{K['svc_page'][:-5]}" class="btn btn-secondary">{K['svc_btn']}</a>
        </div>
        <p style="text-align:center;margin-top:1.6rem;">
          <a href="{p['anchor'].replace('.html','')}" class="gallery-back-link">&larr; Back to all {K['back']}</a>
          &nbsp;&middot;&nbsp;
          <a href="{p['city_page'][:-5]}" class="gallery-back-link">Remodeling in {p['city']}</a>
        </p>
      </div>
    </section>

  </main>

  <footer class="site-footer">
    <div class="container footer-inner">
      <p>© 2026 Guild Builders Inc. All rights reserved.</p>
      <p class="footer-license">Licensed Contractor | CA License #1154614</p>
      <p class="footer-areas">Serving {FOOTER}</p>
    </div>
  </footer>

  <div id="lightbox" class="lightbox">
    <button type="button" class="lightbox-close" id="lightbox-close" aria-label="Close image">&times;</button>
    <button type="button" class="lightbox-arrow lightbox-prev" id="lightbox-prev" aria-label="Previous image">&#10094;</button>
    <img class="lightbox-content" id="lightbox-img" alt="Expanded project image" />
    <button type="button" class="lightbox-arrow lightbox-next" id="lightbox-next" aria-label="Next image">&#10095;</button>
  </div>

  <div class="site-sticky-call">
    <a class="call" href="tel:+16197632982" onclick="return gb_callConversion();">&#128222; (619) 763-2982</a>
    <a class="quote" href="contact">Free Estimate</a>
  </div>

  <script src="{JS}"></script>

</body>
</html>
"""


if __name__ == "__main__":
    # An odd number of specs strands the last one alone in the 2-column strip
    # with dead space beside it. Fail loudly rather than ship it.
    odd = [p["page"] for p in PROJECTS if len(p["specs"]) % 2]
    if odd:
        raise SystemExit("odd spec count (strands a row): " + ", ".join(odd))
    os.chdir(SITE)
    for p in PROJECTS:
        open(p["page"], "w", encoding="utf-8").write(build(p))
        body = re.sub(r"<[^>]+>", " ", p["body"])
        print(f"  {p['page']}  ({len(body.split())} words, {len(list(p['photos']))} photos)")
