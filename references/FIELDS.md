# World Bible · field sheet

One folder = one core rule book. Canonical text is **JSON**. Default
language **English**. Maker skills consume it. Pictures: `/world-bible-pack`.
A plotted job: `/rpg-campaign-maker`. Line: `PIPELINE.md`.

```
<slug>/
  lock.json                 one-page agreement
  world/world.json          the world today, calendar, travel
  play/play.json            who you can be; economy; conflict; opposition
  stage/stage.json          places, people, factions, institutions
  kit/kit.json              gear
  timeline/timeline.json    older marks + playable stretch
  art/art.json              written look (no pictures)
  pack/                     pictures (other skill, later session)
  play-seeds.json           three jobs you could run, not a campaign
  overview.html             compiled
  WORLD_BIBLE.md            compiled
```

Every story object (place, person, faction, institution, signature, event,
role, gear, opposition) uses the same **vignette** shape:

| Field | What it is |
|-------|------------|
| `id` | Stable id (`place.north-try-pots`, `person.sister-cald`) |
| `kind` | `place` / `person` / `faction` / `institution` / `signature` / `event` / `role` / `gear` / `opposition` / `job` |
| `title` | Name + role + when |
| `body` | core 280–500 words. Answers every slot in `SPEC.md` |
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
| `scale` | `seed` (pitch), `sitting` (one district), **`core`** (default CRB). Counts in `LOCK.md` |
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
| `laws[]` | Local rules that **are** gameplay |
| `everyday` | `eat` `pay` `move` `sleep` `die` `news` |
| `calendar` | `day` `week` `clock` `curfew` |
| `travel` | `how` `times` `stop` — named place to named place |
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
| `economy` | `currency` `street_wage` `skilled_wage` `bread` `room` `fine` |
| `opposition[]` | Who can hurt you this window. Count: `lock.scale` |

## 2 · `stage/stage.json`

| Array | Count | What it is |
|-------|-------|------------|
| `places` | `lock.scale` | Locations as briefs |
| `people` | `lock.scale` | People as briefs; one `entry_face`; each has a want and leverage |
| `factions` | `lock.scale` | Who they are this season, where they walk, who they oppose |
| `institutions` | `lock.scale` | Origin of a law, church, license, currency |

## 2b · `kit/kit.json`

| Field | What it is |
|-------|------------|
| `gear[]` | Objects a GM can hand out. Count: `lock.scale`. Prices use `play.economy` |

---

## 3 · `timeline/timeline.json`

| Field | What it is |
|-------|------------|
| `shape` | `linear` / `cyclic` / `concurrent` |
| `worldlines[]` | Tracks; concurrent worlds get a comparison table |
| `world_key[]` | History that still marks the present |
| `story_window[]` | The stretch a game occupies. Beat count: `lock.scale` |

Each event: `id` `when` `title` `residue` `relations` `body` (4–7 sentences).
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
| `crowd` | A street of people at noon |
| `motif[]` | Recurring objects a later pack repeats (`name` `where`) |
| `medium` | Stem for `lock.look.school` (`ART.md`) |
| `look_dev[]` | Text candidates when look is inferred. Different schools |
| `subjects[]` | Captions for `/world-bible-pack`. Required at core |

---

## `play-seeds.json` — hooks + jobs

| Field | What it is |
|-------|------------|
| `jobs[]` | Proof the box can yield later campaigns. Count: `lock.scale`. Each: `site` `clock` `fork` `cast` |
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
