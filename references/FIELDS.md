# World Bible · field sheet

One folder = one world. Canonical text is **JSON**. Default language **English**.
A world alignment seed. Maker skills consume it.

```
<slug>/
  lock.json                 lock (before art)
  world/world.json          1 world
  stage/stage.json          2 places / people / factions
  timeline/timeline.json    3 timeline
  art/art.json + images     4 art
  play-seeds.json           how it could become a game
  overview.html             human overview (compiled)
  WORLD_BIBLE.md            same content as markdown (compiled)
```

Every story object (place, person, faction, institution, signature, event) uses the same **vignette** shape:

| Field | What it is |
|-------|------------|
| `id` | Stable id (`place.north-try-pots`, `person.sister-cald`) |
| `kind` | `place` / `person` / `faction` / `institution` / `signature` / `event` |
| `title` | Name + role + when |
| `body` | 120–250 words: what it is, who uses it, one dated proof of a Law. SKILL.md Voice |
| `residue` | What this leaves on the playable present |
| `relations` | Other ids, not adjectives |
| `play_hook` | One thing a designer can stage tomorrow |

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

## 2 · `stage/stage.json`

| Array | Count | What it is |
|-------|-------|------------|
| `places` | 5–12 | Locations as short stories |
| `people` | 4–10 | Bios as incidents; one `entry_face` |
| `factions` | 3–7 | Who they are this season, where they walk |
| `institutions` | as needed | Origin of a law, church, license, currency |

---

## 3 · `timeline/timeline.json`

| Field | What it is |
|-------|------------|
| `shape` | `linear` / `cyclic` / `concurrent` |
| `worldlines[]` | Tracks; concurrent worlds get a comparison table |
| `world_key[]` | History that still marks the present |
| `story_window[]` | The stretch a game actually occupies |

Each event: `id` `when` `title` `residue` `relations` `body` (2–4 sentences).  
Concurrent extras: `worldline`, optional `comparison[]`.

---

## 4 · `art/art.json` + images

Visual law:

| Field | What it is |
|-------|------------|
| `style_sentence` | Locked school + locked surface + composition (`ART.md`) |
| `palette[]` | 5–8 colors: `name` `hex` `use` |
| `light` | Who lights the world |
| `medium` | Stem for `lock.look.school` (`ART.md`). Copied at W5 |
| `plates[]` | The picture list |

Each plate:

| Field | What it is |
|-------|------------|
| `id` | `art.north-try-pots` |
| `kind` | `scene` / `person` / `prop` / `signature` (count toward 12). Extra: `cover` / `anchor` / `look-dev` |
| `aspect_ratio` | `16:9` `9:16` `1:1` `3:4` `4:3` `3:2` … |
| `path` | File under `art/scenes/` `people/` `props/` `signature/` |
| `title` | Short name |
| `caption` | What the picture is showing. SKILL.md Voice |
| `subject_id` | Place / person / signature this plate belongs to |

**Floor: 4 × 3 = 12.** At least 3 scenes, 3 people, 3 props, 3 signature objects. At least 4 different ratios. Cover, style-anchor, and look-dev are extra. One canonical `kind: anchor`.

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
