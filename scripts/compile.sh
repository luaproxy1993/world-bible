#!/usr/bin/env bash
# Assemble WORLD_BIBLE.md from the four JSON folders.
# Usage: compile.sh <world-root>
set -euo pipefail
SKILL_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ROOT="${1:?world-root required}"
ROOT="${ROOT/#\~/$HOME}"
python3 "$SKILL_ROOT/scripts/compile.py" "$ROOT"
