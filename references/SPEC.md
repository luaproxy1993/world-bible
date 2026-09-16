# World Bible spec

JSON in four folders is what you edit. `WORLD_BIBLE.md` and `overview.html`
are compiled. Do not hand-edit them.

```text
world/world.json
stage/stage.json
timeline/timeline.json
art/art.json
```

Every id you mention must exist. Prefix: `place.` `person.` `faction.`
`institution.` `signature.` `event.`

---

## Brief (`vignette`)

One object on the stage: a place, a person, a faction, an institution,
or the unique thing. Not a wiki card. Not a short story.

```json
{
  "id": "place.",
  "kind": "place",
  "title": "Name, job or use, when",
  "body": "sitting: 220–400 words. seed: 150–250. Answer every slot below.",
  "residue": "what this still does to people in the playable present",
  "relations": ["person.", "signature."],
  "play_hook": "one scene a designer can run tomorrow, using only ids in this bible"
}
```

**Slot test.** If a required slot is missing, the brief is not done.
**Swap test.** Replace the proper names with another genre. If the paragraph
still works, it is too generic. Rewrite.
**Hook test.** A designer can start a scene without inventing a new room or person.
**Voice test.** SKILL.md Voice. If you reread it, look up a word, or it reads
as a diary, rewrite.

Entry face: exactly one `person.*` in `world.json` → `entry_face`.

### Place slots (every `places[]` item)

1. What this place is, in one sentence.
2. Who may enter, who may not, and which door they use.
3. Hours: when it is open, when it is empty.
4. A price, a ticket, a stamp, or a free rule.
5. How the unique thing (`signature`) shows up in this room.
6. One dated incident (year or season) that proves a Law.
7. Which other ids you can walk to from here.

### Person slots (every `people[]` item)

1. Name, age, job.
2. Where they stand on a normal day (a `place.*` id).
3. What they can give, sell, stamp, or refuse.
4. How the unique thing touches them (bag, body, pay, door).
5. One dated incident.
6. Who they deal with (ids, not adjectives).

### Faction slots

1. What they do this year, not their myth.
2. Which streets or rooms they walk (`place.*`).
3. Who they can help or hurt, and with what permission.
4. What they control that a player can steal, stop, or buy.
5. One dated incident this window.

### Institution slots

1. The public rule (sign, ticket, stamp, posted notice).
2. Who enforces it.
3. What happens if you break it this year.
4. One dated proof it still holds.

---

## World (`world/world.json`)

A teammate reads this aloud in about four minutes and can run a scene.

| Field | Dig until |
|-------|-----------|
| `uniqueness` | 280–450 words. Era look, who has power, how the unique thing shows up on a street, what a visitor gets wrong on day one. |
| `laws[]` | 3–7. Each is if/then a local knows, **plus** what breaking it costs this year. 2–4 sentences. |
| `everyday` | `eat` `pay` `move` `sleep` `die` `news`. Each key: 3–5 sentences with a price, a time, or a `place.*`. |
| `signature` | A brief (same slots as above). Procedure: how you get it, how you use it, how it fails. |
| `slang[]` | Optional. About 12 terms. `term` in local speech, `meaning` in ordinary English. |

Out: creation myths with no mark on today, other continents, system math.

---

## Stage (`stage/stage.json`)

Counts: `lock.scale` in `LOCK.md`. Every item is a brief with **all** slots filled.

A place names who uses it. A person names where they stand. A faction names
the streets it walks this year.

---

## Timeline (`timeline/timeline.json`)

`world_key` = older facts that still mark today. As many as leave a mark.
`story_window` = the stretch a game occupies. Beat **count** is `lock.scale`.

Each `story_window` beat body: **4–7 sentences**. Must name:

1. When.
2. Where (`place.*`).
3. Who is on stage (`person.*` or `faction.*`).
4. What changes.
5. What is left for the next beat (`residue`).

A table with no bodies is a date list. Rewrite.

---

## Art look (`art/art.json`)

Words only. Pictures are `/world-bible-pack`. See `ART.md` for schools.

Fill:

| Field | Dig until |
|-------|-----------|
| `medium` | The school stem from `ART.md`, verbatim. |
| `style_sentence` | One line: what you see in a thumbnail + this world's clothes and buildings. |
| `palette[]` | 5–8 pigments, each with `use` on a real surface (wool, brick, lamp). |
| `light` | Who lights a street and a room. 3–6 sentences. |
| `wardrobe` | 80–150 words. What people wear at work and after hours. |
| `buildings` | 80–150 words. Wood, brick, stone, glass — what a camera would hit. |
| `look_dev[]` | Only if the look was inferred. Three **different** schools. |

`subjects[]` optional captions for the pack skill. If empty, the pack reads stage.

---

## Play-seeds (`play-seeds.json`)

Hooks, not a script. At least one form filled.

Sitting scale: FMV or RPG names enough `story_window` beats that a writer
can hang about 3 hours. A seed that invents a new city or a rule the Laws
do not support is a bug.
