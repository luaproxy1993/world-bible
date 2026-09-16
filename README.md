# World Bible

Text-only stage document for a game world: temperament, scale, stage, timeline, written art look.

```text
/world-bible
/world-bible new <slug>
```

JSON in four folders is canonical. Default scale is **sitting** (~3 hours). No pictures.

Portraits, maps, and props:

```bash
npx skills add luaproxy1993/world-bible-pack -y
```

Then `/world-bible-pack`.

## Install

```bash
npx skills add luaproxy1993/world-bible -y
```

Update: same command, or `git -C ~/.grok/skills/world-bible pull`.

Current: **1.11.0**.

## New world

```bash
~/.grok/skills/world-bible/scripts/scaffold.sh my-slug ~/worlds
~/.grok/skills/world-bible/scripts/compile.sh ~/worlds/my-slug
```

Open `overview.html`.

## License

Skill text and scripts: use and modify. Homage extracts class, not copyrighted plot or names.
