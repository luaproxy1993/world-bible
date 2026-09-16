# Art registry

Use at W5 to **write** `art/art.json`. Do not call `image_gen` or `image_edit`
here. Pictures are `/world-bible-art`.

These plates **anchor temperament**. They are not engine-ready sprites.

## Visual law

The lock names *what* is in the picture (wardrobe, architecture, era,
palette) and *how* it is painted (`lock.look`). The registry records that
look. It does not invent a second school.

A world ships **one** `kind: anchor` plate in the registry. Cover, person,
scene, and signature are treatments of that school. Four live style-anchors
are out.

## Schools

`lock.look.school` is one of these. `medium` is the stem **verbatim**.
`named_as` may replace the named painter or camera inside the same school.
It may not change school.

Thumbnail test: two schools must remain distinct at postage-stamp size.
If a prompt could pass for another school, rewrite it.

| school | Tell (thumbnail) | Medium stem | Must | Forbidden |
|--------|------------------|-------------|------|-----------|
| `oil-box` | Impasto bricks of paint; graphic figure-in-frame; 1990s painted game box | Oil on canvas, painted 1990s Japanese game box, Ayami Kojima / Symphony of the Night school: thick visible impasto, glaze, varnish, graphic figure-in-frame. | Visible brush ridges. Box-art composition. Painted, not filmed. | Photograph, lens bokeh, skin pores, cel contour, etching hatch, 3D render, cinematic color grade |
| `glossy-photo` | Catchlights; magazine skin; shallow depth of field | Glossy editorial photograph, 85mm, catchlights in eyes, magazine-ready skin, commercial strobe or golden-hour key. Camera, not a brush. | Photographic grain or sharpness. Real skin. Depth of field. | Brushstrokes, oil glaze, cel outline, woodcut, painterly canvas, 3D render |
| `cinematic-still` | 35mm production frame; practical light; tactile dirt | Contemporary 35mm cinematic production still, anamorphic or spherical, practical lamps, tactile materials, production design. A film frame, not an illustration. | Motion-picture lighting. Set decoration. No paint texture. | Oil impasto, cel fill, etching, editorial beauty strobe, concept-art chrome, 3D render |
| `cel` | Hard black contour; flat fills; no pores | Hand-painted animation cel: hard ink contour, flat color fields, graphic figure-in-frame, no photographic texture. | Closed outlines. Flat or simple cel shade. | Photoreal skin, oil brush, film grain, etching, 3D render |
| `print` | Limited inks; hatch or plate bite; paper tooth | Ink print, woodcut or copper etching: limited inks, visible hatch or plate bite, paper tooth, graphic figure-in-frame. | Hatch or carved edge. Few inks. Print, not paint. | Continuous-tone photo, oil glaze, cel candy color, digital-painting gloss, 3D render |

Map intake to a school by **tell**, not by mood. A dating-show brief is
`glossy-photo`. A cozy American Halloween is `cinematic-still`. A gothic
painted box is `oil-box`. Cel and print only when the brief names that
graphic tradition.

Default when intake does not name a look: `oil-box`.

## Law fields (`art/art.json`)

| Field | Must contain |
|-------|----------------|
| `generated` | `false` after W5. `/world-bible-art` sets `true` when files exist. |
| `medium` | The stem for `lock.look.school` (table above). |
| `style_sentence` | Locked school **tell** + locked surface + composition. One pin-able line. |
| `palette[]` | 5–8 named pigments: `name` `hex` `use`. Prompts pick 2–3 of these. |
| `light` | Who lights the world. |
| `plates[]` | Registry. Each counted plate has `title` `caption` `prompt`. |
| `look_dev[]` | Optional. Text candidates when `lock.look.source` is `inferred`. |

Front-load the school tell, then the locked surface, in `style_sentence`
and in every `prompt`.

## Look-dev (text, at W5)

When `lock.look.source` is `inferred`, or the author asked for options:
write **three** `look_dev` rows. Each row a **different school** from the
table (not three painters in `oil-box`). Same location described. **STOP**
for `look-dev: pick <school>`. Then write `lock.look` (`source` becomes
`author`) and the plate registry. No images.

## Floor — 4 × 3 = 12

Same floor at every scale. Scale adds rooms and beats, not extra style
plates. `/world-bible-art full` may later paint remaining stage subjects.

| Kind | Min | Folder | What |
|------|-----|--------|------|
| `scene` | 3 | `art/scenes/` | playable-present locations |
| `person` | 3 | `art/people/` | entry face + others on stage |
| `prop` | 3 | `art/props/` | ordinary objects that carry the world |
| `signature` | 3 | `art/signature/` | whale-oil class **in use** |

≥12 counting only those four kinds. ≥4 distinct `aspect_ratio` values among them.

Pick ratios from: `16:9` `9:16` `1:1` `3:4` `4:3` `3:2` `2:3`.

Each counted plate: `title` + `caption` + `prompt`. Cover and style-anchor
are extras (`kind: cover|anchor`). They do not count toward 12.

## Plate recipes

**Cover** (`kind: cover`, extra). One picture that could sit on a 1990s
game box — or the equivalent hero frame for this school. Strong
foreground object, the world receding, a designed sky.
`16:9` or `3:2`. No title lettering.

**Style anchor** (`kind: anchor`, extra). A location that teaches the
light. Empty of a hero.

**Person**. Standing three-quarter figure, one subject, isolated on
**flat black**. Clear silhouette, cutout-ready. Ratio `3:4` or `2:3`.

**Scene**. Place in the playable present. No hero in the foreground.
The world's actual light, in the locked school.

**Prop**. An ordinary object of this world, in use or sitting where it
lives. Not a catalog product shot on white.

**Signature**. The unique thing **in use** in this world's light.

## Prompts (written at W5, used by `/world-bible-art`)

Own the prompt (2–5 sentences). Every prompt **starts with the school
tell + medium stem**, then the plate. Restate `forbidden` as the last
sentence of the prompt (positive: "this is X"; then the school's Must).

```
[tell]. [medium stem]. [2–3 pigments]. [subject]. [setting].
[composition]. [this world's light]. [Must].
```

Person plates add: standing three-quarter portrait, isolated on flat
black, one figure, no environment.

No in-image typography.

## Generation

`/world-bible-art` only. Order, edit-chain, and image verify live there.
W5 does not load the `imagine` skill.
