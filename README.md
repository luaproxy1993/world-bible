# World Bible

A **TRPG core rule book** in text. Baldur's Gate 1, 2, and 3 sit on one
D&D core book; this folder is that book. Not a campaign. Not pictures.

```text
/world-bible
/world-bible new <slug>
```

JSON is canonical. Default scale is **core** — thick enough that three
later authors can each cut a different job. No pictures in this skill.

Production line:

1. `/world-bible` — the core book (this skill). Stops at compile.
2. `/world-bible-pack` — portraits, map, places, props. Later session.
3. `/rpg-campaign-maker` — one job from the box. Later session.

```bash
npx skills add luaproxy1993/world-bible -y
npx skills add luaproxy1993/world-bible-pack -y
```

## Install

```bash
npx skills add luaproxy1993/world-bible -y
```

Update: same command, or `git -C ~/.grok/skills/world-bible pull`.

Current: **3.0.0**.

## New world

```bash
~/.grok/skills/world-bible/scripts/scaffold.sh my-slug ~/worlds
~/.grok/skills/world-bible/scripts/compile.sh ~/worlds/my-slug
```

Open `overview.html`.

## License

Skill text and scripts: use and modify. Homage extracts class, not copyrighted plot or names.
