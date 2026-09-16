#!/usr/bin/env python3
"""Validate a world-bible folder: four JSON files, 4×3 art floor, mixed ratios."""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

KINDS = ("scene", "person", "prop", "signature")
MIN_PER = 3
MIN_RATIOS = 4
# Keep in sync with references/ART.md schools.
SCHOOLS = ("oil-box", "glossy-photo", "cinematic-still", "cel", "print")
LOOK_SOURCES = ("author", "inferred")


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def main(root: Path) -> int:
    errors: list[str] = []
    required = [
        root / "lock.json",
        root / "world" / "world.json",
        root / "stage" / "stage.json",
        root / "timeline" / "timeline.json",
        root / "art" / "art.json",
        root / "play-seeds.json",
    ]
    for p in required:
        if not p.is_file():
            errors.append(f"missing {p.relative_to(root)}")
            continue
        try:
            load(p)
        except json.JSONDecodeError as e:
            errors.append(f"invalid JSON {p.relative_to(root)}: {e}")

    lock_path = root / "lock.json"
    if lock_path.is_file():
        try:
            lock = load(lock_path)
        except json.JSONDecodeError:
            lock = {}
        look = lock.get("look") or {}
        if look:
            school = (look.get("school") or "").strip()
            why = (look.get("why") or "").strip()
            source = (look.get("source") or "").strip()
            if not school:
                errors.append("lock.look.school is empty")
            elif school not in SCHOOLS:
                errors.append(f"lock.look.school {school!r} not in {list(SCHOOLS)}")
            if not why:
                errors.append("lock.look.why is empty")
            if source and source not in LOOK_SOURCES:
                errors.append(f"lock.look.source {source!r} not in {list(LOOK_SOURCES)}")

    art_path = root / "art" / "art.json"
    if art_path.is_file():
        art = load(art_path)
        plates = art.get("plates") or []
        counted = [p for p in plates if p.get("kind") in KINDS]
        anchors = [p for p in plates if p.get("kind") == "anchor"]
        if len(anchors) > 1:
            errors.append(f"kind:anchor {len(anchors)} > 1 (one canonical style-anchor)")
        kinds = Counter(p.get("kind") for p in counted)
        for k in KINDS:
            n = kinds.get(k, 0)
            if n < MIN_PER:
                errors.append(f"art kind {k}: {n} < {MIN_PER}")
        if len(counted) < 12:
            errors.append(f"counted plates {len(counted)} < 12")
        ratios = {p.get("aspect_ratio") for p in counted if p.get("aspect_ratio")}
        if len(ratios) < MIN_RATIOS:
            errors.append(f"distinct aspect_ratio {sorted(ratios)} < {MIN_RATIOS}")
        for p in counted:
            rel = p.get("path") or ""
            cap = (p.get("caption") or "").strip()
            title = (p.get("title") or "").strip()
            if not title:
                errors.append(f"{p.get('id')} missing title")
            if not cap:
                errors.append(f"{p.get('id')} missing caption")
            if rel and not (root / rel).is_file():
                errors.append(f"{p.get('id')} file missing: {rel}")

    if errors:
        print("FAIL")
        for e in errors:
            print(f"  - {e}")
        return 2
    print("OK")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: validate.py <world-root>", file=sys.stderr)
        sys.exit(1)
    sys.exit(main(Path(sys.argv[1]).expanduser().resolve()))
