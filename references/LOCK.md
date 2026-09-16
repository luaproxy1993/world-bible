# Lock template

Write `lock.json` at the world root. Empty fields mean the world is not locked.

`audience` defaults to North America / Europe. `language` defaults to `en`.
`scale` defaults to **`core`** — a core rule book, thick enough for later
jobs. `sitting` is one district. `seed` is a pitch.

## Scale (volume)

One folder is one scale. A season of play is several **jobs** cut from one
core book, not several thin bibles. Validate.py keeps this table.

| `scale` | What it is | places | people | factions | institutions | roles | gear | opposition | window | jobs | motif | subjects |
|---------|------------|--------|--------|----------|--------------|-------|------|------------|--------|------|-------|----------|
| `seed` | pitch | 5–8 | 4–6 | 3–4 | 1–3 | 3–5 | 5–8 | 3–4 | 6–10 | 1 | 2–4 | 4+ |
| `sitting` | one district | 10–16 | 8–12 | 4–6 | 2–4 | 5–8 | 8–16 | 4–6 | 14–22 | 2–3 | 3–5 | 8+ |
| `core` | **default.** Shared box for later campaigns | 16–24 | 16–24 | 6–10 | 4–8 | 6–10 | 16–24 | 8–12 | 18–30 | 3–5 | 3–6 | 12+ |

This file is a **core rule book**: toys to run many jobs. It is not a campaign.
A campaign is a later session (`/rpg-campaign-maker`) that picks toys from this box.

Counts are inclusive. `world_key` is older facts that still mark today. The
playable stretch hangs on `story_window`. Briefs stay briefs; volume is more
toys and filled slots, not longer essays.

## Look

Paint school from intake at W0. Schools, stems, and contrast live in `ART.md`. Copy `school` from that list.

- `source`: `author` when the brief named a look. `inferred` when you chose from temperament.
- Default `school` is `oil-box` only when intake has no stronger signal.
- `why` is one sentence a stranger could quote.
- `forbidden` starts from the school's row in `ART.md`, then add what this world must not look like.
- `named_as` is optional: a painter, a show, or a print tradition inside the school.

```json
{
  "schema": "doki.world-bible.lock",
  "version": "1.4.0",
  "slug": "",
  "title": "",
  "language": "en",
  "audience": "North America / Europe",
  "intake": "original",
  "ip": "original",
  "homage_source": "n/a",
  "scale": "core",
  "temperament": {
    "feelings": [
      {"name": "", "lived": ""},
      {"name": "", "lived": ""},
      {"name": "", "lived": ""}
    ],
    "about": "This world is about"
  },
  "story_window": {
    "era": "",
    "start": "",
    "playable_present": "",
    "stop": ""
  },
  "signature": {
    "working_name": "",
    "everyday": "",
    "play": ""
  },
  "look": {
    "school": "oil-box",
    "named_as": "",
    "why": "",
    "forbidden": [],
    "source": "inferred"
  },
  "timeline_shape": "linear",
  "worldlines": [{"id": "prime", "name": "", "status": "canonical"}],
  "target_forms": [],
  "intake_pointers": ["source/"]
}
```
