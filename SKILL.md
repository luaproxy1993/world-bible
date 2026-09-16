---
name: world-bible
description: >
  Turn multimodal seeds into a modular game World Bible — text only
  (temperament, scale, stage, timeline, art style as prose). Use when the
  user runs /world-bible, says World Bible, WB, 世界圣经, 世界观设定. Pictures,
  portraits, maps, and props are /world-bible-pack.
argument-hint: "[world_path] [new|lock|ingest|world|stage|timeline|art|compile]"
user-invocable: true
metadata:
  short-description: Modular game World Bible generator
  version: "1.11.0"
  feeds: "doki-game-maker, galgame-maker, rpg-campaign-maker, game-maker-pipeline, world-bible-pack"
---

# World Bible

A World Bible is a **text stage document**. It tells a writer and a designer
what the world is, how long this file covers, who is on stage, what happened,
and how pictures should look — in words. No pictures here. Portraits, maps,
and props are `/world-bible-pack`.

Default reader: North America / Europe. Default language: **English** in
every JSON field. Another language only when `lock.json` `language` is set.

Clothes, buildings, and era match the world the lock named. The unique
thing sits under that surface, not instead of it.

## Names we use

Ordinary words first. The JSON key is in parentheses.

- The one-page agreement (`lock`)
- How long this bible covers (`scale`). `sitting` means about 3 hours of play
- What this fact still does to people now (`residue`)
- The one unique thing a game can steal, switch, or check (`signature`)
- A short brief (`vignette`): what it is, who uses it, every slot in `SPEC.md`
- The stretch a game occupies (`story_window`)
- Older facts that still mark today (`world_key`)
- How pictures should look, in words (`look`)

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

```text
intake (script / homage / image / audio / pitch)
  → lock (temperament + story window + signature + look)
  → ingest (quote sources; note what still marks today)
  → world + stage + timeline (JSON vignettes)
  → art look (text)
  → compile (WORLD_BIBLE.md + overview.html from JSON)
```

Pictures: `/world-bible-pack` after W6.

Load on demand:

- Field sheet + folder layout → `references/FIELDS.md`
- Lock JSON → `references/LOCK.md`
- Module schemas, vignette form → `references/SPEC.md`
- Multimodal intake → `references/INGEST.md`
- Art look (text) → `references/ART.md`
- Downstream mapping → `references/HANDOFF.md`
- Structure moves (Cyberpunk Red / WoD / GURPS / Edith / Diablo) → `references/CANON.md`
- Tiny filled example → `references/EXAMPLE.md`

## Commands

```
/world-bible
/world-bible new <slug>
/world-bible lock | ingest | world | stage | timeline | art | compile
```

| Arg | Action |
|-----|--------|
| (none) | Read `pipeline_state.json` and continue; else ask intake |
| `new <slug>` | Scaffold, then **lock** |
| `lock` | W0 |
| `ingest` | W1 |
| `world` | W2 |
| `stage` | W3 |
| `timeline` | W4 |
| `art` | W5 written look only. Text look-dev if `lock.look.source` is `inferred` |
| `compile` | W6 |

## Run

Read `pipeline_state.json` first. Do **only** `step`. Do not reopen ids in
`accepted`. Do not start the next step in the same turn.

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

Canonical text is **JSON** in four folders (`world/`, `stage/`, `timeline/`,
`art/`). `WORLD_BIBLE.md` and `overview.html` are compile-only. Layout and
every field: `references/FIELDS.md`.

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
2. **Scale** — `seed` (20–40 min) or `sitting` (~3 hours). Default `sitting`.
   Counts: `references/LOCK.md` scale table
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
  "skill": "world-bible",
  "skill_version": "1.11.0",
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

## W2 · World

**Done when** `world/world.json` answers every World slot in `references/SPEC.md`.
A new teammate can read it aloud in about four minutes and run a scene.

Load `references/SPEC.md` §World. Fill uniqueness, laws (if/then + cost),
everyday (price, time, or place in each key), and the unique thing as a
full brief.

**STOP** — `step W2: accept`

---

## W3 · Stage

**Done when** every place, person, faction, and institution in
`stage/stage.json` answers **every** slot in `references/SPEC.md` (place,
person, faction, institution). Counts match `lock.scale`.

Load `SPEC.md` §Brief and §Stage. Mark the entry face. Relations are ids.

**STOP** — `step W3: accept`

---

## W4 · Timeline

**Done when** every `story_window` beat answers the five beat slots in
`references/SPEC.md` §Timeline, and the beat count matches `lock.scale`.

Load `SPEC.md` §Timeline. History that does not still mark today is out.

**STOP** — `step W4: accept`

---

## W5 · Art

**Done when** `art/art.json` answers every Art-look slot in `references/SPEC.md`
(medium, style_sentence, palette, light, wardrobe, buildings). **No pictures.**

Load `references/ART.md`. Do not load `imagine`. Do not call `image_gen`
or `image_edit`. If `lock.look.source` is `inferred`, write three
different-school `look_dev` rows and **STOP** for `look-dev: pick`.
Optional `subjects[]` may name what a later pack should show (entry face,
key places, signature in use). User-supplied images stay in `source/`.

**STOP** — `step W5: accept`

---

## W6 · Compile + play-seeds

**Done when** the four JSON folders validate, `play-seeds.json` maps the
stage onto at least one playable form, and `overview.html` + `WORLD_BIBLE.md`
are regenerated from JSON.

```bash
{SKILL_ROOT}/scripts/compile.sh <world-root>
```

Play-seeds (SPEC §Play-seeds): how this world becomes FMV / RPG / TCG / Doki.
Seeds are hooks, not systems. Sitting scale: name enough `story_window`
beats that a writer can hang ~3 hours.

After accept, if they want portraits, maps, and props: `/world-bible-pack`.
Do not start it in this turn unless they asked.

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
5. Relations are ids that exist in the four JSON files.
6. Art look is prose, including clothes and buildings. No image files.
   Pictures are `/world-bible-pack`.
7. Hand-edits belong in JSON. `WORLD_BIBLE.md` and `overview.html` are compile-only.

Homage extracts class, not copyrighted plot or names. Write the lock before
a single extra continent. Do not generate pictures in this skill.

## Session bootstrap

```
load:
  - {SKILL_ROOT}/SKILL.md
  - {WORLD}/pipeline_state.json, lock.json, world/world.json   (if they exist)
  - {SKILL_ROOT}/references/INGEST.md     at W1 or when intake is not a sentence
  - {SKILL_ROOT}/references/SPEC.md       at W2–W4 and W6
  - {SKILL_ROOT}/references/ART.md        at W5 (text look)
  - {SKILL_ROOT}/references/HANDOFF.md    when a downstream skill is named
  - {SKILL_ROOT}/references/CANON.md      when prose goes generic
preflight:
  - slug, scale, and story window exist, or this is W0
  - JSON folders are the editing surface; WORLD_BIBLE.md / overview.html are not
  - do only pipeline_state.step; do not generate images
```

On accept: append the step to `accepted`, set `step` to the next id.
`todo_write` tracks W0–W6. Checkpoint → `pipeline_state.json`.
