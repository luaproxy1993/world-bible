---
name: core-rule-book
description: >
  Core rule book (CRB) in text from multimodal seeds: world, roles, local
  conflict, economy, opposition, famous faces, places, gear, timeline,
  written art look. Shared substrate for later campaigns, like D&D under
  Baldur's Gate. Not a campaign and not pictures. Use when the user runs
  /core-rule-book, /crb, /world-bible, says core rule book, CRB, 核心规则书,
  World Bible, WB, 世界圣经. Campaigns are /rpg-campaign-maker. Pictures
  are /world-bible-pack.
argument-hint: "[world_path] [new|lock|ingest|primer|box|timeline|look|compile]"
user-invocable: true
metadata:
  short-description: Modular game core rule book generator
  version: "3.1.0"
  feeds: "doki-game-maker, galgame-maker, rpg-campaign-maker, game-maker-pipeline, world-bible-pack"
---

# Core Rule Book

This skill writes a **core rule book** in text. Baldur's Gate 1, 2, and 3
all sit on one D&D core book; each generation's authors then cut their own
story from that shared box. This folder is that box. Old name: World Bible.

It holds: the world today, who you can be, how trouble is resolved here,
wages and prices, who can hurt you, famous faces, places, gear, a timeline,
and a written look. A later GM uses it to run a job. It is **not** a
campaign and **not** a picture pack.

Production line: `references/PIPELINE.md`. This skill writes the core book
and stops. Campaigns are `/rpg-campaign-maker`. Pictures are
`/world-bible-pack`. Numbers and whitebox are `game-maker-pipeline`. Each
is a later session.

Default reader: North America / Europe. Default language: **English** in
every JSON field. Another language only when `lock.json` `language` is set.

Clothes, buildings, and era match the world the lock named. The unique
thing sits under that surface, not instead of it.

## Names we use

Ordinary words first. The JSON key is in parentheses.

- The one-page agreement (`lock`)
- How thick this book is (`scale`). **`core`** is the default: a shared
  box for later campaigns. `sitting` is one district. `seed` is a pitch
- What this fact still does to people now (`residue`)
- The one unique thing a game can steal, switch, or check (`signature`)
- A short brief (`vignette`): what it is, who uses it, every slot in `SPEC.md`
- The stretch a game occupies (`story_window`)
- Older facts that still mark today (`world_key`)
- How pictures should look, in words (`look`)
- Who you can be on this stage (`roles`)
- How hard a fight is here (`power`)
- How people hurt each other and take risks here (`conflict`)
- Wages and prices (`economy`)
- Who can hurt you this window (`opposition`)
- The toys: places, faces, gear (`box`)
- One later sitting with a goal (`job` in `play-seeds.json`; the campaign
  skill writes the actual job)
- A campaign / one plotted sitting (`rpg-campaign-maker`, not this file)
- Pictures (`world-bible-pack`, not this file)

## Voice

Write like a manual. A production assistant can use every sentence tomorrow.
An average US adult understands it on the first read.

- Complete sentences that chain facts. Do not stack fragments.
- Common words. If a high-schooler would look it up, cut it — unless it is a
  local name glossed in that same sentence.
- Say the thing in English first. Then the local name, once.
- State the rule, the room, who uses it, and what breaks. No interior thought.
- Feeling names are ordinary adjectives a stranger already knows: Wet, Official,
  Hungry.

If a paragraph could be a diary, rewrite it as instructions.

This is a style rule. Structure moves live in `references/CANON.md`.
How deep to dig: `references/SPEC.md`. A filled scrap: `references/EXAMPLE.md`.
The production line: `references/PIPELINE.md`.

```text
intake (script / homage / image / audio / pitch)
  → lock (temperament + story window + signature + look + scale)
  → ingest (quote sources; note what still marks today)
  → primer (world + who you can be + economy + how trouble works)
  → box (places, people, factions, gear, opposition already in play)
  → timeline
  → look (text)
  → compile (three jobs as proof, then stop)
```

Pictures and campaigns are later sessions. See `PIPELINE.md`.

Load on demand:

- Field sheet + folder layout → `references/FIELDS.md`
- Lock JSON → `references/LOCK.md`
- Module schemas, vignette form → `references/SPEC.md`
- Multimodal intake → `references/INGEST.md`
- Art look (text) → `references/ART.md`
- Production line (this skill stops) → `references/PIPELINE.md`
- Downstream field map → `references/HANDOFF.md`
- Structure moves (D&D / Cyberpunk Red / WoD / GURPS / Edith / Diablo) → `references/CANON.md`
- Tiny filled example → `references/EXAMPLE.md`

## Commands

```
/core-rule-book
/core-rule-book new <slug>
/core-rule-book lock | ingest | primer | box | timeline | look | compile
```

`/world-bible` and `/crb` are the same skill.

| Arg | Action |
|-----|--------|
| (none) | Read `pipeline_state.json` and continue; else ask intake |
| `new <slug>` | Scaffold, then **lock** |
| `lock` | W0 one-page agreement |
| `ingest` | W1 quote sources |
| `primer` or `world` | W2 the world, who you can be, economy, how trouble works |
| `box` or `stage` | W3 places, people, factions, gear |
| `timeline` | W4 what still marks today + the playable stretch |
| `look` or `art` | W5 written look. Text options if look was guessed |
| `compile` | W6 three jobs as proof, then stop |

## Run

Read `pipeline_state.json` first. Do **only** `step`. Do not reopen ids in
`accepted`. Do not start the next step in the same turn. Do not start
`/world-bible-pack` or `/rpg-campaign-maker` in this skill.

- Missing lock fields: at most **three** questions, then write the lock
  from intake and mark inferred fields.
- Off-topic author text: one line restating the current step, then continue
  that step.
- `revise` + a step id reopens that step. Nothing else does.
- After the step's files are written, **STOP** with `step W#: accept`.

Session root = the world folder. Resolve: path the user named → `./<slug>` → ask.

```
SKILL_ROOT=~/.grok/skills/world-bible
WORLD=<world-root>
```

Canonical text is **JSON** (`world/`, `play/`, `stage/`, `kit/`,
`timeline/`, `art/`). `WORLD_BIBLE.md` and `overview.html` are
compile-only. Layout and every field: `references/FIELDS.md`.

```bash
{SKILL_ROOT}/scripts/scaffold.sh <slug> [parent_dir]
{SKILL_ROOT}/scripts/compile.sh <world-root>
```

---

## W0 · Lock

**Done when** `lock.json` names scale, three feelings, one about-sentence, the
story window, the signature, IP, and look — and a stranger could quote
the about-sentence and the look `why`.

Write from `references/LOCK.md`. Fill:

1. **Slug / title / language / audience**
2. **Scale** — `seed` (pitch), `sitting` (one district), or **`core`**
   (default: a core rule book). Counts: `references/LOCK.md` scale table
3. **Intake** — original | homage | book | image | audio | mixed
4. **IP** — original | homage | unofficial remix | licensed
5. **Temperament** — three named feelings + one sentence: *this world is about X*.
   Name the feelings the brief actually wants, in ordinary adjectives.
6. **Playable stretch** (`story_window`) — era, start, stop. Older facts only
   if they still change life now
7. **Unique thing** (`signature`) — one technology, law, resource, or curse
   a game can steal, switch, or check
8. **How pictures should look** (`look`) — pick a school from `ART.md` by
   what you see small.
   `source`: `author` if the brief named a look, else `inferred`.
   Default school `oil-box` only when intake has no stronger signal
9. **Timeline shape** — `linear` | `cyclic` | `concurrent` (worldlines)
10. **Target forms** — FMV / RPG / TCG / Doki / unspecified. Listing a form
    does not commit to shipping it

Homage intake: extract temperament, spatial logic, power structure, signature
class, look class. Write an original world. New names, new incidents, new map.

Then `pipeline_state.json`:

```json
{
  "skill": "core-rule-book",
  "skill_version": "3.1.0",
  "slug": "<slug>",
  "step": "W0",
  "status": "in_progress",
  "accepted": []
}
```

**STOP** — `step W0: accept`

---

## W1 · Ingest

**Done when** every claimed fact in later modules can point at a file in
`source/`, or is marked `invented`.

Load `references/INGEST.md`. Dump raw intake into `source/` (immutable).
Write `source/EXTRACT.md`: quoted fragments + inferred residue + open questions.
Do not expand past the story window.

**STOP** — `step W1: accept` (skip the gate only when intake is a single
original sentence already captured in the lock)

---

## W2 · Primer (the world and how you play)

**Done when** `world/world.json` and `play/play.json` answer every World and
Play slot in `SPEC.md`, including calendar, travel, economy, and opposition.

This is the front of a core book: what the world is, who you can be, what
things cost, who can hurt you, how risky things work here. Not a campaign.

Load `references/SPEC.md` §World and §Play.

- World slots: uniqueness, laws (if/then + cost), everyday, calendar, travel,
  unique thing
- Play slots: roles, three rungs of hardness, economy (currency + numbers),
  opposition briefs, how a check and a fight work **in this world** (tied
  to the unique thing). Do not paste D&D or Cyberpunk math. Write this
  box's procedure.

If the turn would truncate, write JSON in batches in this step. The step
is not done until every slot is filled.

**STOP** — `step W2: accept`

---

## W3 · Box (the toys)

**Done when** `stage/stage.json` and `kit/kit.json` answer every slot in
`SPEC.md` (place, person, faction, institution, gear). Counts match
`lock.scale`. Every person names a want this season and leverage a player
can use.

This is the rest of the core book: rooms, famous faces, groups, and gear
a GM can pick up tonight. Not a plotted adventure. Later NPC and quest
design reads these briefs.

Load `SPEC.md` §Brief, §Stage, §Kit. Mark the entry face. Relations are ids.

If the turn would truncate before counts are met, write JSON in batches
in this step. Do not mark the step done early.

**STOP** — `step W3: accept`

---

## W4 · Timeline

**Done when** every `story_window` beat answers the five beat slots in
`references/SPEC.md` §Timeline, and the beat count matches `lock.scale`.

Load `SPEC.md` §Timeline. History that does not still mark today is out.
A timeline is not a campaign outline.

**STOP** — `step W4: accept`

---

## W5 · Art

**Done when** `art/art.json` answers every Art-look slot in `references/SPEC.md`
(medium, style_sentence, palette, light, wardrobe, buildings, crowd, motif).
**No pictures.** At core scale, `subjects[]` meets the count in `LOCK.md`.

Load `references/ART.md`. Do not load `imagine`. Do not call `image_gen`
or `image_edit`. If `lock.look.source` is `inferred`, write three
different-school `look_dev` rows and **STOP** for `look-dev: pick`.
User-supplied images stay in `source/`.

**STOP** — `step W5: accept`

---

## W6 · Compile + jobs

**Done when** JSON validates, `play-seeds.json` holds enough **jobs** for
the scale (core: three, different sites and clocks), and `overview.html` +
`WORLD_BIBLE.md` are regenerated from JSON.

```bash
{SKILL_ROOT}/scripts/compile.sh <world-root>
```

Jobs are the three-games test (`SPEC.md` §Play-seeds): proof that three
later authors could cut three different sittings from this box. Form seeds
(FMV / RPG / TCG / Doki) stay as hooks. Neither is a campaign.

Load `references/PIPELINE.md`. After accept, print the next-skill names
(pictures, a plotted job, numbers). Do not start those skills in this turn
unless the author asked.

Load `references/HANDOFF.md` if the author names a downstream skill. Point
them; do not start that skill's pipeline unless they asked.

**STOP** — `step W6: accept`

---

## Quality bar

1. A teammate can quote the about-sentence, the three feelings, and the look
   why. An average American can read any paragraph once and know what it said.
   Manual voice. No fragment stacks. No unglossed coinage.
2. Every brief answers its SPEC slots. Swap the names; if it still works, rewrite.
3. Every older fact still does something to people in the playable present.
4. The signature is mechanically touchable.
5. Relations are ids that exist in the JSON files.
6. Art look is prose, including clothes, buildings, crowd, and motifs. No
   image files. Pictures are `/world-bible-pack`.
7. Hand-edits belong in JSON. `WORLD_BIBLE.md` and `overview.html` are compile-only.
8. **Three-games test.** At core scale, `jobs[]` names three sittings with
   three sites and three clocks, using only ids in this book. If you can
   only name one, the box is a campaign draft — add toys, do not plot harder.
9. Economy numbers show up in gear and in place prices. Opposition uses
   the unique thing. People name a want and a leverage.

Homage extracts class, not copyrighted plot or names. Write the lock before
a single extra continent. This skill writes text. Pictures and campaigns
are later sessions.

## Session bootstrap

```
load:
  - {SKILL_ROOT}/SKILL.md
  - {WORLD}/pipeline_state.json, lock.json, world/world.json   (if they exist)
  - {SKILL_ROOT}/references/INGEST.md     at W1 or when intake is not a sentence
  - {SKILL_ROOT}/references/SPEC.md       at W2–W4 and W6 (primer, box, timeline, jobs)
  - {SKILL_ROOT}/references/ART.md        at W5 (text look)
  - {SKILL_ROOT}/references/PIPELINE.md   at W6, and when pictures / campaign / numbers are named
  - {SKILL_ROOT}/references/HANDOFF.md    when a downstream skill is named
  - {SKILL_ROOT}/references/CANON.md      when prose goes generic
preflight:
  - slug, scale, and story window exist, or this is W0
  - JSON folders are the editing surface; WORLD_BIBLE.md / overview.html are not
  - do only pipeline_state.step; write no pictures; start no other skill
```

On accept: append the step to `accepted`, set `step` to the next id.
`todo_write` tracks W0–W6. Checkpoint → `pipeline_state.json`.
