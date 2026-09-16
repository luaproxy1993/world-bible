#!/usr/bin/env bash
# Scaffold a world-bible folder (core rule book JSON).
# Usage: scaffold.sh <slug> [parent_dir]
set -euo pipefail
SKILL_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SLUG="${1:?slug required (lowercase-hyphen)}"
PARENT="${2:-.}"
PARENT="${PARENT/#\~/$HOME}"
DEST="$PARENT/$SLUG"

if [[ -e "$DEST" ]]; then
  echo "ERROR: $DEST already exists" >&2
  exit 1
fi

mkdir -p "$DEST"/{world,play,stage,kit,timeline,art,source,pack}
rsync -a "$SKILL_ROOT/templates/" "$DEST/"

if command -v sed >/dev/null; then
  find "$DEST" -type f \( -name '*.json' -o -name '*.md' \) \
    -exec sed -i.bak "s/{{SLUG}}/$SLUG/g" {} +
  find "$DEST" -name '*.bak' -delete
fi

echo "Scaffolded $DEST"
echo "Next: write lock.json, then /core-rule-book lock"
echo "Validate: $SKILL_ROOT/scripts/validate.py $DEST"
echo "Compile:  $SKILL_ROOT/scripts/compile.sh $DEST"
