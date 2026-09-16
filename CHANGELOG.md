# Changelog

## 3.1.0

The skill's name is **Core Rule Book**. Slash command: `/core-rule-book`.
`/world-bible`, WB, and 世界圣经 still route here. Install path and GitHub
repo stay `luaproxy1993/world-bible` so existing `npx skills add` keeps working.
JSON schemas stay `doki.world-bible.*`. Compiled filename stays `WORLD_BIBLE.md`.

## 3.0.0

The bible is a **core rule book**, not a thin setting doc.

Baldur's Gate 1/2/3 sit on one D&D core book. This folder is that book.
Later skills cut pictures, jobs, and numbers from it. They are not this skill.

- Default scale is **`core`**: enough toys for three later campaigns.
  `sitting` is one district. `seed` is a pitch.
- Primer adds calendar, travel, economy, opposition.
- People name a want this season and leverage a player can use.
- `play-seeds.json` `jobs[]` is the three-games test.
- Art look adds crowd, motif, and required subjects at core. Still no pictures.
- Production line: `references/PIPELINE.md`. This skill stops at W6.
  `/world-bible-pack` and `/rpg-campaign-maker` are later sessions.
- Validate checks id existence, core counts, and distinct job sites.

## 2.0.0

This file is a **core rule book**, not a campaign.

- Primer (`world/` + `play/`): the world today, who you can be, three rungs of hardness, how a check and a fight work **here**.
- Box (`stage/` + `kit/`): places, famous faces, groups, gear.
- Timeline, written look, compile stay.
- A plotted job is `/rpg-campaign-maker`. Pictures are `/world-bible-pack`.
- Same chapter job as Cyberpunk 2020 / D&D Basic Rules: toys to tell a story with.

## 1.11.0

- Ordinary words first. Working names (`lock`, `residue`, `signature`, `sitting`) are defined in SKILL.md.
- Each module has required slots in `SPEC.md` (place, person, faction, law, beat, clothes, buildings). A brief that skips a slot is not done.
- Sitting briefs: 220–400 words. Story-window beats: 4–7 sentences naming when, where, who, what changes, what is left.

## 1.10.0

World Bible is **text only**. Art look is prose (`lock.look` + `art/art.json`).
Portraits, maps, places, and props are a second skill: `/world-bible-pack`
(`npx skills add luaproxy1993/world-bible-pack -y`).

## 1.9.0

- **Scale:** `seed` or `sitting` (~3 hours, default).
- **Run loop:** one step per turn; `accepted[]`.
- **Schools:** thumbnail-distinct tells.

## 1.8.0

Public skill release. Manual voice. Vignette as brief. Compile from lock.
