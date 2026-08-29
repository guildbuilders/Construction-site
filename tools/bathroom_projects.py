#!/usr/bin/env python3
"""Bathroom project pages. Same shape as the kitchen entries in
build_projects.PROJECTS, with kind="bathroom".
"""

BATHROOMS = [
{
 "kind": "bathroom",
 "page": "bathroom-remodel-encinitas-camino-de-orchidia.html",
 "project": "Camino de Orchidia",
 "city": "Encinitas", "city_page": "encinitas.html",
 "prefix": "camino", "photos": [1, 2, 3, 4],
 # Portrait shot, rain head about 13% down. Crop from near the top or the
 # 380px hero lands mid-wall and loses it entirely.
 "hero_pos": "center 10%",
 "anchor": "bathrooms.html#bathroom-camino-de-orchidia",
 "blurb": ("An Encinitas bathroom rebuilt in place with quartzite slab shower walls, a ceiling-mounted "
           "rain head, a custom vanity and new tile flooring."),
 "hero_sub": ("Camino de Orchidia &mdash; quartzite slab in the shower, a ceiling-mounted rain head, "
              "a custom vanity and new tile flooring."),
 "specs": [("Location","Encinitas, San Diego County"),
           ("Timeline","4 weeks"),
           ("Scope","Shower-to-shower remodel, fixtures in place"),
           ("Shower","Quartzite slab walls, sealed; ceiling rain head"),
           ("Vanity","Custom"),
           ("Flooring","Tile")],
 "body": """
<p>A shower-to-shower remodel in Encinitas &mdash; the shower stayed where it was, and everything in it came out and went back better.</p>

<h2>What a shower-to-shower remodel actually involves</h2>

<p>It sounds like the easy version, and in scheduling terms it is: the plumbing stays put, so no drain moves and no walls are opened beyond the wet area. What it is not is cosmetic.</p>

<p>The old shower comes out to the studs. Tile, backer board, pan, everything. What goes back in is a new waterproofing assembly &mdash; and that is the whole job. The stone on the wall is what you see; the membrane behind it is what determines whether this bathroom is still sound in fifteen years.</p>

<p>Most failed showers do not fail at the tile. They fail at the pan, at the curb, or at the corners where two planes meet, and by the time it shows on the ceiling below, the framing has been wet for a long time.</p>

<h2>Quartzite in the shower</h2>

<p>The shower walls here are quartzite slab rather than tile, sealed for use in a wet area.</p>

<p>Slab instead of tile changes the room considerably. A tiled wall has grout lines every few inches; a slab wall has two or three seams in the entire shower. The stone's own veining becomes the pattern, and there is far less to clean.</p>

<p>Natural stone in a shower does need to be sealed, and resealed periodically &mdash; quartzite is dense but it is not glass. That is the trade for the look, and homeowners should know it going in rather than discovering it later.</p>

<h2>The rain head</h2>

<p>The rain head is mounted in the ceiling, not on an arm off the wall.</p>

<p>That is a framing decision, not a fixture decision. The supply has to be run through the ceiling joists and the valve set before anything closes up, so it has to be planned before the walls go back. There is no adding a ceiling-mounted head to a finished shower without opening the ceiling.</p>

<h2>Custom vanity</h2>

<p>Built for the room rather than bought to fit it. Bathrooms are where stock cabinetry runs out of usefulness fastest &mdash; the wall lengths are odd, the plumbing comes up in a fixed spot, and a stock vanity that is two inches narrow leaves a gap that never stops looking like a gap.</p>

<h2>The result</h2>

<p>A bathroom that reads as a full rebuild despite nothing moving, finished in four weeks.</p>
"""},

{
 "kind": "bathroom",
 "page": "bathroom-remodel-carmel-valley-lupita-court.html",
 "project": "Lupita Court",
 "city": "Carmel Valley", "city_page": "carmel-valley.html",
 "prefix": "lupita", "photos": [1, 2, 3, 4],
 # Photo 1 is a near-blank wall. Photo 2 is the floor-to-ceiling tile the page
 # is about, and the rain head sits at its top edge - so crop from the top.
 "hero_photo": 2, "hero_pos": "center top",
 "anchor": "bathrooms.html#bathroom-lupita-court",
 "blurb": ("A Carmel Valley bathroom tiled floor to ceiling on every wall, with a prefabricated vanity "
           "and the shower rebuilt in place."),
 "hero_sub": ("Lupita Court &mdash; tile carried floor to ceiling on every wall, with the shower rebuilt "
              "in place."),
 "specs": [("Location","Carmel Valley, San Diego County"),
           ("Timeline","4 weeks"),
           ("Scope","Shower-to-shower remodel, fixtures in place"),
           ("Walls","Tile, floor to ceiling throughout"),
           ("Vanity","Prefabricated"),
           ("Flooring","Tile")],
 "body": """
<p>Every wall in this Carmel Valley bathroom is tiled from the floor to the ceiling &mdash; not just the shower, and not just to a wainscot line.</p>

<h2>Tiling the whole room, floor to ceiling</h2>

<p>Most bathrooms tile the wet area and paint the rest. Carrying tile across all four walls to the ceiling is a different decision and it changes the room in two specific ways.</p>

<p>First, it removes every horizontal break. A tile wall that stops partway up draws a line across the room at that height, and the eye reads the space as shorter than it is. Running to the ceiling gives the eye nothing to stop at.</p>

<p>Second, it removes paint from a room that is repeatedly steamed. Bathroom paint is the finish that ages worst &mdash; it marks near the shower, it picks up moisture at the ceiling line, and it wants redoing long before anything else in the room does.</p>

<h2>Why it takes more planning</h2>

<p>Full-height tile is unforgiving of layout mistakes. On a partly tiled wall, an awkward cut can be hidden low or behind a fixture. Running the full height means every wall has to be set out in advance so the courses land sensibly at the ceiling and the corners align where two walls meet.</p>

<p>Outlets, switches, the mirror and the vanity all have to be located against that layout before the first tile is set, because every one of them is a cut in the field.</p>

<h2>A prefabricated vanity, deliberately</h2>

<p>The vanity here is prefabricated rather than built. In a room where the tile is doing all of the work, a stock vanity that fits the opening properly is the right call &mdash; the walls are the feature, and the vanity's job is to sit quietly against them.</p>

<p>Custom cabinetry earns its place where the room is awkward or where the cabinetry is the focal point. Neither applied here, and pretending otherwise would have added time to a project that did not need it.</p>

<h2>The shower</h2>

<p>Rebuilt in place. Out to the studs, new waterproofing, new pan, and tile carried up to meet the rest of the room so the shower does not read as a separate box inside the bathroom.</p>

<h2>The result</h2>

<p>A bathroom that reads as one continuous surface from floor to ceiling, finished in four weeks.</p>
"""},

{
 "kind": "bathroom",
 "page": "bathroom-remodel-san-diego-avalon-avenue.html",
 "project": "Avalon Avenue",
 "city": "San Diego", "city_page": "san-diego.html",
 "prefix": "avalon", "photos": [1, 2],
 "anchor": "bathrooms.html#bathroom-avalon-avenue",
 "blurb": ("A San Diego bathroom with a custom white oak vanity, a lighted mirror, tile shower walls "
           "and new tile flooring."),
 "hero_sub": ("Avalon Avenue &mdash; a custom white oak vanity, a lighted mirror, and the shower "
              "rebuilt in place with tile walls."),
 "specs": [("Location","San Diego"),
           ("Timeline","3 weeks"),
           ("Scope","Shower-to-shower remodel"),
           ("Layout","Fixtures in place"),
           ("Vanity","Custom white oak"),
           ("Mirror","Lighted"),
           ("Shower","Tile walls"),
           ("Flooring","Tile")],
 "body": """
<p>A three-week bathroom in San Diego, built around a custom white oak vanity and a shower rebuilt from the studs out.</p>

<h2>White oak in a bathroom</h2>

<p>The vanity is custom, in white oak. Wood in a bathroom is a fair question to ask about, and the answer is in how it is built and finished rather than in the species.</p>

<p>White oak is closed-grain and dimensionally stable, which is why it holds up in rooms that swing between dry and steamy several times a day. What matters as much is that the piece is finished on every face, including the underside and the back, so moisture cannot get in through the surfaces nobody sees.</p>

<p>Against a fully tiled room, wood does something tile cannot: it puts one warm, non-repeating surface in a space that is otherwise hard and uniform. In a small bathroom that single element is usually what keeps the room from reading clinical.</p>

<h2>The lighted mirror</h2>

<p>The mirror is lit from within rather than by a fixture above it.</p>

<p>This is an electrical decision made early. The box has to be located behind where the mirror will hang, at the right height, before the wall is closed and tiled. Get it wrong by a few inches and the options afterwards are a visible cord or opening a finished wall.</p>

<p>The reason to do it is light quality. A fixture mounted above a mirror lights the top of a face and leaves the underside in shadow &mdash; which is precisely wrong for the two things people do at a bathroom mirror. Light coming from the mirror's own perimeter arrives from the front and evenly.</p>

<h2>The shower</h2>

<p>Rebuilt in place, out to the studs. New waterproofing, new pan, new tile. Nothing moved, which is what kept this to three weeks &mdash; but nothing was left in place either.</p>

<h2>Tile flooring</h2>

<p>New tile throughout the room. Worth noting that bathroom floor tile should be chosen for slip resistance when wet, not only for how it looks dry &mdash; a large-format polished tile in a small bathroom is a decision people tend to regret in year one.</p>

<h2>The result</h2>

<p>A compact San Diego bathroom with one piece of real cabinetry in it, finished in three weeks.</p>
"""},

{
 "kind": "bathroom",
 "page": "bathroom-remodel-san-diego-sunset-ridge-drive.html",
 "project": "Sunset Ridge Drive",
 "city": "San Diego", "city_page": "san-diego.html",
 "prefix": "sunsetridge", "photos": [1, 2, 3, 4, 5, 6],
 "anchor": "bathrooms.html#bathroom-sunset-ridge-drive",
 "blurb": ("A San Diego master bathroom with a freestanding tub, a large custom tiled shower, a custom "
           "cabinet vanity and new tile flooring."),
 "hero_sub": ("Sunset Ridge Drive &mdash; a master bathroom with a freestanding tub, a large custom "
              "tiled shower and a custom cabinet vanity."),
 "specs": [("Location","San Diego"),
           ("Timeline","4 weeks"),
           ("Scope","Master bathroom"),
           ("Tub","Freestanding"),
           ("Shower","Large custom build"),
           ("Shower walls","Tile"),
           ("Vanity","Custom cabinetry"),
           ("Flooring","Tile")],
 "body": """
<p>A master bathroom in San Diego with the two things that separate a master from every other bathroom in a house: a freestanding tub and a shower built large enough to be its own room.</p>

<h2>The freestanding tub</h2>

<p>A freestanding tub sits away from the walls, which is the point of it &mdash; and also the reason it takes more planning than a tub in an alcove.</p>

<p>An alcove tub hides its plumbing inside the walls it touches. A freestanding tub does not touch any. The supply and the drain have to come up through the floor at exact points, located before the subfloor closes and the tile goes down. A filler in the wrong spot cannot be nudged over afterwards; the floor has to be opened.</p>

<p>Weight is the other consideration. A filled tub with someone in it is a concentrated load, and the framing beneath it has to be checked rather than assumed &mdash; particularly on a second floor.</p>

<p>What you get for the planning is a room where the tub reads as an object standing in the space instead of a fixture built into it, with floor visible all the way around.</p>

<h2>The large custom shower</h2>

<p>Built rather than bought, with tile walls. Size is the obvious difference, but the parts that matter are less visible: pan slope carried correctly across a larger area, a drain positioned so water goes to it from every corner, and waterproofing lapped properly at every change of plane.</p>

<p>A big shower is less forgiving than a small one. Over a short run, a slope error still drains. Over a long one, water finds the flat spot and stays there.</p>

<h2>Custom cabinet vanity</h2>

<p>Built for the wall it sits on. Master bathrooms are usually where stock cabinetry falls furthest short &mdash; the runs are longer, and a long run assembled from stock widths ends in filler panels at both ends.</p>

<h2>Tile flooring</h2>

<p>New tile throughout, run continuously so the tub, the shower and the vanity all sit on one surface. In a room with three distinct zones, a single floor is what keeps it reading as one room.</p>

<h2>The result</h2>

<p>A master bathroom with a genuine separation between the tub and the shower, finished in four weeks.</p>
"""},

{
 "kind": "bathroom",
 "page": "bathroom-remodel-san-diego-lark-street.html",
 "project": "Lark Street",
 "city": "San Diego", "city_page": "san-diego.html",
 "prefix": "lark", "photos": [1, 2],
 # Photo 1 is the vanity; the page is about the tiled shower.
 "hero_photo": 2, "hero_pos": "center 15%",
 "anchor": "bathrooms.html#bathroom-lark-street",
 "blurb": ("A San Diego bathroom rebuilt in place, tiled on every wall and across the floor, with a "
           "custom vanity."),
 "hero_sub": ("Lark Street &mdash; rebuilt in place with tile on every wall and across the floor, and "
              "a custom vanity."),
 "specs": [("Location","San Diego"),
           ("Timeline","3 weeks"),
           ("Scope","Shower-to-shower remodel, fixtures in place"),
           ("Walls","Tile throughout"),
           ("Vanity","Custom"),
           ("Flooring","Tile")],
 "body": """
<p>Three weeks, no fixtures moved, and every surface in the room replaced.</p>

<h2>All tile, walls and floor</h2>

<p>Tile on the walls and tile on the floor, so there is no painted surface in the room to maintain.</p>

<p>In a smaller bathroom this is the decision that does the most work. Paint near a shower is the finish that shows age first, and the wall it sits on is the one most likely to have taken moisture over the years. Replacing it with tile removes both the maintenance and the question of what is behind it.</p>

<p>Running tile across walls and floor also lets the room read as one volume rather than as a floor, a dado and a painted top half. Fewer material changes in a small room make it feel larger, not busier.</p>

<h2>Rebuilding the shower in place</h2>

<p>Nothing moved, which is what held this to three weeks. That does not mean the shower was refreshed &mdash; it came out to the studs.</p>

<p>The waterproofing assembly is the whole reason to do it that way. Retiling over an existing pan and existing backer board is faster and it is how a shower ends up failing quietly behind a wall that looks new. If the tile is coming off, the membrane behind it is coming off too.</p>

<h2>Custom vanity</h2>

<p>Built for the room. In a bathroom this size the vanity is a large share of the visible surface that is not tile, and a stock unit that misses the wall length by an inch or two is visible from the doorway for the life of the room.</p>

<p>Building it also means the storage is arranged around where the plumbing actually comes through the wall, rather than around where a manufacturer assumed it would.</p>

<h2>The result</h2>

<p>A compact San Diego bathroom rebuilt surface by surface without moving a single fixture, in three weeks.</p>
"""},

{
 "kind": "bathroom",
 "page": "bathroom-remodel-solana-beach-south-sierra-avenue.html",
 "project": "S. Sierra Avenue",
 "city": "Solana Beach", "city_page": "solana-beach.html",
 "prefix": "ssierra", "photos": [1, 2, 3],
 # Photo 1 looks through to a cluttered bedroom; photo 2 is the freestanding
 # tub, which is what this master bathroom is about.
 "hero_photo": 2,
 "anchor": "bathrooms.html#bathroom-s-sierra-avenue",
 "blurb": ("A Solana Beach master bathroom with a freestanding tub, tile floors and walls, built "
           "around the existing vanity."),
 "hero_sub": ("S. Sierra Avenue &mdash; a master bathroom with a freestanding tub and tile throughout, "
              "built around a vanity worth keeping."),
 "specs": [("Location","Solana Beach, San Diego County"),
           ("Timeline","3 weeks"),
           ("Scope","Master bathroom"),
           ("Tub","Freestanding"),
           ("Tile","Walls and flooring"),
           ("Vanity","Existing, retained")],
 "body": """
<p>A Solana Beach master bathroom where the vanity stayed and everything around it changed.</p>

<h2>Keeping the existing vanity</h2>

<p>Not every remodel needs to replace everything, and a contractor who tells you otherwise is not looking closely at what you already have.</p>

<p>The vanity here was sound, well built and suited the room. Replacing it would have added time and disruption to produce something no better. So it stayed, and the work went into the surfaces and the tub &mdash; which is where this room actually needed it.</p>

<p>Working around a fixture that is staying is its own discipline. It has to be protected through demolition, the new tile has to meet it cleanly at the floor and the wall, and the layout has to be set out from it rather than the other way round. It is easier to rip everything out. It is not always better.</p>

<h2>The freestanding tub</h2>

<p>The tub is freestanding, standing clear of the walls with floor running underneath it.</p>

<p>The plumbing for that has to come up through the floor at precise points, set before the subfloor closes and the tile is laid. There is no adjusting it later without opening the floor. The framing underneath also has to be verified for the load of a filled tub, which is not the same as the load of an empty one.</p>

<p>In a master bathroom it is the fixture that changes the feel of the room most, because it is the only one that occupies open floor rather than a wall.</p>

<h2>Tile floors and walls</h2>

<p>Tile on the floor and up the walls, replacing the surfaces that carry the moisture in a bathroom that gets daily use. Setting out around a retained vanity means the courses have to be planned from its position, so the cuts land where they are least visible.</p>

<h2>The result</h2>

<p>A master bathroom brought fully up to date in three weeks, with a good vanity still doing its job.</p>
"""},

{
 "kind": "bathroom",
 "page": "bathroom-remodel-carmel-valley-tynebourne-circle.html",
 "project": "Tynebourne Circle",
 "city": "Carmel Valley", "city_page": "carmel-valley.html",
 "prefix": "tynebourne", "photos": [1, 2, 3],
 "anchor": "bathrooms.html#bathroom-tynebourne-circle",
 "blurb": ("A Carmel Valley tub-to-shower conversion with tile walls, tile flooring and a custom "
           "cabinet vanity."),
 "hero_sub": ("Tynebourne Circle &mdash; a tub converted to a walk-in shower, with tile walls and a "
              "custom cabinet vanity."),
 "specs": [("Location","Carmel Valley, San Diego County"),
           ("Timeline","2 weeks"),
           ("Scope","Tub-to-shower conversion"),
           ("Shower","Tile walls"),
           ("Vanity","Custom cabinetry"),
           ("Flooring","Tile")],
 "body": """
<p>The tub came out and a walk-in shower went in. Two weeks, and the room works completely differently than it did.</p>

<h2>Converting a tub to a shower</h2>

<p>This is the most common change we are asked to make in a secondary bathroom, and it is more involved than swapping one fixture for another.</p>

<p>The drain is the first thing. A tub drains at one end; a shower drains from a point the floor slopes toward. So the drain has to be relocated, which means opening the floor and reworking the waste line beneath it &mdash; the part of the job that determines the schedule.</p>

<p>Then the alcove has to become a shower. Framing for a curb or a low threshold, a properly pre-sloped pan, waterproofing carried up the walls and lapped correctly at the corners, and the valve set at shower height rather than tub height.</p>

<p>What none of that involves is guessing. A tub-to-shower conversion done without moving the drain &mdash; using an offset or a sloped tray to fake it &mdash; is a shortcut you will hear about later, usually as a slow drain.</p>

<h2>Why homeowners make this change</h2>

<p>Because most people stop using the tub in a bathroom that has one of each, and a tub occupies the footprint of a considerably better shower.</p>

<p>The exception worth thinking about is whether the house retains a tub somewhere. Families with young children and buyers with them tend to want at least one. If this is the only tub in the house, that is a conversation to have before demolition, not after.</p>

<h2>Tile and the vanity</h2>

<p>Tile on the shower walls and across the floor, and a custom cabinet vanity built for the wall rather than bought to approximate it.</p>

<p>The vanity being custom matters more in a small room than a large one. There is less wall, so the proportion of it taken up by a not-quite-right stock unit is higher.</p>

<h2>The result</h2>

<p>A walk-in shower where a rarely used tub had been, finished in two weeks.</p>
"""},

{
 "kind": "bathroom",
 "page": "bathroom-remodel-pacific-beach-archer-street.html",
 "project": "Archer Street",
 "city": "Pacific Beach", "city_page": "san-diego.html",
 "prefix": "archer", "photos": [1, 2, 3, 4, 5],
 # Photo 1 is the vanity; photo 3 is the tub and the custom tile work.
 "hero_photo": 3, "hero_pos": "center 28%",
 "anchor": "bathrooms.html#bathroom-archer-street",
 "blurb": ("A Pacific Beach bathroom converted from a shower to a tub, with custom tile walls, custom "
           "cabinetry, a lighted mirror and tile flooring."),
 "hero_sub": ("Archer Street &mdash; a shower converted to a tub, with custom tile walls, custom "
              "cabinetry and a lighted mirror."),
 "specs": [("Location","Pacific Beach, San Diego"),
           ("Timeline","3 weeks"),
           ("Scope","Shower-to-tub conversion"),
           ("Tile","Custom tile work on the walls, tile flooring"),
           ("Cabinetry","Custom"),
           ("Mirror","Lighted")],
 "body": """
<p>This one ran the opposite direction to most: the shower came out and a tub went in.</p>

<h2>Converting a shower to a tub</h2>

<p>Nearly every bathroom we convert goes tub to shower. Going the other way is deliberate, and there are good reasons for it.</p>

<p>Usually it is a house that has no tub left in it. Once every bathroom has been converted to a walk-in shower, a family with small children has nowhere to bathe them, and a buyer with small children notices immediately. Putting one back in a secondary bathroom restores that without touching the master.</p>

<p>The work is not the reverse of a tub-to-shower conversion. The drain moves again &mdash; to the end of the alcove where a tub drains, not the centre point a shower slopes toward &mdash; so the floor is opened either way. The alcove has to be framed to the tub's exact dimensions, because a tub is a fixed object that will not tolerate being an inch off. The valve drops to tub height and a diverter goes in. And the framing has to carry a filled tub, which is a heavier load than the shower it replaced.</p>

<h2>Custom tile work</h2>

<p>The tile on the walls is custom-laid rather than a standard running bond straight off the box.</p>

<p>Custom tile work is where a good setter is worth finding. Pattern layout has to be set out so the room's centrelines land properly and the cuts fall at the edges rather than in the middle of a wall. Around a tub there are also more places for a pattern to break &mdash; the deck, the surround, the corners &mdash; and the eye catches a misalignment at eye level instantly.</p>

<h2>Custom cabinetry and a lighted mirror</h2>

<p>Cabinetry built for the room, and a mirror lit from its own perimeter rather than by a fixture overhead.</p>

<p>The mirror is an early decision, not a late one &mdash; the electrical box has to be positioned behind it before the wall is closed and tiled. It is also the better light for the two things people actually do at a bathroom mirror, because it arrives from the front rather than from above.</p>

<h2>The result</h2>

<p>A Pacific Beach bathroom with a tub back in the house, finished in three weeks.</p>
"""},

{
 "kind": "bathroom",
 "page": "bathroom-remodel-san-marcos-tara-way.html",
 "project": "Tara Way",
 "city": "San Marcos", "city_page": "san-marcos.html",
 "prefix": "tara", "photos": [1, 2, 3],
 # Photos 1 and 2 are the vanity; photo 3 is the walk-in shower the tub
 # was converted into.
 "hero_photo": 3,
 "anchor": "bathrooms.html#bathroom-tara-way",
 "blurb": ("A San Marcos tub-to-shower conversion with tile on every wall in the room, a custom vanity, "
           "and lighted mirrors set against tile."),
 "hero_sub": ("Tara Way &mdash; a tub converted to a full walk-in shower, with tile on every wall and "
              "lighted mirrors set against it."),
 "specs": [("Location","San Marcos, San Diego County"),
           ("Timeline","3 weeks"),
           ("Scope","Tub-to-shower conversion"),
           ("Tile","Every wall floor to ceiling, plus the flooring"),
           ("Vanity","Custom"),
           ("Mirrors","Lighted, mounted on tile")],
 "body": """
<p>The tub came out for a full walk-in shower, and the tile did not stop at the shower &mdash; it runs across every wall in the room.</p>

<h2>Tub to full walk-in shower</h2>

<p>Removing a tub is not the hard part. Making the space genuinely work as a shower is.</p>

<p>The drain has to move. A tub drains at one end; a shower drains from a point the floor slopes toward, so the waste line beneath the floor is reworked before anything else can proceed. Then the alcove becomes a wet area properly: pre-sloped pan, waterproofing lapped up the walls and through every corner, valve reset to shower height.</p>

<p>Done this way, the footprint the tub occupied becomes a shower you can actually move in. Done as a shortcut &mdash; a tray dropped in without relocating the drain &mdash; it becomes a shower that drains slowly and a floor that will be opened again later.</p>

<h2>Tile on every wall</h2>

<p>The tile runs across the whole room rather than only the wet area. That is the decision that makes this bathroom read as finished rather than renovated.</p>

<p>When tile stops at the shower, the shower reads as a tiled box installed inside a painted room. Carrying it across every wall removes that boundary; the shower becomes part of the room instead of an insert in it.</p>

<p>It also asks more of the layout. Every wall has to be set out in advance so courses align at the corners and around the door, and every outlet, switch and mirror has to be located before the first tile is set.</p>

<h2>Lighted mirrors against tile</h2>

<p>The mirrors are lit from within and mounted directly on the tile.</p>

<p>That combination has to be coordinated ahead of time. The electrical boxes have to be positioned before the wall closes, and the tile then has to be cut around them cleanly &mdash; on a tiled wall there is no adjusting the mirror's position afterwards to hide anything.</p>

<h2>Custom vanity</h2>

<p>Built for the room, so the storage works around the plumbing rather than around a manufacturer's assumption about it.</p>

<h2>The result</h2>

<p>A fully tiled San Marcos bathroom with a proper walk-in shower where the tub was, in three weeks.</p>
"""},

{
 "kind": "bathroom",
 "page": "bathroom-remodel-encinitas-willowhaven-road.html",
 "project": "Willowhaven Road",
 "city": "Encinitas", "city_page": "encinitas.html",
 "prefix": "willowhaven", "photos": [1, 2, 3],
 # Photo 1 puts the toilet in the foreground; photo 2 is the shower.
 "hero_photo": 2,
 "anchor": "bathrooms.html#bathroom-willowhaven-road",
 "blurb": ("An Encinitas tub-to-shower conversion with tiled shower walls, new tile flooring and a "
           "lighted mirror, finished in two weeks."),
 "hero_sub": ("Willowhaven Road &mdash; a tub converted to a shower, with tiled walls, new flooring "
              "and a lighted mirror."),
 "specs": [("Location","Encinitas, San Diego County"),
           ("Timeline","2 weeks"),
           ("Scope","Tub-to-shower conversion"),
           ("Shower","Tile walls"),
           ("Mirror","Lighted"),
           ("Flooring","Tile")],
 "body": """
<p>Two weeks to take out a tub and put in a shower &mdash; a short project, done properly.</p>

<h2>Why two weeks is realistic and one is not</h2>

<p>A tub-to-shower conversion has a floor in how fast it can go, and that floor is set by the drain and the waterproofing.</p>

<p>The drain has to be relocated, because a tub drains at one end and a shower drains from a point the floor slopes toward. That means opening the floor and reworking the waste line before anything can be built back.</p>

<p>Then the waterproofing has to go in and be given time. A pre-sloped pan, membrane carried up the walls, corners lapped, and the assembly left to cure before tile is set on it. That is not a stage that can be compressed by working later hours, and a contractor promising a finished shower in a few days is compressing exactly that stage.</p>

<p>Two weeks is what it takes to do the sequence in order. It is also short enough that a household with one other bathroom barely notices.</p>

<h2>Tiled shower walls</h2>

<p>New tile on the shower walls over new backer and new membrane. Everything behind the tile is new, which is the point of taking it back to the studs rather than tiling over what was there.</p>

<h2>The lighted mirror</h2>

<p>Lit from its own perimeter rather than from a fixture above. The electrical has to be located behind the mirror before the wall closes, so it is decided at the start of a two-week job rather than near the end of it.</p>

<p>The reason to bother is that light from above a mirror puts the underside of a face in shadow. Light from the mirror itself arrives from the front, which is what you want for shaving or applying anything.</p>

<h2>New tile flooring</h2>

<p>Replaced throughout, and run so the new shower sits on the same floor as the rest of the room rather than on a separate pad.</p>

<h2>The result</h2>

<p>A walk-in shower in place of a tub, with the room's finishes replaced around it, in two weeks.</p>
"""},

{
 "kind": "bathroom",
 "page": "bathroom-remodel-san-diego-honors-drive.html",
 "project": "Honors Drive",
 "city": "San Diego", "city_page": "san-diego.html",
 "prefix": "honors", "photos": [1, 2, 3, 4],
 "anchor": "bathrooms.html#bathroom-honors-drive",
 "blurb": ("A San Diego master bathroom with a freestanding tub, tiled shower walls, custom cabinet "
           "vanities and new tile flooring."),
 "hero_sub": ("Honors Drive &mdash; a master bathroom with a freestanding tub, a tiled shower and "
              "custom cabinet vanities."),
 "specs": [("Location","San Diego"),
           ("Timeline","2 weeks"),
           ("Scope","Master bathroom"),
           ("Tub","Freestanding"),
           ("Tile","Shower walls and flooring"),
           ("Vanities","Custom cabinetry")],
 "body": """
<p>A San Diego master bathroom with a freestanding tub, a separate tiled shower, and cabinetry built for the room rather than bought to fit it.</p>

<h2>Separating the tub and the shower</h2>

<p>A master bathroom is the one room in a house where a tub and a shower can stop sharing a space, and doing so changes both of them.</p>

<p>A tub-shower combination compromises each. The tub is shallow enough to stand in, the shower is bounded by the tub's width, and the whole thing needs a curtain or a screen. Separating them lets the shower be sized for a person standing and the tub be sized for a person lying down.</p>

<h2>The freestanding tub</h2>

<p>Standing clear of the walls, with floor running underneath and around it.</p>

<p>The planning that requires is worth stating plainly. Supply and drain come up through the floor at exact points, located and set before the subfloor closes and the tile goes down &mdash; there is no moving them afterwards without opening the finished floor. The framing beneath has to be checked for the load of a filled tub, which is substantially more than an empty one.</p>

<p>What it buys is that the tub reads as a piece of furniture in the room rather than as plumbing built into a wall.</p>

<h2>Custom cabinet vanities</h2>

<p>Vanities, plural, built for the walls they sit on.</p>

<p>Master bathrooms are where stock cabinetry falls furthest short, because the runs are longest. A long vanity assembled from stock widths ends with filler panels at one or both ends, and those fillers are the first thing a careful eye lands on. Built to the wall, the run goes end to end with nothing making up the difference.</p>

<h2>Tile shower walls and flooring</h2>

<p>Tile on the shower walls over new waterproofing, and new tile across the whole floor so the tub, the shower and the vanities all sit on one continuous surface.</p>

<p>In a room with three separate zones, a single unbroken floor is the thing that keeps it reading as one room rather than three areas that happen to adjoin.</p>

<h2>The result</h2>

<p>A master bathroom with a genuine separation between bathing and showering, and cabinetry that fits the walls exactly &mdash; finished in two weeks.</p>
"""},

{
 "kind": "bathroom",
 "page": "bathroom-remodel-rancho-santa-fe-dalia-drive.html",
 "project": "Dalia Drive",
 "city": "Rancho Santa Fe", "city_page": "rancho-santa-fe.html",
 "prefix": "dalia", "photos": [9, 10, 11, 12, 13, 14, 15, 16, 20],
 # Photo 9 is a guest bath; photo 15 is the master - freestanding tub and the
 # custom cabinetry - which is what the page leads with.
 "hero_photo": 15,
 "anchor": "bathrooms.html#bathroom-dalia-drive",
 "gallery_h2": "The Finished Bathrooms",
 "blurb": ("Four bathrooms in Rancho Santa Fe: a master with a relocated shower, tub and vanity, two "
           "guest baths, and a powder room with panelled walls and a wall-mounted quartz vanity."),
 "hero_sub": ("Dalia Drive &mdash; a master bathroom rebuilt with every fixture relocated, two guest "
              "baths, and a powder room with panelled walls and a floating quartz vanity."),
 "specs": [("Location","Rancho Santa Fe, San Diego County"),
           ("Timeline","6 weeks for all four"),
           ("Scope","Four bathrooms"),
           ("Rooms","Master, two guest, powder room"),
           ("Master","Shower, tub and vanity all relocated"),
           ("Master tub","Freestanding"),
           ("Master counter","Quartzite with a farmhouse sink"),
           ("Guest baths","Shower-to-shower and tub-to-tub, custom vanities"),
           ("Powder room","Custom wall panelling, wall-mounted quartz vanity"),
           ("Flooring","Tile")],
 "body": """
<p>Four bathrooms in one Rancho Santa Fe house, each doing a different job. The master was rebuilt from the layout up; the two guest baths were rebuilt in place; the powder room was treated as a small room that could afford to be unusual.</p>

<h2>The master: moving everything</h2>

<p>The shower, the tub and the vanity all moved. That is what separates this from the other three bathrooms in the house.</p>

<p>Relocating fixtures in a bathroom means reworking the waste lines under the floor and the supply inside the walls before anything is built back. It is the most disruptive way to remodel a bathroom and the only way to fix a layout that was wrong to begin with.</p>

<p>Older master bathrooms were frequently laid out around where the plumbing already ran rather than around how the room would be used &mdash; a shower tucked where it fits, a vanity on the wall with the existing supply, a tub filling whatever is left. Moving all three means starting from the room's proportions and its light instead.</p>

<h2>The freestanding tub and the huge shower</h2>

<p>The tub stands clear of the walls, with supply and drain coming up through the floor at points fixed before the tile went down. The framing beneath was verified for the load of a filled tub rather than assumed.</p>

<p>The shower is large and custom-built. Size is the visible part; the parts that matter are the pan slope carried correctly across a big area and a drain positioned so water reaches it from every corner. Large showers are less forgiving than small ones &mdash; over a short run a slope error still drains, over a long one water finds the flat spot and sits there.</p>

<h2>Quartzite and a farmhouse sink</h2>

<p>The master counter is quartzite, with a farmhouse sink set into it.</p>

<p>A farmhouse sink in a bathroom is unusual &mdash; it is a kitchen fixture by convention. It works here because the apron front breaks up what would otherwise be an uninterrupted run of cabinetry, and because it gives the master a piece of character that matches the scale of the room.</p>

<p>It is also a cabinetry decision more than a plumbing one. An apron-front sink is carried by the cabinet beneath it, so that cabinet has to be built for it from the start.</p>

<h2>The two guest bathrooms</h2>

<p>One was a shower-to-shower remodel, the other a tub-to-tub. Both mean the fixture stayed in place and everything around it was rebuilt: out to the studs, new waterproofing, new pan or new tub, new tile on the walls and floors, and custom vanities in both.</p>

<p>Keeping fixtures in place is the right call in a guest bathroom where the layout already works. The money and the disruption go into the assembly behind the tile, which is what actually determines how long the room lasts.</p>

<h2>The powder room</h2>

<p>The smallest room in the house and the one with the most character in it.</p>

<p>The walls are finished in custom panelling rather than tile or paint alone. A powder room has no shower and no tub, so it is free of the constraints that govern every other bathroom &mdash; which makes it the one place in a house where millwork on the walls is straightforward rather than a moisture problem.</p>

<p>The vanity is a slab of quartz mounted directly to the wall, with no legs and no cabinet under it. That is a structural detail: the blocking has to go into the wall framing before the drywall closes, sized and positioned for the exact height and depth of the stone. It cannot be added to a finished wall, and it cannot be adjusted afterwards.</p>

<p>What it buys is floor. In a room where the floor area is measured in a few square feet, seeing all of it continue under the vanity is the difference between tight and deliberate.</p>

<h2>Six weeks for four bathrooms, two at a time</h2>

<p>We did not open all four at once. We worked in pairs &mdash; two bathrooms under construction while the other two stayed in service, then switched.</p>

<p>That is the part homeowners care about most and it rarely gets discussed before demolition. A house with four bathrooms that suddenly has none is a house nobody can live in, and a contractor who guts everything on day one has made your schedule their convenience. Running in pairs means the family stayed in the house for the whole project with a working bathroom at every point.</p>

<p>It also does not cost time here, because the constraint is not how many rooms are open. It is the sequence inside each one: demolition, plumbing rough, inspection, waterproofing, cure, tile, finish. Several of those stages are waiting rather than working &mdash; an inspection has to be scheduled, a membrane has to cure &mdash; and while one pair of bathrooms sits in a waiting stage, the crew is working in the other pair.</p>

<p>That is what makes a full relayout in the master fit inside six weeks. The master alone would take most of six weeks on its own; the simpler bathrooms were built in the gaps its inspections and cure times created.</p>

<h2>The result</h2>

<p>Four bathrooms treated according to what each one needed &mdash; a full relayout in the master, careful rebuilds in the guest baths, and a powder room built as a small set piece. Six weeks for all of them.</p>
"""},

{
 "kind": "bathroom",
 "page": "bathroom-remodel-carmel-valley-arabian-crest-drive.html",
 "project": "Arabian Crest Drive",
 "city": "Carmel Valley", "city_page": "carmel-valley.html",
 "prefix": "arabiancrest", "photos": [5, 6, 7, 8],
 "anchor": "bathrooms.html#bathroom-arabian-crest-drive",
 "gallery_h2": "The Finished Bathrooms",
 "blurb": ("Two Carmel Valley bathrooms rebuilt in place with custom cabinets and tile walls &mdash; "
           "tile flooring in one, engineered hardwood in the other."),
 "hero_sub": ("Arabian Crest Drive &mdash; two bathrooms rebuilt in place with custom cabinets and tile "
              "walls, one floored in tile and one in engineered hardwood."),
 "specs": [("Location","Carmel Valley, San Diego County"),
           ("Timeline","4 weeks"),
           ("Scope","Two bathrooms, shower-to-shower in both"),
           ("Cabinetry","Custom in both"),
           ("Walls","Tile"),
           ("Flooring","Tile in one, engineered hardwood in the other")],
 "body": """
<p>Two bathrooms in the same Carmel Valley house, rebuilt at the same time, finished differently underfoot.</p>

<h2>Shower-to-shower in both</h2>

<p>Neither shower moved, which is what allowed two full bathrooms to be done in four weeks. It does not mean either was treated lightly.</p>

<p>Both came out to the studs. Old tile, old backer, old pan &mdash; all of it. What went back is a new waterproofing assembly with a pre-sloped pan and membrane lapped correctly through the corners and up the walls.</p>

<p>That is the entire argument for taking a working shower back to the framing. The tile is the visible half of a shower; the assembly behind it is the half that decides whether the framing stays dry. Retiling over what is already there is faster and leaves you with a new-looking shower built on an unknown.</p>

<h2>Different flooring in each</h2>

<p>One bathroom got tile. The other got engineered hardwood.</p>

<p>Hardwood in a bathroom is a fair thing to question, and engineered is the reason it works. An engineered plank is a hardwood wear layer over a cross-laminated core, and that core is what keeps it from moving with humidity the way a solid board does. In a bathroom that swings from dry to steamy several times a day, that stability is the whole difference.</p>

<p>It is also a continuity decision. When a bathroom opens off a bedroom or a hall already floored in hardwood, carrying the same floor through means the doorway stops being a threshold between two materials. Tiling it would have drawn a line at the door.</p>

<p>The other bathroom took tile, which is the more conventional answer and the right one where the room is used harder or opens off a tiled space.</p>

<h2>Custom cabinets in both</h2>

<p>Built for each room rather than ordered to approximate it. Doing two bathrooms at once makes custom cabinetry more sensible than it would be for one &mdash; the same shop drawings, the same finish, one delivery, two rooms that relate to each other rather than looking separately specified.</p>

<h2>Tile walls</h2>

<p>Tile on the walls in both, set out in advance so the courses land properly at the corners and the cuts fall where they are least visible.</p>

<h2>The result</h2>

<p>Two bathrooms rebuilt to the same standard in four weeks, each floored for the space it opens onto.</p>
"""},

{
 "kind": "bathroom",
 "page": "bathroom-remodel-carlsbad-brava-street.html",
 "project": "Brava Street",
 "city": "Carlsbad", "city_page": "carlsbad.html",
 "prefix": "brava", "photos": [8, 9, 10, 11, 12, 13],
 # Photo 8 is a vanity; photo 9 is the wavy textured tile, the one detail in
 # these three bathrooms that exists nowhere else on the site.
 "hero_photo": 9,
 "anchor": "bathrooms.html#bathroom-brava-street",
 "gallery_h2": "The Finished Bathrooms",
 "blurb": ("Three Carlsbad bathrooms: a master with a freestanding tub and custom vanity, a shower-to-tub "
           "conversion in wavy textured tile, and a shower rebuilt in place."),
 "hero_sub": ("Brava Street &mdash; three bathrooms, including a master with a freestanding tub and a "
              "shower-to-tub conversion finished in wavy textured tile."),
 "specs": [("Location","Carlsbad, San Diego County"),
           ("Timeline","6 weeks for all three"),
           ("Scope","Three bathrooms: master, shower-to-tub conversion, shower-to-shower"),
           ("Master","Freestanding tub, tiled shower, custom vanity, lighted mirror"),
           ("Second bath","Shower converted to a tub, custom wavy textured tile"),
           ("Third bath","Shower rebuilt in place, tile walls")],
 "body": """
<p>Three bathrooms in one Carlsbad house, each given a different treatment, six weeks for all of them.</p>

<h2>The master</h2>

<p>A freestanding tub, a separate tiled shower, a custom vanity and a lighted mirror.</p>

<p>The tub stands clear of the walls, which means the supply and drain come up through the floor at points fixed before the tile went down &mdash; not adjustable afterwards without opening the finished floor. The framing underneath was checked for the load of a filled tub rather than assumed to carry it.</p>

<p>Separating the tub from the shower is what makes a master bathroom feel like one. A combination unit compromises both: the tub is shallow enough to stand in and the shower is only as wide as the tub. Given their own space, each can be sized for what it is actually for.</p>

<p>The mirror is lit from its own perimeter, which is an early decision &mdash; the electrical box has to be located behind it before the wall closes and tiles.</p>

<h2>The second bathroom: shower to tub, in wavy tile</h2>

<p>The shower here came out and a tub went in. That is the less common direction, and it is usually the right call in a house where the other bathrooms are showers and there is nowhere left to bathe a small child.</p>

<p>The drain moves to the end of the alcove where a tub drains rather than the centre point a shower slopes toward, the alcove is framed to the tub's exact dimensions, and the valve drops to tub height with a diverter added.</p>

<p>What makes this room is the tile: a custom wavy, textured tile on the tub walls.</p>

<p>Dimensional tile is considerably harder to set than flat tile. Every piece has relief, so the setting bed has to be consistent or the surface reads uneven across a wall &mdash; and a wavy tile shows that immediately, because the light travelling across it is exactly what you are meant to be looking at.</p>

<p>It also has to be lit to work. A textured wall under flat overhead light is just a wall. Lit from an angle, the relief throws its own shadow and the surface moves.</p>

<h2>The third bathroom</h2>

<p>A shower-to-shower remodel with tile walls. The fixture stayed put; everything around it came out to the studs and went back over a new waterproofing assembly.</p>

<p>In a house where two other bathrooms are being rebuilt at the same time, this is the sensible treatment for the one whose layout already works. Nothing is gained by moving a shower that is in the right place.</p>

<h2>Doing three at once</h2>

<p>Six weeks total, which is faster than three separate projects because the trades overlap: one demolition phase, one plumbing rough, one tile crew moving room to room, one inspection cycle.</p>

<p>It is more disruptive in the moment &mdash; the whole house is a job site rather than one room &mdash; but it is a considerably shorter total disruption than three bathrooms done one after another.</p>

<h2>The result</h2>

<p>Three bathrooms with distinct characters, built as one project.</p>
"""},

{
 "kind": "bathroom",
 "page": "bathroom-remodel-pacific-beach-dixie-drive.html",
 "project": "Dixie Drive",
 "city": "Pacific Beach", "city_page": "san-diego.html",
 "prefix": "dixie", "photos": [11, 12, 13, 14, 15, 16, 18, 19, 20],
 "anchor": "bathrooms.html#bathroom-dixie-drive",
 "gallery_h2": "The Finished Bathrooms",
 "blurb": ("Four Pacific Beach bathrooms on a coastal theme, including a master with both a shower and "
           "a freestanding tub, tiled floors and shower walls throughout."),
 "hero_sub": ("Dixie Drive &mdash; four bathrooms carried on one coastal theme, including a master with "
              "both a shower and a freestanding tub."),
 "specs": [("Location","Pacific Beach, San Diego"),
           ("Timeline","8 weeks for all four"),
           ("Scope","Four bathrooms, including a master"),
           ("Master","Shower and freestanding tub"),
           ("Theme","Coastal, carried across all four"),
           ("Vanities","Prefabricated, with one custom"),
           ("Flooring","Tile"),
           ("Shower walls","Tile")],
 "body": """
<p>Four bathrooms in a Pacific Beach house, done as one project over eight weeks, tied together by a single coastal direction.</p>

<h2>Carrying one theme across four rooms</h2>

<p>Bathrooms in the same house are usually remodelled years apart, and it shows &mdash; each one reflects whatever was current when it was done, and the house reads as a sequence of decisions rather than a single one.</p>

<p>Doing four at once removes that. One material direction runs through all of them, so the master, the guest baths and the smallest room in the house all belong to the same building.</p>

<p>Coastal was the right direction here for the obvious reason: the house is a few blocks from the sand. A theme that answers where a house actually is tends to age considerably better than one imported from somewhere else.</p>

<h2>The master: shower and freestanding tub</h2>

<p>Both, in separate places.</p>

<p>The freestanding tub stands clear of the walls, so the supply and drain come up through the floor at exact points, set before the subfloor closed and the tile went down. The framing beneath was verified for the load of a filled tub.</p>

<p>Having both means neither compromises. A tub-shower combination gives you a shallow tub and a narrow shower; separating them lets the shower be sized for standing and the tub for lying down.</p>

<h2>Prefabricated vanities, and one custom</h2>

<p>Three of the four bathrooms have prefabricated vanities. One is custom.</p>

<p>That split is deliberate and it is how a four-bathroom project stays sensible. Prefabricated vanities are entirely adequate where the wall is a standard length and the plumbing comes up where it is expected &mdash; which describes most secondary bathrooms.</p>

<p>Custom earns its place where the room is awkward, where the run is long, or where the vanity is the thing you look at when you walk in. Specifying custom in all four would have added time to three rooms that did not need it.</p>

<h2>Tile floors and shower walls</h2>

<p>Tile on the floors and on the shower walls in every bathroom, over new waterproofing in each.</p>

<p>Coastal houses give a specific reason to be careful here. Sand comes in on feet, salt air comes in through the windows, and the humidity is higher year round than it is inland. A bathroom floor a few blocks from the beach works harder than the same floor in Escondido.</p>

<h2>Eight weeks for four bathrooms</h2>

<p>Sequenced as one project rather than four: one demolition phase, one plumbing rough, one tile crew moving room to room, one inspection cycle. Doing them separately would have meant four of everything and a house repeatedly returned to as a job site.</p>

<h2>The result</h2>

<p>Four bathrooms that read as one house, finished in eight weeks.</p>
"""},

{
 "kind": "bathroom",
 "page": "bathroom-remodel-carmel-valley-kingsfield-court.html",
 "project": "Kingsfield Court",
 "city": "Carmel Valley", "city_page": "carmel-valley.html",
 "prefix": "kingsfield", "photos": [7, 8, 9, 10, 11, 12, 13],
 "anchor": "bathrooms.html#bathroom-kingsfield-court",
 "gallery_h2": "The Finished Bathrooms",
 "blurb": ("Three Carmel Valley bathrooms in six weeks: a large master with a big tiled shower, a "
           "tub-to-tub rebuild, and a shower rebuilt in place &mdash; custom vanities in all three."),
 "hero_sub": ("Kingsfield Court &mdash; three bathrooms in six weeks, including a large master with a "
              "big tiled shower, with custom vanities throughout."),
 "specs": [("Location","Carmel Valley, San Diego County"),
           ("Timeline","6 weeks for all three"),
           ("Scope","Three bathrooms"),
           ("Rooms","Master, tub-to-tub, shower-to-shower"),
           ("Master","Large shower, custom cabinets, tile walls and floors"),
           ("Second bath","Tub-to-tub rebuild, tile walls and floors"),
           ("Third bath","Shower-to-shower rebuild, tile walls and floors"),
           ("Vanities","Custom in all three")],
 "body": """
<p>Three bathrooms in a Carmel Valley house, rebuilt as one six-week project, with custom vanities in every one.</p>

<h2>The master</h2>

<p>A large shower, custom cabinets, and tile on the walls and floors.</p>

<p>Building a big shower is not simply a matter of framing a bigger box. The pan has to be pre-sloped correctly across the whole area and the drain positioned so water reaches it from every corner. Large showers are less forgiving than small ones &mdash; over a short run a slope error still drains, over a long one water finds the flat spot and stays there.</p>

<p>The waterproofing has more to get right too. More wall area means more corners, more changes of plane, and more places for the membrane to be lapped properly or not.</p>

<h2>The second bathroom: tub to tub</h2>

<p>The tub stayed a tub &mdash; a new one, in the same place, with everything around it rebuilt.</p>

<p>Tub-to-tub is the right treatment when the layout already works and the household wants to keep a bath. It is faster than a conversion because the drain does not move, and it is not cosmetic: the tub comes out, the walls go back to the studs, new waterproofing goes in, and new tile goes on.</p>

<p>It is also worth keeping at least one tub in a house. Once every bathroom has become a walk-in shower, a family with small children has nowhere to bathe them &mdash; and buyers with small children notice.</p>

<h2>The third bathroom: shower to shower</h2>

<p>Rebuilt in place. Out to the studs, new pan, new membrane, new tile. Nothing moved, because nothing needed to.</p>

<p>Retiling over an existing pan would have been quicker and would have left a new-looking shower sitting on an assembly nobody had looked at. If the tile is coming off, what is behind it comes off too.</p>

<h2>Custom vanities in all three</h2>

<p>Every vanity in the project was built rather than bought.</p>

<p>Doing three bathrooms at once is what makes that practical. The same shop drawings, the same finish and one delivery cover all three, and the rooms end up relating to each other instead of looking separately specified years apart.</p>

<h2>Tile on walls and floors throughout</h2>

<p>All three bathrooms tiled on the walls and the floors, each over new waterproofing, and each set out in advance so the courses land properly at the corners.</p>

<h2>Six weeks for three bathrooms</h2>

<p>Sequenced as one project: one demolition phase, one plumbing rough, one tile crew moving room to room, one inspection cycle. Three separate projects would have meant three of each and the house returned to as a job site three times.</p>

<h2>The result</h2>

<p>Three bathrooms finished to the same standard, in six weeks.</p>
"""},
{
 "kind": "bathroom",
 "page": "bathroom-remodel-san-diego-donahue-drive.html",
 "project": "Donahue Drive",
 "city": "San Diego", "city_page": "san-diego.html",
 "prefix": "donahue", "photos": [10, 11, 12, 13, 14],
 "anchor": "bathrooms.html#bathroom-donahue-drive",
 "blurb": ("Two bathrooms rebuilt in a San Diego whole-home renovation: large-format porcelain showers "
           "with recessed niches and sliding glass, quartz-topped shaker vanities, and lit mirrors in both."),
 "hero_sub": ("Donahue Drive &mdash; two bathrooms rebuilt with large-format porcelain showers, recessed "
              "niches, quartz-topped vanities and lit mirrors."),
 "specs": [("Location","San Diego"),
           ("Timeline","Part of an 8 week whole-home renovation"),
           ("Scope","Two full bathroom remodels"),
           ("Showers","Large-format porcelain, recessed niches, sliding glass"),
           ("Vanities","White shaker; one single, one double"),
           ("Counters","Quartz"),
           ("Mirrors","Backlit LED in one, lighted bar in the other"),
           ("Flooring","Luxury vinyl plank")],
 "body": """
<p>Two bathrooms in the same house, rebuilt at the same time, in the same materials. That is the part worth noticing before any individual detail: they were specified together, so they belong to one house rather than to two different years.</p>

<h2>Large-format porcelain instead of tile</h2>

<p>Both showers are lined in large porcelain panels with a marble veining, rather than in conventional tile.</p>

<p>The difference is the grout. A standard tiled shower has grout lines every few inches, and grout is the part that stains, that needs sealing, and that eventually has to be raked out and replaced. Large-format panels reduce that to a handful of joints in the entire enclosure, so the wall reads as stone and there is very little left to clean.</p>

<p>The trade is in the handling. Panels this size are heavy and unforgiving of a wall that is not flat, so the substrate has to be brought true before anything is set. A small tile can absorb a slight bow in a wall across many joints; a large panel cannot, and any deviation shows as a shadow along the edge.</p>

<p>Underneath both, the waterproofing assembly is the actual job. The stone is what you see, and the membrane and the pre-sloped pan behind it are what decide whether the framing is still dry in fifteen years.</p>

<h2>The niches</h2>

<p>Each shower has a recessed niche set into the wall, lined in the same porcelain.</p>

<p>A niche is framing, not finishing. The opening has to be built into the stud bay before the walls close, positioned between studs, and waterproofed as part of the shower assembly rather than cut into it afterwards. It is a decision made at rough-in and it cannot be added later without opening the wall.</p>

<p>The alternative is a caddy hanging off the shower head, which is what people resort to when nobody planned for the bottles that a shower obviously has to hold.</p>

<h2>Sliding glass rather than a swinging door</h2>

<p>Both enclosures use glass panels on a top track that slide rather than swing.</p>

<p>In bathrooms of this size that is the difference between a door that opens and one that hits the toilet. A hinged shower door needs its whole arc kept clear on the outside, and in a compact room that arc is usually occupied. Sliding panels need none of it.</p>

<h2>Two vanities, sized to two rooms</h2>

<p>One bathroom takes a single vanity with an undermount basin; the other takes a double.</p>

<p>The double is in the bathroom with the wall length to carry it, and two basins in a shared bathroom removes the queue that a single one creates every morning. Putting a double into the smaller room would have meant two cramped basins and no counter between them, which is worse than one basin with somewhere to set things down.</p>

<p>Both are white shaker with quartz tops, matching the kitchen counters, and both have drawer banks rather than a pair of doors over an open cavity. Drawers are more work to build and considerably more useful: everything in them is reachable without kneeling on the floor.</p>

<h2>Lit mirrors</h2>

<p>One room has a mirror with the light built into the glass itself, the other a decorative bar mounted above.</p>

<p>Both had to be planned before the drywall went on. A backlit mirror needs power arriving inside the wall at the exact height and centre of the finished mirror, and blocking behind that point to hang the weight from. There is no adding it neatly to a finished wall.</p>

<p>Lighting from the front of a mirror, rather than from a fixture above and behind you, is also the reason these rooms are usable for anything requiring a close look. A ceiling light alone puts your own face in shadow.</p>

<h2>The result</h2>

<p>Two bathrooms that were treated as one decision, sharing the same stone, the same cabinetry and the same waterproofing standard, finished within the eight weeks the whole house took.</p>
"""},
]
