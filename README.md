# World Bible

A coding-agent skill that turns multimodal seeds into a modular game World Bible: temperament, stage, timeline, art plates. Downstream maker skills consume it.

```text
/world-bible
/world-bible new <slug>
```

JSON in four folders is canonical. `WORLD_BIBLE.md` and `overview.html` are compile-only.

Voice is a production manual: complete sentences, common words, the rule and the room. Not a diary. Not a fragment stack.

## Install

```bash
npx skills add luaproxy1993/world-bible -y
```

From a local clone:

```bash
npx skills add /absolute/path/to/world-bible -y
./install.sh --all-agents --force
```

## Update

```bash
npx skills add luaproxy1993/world-bible -y
```

If this folder is a git clone:

```bash
git -C ~/.grok/skills/world-bible pull
```

Check `VERSION` after update. Current: **1.8.0**.

## New world

```bash
~/.grok/skills/world-bible/scripts/scaffold.sh my-slug ~/worlds
```

Write `lock.json` before generating a single image. Compile:

```bash
~/.grok/skills/world-bible/scripts/compile.sh ~/worlds/my-slug
```

Open `overview.html`.

## License

Skill text and scripts: use and modify. Homage extracts class, not copyrighted plot or names.
