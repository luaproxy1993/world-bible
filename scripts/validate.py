#!/usr/bin/env python3
"""Validate a world-bible folder: JSON, scale counts, 4×3 art registry."""
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
# Keep in sync with references/LOCK.md scale table.
SCALE = {
    "seed": {"places": (5, 8), "people": (4, 6), "factions": (3, 4), "window": (6, 10)},
    "sitting": {"places": (10, 16), "people": (8, 12), "factions": (4, 6), "window": (14, 22)},
}


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def count_range(errors: list[str], label: str, n: int, lo: int, hi: int) -> None:
    if n < lo or n > hi:
        errors.append(f"{label}: {n} not in {lo}–{hi}")


def main(root: Path, require_images: bool = False) -> int:
    errors: list[str] = []
    required = [
        root / "lock.json",
        root / "world" / "world.json",
        root / "stage" / "stage.json",
        root / "timeline" / "timeline.json",
        root / "art" / "art.json",
        root / "play-seeds.json",
    ]
    loaded: dict[str, dict] = {}
    for p in required:
        if not p.is_file():
            errors.append(f"missing {p.relative_to(root)}")
            continue
        try:
            loaded[str(p.relative_to(root))] = load(p)
        except json.JSONDecodeError as e:
            errors.append(f"invalid JSON {p.relative_to(root)}: {e}")

    lock = loaded.get("lock.json") or {}
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

    scale = (lock.get("scale") or "").strip()
    if scale and scale not in SCALE:
        errors.append(f"lock.scale {scale!r} not in {list(SCALE)}")
    elif scale:
        bounds = SCALE[scale]
        stage = loaded.get("stage/stage.json") or {}
        timeline = loaded.get("timeline/timeline.json") or {}
        count_range(errors, "places", len(stage.get("places") or []), *bounds["places"])
        count_range(errors, "people", len(stage.get("people") or []), *bounds["people"])
        count_range(errors, "factions", len(stage.get("factions") or []), *bounds["factions"])
        count_range(
            errors,
            "story_window",
            len(timeline.get("story_window") or []),
            *bounds["window"],
        )

    art_path = root / "art" / "art.json"
    if art_path.is_file() and "art/art.json" in loaded:
        art = loaded["art/art.json"]
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
        generated = art.get("generated")
        check_files = require_images or generated is True or generated is None
        for p in counted:
            rel = p.get("path") or ""
            cap = (p.get("caption") or "").strip()
            title = (p.get("title") or "").strip()
            prompt = (p.get("prompt") or "").strip()
            if not title:
                errors.append(f"{p.get('id')} missing title")
            if not cap:
                errors.append(f"{p.get('id')} missing caption")
            if generated is False and not prompt:
                errors.append(f"{p.get('id')} missing prompt")
            if check_files and rel and not (root / rel).is_file():
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
        print("usage: validate.py <world-root> [--images]", file=sys.stderr)
        sys.exit(1)
    root = Path(sys.argv[1]).expanduser().resolve()
    require_images = "--images" in sys.argv[2:]
    sys.exit(main(root, require_images=require_images))
