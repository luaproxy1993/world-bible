# Lock template

Write `lock.json` at the world root. Empty fields mean the world is not locked.

`audience` defaults to North America / Europe. `language` defaults to `en`.

**Look** is the paint school. Judge it from intake at W0. Schools, medium stems, and look-dev live in `ART.md`. Copy `school` from that list.

- `source`: `author` when the brief named a look (a painter, a show, "box art", "dating-show glossy", a film still). `inferred` when you chose from temperament.
- Default `school` is `oil-box` only when intake has no stronger signal.
- `why` is one sentence a stranger could quote.
- `forbidden` starts from the school's row in `ART.md`, then add what this world must not look like.
- `named_as` is optional: a painter, a show, or a print tradition inside the school.

```json
{
  "schema": "doki.world-bible.lock",
  "version": "1.2.0",
  "slug": "",
  "title": "",
  "language": "en",
  "audience": "North America / Europe",
  "intake": "original",
  "ip": "original",
  "homage_source": "n/a",
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
