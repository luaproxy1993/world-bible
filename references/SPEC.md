# Core Rule Book spec

JSON in these folders is what you edit. `WORLD_BIBLE.md` and
`overview.html` are compiled. Do not hand-edit them.

```text
world/world.json
play/play.json
stage/stage.json
kit/kit.json
timeline/timeline.json
art/art.json
play-seeds.json
```

Every id you mention must exist. Prefix: `place.` `person.` `faction.`
`institution.` `signature.` `event.` `role.` `gear.` `opposition.` `job.`
`law.`

Counts: `lock.scale` table in `LOCK.md`. Default scale is **core** — a
core rule book, not one sitting.

---

## Brief (`vignette`)

One object on the stage: a place, a person, a faction, an institution,
the unique thing, a role, a piece of gear, or a kind of opposition.
Not a wiki card. Not a short story.

```json
{
  "id": "place.",
  "kind": "place",
  "title": "Name, job or use, when",
  "body": "core: 280–500 words. sitting: 220–400. seed: 150–250. Answer every slot below.",
  "residue": "what this still does to people in the playable present",
  "relations": ["person.", "signature."],
  "play_hook": "one scene a designer can run tomorrow, using only ids in this book"
}
```

**Slot test.** If a required slot is missing, the brief is not done.
**Swap test.** Replace the proper names with another genre. If the paragraph
still works, it is too generic. Rewrite.
**Hook test.** A designer can start a scene without inventing a new room or person.
**Voice test.** SKILL.md Voice. If you reread it, look up a word, or it reads
as a diary, rewrite.
**Id test.** Every name in `relations` exists in this book's JSON.

Entry face: exactly one `person.*` in `world.json` → `entry_face`.

### Place slots (every `places[]` item)

1. What this place is, in one sentence.
2. Who may enter, who may not, and which door they use.
3. Hours: when it is open, when it is empty.
4. A price, a ticket, a stamp, or a free rule. Use `play.economy` currency.
5. How the unique thing (`signature`) shows up in this room.
6. One dated incident (year or season) that proves a Law.
7. Which other ids you can walk to from here.
8. What a player can take, copy, or overhear here (one concrete thing).

### Person slots (every `people[]` item)

1. Name, age, job.
2. Where they stand on a normal day (a `place.*` id).
3. What they can give, sell, stamp, or refuse.
4. How the unique thing touches them (bag, body, pay, door).
5. One dated incident.
6. Who they deal with (ids, not adjectives).
7. What they want this season (a thing a player can give, steal, or block).
8. Leverage a player can use (debt, stamp, secret, or a relation id).

### Faction slots

1. What they do this year, not their myth.
2. Which streets or rooms they walk (`place.*`).
3. Who they can help or hurt, and with what permission.
4. What they control that a player can steal, stop, or buy.
5. One dated incident this window.
6. Who they oppose this year (`faction.*` or `opposition.*`).

### Institution slots

1. The public rule (sign, ticket, stamp, posted notice).
2. Who enforces it.
3. What happens if you break it this year.
4. One dated proof it still holds.
5. What it costs to buy, wait, or bribe (a number in `play.economy` currency).

---

## World (`world/world.json`)

A teammate reads this aloud in about eight minutes (core) or four (sitting)
and can run a scene.

| Field | Dig until |
|-------|-----------|
| `uniqueness` | core 400–700 words; sitting/seed 280–450. Era look, who has power, how the unique thing shows up on a street, what a visitor gets wrong on day one. |
| `laws[]` | core 5–9; sitting/seed 3–7. Each has `id` (`law.`) and `text`: if/then a local knows, **plus** what breaking it costs this year. 2–4 sentences. |
| `everyday` | `eat` `pay` `move` `sleep` `die` `news`. Each key: core 5–8 sentences; sitting 3–5. A price, a time, or a `place.*`. |
| `calendar` | `day` `week` `clock` `curfew`. Each key 2–5 sentences. The public clock people actually use (bell, shift, tide). Who must be indoors, when, what happens if not. |
| `travel` | `how` `times` `stop`. How a body moves between **named** places. At least four place-to-place times. What stops you (gate, stamp, weather, unique thing). |
| `signature` | A brief (same slots as above). Procedure: how you get it, how you use it, how it fails. |
| `slang[]` | Optional. About 12 terms. `term` in local speech, `meaning` in ordinary English. |

Out: creation myths with no mark on today, other continents, generic D20 math.

---

## Play (`play/play.json`)

How this core book lets you **be someone**, **pay**, and **take a risk**.
Tied to this world's unique thing. Not a pasted combat chapter from
another game. Later numbers skills read this page; they do not invent
a second economy.

```json
{
  "schema": "doki.world-bible.play",
  "version": "1.1.0",
  "roles": [],
  "power": {
    "street": "what a street-level risk does to a body or a plan",
    "hard": "what a mill, yard, or official room does",
    "rare": "what a hall, temple, or last-car fight does"
  },
  "conflict": {
    "check": "how you try something risky here (one procedure)",
    "fight": "how people hurt each other here, using the unique thing",
    "fail": "what failure costs this year"
  },
  "economy": {
    "currency": "what people pay with, in one sentence",
    "street_wage": "a day's pay for street work, with a number",
    "skilled_wage": "a day's pay for a skilled job, with a number",
    "bread": "what a meal costs",
    "room": "what a night's bed costs",
    "fine": "what an official fine costs this year"
  },
  "opposition": []
}
```

Role brief slots (every `roles[]` item, vignette shape, `kind: role`):

1. Who you are on this stage, in one sentence.
2. Where you stand (`place.*`).
3. What only this role can do here.
4. How the unique thing helps or blocks you.
5. One dated incident.
6. What you get paid, or what you owe (a number in `economy` currency).

`power` each rung: 3–6 sentences with a concrete example from this world.
`conflict` each key: 4–8 sentences. A GM can run a scuffle from this page
without opening another book.
`economy` each key: one or two sentences with a number. Gear prices in
`kit/` use the same currency.

Opposition brief slots (every `opposition[]` item, `kind: opposition`):

1. What it is (office, crew, beast, weather, machine).
2. Where it stands (`place.*`).
3. How it hurts, using the unique thing.
4. Which hardness rung it is (`street` / `hard` / `rare`).
5. One dated incident.
6. What it drops, demands, or leaves when it is stopped.

Do not invent hit points, classes, or netrunning unless this world has them.

---

## Stage (`stage/stage.json`)

Counts: `lock.scale` in `LOCK.md`. Every item is a brief with **all** slots filled.

A place names who uses it. A person names where they stand and what they
want this season. A faction names the streets it walks this year.

If the turn would truncate before counts are met, write JSON in batches
in this step. The step is not done until the counts match.

---

## Kit (`kit/kit.json`)

Gear a GM can hand a player tonight. The unique thing is here too if it
is an object. Not a shopping catalog from another game.

```json
{
  "schema": "doki.world-bible.kit",
  "version": "1.0.0",
  "gear": []
}
```

Each `gear[]` item is a brief (`kind: gear`). Slots:

1. What it is, in one sentence.
2. Who owns or sells it (`person.*` or `place.*`).
3. What it costs, or that it is free / stolen / stamped. Same currency as `play.economy`.
4. How the unique thing interacts with it (fails, lights, opens).
5. One dated use.
6. What a later numbers skill can treat as a bonus, a key, or a burden (one clause, no foreign math).

Counts: `lock.scale` in `LOCK.md`.

---

## Timeline (`timeline/timeline.json`)

`world_key` = older facts that still mark today. As many as leave a mark.
`story_window` = the stretch a game occupies. Beat **count** is `lock.scale`.
This is history that still marks today. It is not a campaign outline.

Each `story_window` beat body: **4–7 sentences**. Must name:

1. When.
2. Where (`place.*`).
3. Who is on stage (`person.*` or `faction.*`).
4. What changes.
5. What is left for the next beat (`residue`).

A table with no bodies is a date list. Rewrite.

---

## Art look (`art/art.json`)

Words only. Pictures are `/world-bible-pack`, a later session. See `ART.md`.

Fill:

| Field | Dig until |
|-------|-----------|
| `medium` | The school stem from `ART.md`, verbatim. |
| `style_sentence` | One line: what you see in a thumbnail + this world's clothes and buildings. |
| `palette[]` | 5–8 pigments, each with `use` on a real surface (wool, brick, lamp). |
| `light` | Who lights a street and a room. 3–6 sentences. |
| `wardrobe` | 80–150 words. What people wear at work and after hours. |
| `buildings` | 80–150 words. Wood, brick, stone, glass — what a camera would hit. |
| `crowd` | 40–80 words. What a street of people looks like at noon. |
| `motif[]` | Recurring objects a later pack must repeat (`name` + `where`). Count: `LOCK.md`. |
| `look_dev[]` | Only if the look was inferred. Three **different** schools. |
| `subjects[]` | Captions for `/world-bible-pack`. Required at **core**. Entry face, key places, unique thing in use, ordinary props. Count: `LOCK.md`. |

`subjects[]` item: `id`, `kind` (`person` \| `place` \| `prop` \| `signature` \| `map`), `subject_id` (an id in this book), `caption`.

---

## Play-seeds (`play-seeds.json`)

Hooks, not a script. Form seeds (`fmv` `rpg` `tcg` `doki`) stay. **Jobs**
are the proof this folder is a core book, not one campaign.

```json
{
  "id": "job.",
  "title": "Name of the job",
  "site": "place.",
  "clock": "what runs out this sitting",
  "fork": "the choice that splits two later playthroughs",
  "cast": ["person."],
  "body": "4–8 sentences. Only ids in this book."
}
```

Job slots:

1. One site that already exists (`place.*`).
2. One clock (a tide, a stamp, a shift, a body).
3. One fork (two later authors would pick opposite sides).
4. Cast from `people[]` or `opposition[]` already in this book.

**Three-games test (core).** Three jobs. Three different `site` ids.
Three different clocks. No new city, no new law, no new unique thing.
If you can only name one job, the box is a campaign draft. Go back to
W2/W3 and add toys.

Sitting: at least two jobs. Seed: one job.

A seed that invents a new city or a rule the Laws do not support is a bug.
