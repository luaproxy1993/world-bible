# Changelog

## 1.9.0

- **Scale:** `lock.scale` is `seed` (20–40 min) or `sitting` (~3 hours, default). Sitting floors: places 10–16, people 8–12, factions 4–6, story_window 14–22 beats. A season is several sitting bibles.
- **Run loop:** do only `pipeline_state.step`. `accepted[]` is closed. At most three lock questions. Off-topic text does not change step. Next step waits for accept.
- **Art split:** W5 writes a registry (`generated: false`, caption+prompt). No `image_gen` in `/world-bible`. Pictures are `/world-bible-art`.
- **Schools:** each school has a thumbnail tell, Must, and Forbidden that includes the other schools. Look-dev uses three different schools, not three painters.

## 1.8.0

Public skill release.

- **Voice:** production manual. Complete sentences that chain facts.
- **Vignette:** a brief (what it is, who uses it, one dated proof of a Law).
- **Look:** `lock.look` judged from intake at W0.
- **Compile:** `overview.html` falls back to `lock.json` when world JSON is still empty.
