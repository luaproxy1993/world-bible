# Lock template

Write `lock.json` at the world root. Empty fields mean the world is not locked.

`audience` defaults to North America / Europe. `language` defaults to `en`.
`scale` defaults to `sitting` (~3 hours of play).

## Scale (volume)

One bible covers one scale. A season is several sitting bibles, not one fat folder.

| `scale` | Play time | places | people | factions | roles | gear | window beats |
|---------|-----------|--------|--------|----------|-------|------|--------------|
| `seed` | 20–40 min | 5–8 | 4–6 | 3–4 | 3–5 | 5–8 | 6–10 |
| `sitting` | ~3 hours | 10–16 | 8–12 | 4–6 | 5–8 | 8–16 | 14–22 |

This file is a **core rule book**: toys to run a job. It is not a campaign.
A campaign is a later pack (`/rpg-campaign-maker`) that picks toys from this box.

Counts are inclusive. `world_key` is older facts that still mark today. The
playable stretch hangs on `story_window`. Briefs stay briefs; volume is more
toys, not longer essays.

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
  "version": "1.3.0",
  "slug": "",
  "title": "",
  "language": "en",
  "audience": "North America / Europe",
  "intake": "original",
  "ip": "original",
  "homage_source": "n/a",
  "scale": "sitting",
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
