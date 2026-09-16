#!/usr/bin/env python3
"""Validate a world-bible folder: JSON, scale counts, written art look."""
from __future__ import annotations

import json
import sys
from pathlib import Path

# Keep in sync with references/ART.md schools.
SCHOOLS = ("oil-box", "glossy-photo", "cinematic-still", "cel", "print")
LOOK_SOURCES = ("author", "inferred")
# Keep in sync with references/LOCK.md scale table.
SCALE = {
    "seed": {
        "places": (5, 8), "people": (4, 6), "factions": (3, 4),
        "roles": (3, 5), "gear": (5, 8), "window": (6, 10),
    },
    "sitting": {
        "places": (10, 16), "people": (8, 12), "factions": (4, 6),
        "roles": (5, 8), "gear": (8, 16), "window": (14, 22),
    },
}


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def count_range(errors: list[str], label: str, n: int, lo: int, hi: int) -> None:
    if n < lo or n > hi:
        errors.append(f"{label}: {n} not in {lo}–{hi}")


def main(root: Path) -> int:
    errors: list[str] = []
    required = [
        root / "lock.json",
        root / "world" / "world.json",
        root / "stage" / "stage.json",
        root / "timeline" / "timeline.json",
        root / "art" / "art.json",
        root / "play-seeds.json",
        # play.json and kit.json are 2.0; old worlds may omit them
    ]
    optional = [
        root / "play" / "play.json",
        root / "kit" / "kit.json",
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

    for p in optional:
        if p.is_file():
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
        play = loaded.get("play/play.json")
        kit = loaded.get("kit/kit.json")
        if play is not None:
            count_range(errors, "roles", len(play.get("roles") or []), *bounds["roles"])
            conf = play.get("conflict") or {}
            for key in ("check", "fight", "fail"):
                if not (conf.get(key) or "").strip():
                    errors.append(f"play.conflict.{key} is empty")
            pwr = play.get("power") or {}
            for key in ("street", "hard", "rare"):
                if not (pwr.get(key) or "").strip():
                    errors.append(f"play.power.{key} is empty")
        if kit is not None:
            count_range(errors, "gear", len(kit.get("gear") or []), *bounds["gear"])

    if "art/art.json" in loaded:
        art = loaded["art/art.json"]
        if not (art.get("style_sentence") or "").strip():
            errors.append("art.style_sentence is empty")
        if not (art.get("medium") or "").strip():
            errors.append("art.medium is empty")
        if not (art.get("light") or "").strip():
            errors.append("art.light is empty")
        palette = art.get("palette") or []
        if len(palette) < 5:
            errors.append(f"art.palette {len(palette)} < 5")

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
