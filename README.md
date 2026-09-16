# Core Rule Book

A **TRPG core rule book** in text. Baldur's Gate 1, 2, and 3 sit on one
D&D core book; this folder is that book. Not a campaign. Not pictures.
Old name: World Bible.

```text
/core-rule-book
/core-rule-book new <slug>
```

JSON is canonical. Default scale is **core** — thick enough that three
later authors can each cut a different job. No pictures in this skill.

Production line:

1. `/core-rule-book` — the core book (this skill). Stops at compile.
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

Current: **3.1.0**. Slash command: `/core-rule-book` (`/world-bible` still works).

## New world

```bash
~/.grok/skills/world-bible/scripts/scaffold.sh my-slug ~/worlds
~/.grok/skills/world-bible/scripts/compile.sh ~/worlds/my-slug
```

Open `overview.html`.

## License

Skill text and scripts: use and modify. Homage extracts class, not copyrighted plot or names.
