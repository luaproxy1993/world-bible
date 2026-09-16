# Production line

This skill writes the **core rule book** and stops. Later skills read it.
They do not start from this session unless the author named that skill
in this turn.

Baldur's Gate 1, 2, and 3 sit on one D&D core book. Each generation's
authors cut a new story from that shared box. The core book is not a
Baldur's Gate campaign. This folder is that box.

```text
intake
  → /core-rule-book           CRB. Text only. Stops at W6.
       │
       ├─ /world-bible-pack         pictures (portraits, map, places, props)
       ├─ /rpg-campaign-maker       one job: one site, one clock, one fork
       ├─ game-maker-pipeline       systems, numbers, whitebox
       └─ later NPC / quest packs   faces and jobs pulled from the box
```

Each arrow is a **new session**. This skill does not call Imagine, does
not write `pack/`, and does not write a campaign tree.

## What this folder is

A core rule book: world today, who you can be, how a check and a fight
work here, wages and prices, who can hurt you, famous faces, places,
gear, a timeline, and a written look. Raw material. Not a plotted sitting.

## What later skills consume

| Later skill | Reads | Writes |
|-------------|-------|--------|
| `/world-bible-pack` | `lock.look` + `art/` + stage people/places + signature | `{WORLD}/pack/` pictures |
| `/rpg-campaign-maker` | lock window, one site, Laws, people on stage this sitting | a campaign folder with a tree |
| `game-maker-pipeline` | temperament, look, signature, spatial logic | Design Bible / GDD candidates |
| doki / galgame makers | entry face, laws, places | pack or worldbook |

They copy or cite. Canonical JSON stays in this folder.

## After W6

Print the next-skill names. **STOP.** Start one of them only when the
author asked in this turn.

Pictures → `/world-bible-pack`
A plotted job → `/rpg-campaign-maker`
Numbers / whitebox → `game-maker-pipeline`

## Three-games test

A core book is thick enough that three later authors could each cut a
different job without inventing a new city, a new law, or a new unique
thing. `play-seeds.json` `jobs[]` is that proof. A single plotted hook
means this folder is a campaign draft. Rewrite the box, not the job.
