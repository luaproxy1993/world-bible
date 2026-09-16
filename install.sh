#!/usr/bin/env bash
# Install world-bible into a coding-agent skills directory.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
FORCE=0
ALL=0
DEST=""

usage() {
  cat <<'EOF'
Usage: install.sh [OPTIONS]

Options:
  --dir PATH      Install destination
  --all-agents    Also copy to ~/.claude/skills, ~/.cursor/skills,
                  ~/.codex/skills, ~/.agents/skills
  --force         Overwrite
  -h, --help

Default: ~/.grok/skills/world-bible

  npx skills add <this-folder> -y
  npx skills add luaproxy1993/world-bible -y
EOF
}

while [ $# -gt 0 ]; do
  case "$1" in
    --dir) DEST="${2:?}"; shift 2 ;;
    --all-agents) ALL=1; shift ;;
    --force) FORCE=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage; exit 1 ;;
  esac
done

install_one() {
  local target="$1"
  case "$target" in
    "~/"*) target="$HOME/${target#~/}" ;;
  esac
  mkdir -p "$(dirname "$target")"
  if [ -e "$target" ] && [ "$FORCE" -ne 1 ]; then
    echo "skip existing $target  use --force to overwrite"
    return 0
  fi
  rm -rf "$target"
  mkdir -p "$target"
  rsync -a --exclude dist --exclude .git --exclude .DS_Store --exclude __pycache__ "$SCRIPT_DIR/" "$target/"
  chmod +x "$target/install.sh" "$target/scripts/"*.sh 2>/dev/null || true
  echo "installed -> $target"
}

install_art() {
  local parent="$1"
  local src="$SCRIPT_DIR/world-bible-art"
  [ -d "$src" ] || return 0
  local dest
  dest="$(dirname "$parent")/world-bible-art"
  if [ -e "$dest" ] && [ "$FORCE" -ne 1 ]; then
    echo "skip existing $dest  use --force to overwrite"
    return 0
  fi
  rm -rf "$dest"
  mkdir -p "$dest"
  rsync -a --exclude .git --exclude .DS_Store "$src/" "$dest/"
  echo "installed -> $dest"
}

if [ -n "$DEST" ]; then
  install_one "$DEST"
  install_art "$DEST"
else
  install_one "$HOME/.grok/skills/world-bible"
  install_art "$HOME/.grok/skills/world-bible"
fi

if [ "$ALL" -eq 1 ]; then
  install_one "$HOME/.claude/skills/world-bible"
  install_art "$HOME/.claude/skills/world-bible"
  install_one "$HOME/.cursor/skills/world-bible"
  install_art "$HOME/.cursor/skills/world-bible"
  install_one "$HOME/.codex/skills/world-bible"
  install_art "$HOME/.codex/skills/world-bible"
  install_one "$HOME/.agents/skills/world-bible"
  install_art "$HOME/.agents/skills/world-bible"
fi

VERSION="$(cat "$SCRIPT_DIR/VERSION" 2>/dev/null || echo unknown)"
echo ""
echo "world-bible v${VERSION}"
echo "In the agent: /world-bible"
echo "Pictures:     /world-bible-art"
echo "Update: npx skills add luaproxy1993/world-bible -y"
echo "        or git -C ~/.grok/skills/world-bible pull"
