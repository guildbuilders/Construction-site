#!/usr/bin/env python3
"""Whole-home renovation pages.

Each of these houses already has a kitchen page and a bathroom page. This is
the third view of the same job - the one that explains what it took to run
all of it as a single project - and it cross-links to the other two rather
than repeating them at length.
"""

FULLHOMES = [
{
 "kind": "fullhome",
 "page": "home-renovation-carmel-valley-kingsfield-court.html",
 "project": "Kingsfield Court",
 "city": "Carmel Valley", "city_page": "carmel-valley.html",
 "prefix": "kingsfield", "photos": range(1, 21),
 "anchor": "full-home-renovations.html#fullhome-kingsfield-court",
 "related": [("The kitchen in detail", "kitchen-remodel-carmel-valley-kingsfield-court.html"),
             ("The bathrooms in detail", "bathroom-remodel-carmel-valley-kingsfield-court.html")],
 "blurb": ("A whole-home renovation in Carmel Valley: a full kitchen gut with custom white oak "
           "cabinetry, three bathrooms rebuilt, and 2,600 sq ft of engineered hardwood laid "
           "throughout the house."),
 "hero_sub": ("Kingsfield Court &mdash; a kitchen gutted and rebuilt, three bathrooms remodelled, and "
              "2,600 sq ft of hardwood laid across the whole house."),
 "specs": [("Location","Carmel Valley, San Diego County"),
           ("Scope","Kitchen and three bathrooms"),
           ("Whole home","New flooring throughout"),
           ("Kitchen","8 weeks &mdash; full gut, appliances relocated"),
           ("Bathrooms","6 weeks &mdash; master, tub-to-tub, shower-to-shower"),
           ("Cabinetry","Custom white oak; navy island and hood"),
           ("Counters","Quartzite"),
           ("Flooring","2,600 sq ft glued-down engineered hardwood")],
 "body": """
<p>Three separate projects in one house, run as one: a kitchen taken back to the studs, three bathrooms rebuilt, and a single hardwood floor laid across all 2,600 square feet of the home.</p>

<h2>The floor is what makes it one house</h2>

<p>Of everything here, the flooring is the decision that turns a set of remodelled rooms into a renovated house.</p>

<p>Rooms remodelled at different times end up sitting on different floors, and every doorway becomes a transition strip between two materials that were each chosen to be current in a different year. You feel it walking through even if you never look down.</p>

<p>Laying 2,600 square feet in one go removes every one of those thresholds. The kitchen, the halls and the living space are on one continuous surface, and the house reads as a whole rather than as a sequence of decisions.</p>

<p>It was glued down rather than floated. A floated floor rests on an underlayment and moves as a sheet; over a large open area that produces a hollow sound underfoot and a slight give at the edges. Glued down, the floor is bonded to the slab &mdash; quieter, more solid, and considerably more work to install, which is the trade.</p>

<h2>The kitchen</h2>

<p>A full gut with every appliance relocated, rebuilt in custom white oak with a navy island and hood, and quartzite counters.</p>

<p>Going custom was not a preference here. The room has a long run of tall cabinetry, a chimney breast for the hood, and a ceiling carrying structural beams &mdash; modular boxes would have left filler strips and a bulkhead. Built to the room, the cabinetry runs floor to ceiling with no dead space.</p>

<p>The navy on the island and hood is what keeps a room of unbroken white oak from reading flat. Two focal elements in a deeper tone give the eye somewhere to land.</p>

<h2>The three bathrooms</h2>

<p>A master with a large tiled shower and custom cabinets, a tub-to-tub rebuild, and a shower rebuilt in place. Custom vanities in all three.</p>

<p>Each was treated according to what it needed rather than to a single formula. The master's shower is large, which is less forgiving than it sounds &mdash; the pan has to be pre-sloped correctly across the whole area and the drain positioned so water reaches it from every corner. The other two kept their fixtures where they were, because those layouts already worked, and the effort went into the waterproofing behind the tile instead.</p>

<h2>Running it as one project</h2>

<p>This is the part that is hard to see in photographs and is most of the reason a whole-home renovation is worth doing as one job.</p>

<p>Every trade comes through once. One demolition phase, one plumbing rough across the kitchen and three bathrooms, one electrical rough, one inspection cycle, one tile crew moving room to room, one flooring installation covering the entire house at the end.</p>

<p>Done room by room over several years, each of those repeats. The plumber comes four separate times. The house becomes a job site four separate times. And the flooring can never be one continuous floor, because by the time the last room is done the first room's material has been discontinued.</p>

<p>The sequencing also has to account for the floor going in late. Hardwood across the whole house cannot be laid until the wet trades are finished and out, or it gets damaged by the work that follows. That constrains the order everything else happens in.</p>

<h2>The result</h2>

<p>A Carmel Valley house where the kitchen, the bathrooms and the floor underneath all of it were decided at the same time, by the same people, and built by one crew.</p>
"""},

{
 "kind": "fullhome",
 "page": "home-renovation-carmel-valley-arabian-crest-drive.html",
 "project": "Arabian Crest Drive",
 "city": "Carmel Valley", "city_page": "carmel-valley.html",
 "prefix": "arabiancrest", "photos": range(1, 11),
 "anchor": "full-home-renovations.html#fullhome-arabian-crest-drive",
 "related": [("The kitchen in detail", "kitchen-remodel-carmel-valley-arabian-crest-drive.html"),
             ("The bathrooms in detail", "bathroom-remodel-carmel-valley-arabian-crest-drive.html")],
 "blurb": ("A whole-home renovation in Carmel Valley: a full kitchen gut in white oak with a custom "
           "built-in glass wine cellar, and two bathrooms rebuilt with custom cabinetry."),
 "hero_sub": ("Arabian Crest Drive &mdash; a kitchen gutted and rebuilt in white oak around a custom "
              "glass wine cellar, and two bathrooms rebuilt with custom cabinetry."),
 "specs": [("Location","Carmel Valley, San Diego County"),
           ("Scope","Kitchen and two bathrooms"),
           ("Kitchen","7 weeks &mdash; full gut and rebuild"),
           ("Bathrooms","4 weeks &mdash; shower-to-shower in both"),
           ("Cabinetry","White oak in the kitchen, custom in both bathrooms"),
           ("Counters","Quartz"),
           ("Feature","Custom built-in glass wine cellar"),
           ("Flooring","Tile in one bathroom, engineered hardwood in the other")],
 "body": """
<p>A kitchen and two bathrooms in the same Carmel Valley house, rebuilt as one project.</p>

<h2>The kitchen and its wine cellar</h2>

<p>A full gut, rebuilt in white oak with quartz counters, and built around a custom glass-fronted wine cellar.</p>

<p>The wine cellar is the part that had to be designed before anything else was ordered. A built-in glass enclosure is not a cabinet with a door on it &mdash; it needs its own framed opening, its own cooling, power run to the right spot, and glass specified to the finished dimensions. All of that is fixed before the cabinetry around it is built, because the cabinetry has to meet it exactly.</p>

<p>It also has to be positioned where it is visible without being in the way. A wine cellar behind a door is a refrigerator; one you can see into is the feature of the room.</p>

<h2>The two bathrooms</h2>

<p>Both were shower-to-shower remodels with custom cabinetry, and they were floored differently on purpose &mdash; one in tile, one in engineered hardwood.</p>

<p>Hardwood in a bathroom is a fair thing to question, and engineered is the reason it works. The plank is a hardwood wear layer over a cross-laminated core, and that core keeps it from moving with humidity the way a solid board does.</p>

<p>The reason to do it is continuity. Where a bathroom opens off a bedroom or hall already floored in hardwood, carrying the same floor through means the doorway stops being a boundary between two materials. Tiling it would have drawn a line at the door. The other bathroom took tile, which was right for the space it opens onto.</p>

<p>Neither shower moved. Both came out to the studs anyway &mdash; old tile, old backer, old pan &mdash; and went back over a new waterproofing assembly. The tile is the visible half of a shower; the assembly behind it is the half that decides whether the framing stays dry.</p>

<h2>Custom cabinetry across three rooms</h2>

<p>White oak in the kitchen and custom vanities in both bathrooms, specified together.</p>

<p>That is one of the practical advantages of doing rooms at the same time. The same shop drawings, the same finish and one delivery cover all three rooms, and they end up relating to each other rather than looking separately specified years apart.</p>

<h2>Running it as one project</h2>

<p>One demolition phase, one plumbing rough, one electrical rough, one inspection cycle, one tile crew moving between the two bathrooms.</p>

<p>Seven weeks in the kitchen and four across the bathrooms, sequenced so the crew always had work: while the kitchen waited on cabinetry lead time or an inspection, the bathrooms progressed, and vice versa. Those waiting stages are unavoidable individually and largely absorbable when there is more than one room in play.</p>

<h2>The result</h2>

<p>Three rooms in one Carmel Valley house that were designed together and built together, with a wine cellar that had to be planned before a single cabinet was ordered.</p>
"""},

{
 "kind": "fullhome",
 "page": "home-renovation-carlsbad-brava-street.html",
 "project": "Brava Street",
 "city": "Carlsbad", "city_page": "carlsbad.html",
 "prefix": "brava", "photos": range(1, 14),
 "anchor": "full-home-renovations.html#fullhome-brava-street",
 "related": [("The kitchen in detail", "kitchen-remodel-carlsbad-brava-street.html"),
             ("The bathrooms in detail", "bathroom-remodel-carlsbad-brava-street.html")],
 "blurb": ("A whole-home renovation in Carlsbad: a full kitchen gut with a curved island, a bar area "
           "built out, quartzite carried onto the structural posts, and three bathrooms rebuilt."),
 "hero_sub": ("Brava Street &mdash; a kitchen gutted around a curved custom island, a bar area built "
              "out, quartzite clad onto the posts, and three bathrooms rebuilt."),
 "specs": [("Location","Carlsbad, San Diego County"),
           ("Scope","Kitchen, bar area and three bathrooms"),
           ("Kitchen","8 weeks &mdash; full gut, all appliances relocated"),
           ("Bathrooms","6 weeks &mdash; master, shower-to-tub, shower-to-shower"),
           ("Cabinetry","Custom island and bar, semi-custom white perimeter, custom vanities"),
           ("Counters","Quartzite, curved island"),
           ("Stone","Quartzite backsplash and stone-clad structural posts"),
           ("Flooring","New luxury vinyl plank")],
 "body": """
<p>A Carlsbad house where the kitchen, a new bar area and three bathrooms were all rebuilt as one project.</p>

<h2>The kitchen and the bar</h2>

<p>A full gut with every appliance relocated, and a bar area built out alongside it.</p>

<p>The cabinetry splits deliberately: custom for the island and the bar, semi-custom white for the perimeter. The perimeter runs divided sensibly into standard widths, so semi-custom did the job there. The island could not be anything but custom, because it is curved &mdash; and a curve has to be templated, fabricated and built to a radius that no catalogue carries. The bar had to be built to a space that did not previously exist as one.</p>

<p>Building the bar at the same time as the kitchen is what makes them read as one room. Added later, a bar is always something appended to a finished kitchen.</p>

<h2>Stone on the posts</h2>

<p>The structural posts are clad in the same quartzite as the counters and the backsplash. This is the detail that ties the house together and the one most likely to be skipped.</p>

<p>Posts are usually treated as a nuisance &mdash; necessary structure standing in an open plan, boxed in drywall and painted to be ignored. Wrapping them in the counter stone turns them from an obstacle into part of the design, and the space stops reading as a kitchen with columns in it.</p>

<p>It is fussy work. Stone on a vertical surface has to be supported, and the joints have to align with the horizontal runs nearby or the eye catches it immediately.</p>

<h2>The three bathrooms</h2>

<p>A master with a freestanding tub, a separate tiled shower, a custom vanity and a lighted mirror. A second bathroom converted from a shower back to a tub, finished in a custom wavy textured tile. A third rebuilt in place.</p>

<p>The shower-to-tub conversion is the unusual one and it is worth explaining. Nearly every conversion runs the other direction. Going back to a tub is what you do in a house where every other bathroom has become a walk-in shower and there is nowhere left to bathe a small child &mdash; something buyers with young families notice immediately.</p>

<p>The wavy tile in that room is considerably harder to set than flat tile. Every piece has relief, so the setting bed has to be consistent or the surface reads uneven &mdash; and a textured wall shows that instantly, because the light travelling across it is exactly what you are meant to be looking at.</p>

<h2>Running it as one project</h2>

<p>Eight weeks in the kitchen, six across three bathrooms, sequenced as a single job rather than four.</p>

<p>One demolition phase, one plumbing rough covering the kitchen's relocated appliances and three bathrooms, one electrical rough, one inspection cycle, one tile crew moving room to room, one flooring installation.</p>

<p>It is more disruptive in the moment &mdash; the house is a job site rather than one room &mdash; but it is a considerably shorter total disruption than four projects run one after another, and the quartzite ends up on the kitchen counters, the backsplash, the posts and the bar because it was all specified at once.</p>

<h2>The result</h2>

<p>A Carlsbad house tied together by one stone and one set of decisions, with a curved island and a bar built as part of the same room.</p>
"""},

{
 "kind": "fullhome",
 "page": "home-renovation-pacific-beach-dixie-drive.html",
 "project": "Dixie Drive",
 "city": "Pacific Beach", "city_page": "san-diego.html",
 "prefix": "dixie", "photos": range(1, 21),
 "anchor": "full-home-renovations.html#fullhome-dixie-drive",
 "related": [("The kitchen in detail", "kitchen-remodel-pacific-beach-dixie-drive.html"),
             ("The bathrooms in detail", "bathroom-remodel-pacific-beach-dixie-drive.html")],
 "blurb": ("A whole-home renovation in Pacific Beach: a two-tone custom kitchen with quartzite counters "
           "and backsplash, four bathrooms on a coastal theme, new windows and new LVP throughout."),
 "hero_sub": ("Dixie Drive &mdash; a two-tone custom kitchen, four bathrooms on one coastal theme, new "
              "windows throughout and new flooring across the house."),
 "specs": [("Location","Pacific Beach, San Diego"),
           ("Scope","Kitchen, four bathrooms, windows and flooring"),
           ("Kitchen","7 weeks &mdash; full gut, all appliances relocated"),
           ("Bathrooms","8 weeks &mdash; four, including a master"),
           ("Cabinetry","Custom blue base with custom white uppers; one custom vanity"),
           ("Counters","Quartzite, carried up as the backsplash"),
           ("Windows","New throughout"),
           ("Flooring","New luxury vinyl plank")],
 "body": """
<p>The largest of these projects: a kitchen, four bathrooms, new windows and new flooring in one Pacific Beach house.</p>

<h2>The kitchen</h2>

<p>A full gut with every appliance relocated, built in two-tone custom cabinetry &mdash; blue below, white above &mdash; with quartzite carried from the counters straight up the wall as the backsplash.</p>

<p>Two-tone is not only a colour decision. Darker cabinets below and lighter above give the room a base and let the top half recede, so the space reads taller and less closed in. That is a useful move in beach houses, where kitchens tend to be smaller and ceilings lower than in newer inland construction.</p>

<p>Carrying one stone across the counters and the backsplash removes the horizontal seam where a counter usually stops and tile begins, so the surface reads as continuous.</p>

<h2>Four bathrooms on one theme</h2>

<p>A master with both a shower and a freestanding tub, plus three more, all carried on a single coastal direction.</p>

<p>Bathrooms in the same house are usually remodelled years apart, and it shows &mdash; each reflects whatever was current when it was done, and the house reads as a sequence of decisions rather than one. Doing four at once removes that.</p>

<p>Three took prefabricated vanities and one is custom. That split is what keeps a four-bathroom project sensible: prefabricated is entirely adequate where the wall is a standard length and the plumbing arrives where expected, which describes most secondary bathrooms. Custom earns its place where the room is awkward or where the vanity is the thing you look at walking in.</p>

<h2>Windows and flooring</h2>

<p>New windows throughout the house and new luxury vinyl plank across it.</p>

<p>Doing the windows during the renovation rather than after is considerably less disruptive, because the walls are already open and the finishes are not yet in. Coastal houses give a specific reason to bother: salt air works on frames, and older single-pane units are usually the weakest point in the whole envelope.</p>

<p>LVP is fully waterproof, which is worth having a few blocks from the sand, and forgiving of the sand itself. Laid across the house in one installation, it also removes the transition strips that appear when rooms are floored years apart.</p>

<h2>Running it as one project</h2>

<p>Seven weeks in the kitchen and eight across four bathrooms, sequenced as one job.</p>

<p>One demolition phase, one plumbing rough covering a relocated kitchen and four bathrooms, one electrical rough, one window installation, one inspection cycle, one tile crew moving room to room, and one flooring installation at the end once the wet trades were finished and out.</p>

<p>That last constraint drives the order of everything else. Flooring across a whole house cannot go down until the work that would damage it is complete, so the schedule is built backwards from it.</p>

<h2>The result</h2>

<p>A Pacific Beach house where the kitchen, four bathrooms, the windows and the floor were all decided together, and finished as one coastal house rather than five separate projects.</p>
"""},

{
 "kind": "fullhome",
 "page": "home-renovation-rancho-santa-fe-dalia-drive.html",
 "project": "Dalia Drive",
 "city": "Rancho Santa Fe", "city_page": "rancho-santa-fe.html",
 "prefix": "dalia", "photos": range(1, 22),
 "anchor": "full-home-renovations.html#fullhome-dalia-drive",
 "related": [("The kitchen in detail", "kitchen-remodel-rancho-santa-fe-dalia-drive.html"),
             ("The bathrooms in detail", "bathroom-remodel-rancho-santa-fe-dalia-drive.html")],
 "blurb": ("A whole-home renovation in Rancho Santa Fe: a custom white kitchen with an integrated "
           "panel-front refrigerator, and four bathrooms including a fully relocated master and a "
           "panelled powder room."),
 "hero_sub": ("Dalia Drive &mdash; a custom white kitchen with a panel-front integrated refrigerator, "
              "and four bathrooms including a master rebuilt from the layout up."),
 "specs": [("Location","Rancho Santa Fe, San Diego County"),
           ("Scope","Kitchen and four bathrooms"),
           ("Kitchen","8 weeks &mdash; full gut, all appliances relocated"),
           ("Bathrooms","6 weeks &mdash; master, two guest, powder room"),
           ("Cabinetry","Custom white throughout, built-in hood, custom vanities"),
           ("Refrigerator","Panel-front, integrated into the cabinetry"),
           ("Counters","Quartz in the kitchen, quartzite in the master bathroom"),
           ("Flooring","Engineered hardwood, tile in the bathrooms")],
 "body": """
<p>A Rancho Santa Fe house where the kitchen and all four bathrooms were rebuilt as one project, in custom cabinetry throughout.</p>

<h2>The kitchen</h2>

<p>A full gut with every appliance relocated, built in custom white cabinetry with a built-in hood and a refrigerator you cannot pick out of the run.</p>

<p>The refrigerator is fronted in the same panels as the cabinets around it, so from across the room it reads as tall cabinetry rather than as an appliance. That is a construction decision rather than a finish one: a panel-ready refrigerator has to be specified before the cabinets are built, because the surrounding boxes are made to its exact dimensions and the panels are made to match the doors beside them. There is no retrofitting it.</p>

<p>The hood is treated the same way &mdash; built in and clad to match, with venting routed before anything closed up.</p>

<p>What both buy is quiet. A stainless refrigerator is a large reflective rectangle that pulls the eye every time you walk in; panelling it lets the room be about the room.</p>

<h2>The master bathroom</h2>

<p>The shower, the tub and the vanity all moved. That is what separates the master from the other three bathrooms in the house.</p>

<p>Relocating fixtures means reworking the waste lines under the floor and the supply inside the walls before anything is built back. It is the most disruptive way to remodel a bathroom and the only way to fix a layout that was wrong to begin with &mdash; and older master bathrooms were frequently laid out around where the plumbing already ran rather than around how the room would be used.</p>

<p>It has a freestanding tub, a large custom shower, and a quartzite counter with a farmhouse sink set into it. A farmhouse sink in a bathroom is unusual &mdash; it is a kitchen fixture by convention &mdash; and it works because the apron front breaks up what would otherwise be an uninterrupted run of cabinetry.</p>

<h2>The guest baths and the powder room</h2>

<p>One guest bath was a shower-to-shower remodel, the other a tub-to-tub: fixtures stayed, everything around them was rebuilt over new waterproofing, with custom vanities in both.</p>

<p>The powder room is the smallest room in the house and the one with the most character. Its walls are finished in custom panelling, and the vanity is a slab of quartz mounted directly to the wall with no legs and no cabinet beneath it.</p>

<p>That is a structural detail. The blocking has to go into the wall framing before the drywall closes, sized and positioned for the exact height and depth of the stone &mdash; it cannot be added to a finished wall or adjusted afterwards. What it buys is floor: in a room measured in a few square feet, seeing all of it continue under the vanity is the difference between tight and deliberate.</p>

<h2>Running it as one project</h2>

<p>Eight weeks in the kitchen and six across four bathrooms, and the bathrooms ran two at a time rather than all at once &mdash; two under construction while the other two stayed in service, then switched.</p>

<p>That matters more than it sounds. A house with four bathrooms that suddenly has none is a house nobody can live in. Running in pairs meant the family stayed put for the whole project with a working bathroom at every point, and it cost nothing in schedule, because the constraint is the sequence inside each room rather than how many rooms are open. While one pair waited on an inspection or a membrane curing, the crew worked in the other.</p>

<p>The same logic covers the kitchen. Its cabinetry lead times and inspections created gaps that the bathrooms were built into.</p>

<h2>The result</h2>

<p>Five rooms in one Rancho Santa Fe house, all in custom cabinetry, built as a single project the family was able to live through.</p>
"""},
{
 "kind": "fullhome",
 "page": "home-renovation-san-diego-donahue-drive.html",
 "project": "Donahue Drive",
 "city": "San Diego", "city_page": "san-diego.html",
 "prefix": "donahue", "photos": range(1, 16),
 "anchor": "full-home-renovations.html#fullhome-donahue-drive",
 "related": [("The kitchen in detail", "kitchen-remodel-san-diego-donahue-drive.html"),
             ("The bathrooms in detail", "bathroom-remodel-san-diego-donahue-drive.html")],
 "blurb": ("A whole-home renovation in San Diego: 1,500 sq ft rebuilt in eight weeks with a new kitchen, "
           "two full bathrooms, a quartz fireplace, new windows and french doors, and new flooring, paint, "
           "doors and lighting throughout."),
 "hero_sub": ("Donahue Drive &mdash; 1,500 sq ft rebuilt in eight weeks: a new kitchen, two bathrooms, a "
              "quartz fireplace, new windows and french doors, and new flooring throughout."),
 "specs": [("Location","San Diego"),
           ("Home","1,500 sq ft"),
           ("Timeline","8 weeks"),
           ("Scope","Kitchen, two bathrooms, fireplace and whole-house finishes"),
           ("Kitchen","White shaker, quartz counters, farmhouse apron sink"),
           ("Bathrooms","Two full remodels"),
           ("Fireplace","Quartz slab surround and mantel"),
           ("Windows and doors","New windows and new french doors"),
           ("Flooring","Luxury vinyl plank throughout"),
           ("Throughout","New paint, interior doors, hardware and lighting")],
 "body": """
<p>Fifteen hundred square feet, eight weeks, and everything inside it replaced. A kitchen, two bathrooms, the fireplace, the windows, the doors, the floor, the paint, the hardware and the lighting.</p>

<h2>One stone through three rooms</h2>

<p>The same quartz appears on the kitchen counters, on both bathroom vanities and clad across the fireplace surround and its mantel.</p>

<p>That is the decision that ties this house together, and it is only available when the rooms are done at once. Stone is bought as slabs from a particular block, and slabs from the same block share their veining. Order the kitchen this year and the fireplace in three years and you are choosing from whatever is on the floor at the time, in a pattern that will be close but not the same. Side by side, close but not the same is worse than deliberately different.</p>

<p>Running it onto the fireplace is the part most people skip. A fireplace surround is usually treated as its own thing, in its own material, chosen to suit the living room alone. Clad in the counter stone, it stops being a separate feature and becomes the point where the living room and the kitchen are visibly the same house.</p>

<h2>Why eight weeks was possible</h2>

<p>Eight weeks is quick for a whole house, and the reason is the scope. This renovation replaced everything you see and touch without moving the structure behind it. No walls came down, the kitchen kept its footprint, and the fixtures went back where the plumbing already served them.</p>

<p>That removes the two things that stretch a schedule most: structural work, which brings engineering and its own inspections, and relocated plumbing, which means opening the slab and waiting on rough inspections before anything can close.</p>

<p>What is left is a very large amount of finishing work, and finishing work is compressible in a way that structural work is not. It can run in parallel across rooms, and it is what a crew can be scaled up on.</p>

<h2>Running the trades once</h2>

<p>One demolition phase. One electrical rough covering the kitchen, both bathrooms, the recessed lighting through the living space and the fixtures in every bedroom. One tile crew moving between the two showers. One painter, once, through an empty house. One flooring installation across all 1,500 square feet at the end.</p>

<p>Done room by room across several years, every one of those repeats, and the house becomes a job site each time. The flooring in particular can never be recovered: laid in stages, it meets at every doorway in a threshold strip, and by the time the last room is done the first room's plank has been discontinued.</p>

<p>The floor going in last is also what dictates the order of everything before it. Luxury vinyl plank across the whole house cannot be laid until the wet trades are finished and out, so the schedule is built backwards from that point.</p>

<h2>Windows and french doors</h2>

<p>New windows throughout, and new french doors off both the dining room and the main bedroom.</p>

<p>Doing windows during the renovation rather than after is considerably less disruptive, because the interior finishes are not yet in and the patching that follows a window swap is absorbed by work already scheduled. Afterwards, the same job means protecting a finished room and repainting it.</p>

<p>The french doors are doing something a window cannot. Both rooms open onto the outside space, and in a house of this size the usable area is not only what is under the roof. A pair of glazed doors turns the patio into part of the room in a way a slider never quite does, because the whole opening clears rather than half of it.</p>

<h2>The things nobody photographs</h2>

<p>New interior doors and new hardware on all of them. New lighting throughout. Fresh paint on every surface in the house.</p>

<p>These are the items that get cut when a budget tightens, and they are the reason a renovated house either reads as finished or reads as a new kitchen in an old house. Original hollow doors with mismatched handles, left in place around new work, undo a good deal of what the new work bought.</p>

<p>Replacing them all at once is also the only practical time to do it. Doors and hardware are cheap individually and tedious to do piecemeal, and paint is quick in an empty house and slow in a furnished one.</p>

<h2>The result</h2>

<p>A San Diego house where the kitchen, both bathrooms, the fireplace and every surface between them were decided together and built as one job, in eight weeks rather than across several years.</p>
"""},
]
