---
name: world-bible-art
description: >
  Paint a World Bible art pack from an accepted art registry. Use when the
  user runs /world-bible-art, says 素材包, generate WB plates, paint the
  bible, or wants pictures from a locked World Bible. Not for writing the
  bible — that is /world-bible.
argument-hint: "[world_path] [floor|full]"
user-invocable: true
metadata:
  short-description: Generate World Bible art plates from the registry
  version: "1.0.0"
  requires: "world-bible"
---

# World Bible Art

Reads an accepted World Bible `art/art.json` registry and writes the
pictures. Does not author lock, world, stage, or timeline.

```
SKILL_ROOT=~/.grok/skills/world-bible
ART_SKILL=~/.grok/skills/world-bible-art
WORLD=<world-root>
```

Load:

- `{WORLD}/lock.json`, `{WORLD}/art/art.json`, `{WORLD}/stage/stage.json`
- `{SKILL_ROOT}/references/ART.md` (schools, recipes, prompt law)
- `imagine` skill before any `image_gen` / `image_edit`

Abort if `art.json` is missing, or counted plates lack `prompt`. If
`lock.look.source` is still `inferred`, **STOP** and send them back to
`/world-bible art` for `look-dev: pick`.

## Commands

```
/world-bible-art
/world-bible-art <world_path>
/world-bible-art <world_path> floor
/world-bible-art <world_path> full
```

| Arg | Action |
|-----|--------|
| (none) | Resolve world folder, then `floor` |
| `floor` | Generate registry plates (4×3 + cover + anchor) |
| `full` | Floor, then one extra plate per remaining `place.*` / `person.*` |

## Run

Do only this pack. Do not edit world JSON except `art.json` paths and
`generated`. Do not start `/world-bible`.

Use each plate's `prompt` verbatim. Recurring subjects: canonical plate,
then `image_edit`. Restate fixed traits on every edit.

## Order (`floor`)

```
style anchor          image_gen
  → cover             image_edit from anchor (extra)
  → 3 signature       mixed ratios; in use
  → entry-face        image_gen on flat black, freeze
  → other people      first of each is gen on black
  → 3 scenes          image_edit from anchor when ratio matches
  → 3 props           image_edit from anchor when ratio matches
```

Different `aspect_ratio` than the anchor: `image_gen` with the same
prompt stem (edit preserves ratio). Parallelize only within one step.

Copy files onto `plates[].path`. Then set `art.json` `"generated": true`.

## Verify

Describe the image before re-reading ART.md. Fail if:

- it reads as a different school than `lock.look.school` (thumbnail test)
- it misses the school's Must, or shows a Forbidden tell
- a person plate has a full environment behind the figure
- it could be another world's city
- the entry face drifted
- in-image typography

One retry, then keep and flag.

```bash
{SKILL_ROOT}/scripts/validate.py <world-root> --images
```

**STOP** — `art-pack: accept`

`full` after floor accept only, if the author asked.
