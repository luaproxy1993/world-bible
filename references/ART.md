# Art look (text)

Use at W5 to **write** `art/art.json`. Do not call `image_gen` or
`image_edit`. Portraits, maps, and props are `/world-bible-pack`.

This file names **how the world should look in words**. It does not paint.

## Visual law

The lock names *what* is on stage (wardrobe, architecture, era, palette)
and *how* it is pictured (`lock.look`). W5 records that look as prose.

One school. `named_as` may replace the painter or camera inside the same
school. It may not change school.

## Schools

`lock.look.school` is one of these. `medium` is the stem **verbatim**.

Thumbnail test: two schools must remain distinct at postage-stamp size.
If a sentence could pass for another school, rewrite it.

| school | What you see small | Medium stem | Must include | Never |
|--------|------|-------------|------|-----------|
| `oil-box` | Impasto bricks of paint; graphic figure-in-frame; 1990s painted game box | Oil on canvas, painted 1990s Japanese game box, Ayami Kojima / Symphony of the Night school: thick visible impasto, glaze, varnish, graphic figure-in-frame. | Visible brush ridges. Box-art composition. Painted, not filmed. | Photograph, lens bokeh, skin pores, cel contour, etching hatch, 3D render, cinematic color grade |
| `glossy-photo` | Catchlights; magazine skin; shallow depth of field | Glossy editorial photograph, 85mm, catchlights in eyes, magazine-ready skin, commercial strobe or golden-hour key. Camera, not a brush. | Photographic grain or sharpness. Real skin. Depth of field. | Brushstrokes, oil glaze, cel outline, woodcut, painterly canvas, 3D render |
| `cinematic-still` | 35mm production frame; practical light; tactile dirt | Contemporary 35mm cinematic production still, anamorphic or spherical, practical lamps, tactile materials, production design. A film frame, not an illustration. | Motion-picture lighting. Set decoration. No paint texture. | Oil impasto, cel fill, etching, editorial beauty strobe, concept-art chrome, 3D render |
| `cel` | Hard black contour; flat fills; no pores | Hand-painted animation cel: hard ink contour, flat color fields, graphic figure-in-frame, no photographic texture. | Closed outlines. Flat or simple cel shade. | Photoreal skin, oil brush, film grain, etching, 3D render |
| `print` | Limited inks; hatch or plate bite; paper tooth | Ink print, woodcut or copper etching: limited inks, visible hatch or plate bite, paper tooth, graphic figure-in-frame. | Hatch or carved edge. Few inks. Print, not paint. | Continuous-tone photo, oil glaze, cel candy color, digital-painting gloss, 3D render |

Pick the school by **what you see small**, not by mood. A dating-show brief is
`glossy-photo`. A cozy American Halloween is `cinematic-still`. A gothic
painted box is `oil-box`. Cel and print only when the brief names that
graphic tradition.

Default when intake does not name a look: `oil-box`.

## Law fields (`art/art.json`)

| Field | Must contain |
|-------|----------------|
| `medium` | The stem for `lock.look.school`. |
| `style_sentence` | What you see small + this world's clothes and buildings. One line. |
| `palette[]` | 5–8 named pigments: `name` `hex` `use` on a real surface. |
| `light` | Who lights a street and a room. 3–6 sentences. |
| `wardrobe` | 80–150 words. Work clothes and after-hours clothes. |
| `buildings` | 80–150 words. Wood, brick, stone, glass. |
| `look_dev[]` | Three written options when the look was guessed. Different schools. |
| `subjects[]` | Optional captions for `/world-bible-pack`. |

No image paths. No `generated` flag. `/world-bible-pack` writes `pack/`.

## Look-dev (text)

When `lock.look.source` is `inferred`, or the author asked for options:
write **three** `look_dev` rows. Each row a **different school**. Same
location described in one sentence. **STOP** for `look-dev: pick <school>`.
Then write `lock.look` (`source` becomes `author`) and the law fields.

## Subjects (optional)

A subject is a caption, not a file:

```json
{
  "id": "art.lena-voss",
  "kind": "person",
  "subject_id": "person.lena-voss",
  "caption": "29, patent clerk, wool coat, soot on the collar."
}
```

`kind`: `person` | `place` | `prop` | `signature` | `map`. If omitted, the
pack skill derives subjects from `stage/stage.json`.
