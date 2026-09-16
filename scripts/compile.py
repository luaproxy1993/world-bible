#!/usr/bin/env python3
"""Compile WORLD_BIBLE.md and overview.html from JSON folders."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from html_overview import write_overview


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def vignette_md(v: dict) -> str:
    rel = " ".join(f"`{r}`" for r in (v.get("relations") or []))
    lines = [
        f"### {v.get('title') or v.get('name') or v.get('id')}",
        "",
        v.get("body") or "",
        "",
        f"- **Residue:** {v.get('residue') or ''}",
        f"- **Relations:** {rel}",
        f"- **Play hook:** {v.get('play_hook') or ''}",
        "",
    ]
    return "\n".join(lines)


def event_row(e: dict) -> str:
    rel = " ".join(f"`{r}`" for r in (e.get("relations") or []))
    return f"| {e.get('when', '')} | {e.get('title', '')} | {e.get('residue', '')} | {rel} |"


def main(root: Path) -> None:
    lock = load(root / "lock.json")
    world = load(root / "world" / "world.json")
    stage = load(root / "stage" / "stage.json")
    timeline = load(root / "timeline" / "timeline.json")
    art = load(root / "art" / "art.json")
    seeds = load(root / "play-seeds.json")

    title = world.get("title") or lock.get("title") or root.name
    slug = world.get("slug") or lock.get("slug") or root.name
    t = world.get("temperament") or {}
    feelings = t.get("feelings") or []
    if not (t.get("about") or any(
        (f.get("name") if isinstance(f, dict) else f) for f in feelings
    )):
        t = lock.get("temperament") or {}
        feelings = t.get("feelings") or []

    out: list[str] = [
        "<!-- compiled from JSON folders — edit JSON, then world-bible/scripts/compile.sh -->",
        "",
        f"# {title} · World Bible",
        "",
        f"> slug `{slug}` · regenerate this file; do not hand-edit",
        "",
        "## 1 · World",
        "",
        f"**About:** {t.get('about', '')}",
        "",
        "### Temperament",
        "",
    ]
    for f in feelings:
        if isinstance(f, dict):
            out.append(f"- **{f.get('name', '')}** — {f.get('lived', '')}")
        else:
            out.append(f"- {f}")
    uniqueness = (world.get("uniqueness") or "").strip() or (t.get("about") or "")
    out += ["", "### Uniqueness", "", uniqueness, ""]
    win = world.get("window") or {}
    if not any(win.get(k) for k in ("era", "start", "playable_present", "stop")):
        win = lock.get("story_window") or {}
    out += [
        "### Window",
        "",
        f"- era: {win.get('era', '')}",
        f"- start: {win.get('start', '')}",
        f"- present: {win.get('playable_present', '')}",
        f"- stop: {win.get('stop', '')}",
        "",
        "### Laws",
        "",
    ]
    for i, law in enumerate(world.get("laws") or [], 1):
        text = law.get("text") if isinstance(law, dict) else str(law)
        out.append(f"{i}. {text}")
    everyday = world.get("everyday") or {}
    out += ["", "### Everyday", ""]
    for k in ("eat", "pay", "move", "sleep", "die", "news"):
        if everyday.get(k):
            out.append(f"- **{k}:** {everyday[k]}")
    sig = world.get("signature") or {}
    if not (sig.get("body") or sig.get("title")):
        ls = lock.get("signature") or {}
        if ls.get("working_name") or ls.get("everyday"):
            sig = {
                "title": ls.get("working_name") or "",
                "body": ls.get("everyday") or "",
                "play_hook": ls.get("play") or "",
                "residue": "",
            }
    out += ["", "### Signature", "", vignette_md(sig) if sig else ""]

    out += ["---", "", "## 2 · Stage", "", "### Places", ""]
    for v in stage.get("places") or []:
        out.append(vignette_md(v))
    out += ["### People", ""]
    for v in stage.get("people") or []:
        out.append(vignette_md(v))
    out += ["### Factions", ""]
    for v in stage.get("factions") or []:
        out.append(vignette_md(v))
    out += ["### Institutions", ""]
    for v in stage.get("institutions") or []:
        out.append(vignette_md(v))

    out += [
        "---",
        "",
        "## 3 · Timeline",
        "",
        f"Shape: `{timeline.get('shape', '')}`",
        "",
        "### World-key",
        "",
        "| When | Event | Residue | Ids |",
        "|------|-------|---------|-----|",
    ]
    for e in timeline.get("world_key") or []:
        out.append(event_row(e))
    out += ["", "### Story window", "", "| When | Event | Residue | Ids |", "|------|-------|---------|-----|"]
    for e in timeline.get("story_window") or []:
        out.append(event_row(e))
    out.append("")
    for e in (timeline.get("world_key") or []) + (timeline.get("story_window") or []):
        if e.get("body"):
            out += [f"#### {e.get('id')}", "", e["body"], ""]

    look = lock.get("look") or {}
    look_line = ""
    if look.get("school"):
        named = look.get("named_as") or ""
        src = look.get("source") or ""
        bits = [str(look.get("school"))]
        if named:
            bits.append(named)
        if src:
            bits.append(src)
        look_line = f"**Look:** {' · '.join(bits)}"
        if look.get("why"):
            look_line += f"\n**Look why:** {look['why']}"

    art_head = [
        "---",
        "",
        "## 4 · Art",
        "",
    ]
    if look_line:
        art_head += [look_line, ""]
    art_head += [
        f"**Style:** {art.get('style_sentence', '')}",
        f"**Medium:** {art.get('medium', '')}",
        "",
        "| id | kind | ratio | title | path |",
        "|----|------|-------|-------|------|",
    ]
    out += art_head
    for p in art.get("plates") or []:
        out.append(
            f"| `{p.get('id', '')}` | {p.get('kind', '')} | {p.get('aspect_ratio', '')} | {p.get('title', '')} | `{p.get('path', '')}` |"
        )
    out.append("")
    for p in art.get("plates") or []:
        if p.get("caption"):
            out += [f"### {p.get('title') or p.get('id')}", "", p["caption"], ""]

    doki = seeds.get("doki") or {}
    out += [
        "---",
        "",
        "## Play-seeds",
        "",
        f"**FMV:** {seeds.get('fmv', '')}",
        "",
        f"**RPG:** {seeds.get('rpg', '')}",
        "",
        f"**TCG:** {seeds.get('tcg', '')}",
        "",
        f"**Doki:** {doki.get('tagline', '')} · {doki.get('three_minute_accept', '')}",
        "",
    ]

    dest = root / "WORLD_BIBLE.md"
    dest.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {dest}")
    html_path = write_overview(root)
    print(f"Wrote {html_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: compile.py <world-root>", file=sys.stderr)
        sys.exit(1)
    main(Path(sys.argv[1]).expanduser().resolve())
