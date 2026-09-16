---
name: world-bible
description: >
  Turn multimodal seeds into a modular game World Bible (temperament, stage,
  timeline, art plates). Use when the user runs /world-bible, says World Bible,
  WB, 世界圣经, 世界观设定, or wants a world alignment doc before an FMV, RPG,
  TCG, or Doki pack.
argument-hint: "[world_path] [new|lock|ingest|world|stage|timeline|art|compile]"
user-invocable: true
metadata:
  short-description: Modular game World Bible generator
  version: "1.8.0"
  feeds: "doki-game-maker, galgame-maker, rpg-campaign-maker, game-maker-pipeline"
---

# World Bible

A World Bible is the **seed** a team aligns on before anyone builds a game:
temperament, stage, timeline, art. Modular, editable, genre-agnostic.
Downstream maker skills consume it.

Default audience: **North America / Europe**. Default language: **English**
in every JSON field, caption, overview, and compile. Another language only
when `lock.json` `language` is set. Taste: commercial Western entertainment
unless the lock names a different audience.

**Surface first.** Wardrobe, architecture, and era look like the world the
lock named. Unique residue (the signature object, a law, a lived detail)
sits *under* that surface. Paint school is `lock.look`, judged from
intake at W0. Default school is oil box-art when intake does not name a
look. Schools and look-dev: `references/ART.md`.

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
Density: `references/EXAMPLE.md`.

```text
intake (script / homage / image / audio / pitch)
  → lock (temperament + story window + signature + look)
  → ingest (cite; extract residue)
  → world + stage + timeline (JSON vignettes)
  → art plates
  → compile (WORLD_BIBLE.md + overview.html from JSON)
```

Load on demand:

- Field sheet + folder layout → `references/FIELDS.md`
- Lock JSON → `references/LOCK.md`
- Module schemas, vignette form → `references/SPEC.md`
- Multimodal intake → `references/INGEST.md`
- Art plates + Imagine protocol → `references/ART.md`
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
| `art` | W5 (look-dev first when `lock.look.source` is `inferred`) |
| `compile` | W6 |

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

**Done when** `lock.json` names three feelings, one about-sentence, the
story window, the signature, IP, and look — and a stranger could quote
the about-sentence and the look `why`.

Write from `references/LOCK.md`. Fill:

1. **Slug / title / language / audience**
2. **Intake** — original | homage | book | image | audio | mixed
3. **IP** — original | homage | unofficial remix | licensed
4. **Temperament** — three named feelings + one sentence: *this world is about X*.
   Name the feelings the brief actually wants, in ordinary adjectives.
5. **Story window** — the playable present (era, start, stop). History exists
   only as **residue** on this window
6. **Signature** — one technology, law, resource, or curse that makes the stage
   unique and that games can mechanically touch
7. **Look** — paint school from intake (`references/ART.md` schools).
   `source`: `author` if the brief named a look, else `inferred`.
   Default school `oil-box` only when intake has no stronger signal
8. **Timeline shape** — `linear` | `cyclic` | `concurrent` (worldlines)
9. **Target forms** — FMV / RPG / TCG / Doki / unspecified. Listing a form
   does not commit to shipping it

Homage intake: extract temperament, spatial logic, power structure, signature
class, look class. Write an original world. New names, new incidents, new map.

Then `pipeline_state.json`:

```json
{
  "skill": "world-bible",
  "skill_version": "1.8.0",
  "slug": "<slug>",
  "step": "W0",
  "status": "in_progress"
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

**Done when** `world/world.json` is an intro a new teammate could read aloud
in three minutes and know the world's uniqueness, era, laws, everyday life,
and signature.

Load `references/SPEC.md` §World. Write:

- Uniqueness (what makes this stage this world)
- Temperament restated as lived atmosphere
- Story-window era
- **Laws** — world rules that *are* gameplay
- **Everyday life** — how people eat, pay, move, die
- **Signature** — full vignette, not a label

Specificity test: swap the proper nouns for another genre; if the paragraph
still works, rewrite. Voice test: SKILL.md Voice. First read. If it reads as
a diary, rewrite.

**STOP** — `step W2: accept`

---

## W3 · Stage

**Done when** every place, person, faction, and institution in
`stage/stage.json` is a **vignette** object with residue and a play hook.

Load `references/SPEC.md` §Vignette. A vignette is a brief: what it is, who
uses it, one dated proof of a Law. Not a short story and not a wiki infobox.

Minimum ship: places 5–12, people 4–10 (mark the **entry face**), factions
3–7, institutions as needed. Ids live on the objects. Relations are ids.

**STOP** — `step W3: accept`

---

## W4 · Timeline

**Done when** `timeline/timeline.json` enumerates world-key events **and**
the story-window slice, in the shape locked at W0.

Load `references/SPEC.md` §Timeline.

- `linear` — dated table, residue column
- `cyclic` — beat table: what returns, what changes
- `concurrent` — worldline comparison table (event × line)

History that does not leave residue on the stage is out. Events get ids and
relations to places / people / factions.

**STOP** — `step W4: accept`

---

## W5 · Art

**Done when** `art/art.json` medium matches `lock.look`, one canonical
style-anchor exists (look-dev resolved), every counted plate has a
caption, and the 4×3 floor is met with mixed ratios.

Load `references/ART.md`. Also load the `imagine` skill before any
`image_gen` / `image_edit`. If `lock.look.source` is `inferred` (or the
author asked for options), run look-dev and **STOP** for `look-dev: pick`
before generating the twelve. Recurring subjects: one canonical plate, then
`image_edit`. People plates are standing portraits on flat black. User-supplied
images stay in `source/` and may become anchors; do not redraw them unless
asked.

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
Seeds are hooks, not systems.

Load `references/HANDOFF.md` if the author names a downstream skill. Point
them; do not start that skill's pipeline unless they asked.

**STOP** — `step W6: accept`

---

## Quality bar

1. A teammate can quote the about-sentence, the three feelings, and the look
   why. An average American can read any paragraph once and know what it said.
   Manual voice. No fragment stacks. No unglossed coinage.
2. Every vignette fails the swap-the-nouns test (it is only true here). Residue
   sits under the locked surface.
3. Every historical fact leaves residue on the playable present.
4. The signature is mechanically touchable.
5. Relations are ids that exist in the four JSON files.
6. Art: 4×3 floor, mixed ratios, caption per plate, one style anchor.
   Plates match the locked surface and `lock.look` (`references/ART.md`).
7. Hand-edits belong in JSON. `WORLD_BIBLE.md` and `overview.html` are compile-only.

Homage extracts class, not copyrighted plot or names. Write the lock before
generating a single image or a single extra continent.

## Session bootstrap

```
load:
  - {SKILL_ROOT}/SKILL.md
  - {WORLD}/pipeline_state.json, lock.json, world/world.json   (if they exist)
  - {SKILL_ROOT}/references/INGEST.md     at W1 or when intake is not a sentence
  - {SKILL_ROOT}/references/SPEC.md       at W2–W4 and W6
  - {SKILL_ROOT}/references/ART.md        at W5
  - {SKILL_ROOT}/references/HANDOFF.md    when a downstream skill is named
  - {SKILL_ROOT}/references/CANON.md      when prose goes generic
  - imagine skill                         before any image_gen / image_edit
preflight:
  - slug and story window exist, or this is W0
  - JSON folders are the editing surface; WORLD_BIBLE.md / overview.html are not
```

`todo_write` tracks W0–W6. Checkpoint → `pipeline_state.json`.
