# Ingest

Use at W1, or whenever the intake is more than one original sentence.

Goal: a cited `source/` tree and `source/EXTRACT.md`. Later modules quote or mark `invented`. The bible is not a summary in another language.

## Detect

| Clue | Treat as |
|------|----------|
| Original script, treatment, outline | **script** — quote scenes; keep voice |
| "like Dishonored" / "Disco Elysium meets Spirited Away" / one named work | **homage** — extract class, write original |
| Pitch PDF, concept doc, GDD fragment | **pitch** — temperament + spatial logic first |
| TRPG core / worldbook / AP | **book** — setting chapters, not the combat math |
| Images, moodboards, stills | **image** — describe, then keep as plates |
| Audio, song, voice memo, ambience | **audio** — transcript or described texture |
| Existing `WORLD_BIBLE.md` / pack `docs/` | **revise** — diff against this spec; fill holes |
| Mixed | run each branch; one EXTRACT |

If unsure, ask which **story window** to keep. Do not ingest a 400-page setting into one bible.

## Script

1. Copy the file into `source/script/`.
2. List scenes that fall inside the lock's window. Scenes past the stop beat stay in `source/` and do not enter the stage.
3. Quote, then structure. Do not "improve" the author's rhythm.
4. Named people / places become registry stubs (id + name only). Vignettes wait for W3.

## Homage

Extract five classes, then invent:

| Class | Ask |
|-------|-----|
| Temperament | three feelings the source actually has, not its Wikipedia genre |
| Spatial logic | how space is used (vertical city, one house, a dungeon under a town) |
| Power | who hurts whom, and with what permission |
| Signature class | whale oil, the Masquerade, the NET, a family curse — the *kind* of unique thing |
| Look | how the source is painted (box art, dating-show glossy, cel) — class, not a copied still |

Write an original world. New names, new incidents, new map. IP field = `homage`. State the source work in the lock. Do not reproduce plot beats, dialogue, or character names.

Ground real-world facts (a city, a year, a public-domain myth) with search before treating them as true.

## Pitch / concept doc

Read for: about-sentence, tone section, setting paragraph, example walkthrough, reference images.

Edith-shaped docs: steal the *move* (named feelings, story cards with age+year, "what we mean by X"). Diablo-shaped docs: steal spatial descent and expandability. Do not copy their worlds.

## Book (TRPG / worldbook)

1. Setting chapters in, rules chapters out (unless a rule is a Law of the world).
2. One window: one city, one season, one chronicle slice — not the whole metaplot.
3. WoD-like sects become factions. Lifepath tables become people seeds, not a generator to ship.
4. Keep printed names if IP is licensed; otherwise homage rules apply.

## Image

1. Copy into `source/images/` (keep filenames).
2. For each: subject, light, medium, what it claims about temperament.
3. User plates that will be canonical: register as `art.*` with `kind: anchor|scene|person|prop|signature` and path under `art/` (copy, do not redraw, unless asked).
4. Moodboards inform `lock.look`; they are not the style anchor until W5 promotes one.

## Audio

1. Copy into `source/audio/`.
2. Transcript if speech (whisper / available ASR / user-supplied text). If none, describe texture: instrumentation, room, weather, voice age.
3. Ambience becomes Everyday life + Art light. Songs become temperament, not a soundtrack to ship.

## Revise

Diff the existing bible against this spec's required headings. Fill missing Laws, residue columns, play hooks, registry ids. Do not rewrite voice that already passes the specificity test.

## EXTRACT.md

```markdown
# Extract

## Cited
- `source/...` p.N / timecode — quoted fragment — maps to (world|place|person|event|?)

## Inferred residue
- (claim) — from (cite) — confidence high|medium

## Open questions
- (thing the lock or the author must answer)

## Invented (empty until W2+)
```

**Done:** every later module can point at `source/` or say `invented`. Open questions are listed, not silently filled.
