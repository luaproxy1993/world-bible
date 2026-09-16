# Handoff

The production line is `PIPELINE.md`. This file is the field map. This
skill stops at an accepted core rule book. Named downstream skills consume
it. Do not start their pipeline unless the author asked in this turn.

## doki-game-maker

WB is the pack's alignment seed. Pack shape stays `doki-game-maker`.

| WB | Pack |
|----|------|
| `entry_face` + person vignette | `content/characters/<key>.json` display fields; long prose stays in WB / `*_full.md` |
| temperament + `lock.look` + art style sentence | pack `ART_BIBLE.md` |
| `place.*` | `assets/scenes/{zone}/{id}/` + mechanics map ids |
| `world/world.json` atmosphere excerpt | `mechanics/data/r1_world.json` `world_setting` (**scene, not plot**; not the character system prompt) |
| play-seeds → Doki | pack tagline + 3-minute accept |
| signature | a visible object or law the shell can touch (lamp, currency, curfew) — not a new host table |

Do not copy WB prose into `r1_world.world_setting`. Two–four concrete scene sentences.

If the pack has no temperament lock, run `/world-bible` first rather than a one-page `docs/WORLD_BIBLE.md`.

## galgame-maker

WB is upstream of ST worldbook.

| WB | Route B |
|----|---------|
| Laws + story-window facts | WI-01 |
| Timeline | WI-01B |
| People | cards; Narrator vs live speaker from entry face / flashback-only |
| Places | `SCENE_MAP` / backgrounds |

`/galgame-maker bible` splits a **locked** WB into WI. It does not author a new bible.

## rpg-campaign-maker

WB is the **core book**. This skill is one **job** pulled from the box
(see `play-seeds.json` `jobs[]`). Do not rewrite the core book. Cut a
slice: one site, one clock, one fork. Separate session.

| WB | Campaign |
|----|----------|
| story window | `docs/LOCK.md` start / stop / out |
| one site + one clock + one fork | the sitting |
| people on stage this sitting | sheet + portraits; flashback-only stay in prose |
| Laws | which checks actually fire |

Do not ingest the whole timeline into `play/story.js`.

## world-bible-pack

WB is text. This skill writes `pack/` pictures.

| WB | Pack |
|----|------|
| `lock.look` + `art.json` look | prompt stem |
| `stage.people` | standing portraits on flat black |
| `stage.places` | location plates + one playable-window map |
| `signature` + ordinary objects | props in use |

Do not start `/world-bible-pack` from `/world-bible` unless the author asked
in this turn. Pictures are a later session.

## game-maker-pipeline

WB is not the ≥99p Design Bible.

| WB | Pipeline |
|----|----------|
| temperament + `lock.look` + style sentence | `art/style-anchor.json` / re_00 tone. Pictures from `/world-bible-pack` |
| signature + spatial logic | GDD systems *candidates* — still require `gdd: accept` |
| plates | references for production; re-register in `art-prompt-registry.json` before regen |

Ad-hoc pic gen from WB plates as final assets is out. Production still goes through RE-19～28.

## dokiimport

A World Bible is content. An App SDK `manifest.json` with `kind: "world"` is a runtime envelope. Do not treat the bible folder as a deliverable world app.

## What stays in the WB folder

`lock.json`, `world/` `play/` `stage/` `kit/` `timeline/` `art/` (text),
`source/`, `play-seeds.json`, compiled `WORLD_BIBLE.md` and `overview.html`.

`pack/` is written by `/world-bible-pack`, not this skill.

Maker skills copy or cite; they do not move the canonical files.
