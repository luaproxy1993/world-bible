#!/usr/bin/env python3
"""Validate a world-bible folder: JSON, scale counts, written art look, ids."""
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
        "places": (5, 8),
        "people": (4, 6),
        "factions": (3, 4),
        "institutions": (1, 3),
        "roles": (3, 5),
        "gear": (5, 8),
        "opposition": (3, 4),
        "window": (6, 10),
        "jobs": (1, 1),
        "motif": (2, 4),
        "subjects": (4, 40),
    },
    "sitting": {
        "places": (10, 16),
        "people": (8, 12),
        "factions": (4, 6),
        "institutions": (2, 4),
        "roles": (5, 8),
        "gear": (8, 16),
        "opposition": (4, 6),
        "window": (14, 22),
        "jobs": (2, 3),
        "motif": (3, 5),
        "subjects": (8, 60),
    },
    "core": {
        "places": (16, 24),
        "people": (16, 24),
        "factions": (6, 10),
        "institutions": (4, 8),
        "roles": (6, 10),
        "gear": (16, 24),
        "opposition": (8, 12),
        "window": (18, 30),
        "jobs": (3, 5),
        "motif": (3, 6),
        "subjects": (12, 80),
    },
}
ECONOMY_KEYS = ("currency", "street_wage", "skilled_wage", "bread", "room", "fine")
CALENDAR_KEYS = ("day", "week", "clock", "curfew")
TRAVEL_KEYS = ("how", "times", "stop")
CONFLICT_KEYS = ("check", "fight", "fail")
POWER_KEYS = ("street", "hard", "rare")
# Relation prefixes this book mints. Unknown prefixes (old `law.*` without ids) are ignored.
MINTED_PREFIXES = (
    "place", "person", "faction", "institution", "signature", "event",
    "role", "gear", "opposition", "job", "law",
)


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def count_range(errors: list[str], label: str, n: int, lo: int, hi: int) -> None:
    if n < lo or n > hi:
        errors.append(f"{label}: {n} not in {lo}–{hi}")


def filled(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, dict):
        return any(filled(v) for v in value.values())
    if isinstance(value, list):
        return len(value) > 0
    return True


def collect_ids(loaded: dict[str, dict]) -> set[str]:
    ids: set[str] = set()

    def add_list(items: object) -> None:
        for item in items or []:
            if isinstance(item, dict) and item.get("id"):
                ids.add(str(item["id"]))

    world = loaded.get("world/world.json") or {}
    sig = world.get("signature") or {}
    if isinstance(sig, dict) and sig.get("id"):
        ids.add(str(sig["id"]))
    add_list(world.get("laws"))

    stage = loaded.get("stage/stage.json") or {}
    for key in ("places", "people", "factions", "institutions"):
        add_list(stage.get(key))

    play = loaded.get("play/play.json") or {}
    add_list(play.get("roles"))
    add_list(play.get("opposition"))

    kit = loaded.get("kit/kit.json") or {}
    add_list(kit.get("gear"))

    timeline = loaded.get("timeline/timeline.json") or {}
    add_list(timeline.get("world_key"))
    add_list(timeline.get("story_window"))

    seeds = loaded.get("play-seeds.json") or {}
    add_list(seeds.get("jobs"))

    art = loaded.get("art/art.json") or {}
    add_list(art.get("subjects"))
    return ids


def prefix_of(token: str) -> str:
    return token.split(".", 1)[0] if "." in token else ""


def missing_id(token: str, ids: set[str]) -> bool:
    if not token or token in ids:
        return False
    pre = prefix_of(token)
    minted = {prefix_of(i) for i in ids}
    return pre in MINTED_PREFIXES and pre in minted


def check_relations(errors: list[str], items: object, ids: set[str], label: str) -> None:
    for item in items or []:
        if not isinstance(item, dict):
            continue
        iid = item.get("id") or "?"
        for rel in item.get("relations") or []:
            if missing_id(rel, ids):
                errors.append(f"{label} `{iid}` relation `{rel}` is not an id in this book")
        for rel in item.get("cast") or []:
            if missing_id(rel, ids):
                errors.append(f"{label} `{iid}` cast `{rel}` is not an id in this book")
        site = item.get("site")
        if missing_id(site or "", ids):
            errors.append(f"{label} `{iid}` site `{site}` is not an id in this book")
        subject_id = item.get("subject_id")
        if missing_id(subject_id or "", ids):
            errors.append(f"{label} `{iid}` subject_id `{subject_id}` is not an id in this book")


def require_map(errors: list[str], obj: dict, keys: tuple[str, ...], prefix: str) -> None:
    for key in keys:
        if not filled((obj or {}).get(key)):
            errors.append(f"{prefix}.{key} is empty")


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

    thick = scale == "core"
    if thick:
        if "play/play.json" not in loaded:
            errors.append("missing play/play.json (required at scale core)")
        if "kit/kit.json" not in loaded:
            errors.append("missing kit/kit.json (required at scale core)")

    if scale in SCALE:
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
        if thick or (stage.get("institutions") or []):
            count_range(
                errors,
                "institutions",
                len(stage.get("institutions") or []),
                *bounds["institutions"],
            )

        play = loaded.get("play/play.json")
        kit = loaded.get("kit/kit.json")
        if play is not None:
            count_range(errors, "roles", len(play.get("roles") or []), *bounds["roles"])
            conf = play.get("conflict") or {}
            for key in CONFLICT_KEYS:
                if not filled(conf.get(key)):
                    errors.append(f"play.conflict.{key} is empty")
            pwr = play.get("power") or {}
            for key in POWER_KEYS:
                if not filled(pwr.get(key)):
                    errors.append(f"play.power.{key} is empty")
            if thick or (play.get("opposition") or []):
                count_range(
                    errors,
                    "opposition",
                    len(play.get("opposition") or []),
                    *bounds["opposition"],
                )
            if thick:
                require_map(errors, play.get("economy") or {}, ECONOMY_KEYS, "play.economy")
        if kit is not None:
            count_range(errors, "gear", len(kit.get("gear") or []), *bounds["gear"])

        world = loaded.get("world/world.json") or {}
        if thick:
            if not filled(world.get("uniqueness")):
                errors.append("world.uniqueness is empty")
            n_laws = len(world.get("laws") or [])
            if n_laws < 5 or n_laws > 9:
                errors.append(f"laws: {n_laws} not in 5–9")
            for i, law in enumerate(world.get("laws") or []):
                if not isinstance(law, dict):
                    errors.append(f"laws[{i}] must be an object with id and text")
                    continue
                if not filled(law.get("id")):
                    errors.append(f"laws[{i}].id is empty")
                elif not str(law.get("id")).startswith("law."):
                    errors.append(f"laws[{i}].id {law.get('id')!r} must start with law.")
                if not filled(law.get("text")):
                    errors.append(f"laws[{i}].text is empty")
            require_map(
                errors,
                world.get("everyday") or {},
                ("eat", "pay", "move", "sleep", "die", "news"),
                "world.everyday",
            )
            require_map(errors, world.get("calendar") or {}, CALENDAR_KEYS, "world.calendar")
            require_map(errors, world.get("travel") or {}, TRAVEL_KEYS, "world.travel")

        seeds = loaded.get("play-seeds.json") or {}
        jobs = seeds.get("jobs") or []
        if thick or jobs:
            count_range(errors, "jobs", len(jobs), *bounds["jobs"])
            sites = [j.get("site") for j in jobs if isinstance(j, dict) and j.get("site")]
            if thick and len(set(sites)) < min(3, bounds["jobs"][0]):
                errors.append(
                    f"jobs must use {min(3, bounds['jobs'][0])} different site ids; got {len(set(sites))}"
                )
            for i, job in enumerate(jobs):
                if not isinstance(job, dict):
                    continue
                for key in ("id", "title", "site", "clock", "fork", "body"):
                    if not filled(job.get(key)):
                        errors.append(f"jobs[{i}].{key} is empty")

        art = loaded.get("art/art.json") or {}
        if thick:
            if not filled(art.get("crowd")):
                errors.append("art.crowd is empty")
            if not filled(art.get("wardrobe")):
                errors.append("art.wardrobe is empty")
            if not filled(art.get("buildings")):
                errors.append("art.buildings is empty")
            count_range(errors, "art.motif", len(art.get("motif") or []), *bounds["motif"])
            count_range(
                errors,
                "art.subjects",
                len(art.get("subjects") or []),
                *bounds["subjects"],
            )
            for i, sub in enumerate(art.get("subjects") or []):
                if not isinstance(sub, dict):
                    continue
                if not filled(sub.get("subject_id")):
                    errors.append(f"art.subjects[{i}].subject_id is empty")
                if not filled(sub.get("caption")):
                    errors.append(f"art.subjects[{i}].caption is empty")

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

    ids = collect_ids(loaded)
    world = loaded.get("world/world.json") or {}
    entry = world.get("entry_face")
    if entry and entry not in ids:
        errors.append(f"world.entry_face `{entry}` is not an id in this book")
    sig_id = world.get("signature_id")
    if sig_id and sig_id not in ids:
        errors.append(f"world.signature_id `{sig_id}` is not an id in this book")
    if isinstance(world.get("signature"), dict):
        check_relations(errors, [world["signature"]], ids, "signature")

    stage = loaded.get("stage/stage.json") or {}
    for key in ("places", "people", "factions", "institutions"):
        check_relations(errors, stage.get(key), ids, key)

    play = loaded.get("play/play.json") or {}
    check_relations(errors, play.get("roles"), ids, "roles")
    check_relations(errors, play.get("opposition"), ids, "opposition")

    kit = loaded.get("kit/kit.json") or {}
    check_relations(errors, kit.get("gear"), ids, "gear")

    timeline = loaded.get("timeline/timeline.json") or {}
    check_relations(errors, timeline.get("world_key"), ids, "world_key")
    check_relations(errors, timeline.get("story_window"), ids, "story_window")

    seeds = loaded.get("play-seeds.json") or {}
    check_relations(errors, seeds.get("jobs"), ids, "jobs")

    art = loaded.get("art/art.json") or {}
    check_relations(errors, art.get("subjects"), ids, "subjects")

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
