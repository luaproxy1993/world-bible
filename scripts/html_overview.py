#!/usr/bin/env python3
"""Build overview.html from the four JSON folders."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def e(s) -> str:
    return html.escape("" if s is None else str(s), quote=True)


def hex_lum(hx: str) -> float:
    h = hx.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        return 0.5
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255


def palette_css(art: dict) -> str:
    raw = [p for p in (art.get("palette") or []) if p.get("hex")]
    by_name = {str(p.get("name") or ""): p["hex"] for p in raw}
    sorted_p = sorted(raw, key=lambda p: hex_lum(p["hex"]))
    darkest = sorted_p[0]["hex"] if sorted_p else "#1c1814"
    lightest = sorted_p[-1]["hex"] if sorted_p else "#f4eee4"
    mid = sorted_p[len(sorted_p) // 2]["hex"] if sorted_p else "#7a7368"
    accent = (
        by_name.get("红点")
        or by_name.get("rec")
        or next((p["hex"] for p in raw if hex_lum(p["hex"]) < 0.45), None)
        or "#c41e3a"
    )
    gold = by_name.get("黄金时") or by_name.get("gold") or mid
    paper = by_name.get("盐白") or by_name.get("paper") or lightest
    if hex_lum(paper) < 0.6:
        paper = "#f4eee4"
    return (
        f"--paper:{paper};--ink:{darkest};--mute:{mid};"
        f"--accent:{accent};--gold:{gold};"
    )


def ar_class(ratio: str) -> str:
    r = (ratio or "").strip().replace(":", "-")
    return f"ar-{r}" if r else "ar-16-9"


def labels(lang: str) -> dict:
    zh = (lang or "zh").lower().startswith("zh")
    if zh:
        return {
            "kicker": "World Bible",
            "nav": ["世界", "舞台", "时间线", "美术"],
            "feelings": "气质",
            "world": "整体世界",
            "stage": "地点与人物",
            "timeline": "大事件时间线",
            "art": "美术设定",
            "laws": "律令",
            "everyday": "日常",
            "signature": "Signature",
            "places": "地点",
            "people": "人物",
            "factions": "势力",
            "institutions": "制度",
            "world_key": "世界残响",
            "story": "故事窗口",
            "residue": "残响",
            "hook": "可玩钩",
            "seeds": "Play-seeds",
            "eat": "吃",
            "pay": "付",
            "move": "走",
            "sleep": "睡",
            "die": "死",
            "news": "消息",
            "era": "时代",
            "start": "起",
            "present": "现在",
            "stop": "止",
            "style": "风格句",
            "light": "光",
            "medium": "媒介",
            "look": "画派",
            "look_why": "画派理由",
            "foot": "compiled from JSON · do not hand-edit",
        }
    return {
        "kicker": "World Bible",
        "nav": ["World", "Stage", "Timeline", "Art"],
        "feelings": "Temperament",
        "world": "World",
        "stage": "Stage",
        "timeline": "Timeline",
        "art": "Art",
        "laws": "Laws",
        "everyday": "Everyday",
        "signature": "Signature",
        "places": "Places",
        "people": "People",
        "factions": "Factions",
        "institutions": "Institutions",
        "world_key": "World-key",
        "story": "Story window",
        "residue": "Residue",
        "hook": "Play hook",
        "seeds": "Play-seeds",
        "eat": "Eat",
        "pay": "Pay",
        "move": "Move",
        "sleep": "Sleep",
        "die": "Die",
        "news": "News",
        "era": "Era",
        "start": "Start",
        "present": "Present",
        "stop": "Stop",
        "style": "Style",
        "light": "Light",
        "medium": "Medium",
        "look": "Look",
        "look_why": "Look why",
        "foot": "compiled from JSON · do not hand-edit",
    }


def vignette_html(v: dict, L: dict) -> str:
    body = e(v.get("body") or "")
    return f"""<article class="vignette" id="{e(v.get('id') or '')}">
  <h3>{e(v.get('title') or v.get('id'))}</h3>
  <p class="body">{body}</p>
  <div class="foot"><span><b>{e(L['residue'])}</b> {e(v.get('residue') or '')}</span>
  <span><b>{e(L['hook'])}</b> {e(v.get('play_hook') or '')}</span></div>
</article>"""


def plates_html(plates: list, kinds: tuple[str, ...] | None = None) -> str:
    bits = ['<div class="plates">']
    for p in plates:
        if kinds and p.get("kind") not in kinds:
            continue
        path = p.get("path") or ""
        if not path:
            continue
        ar = p.get("aspect_ratio") or "16:9"
        bits.append(
            f"""<figure class="plate {ar_class(ar)}" data-ar="{e(ar)}">
  <div class="kind-tag">{e(p.get('kind') or '')} · {e(ar)}</div>
  <img src="{e(path)}" alt="{e(p.get('title') or '')}">
  <figcaption><strong>{e(p.get('title') or '')}</strong>{e(p.get('caption') or '')}</figcaption>
</figure>"""
        )
    bits.append("</div>")
    return "\n".join(bits)


def write_overview(root: Path) -> Path:
    css_path = Path(__file__).resolve().parent / "overview.css"
    css = css_path.read_text(encoding="utf-8")
    lock = load(root / "lock.json")
    world = load(root / "world" / "world.json")
    stage = load(root / "stage" / "stage.json")
    timeline = load(root / "timeline" / "timeline.json")
    art = load(root / "art" / "art.json")
    seeds = load(root / "play-seeds.json")

    L = labels(world.get("language") or lock.get("language") or "en")
    title = world.get("title") or lock.get("title") or root.name
    slug = world.get("slug") or lock.get("slug") or root.name
    t = world.get("temperament") or {}
    if not (t.get("about") or any(
        (f.get("name") if isinstance(f, dict) else f)
        for f in (t.get("feelings") or [])
    )):
        t = lock.get("temperament") or {}
    win = world.get("window") or {}
    if not any(win.get(k) for k in ("era", "start", "playable_present", "stop")):
        win = lock.get("story_window") or {}
    uniqueness = (world.get("uniqueness") or "").strip() or (t.get("about") or "")
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
    plates = art.get("plates") or []
    cover = next((p for p in plates if p.get("kind") == "cover" and p.get("path")), None)
    if not cover:
        cover = next((p for p in plates if p.get("path")), None)

    feelings = []
    for f in t.get("feelings") or []:
        if isinstance(f, dict):
            if not (f.get("name") or f.get("lived")):
                continue
            feelings.append(
                f'<div class="feeling"><h3>{e(f.get("name"))}</h3><p>{e(f.get("lived"))}</p></div>'
            )
        elif f:
            feelings.append(f'<div class="feeling"><h3>{e(f)}</h3></div>')

    laws = "".join(
        f"<li>{e(x.get('text') if isinstance(x, dict) else x)}</li>"
        for x in (world.get("laws") or [])
    )
    everyday = world.get("everyday") or {}
    everyday_html = "".join(
        f"<div><h4>{e(L[k])}</h4><p>{e(everyday.get(k) or '')}</p></div>"
        for k in ("eat", "pay", "move", "sleep", "die", "news")
        if everyday.get(k)
    )

    def rail(events: list) -> str:
        items = []
        for ev in events or []:
            body = e(ev.get("body") or ev.get("residue") or "")
            items.append(
                f"""<li><div class="when">{e(ev.get('when') or '')}</div>
<div><h3>{e(ev.get('title') or ev.get('id'))}</h3><p>{body}</p></div></li>"""
            )
        return "<ol class='rail'>" + "".join(items) + "</ol>"

    swatches = "".join(
        f'<div class="swatch"><span class="chip" style="background:{e(p.get("hex"))}"></span>'
        f'{e(p.get("name"))} {e(p.get("hex"))}</div>'
        for p in (art.get("palette") or [])
        if p.get("hex")
    )

    doki = seeds.get("doki") or {}
    seed_bits = []
    for key, label in (("fmv", "FMV"), ("rpg", "RPG"), ("tcg", "TCG")):
        if seeds.get(key):
            seed_bits.append(f"<div><h3>{label}</h3><p>{e(seeds.get(key))}</p></div>")
    if doki.get("tagline") or doki.get("three_minute_accept"):
        seed_bits.append(
            f"<div><h3>Doki</h3><p>{e(doki.get('tagline') or '')} {e(doki.get('three_minute_accept') or '')}</p></div>"
        )

    counted = [p for p in plates if p.get("kind") in ("scene", "person", "prop", "signature")]

    look = lock.get("look") or {}
    look_bits = []
    if look.get("school"):
        named = look.get("named_as") or ""
        src = look.get("source") or ""
        label = look["school"]
        if named:
            label += f" · {named}"
        if src:
            label += f" · {src}"
        look_bits.append(f"<p><b>{e(L['look'])}.</b> {e(label)}</p>")
        if look.get("why"):
            look_bits.append(f"<p><b>{e(L['look_why'])}.</b> {e(look['why'])}</p>")
    look_html = "\n      ".join(look_bits)

    nav = L["nav"]
    html_out = f"""<!DOCTYPE html>
<html lang="{e(world.get('language') or lock.get('language') or 'en')}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} · World Bible</title>
<style>{css}
:root {{ {palette_css(art)} }}
</style>
</head>
<body>
<nav class="nav">
  <a href="#world">{e(nav[0])}</a>
  <a href="#stage">{e(nav[1])}</a>
  <a href="#timeline">{e(nav[2])}</a>
  <a href="#art">{e(nav[3])}</a>
</nav>

<header class="cover">
  {"<img src='" + e(cover.get('path')) + "' alt='" + e(title) + "'>" if cover else ""}
  <div class="cover-copy">
    <p class="kicker">{e(L['kicker'])} · {e(slug)}</p>
    <h1>{e(title)}</h1>
    <p class="about">{e(t.get('about') or '')}</p>
  </div>
</header>

<section class="band">
  <div class="wrap">
    <p class="lede">{e(t.get('about') or '')}</p>
    <div class="feelings">{"".join(feelings)}</div>
  </div>
</section>

<section class="ch" id="world">
  <div class="wrap">
    <p class="ch-num">01</p>
    <h2>{e(L['world'])}</h2>
    <div class="prose"><p>{e(uniqueness)}</p></div>
    <dl class="meta">
      <dt>{e(L['era'])}</dt><dd>{e(win.get('era') or '')}</dd>
      <dt>{e(L['start'])}</dt><dd>{e(win.get('start') or '')}</dd>
      <dt>{e(L['present'])}</dt><dd>{e(win.get('playable_present') or '')}</dd>
      <dt>{e(L['stop'])}</dt><dd>{e(win.get('stop') or '')}</dd>
    </dl>
    <p class="ch-num">{e(L['laws'])}</p>
    <ol class="laws">{laws}</ol>
    <p class="ch-num">{e(L['everyday'])}</p>
    <div class="everyday">{everyday_html}</div>
    <p class="ch-num" style="margin-top:2.5rem">{e(L['signature'])}</p>
    {vignette_html(sig, L)}
  </div>
</section>

<section class="ch" id="stage">
  <div class="wrap">
    <p class="ch-num">02</p>
    <h2>{e(L['stage'])}</h2>
    <h3 style="margin:0 0 0.5rem">{e(L['places'])}</h3>
    <div class="vignettes">{"".join(vignette_html(v, L) for v in stage.get('places') or [])}</div>
    <h3 style="margin:2.5rem 0 0.5rem">{e(L['people'])}</h3>
    <div class="vignettes">{"".join(vignette_html(v, L) for v in stage.get('people') or [])}</div>
    <div class="split">
      <div>
        <h3 style="margin:2.5rem 0 0.5rem">{e(L['factions'])}</h3>
        <div class="vignettes">{"".join(vignette_html(v, L) for v in stage.get('factions') or [])}</div>
      </div>
      <div>
        <h3 style="margin:2.5rem 0 0.5rem">{e(L['institutions'])}</h3>
        <div class="vignettes">{"".join(vignette_html(v, L) for v in stage.get('institutions') or [])}</div>
      </div>
    </div>
  </div>
</section>

<section class="ch" id="timeline">
  <div class="wrap">
    <p class="ch-num">03</p>
    <h2>{e(L['timeline'])}</h2>
    <p class="not">shape · {e(timeline.get('shape') or '')}</p>
    <h3 style="margin:2rem 0 0.6rem">{e(L['world_key'])}</h3>
    {rail(timeline.get('world_key') or [])}
    <h3 style="margin:2.5rem 0 0.6rem">{e(L['story'])}</h3>
    {rail(timeline.get('story_window') or [])}
  </div>
</section>

<section class="ch" id="art">
  <div class="wrap">
    <p class="ch-num">04</p>
    <h2>{e(L['art'])}</h2>
    <div class="prose">
      {look_html}
      <p><b>{e(L['style'])}.</b> {e(art.get('style_sentence') or '')}</p>
      <p><b>{e(L['light'])}.</b> {e(art.get('light') or '')}</p>
      <p><b>{e(L['medium'])}.</b> {e(art.get('medium') or '')}</p>
    </div>
    <div class="palette">{swatches}</div>
    {plates_html(counted)}
  </div>
</section>

<section class="ch" id="seeds">
  <div class="wrap">
    <p class="ch-num">05</p>
    <h2>{e(L['seeds'])}</h2>
    <div class="seeds">{"".join(seed_bits)}</div>
  </div>
</section>

<footer>{e(L['foot'])} · {e(slug)}</footer>
</body>
</html>
"""
    # collapse accidental extra spaces in tags from empty cover
    html_out = re.sub(r"\n{3,}", "\n\n", html_out)
    dest = root / "overview.html"
    dest.write_text(html_out, encoding="utf-8")
    return dest
