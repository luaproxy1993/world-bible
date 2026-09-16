# World Bible spec

Canonical text is JSON in four folders. `WORLD_BIBLE.md` and `overview.html` are compile-only.

```text
world/world.json
stage/stage.json
timeline/timeline.json
art/art.json          + art/{scenes,people,props,signature}/
```

Ids live on objects. An id that is related but missing is a bug.

`timeline_shape`: `linear` | `cyclic` | `concurrent`.

Id prefix: `place.` `person.` `faction.` `institution.` `signature.` `event.` `art.`

Art `kind`: `scene` | `person` | `prop` | `signature` (count toward 4×3). Extras: `cover` | `anchor` | `look-dev`.

---

## Vignette (JSON)

Writing unit for places, people, factions, institutions, signature.

```json
{
  "id": "place.",
  "kind": "place",
  "title": "Name, role, when",
  "body": "120–250 words. What it is, who uses it, one dated incident that proves a Law. SKILL.md Voice.",
  "residue": "what this leaves on the playable present",
  "relations": ["person.", "signature."],
  "play_hook": "one thing a designer can stage tomorrow"
}
```

People titles: `Name, age or office, year or beat`. Places: a tour stop, not a wiki name. Factions name a behaviour. Default language: English. Density: `references/EXAMPLE.md`.

**Specificity test.** Swap proper nouns for another genre; if the paragraph still works, rewrite.

**Play-hook test.** A designer can start a scene from this object without inventing a new location or person.

**Voice test.** SKILL.md Voice. If you reread it, look up a word, or it reads as a diary, rewrite.

Entry face: exactly one `person.*` in `world.json` → `entry_face`.

---

## World (`world/world.json`)

```json
{
  "schema": "doki.world-bible.world",
  "version": "1.1.0",
  "slug": "",
  "title": "",
  "language": "en",
  "ip": "original",
  "entry_face": "person.",
  "signature_id": "signature.",
  "uniqueness": "",
  "temperament": {
    "feelings": [
      {"name": "", "lived": ""},
      {"name": "", "lived": ""},
      {"name": "", "lived": ""}
    ],
    "about": ""
  },
  "window": {"era": "", "start": "", "playable_present": "", "stop": ""},
  "laws": [{"id": "law.1", "text": ""}],
  "everyday": {
    "eat": "", "pay": "", "move": "", "sleep": "", "die": "", "news": ""
  },
  "signature": { },
  "slang": [{"term": "", "meaning": ""}]
}
```

`signature` is a vignette object. Laws are commandments a local would know (3–7). Everyday: eat, pay, move, sleep, die, get news.

Out: creation myths with no residue, other continents, system math.

---

## Stage (`stage/stage.json`)

```json
{
  "schema": "doki.world-bible.stage",
  "version": "1.1.0",
  "places": [],
  "people": [],
  "factions": [],
  "institutions": []
}
```

Each array is vignettes. Minimum: places 5–12, people 4–10, factions 3–7, institutions as needed. A place names who uses it. A person names where they stand. A faction names the streets it walks.

---

## Timeline (`timeline/timeline.json`)

```json
{
  "schema": "doki.world-bible.timeline",
  "version": "1.1.0",
  "shape": "linear",
  "worldlines": [{"id": "prime", "name": "", "status": "canonical"}],
  "world_key": [],
  "story_window": []
}
```

Event:

```json
{
  "id": "event.",
  "when": "dated beat or cyclic return",
  "title": "",
  "residue": "",
  "relations": ["place."],
  "body": "2–4 sentences. Tables without bodies are a date list."
}
```

`world_key` = events that created present residue. `story_window` = the stretch a game occupies.

- `linear` — dated `when`
- `cyclic` — `when` is a beat; add `returns` / `changes`
- `concurrent` — add `worldline` per event, plus optional `comparison[]` rows `{ "event_id", "lines": { "prime": "", "ash": "" }, "shared_residue" }`

---

## Art (`art/art.json`)

See `ART.md` for generation. `medium` is the stem for `lock.look.school`. One canonical `kind: anchor`. Look-dev plates do not count. Schema:

```json
{
  "schema": "doki.world-bible.art",
  "version": "1.1.0",
  "style_sentence": "",
  "palette": [{"name": "", "hex": "", "use": ""}],
  "light": "",
  "medium": "",
  "plates": []
}
```

Plate:

```json
{
  "id": "art.",
  "kind": "scene",
  "aspect_ratio": "16:9",
  "path": "art/scenes/.png",
  "title": "",
  "caption": "what the picture is showing. SKILL.md Voice",
  "subject_id": "place."
}
```

Floor: 4 kinds × 3 plates = **12**. Distinct `aspect_ratio` among those 12: **≥ 4**. Caption required. Cover/anchor/look-dev extras allowed.

---

## Play-seeds (`play-seeds.json`)

Hooks, not systems. At least one form filled.

```json
{
  "schema": "doki.world-bible.play-seeds",
  "version": "1.1.0",
  "fmv": "",
  "rpg": "",
  "tcg": "",
  "doki": {
    "entry_face": "",
    "tagline": "",
    "world_setting": "",
    "three_minute_accept": ""
  }
}
```

A seed that invents a new city or a mechanic the Laws do not support is a bug.
