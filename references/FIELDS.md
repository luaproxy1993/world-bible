# World Bible · field sheet

One folder = one world. Canonical text is **JSON**. Default language **English**.
A world stage document. Maker skills consume it. Pictures: `/world-bible-pack`.

```
<slug>/
  lock.json                 one-page agreement
  world/world.json          primer: the world today
  play/play.json            who you can be; how trouble works here
  stage/stage.json          places, people, factions
  kit/kit.json              gear
  timeline/timeline.json    older marks + playable stretch
  art/art.json              written look
  pack/                     pictures (other skill)
  play-seeds.json           jobs you could run tonight, not a campaign
  overview.html             compiled
  WORLD_BIBLE.md            compiled
```

Every story object (place, person, faction, institution, signature, event) uses the same **vignette** shape:

| Field | What it is |
|-------|------------|
| `id` | Stable id (`place.north-try-pots`, `person.sister-cald`) |
| `kind` | `place` / `person` / `faction` / `institution` / `signature` / `event` |
| `title` | Name + role + when |
| `body` | sitting 220–400 words. Answers every slot in `SPEC.md` |
| `residue` | What this still does to people now |
| `relations` | Other ids, not adjectives |
| `play_hook` | One scene a designer can run tomorrow |

---

## `lock.json` — lock first

| Field | What it is |
|-------|------------|
| `slug` / `title` / `language` | Folder name, display title, `en` unless you say otherwise |
| `intake` / `ip` / `homage_source` | Where it came from; original / homage / licensed |
| `audience` | Default: North America / Europe |
| `temperament.feelings[3]` | Three named feelings + how they show up in life |
| `temperament.about` | One sentence: this world is about X |
| `story_window` | `era`, `start`, `playable_present`, `stop` |
| `signature` | The one unique thing you can steal / switch / check (`working_name`, `everyday`, `play`) |
| `scale` | `seed` (20–40 min) or `sitting` (~3 hours). Counts in `LOCK.md`. Default `sitting` |
| `look` | Paint school from intake: `school` `named_as` `why` `forbidden[]` `source` (`author` / `inferred`). Schools in `ART.md` |
| `timeline_shape` | `linear` / `cyclic` / `concurrent` |
| `worldlines` | Timeline tracks; one is `canonical` |
| `target_forms` | FMV / RPG / TCG / Doki — hooks only, does not ship a game |

---

## 1 · `world/world.json`

| Field | What it is |
|-------|------------|
| `uniqueness` | What makes this stage this world |
| `temperament` | Same three feelings, written as lived atmosphere |
| `window` | When we are; where the story stops |
| `laws[]` | 3–7 local rules that **are** gameplay |
| `everyday` | `eat` `pay` `move` `sleep` `die` `news` |
| `signature` | Full vignette of the unique thing |
| `slang[]` | Optional, ~12 terms (`term` / `meaning`) |
| `entry_face` | Id of the face on the card |
| `signature_id` | Id of the unique thing |

---

## 1b · `play/play.json`

| Field | What it is |
|-------|------------|
| `roles[]` | Who you can be on this stage. Count: `lock.scale` |
| `power.street/hard/rare` | Three rungs of how bad a risk gets |
| `conflict.check/fight/fail` | How you try, how you hurt, what failure costs **here** |

## 2 · `stage/stage.json`

| Array | Count | What it is |
|-------|-------|------------|
| `places` | `lock.scale` | Locations as briefs |
| `people` | `lock.scale` | People as briefs; one `entry_face` |
| `factions` | `lock.scale` | Who they are this season, where they walk |
| `institutions` | as needed | Origin of a law, church, license, currency |

## 2b · `kit/kit.json`

| Field | What it is |
|-------|------------|
| `gear[]` | Objects a GM can hand out. Count: `lock.scale` |

---

## 3 · `timeline/timeline.json`

| Field | What it is |
|-------|------------|
| `shape` | `linear` / `cyclic` / `concurrent` |
| `worldlines[]` | Tracks; concurrent worlds get a comparison table |
| `world_key[]` | History that still marks the present |
| `story_window[]` | The stretch a game occupies. Beat count: `lock.scale` |

Each event: `id` `when` `title` `residue` `relations` `body` (2–4 sentences).  
Concurrent extras: `worldline`, optional `comparison[]`.

---

## 4 · `art/art.json` (text look)

| Field | What it is |
|-------|------------|
| `style_sentence` | What you see small + clothes and buildings |
| `palette[]` | 5–8 colors: `name` `hex` `use` |
| `light` | Who lights a street and a room |
| `wardrobe` | Work clothes and after-hours clothes |
| `buildings` | Wood, brick, stone, glass |
| `medium` | Stem for `lock.look.school` (`ART.md`) |
| `look_dev[]` | Text candidates when look is inferred. Different schools |
| `subjects[]` | Optional captions for `/world-bible-pack`. Else the pack reads stage |

---

## `play-seeds.json` — hooks

| Field | What it is |
|-------|------------|
| `fmv` | Which vignettes become episodes |
| `rpg` | One sitting: where it starts/stops, what a check is |
| `tcg` | Factions as colors, signature as cards |
| `doki.entry_face` | Card face |
| `doki.tagline` | Short hook |
| `doki.world_setting` | Scene, not plot (2–4 concrete sentences) |
| `doki.three_minute_accept` | What the player feels that is not “just chat” |

---

## Compiled (do not hand-edit)

| File | For |
|------|-----|
| `overview.html` | Open in a browser; full picture pass |
| `WORLD_BIBLE.md` | Search / diff / paste |
