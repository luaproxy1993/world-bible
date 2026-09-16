# Install — world-bible v1.8.0

## The one command

```bash
npx skills add luaproxy1993/world-bible -y
```

Target specific agents:

```bash
npx skills add luaproxy1993/world-bible --agent claude-code --agent cursor -g -y
```

## Update

Same command. It overwrites the installed skill with the latest GitHub copy.

If you cloned the repo into `~/.grok/skills/world-bible`:

```bash
git -C ~/.grok/skills/world-bible pull
```

## Manual copy

```bash
./install.sh
./install.sh --all-agents --force
./install.sh --dir ~/.claude/skills/world-bible --force
```

| Agent | Typical path |
|-------|----------------|
| Grok | `~/.grok/skills/world-bible/` |
| Claude Code | `~/.claude/skills/world-bible/` |
| Cursor | `~/.cursor/skills/world-bible/` |
| Codex | `~/.codex/skills/` |

## Verify

```bash
test -f ~/.grok/skills/world-bible/SKILL.md && echo grok-ok
cat ~/.grok/skills/world-bible/VERSION
```

Then in the agent: `/world-bible`.
