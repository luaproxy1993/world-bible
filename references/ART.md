# Art plates

Use at W5. Load the `imagine` skill before any `image_gen` / `image_edit`.
Recurring subjects: edit-chain from a canonical plate.

These plates **anchor temperament**. They are not engine-ready sprites.

## Visual law

The lock names *what* is in the picture (wardrobe, architecture, era,
palette) and *how* it is painted (`lock.look`). W5 executes that look.
It does not invent a second school.

A world ships **one** `kind: anchor` plate. Cover, person, scene, and
signature are treatments of that school (box, card crop, place, object
in use). Four live style-anchors are out.

## Schools

`lock.look.school` is one of these. Medium stems go into `art.json`
`medium` verbatim, with `named_as` substituted when the lock set one.

| school | Medium stem | Start `forbidden` |
|--------|-------------|-------------------|
| `oil-box` | Oil on canvas in the manner of Ayami Kojima's Castlevania Symphony of the Night box art: thick visible brushstrokes, glaze, varnish. | photograph, cinematic still, 3D render |
| `glossy-photo` | Glossy editorial photograph, magazine-ready skin, commercial entertainment lighting. | oil painting, horror-blue grade, 3D render |
| `cinematic-still` | Contemporary cinematic production still, tactile materials, practical light. | oil painting, concept-art chrome, generic brown apocalypse |
| `cel` | Hand-painted animation cel: flat color fields, clean contour, graphic figure-in-frame. | photoreal skin, painterly oil, 3D render |
| `print` | Ink print (woodcut or etching): graphic figure-in-frame, visible plate texture, limited inks. | photograph, digital-painting gloss, 3D render |

Default when intake does not name a look: `oil-box`, Kojima / SotN as
`named_as`. A named painter inside `oil-box` replaces Kojima in the
stem and keeps visible brush and box-art composition.

Map intake to a school. A dating-show brief is `glossy-photo`. A cozy
American Halloween is `cinematic-still`. A gothic boarding college may
be `oil-box`. Cel and print only when the brief names that graphic
tradition.

## Law fields (`art/art.json`)

| Field | Must contain |
|-------|----------------|
| `medium` | The stem for `lock.look.school` (table above). |
| `style_sentence` | Locked school + locked surface + composition. One pin-able line. |
| `palette[]` | 5–8 named pigments: `name` `hex` `use`. Prompts pick 2–3 of these. |
| `light` | Who lights the world. Paint that light. |

Front-load the school, then the locked surface, in `style_sentence`.
Signature objects appear in that world's light, in that school.

Specificity is residue under the surface — a designer pin on a
collarbone; a lamp burning oil on a wet street. It is not a different
school.

## Look-dev

Run **before** the twelve plates when `lock.look.source` is `inferred`,
or when the author asked to see options. Skip when `source` is `author`.

Same location as the future style-anchor (empty of a hero, teaches the
light). Two to four candidates. Distinct schools from the table that
could still serve this temperament. Include the inferred school.

```
art/look-dev/<school>.png
kind: look-dev
```

Look-dev plates do not count toward 12. **STOP** for:

```
look-dev: pick <school>
look-dev: pick <school> — named_as: <painter or show>
```

Then: write the pick into `lock.look` (`source` becomes `author`),
promote the winner to `art/anchors/style-anchor.png` (`kind: anchor`),
leave losers in `art/look-dev/`. Generate the floor from that anchor.

## Floor — 4 × 3 = 12

| Kind | Min | Folder | What |
|------|-----|--------|------|
| `scene` | 3 | `art/scenes/` | playable-present locations |
| `person` | 3 | `art/people/` | entry face + others on stage |
| `prop` | 3 | `art/props/` | ordinary objects that carry the world |
| `signature` | 3 | `art/signature/` | whale-oil class **in use** |

≥12 counting only those four kinds. ≥4 distinct `aspect_ratio` values among them.

Pick ratios from: `16:9` `9:16` `1:1` `3:4` `4:3` `3:2` `2:3`. Do not ship twelve 16:9 stills.

Each plate has `title` + `caption` in `art/art.json`. A plate without caption does not count.

Cover, style-anchor, and look-dev are extras (`kind: cover|anchor|look-dev`). They do not count toward 12.

## Plate recipes

**Cover** (`kind: cover`, extra). One picture that could sit on a 1990s
game box — or the equivalent hero frame for this school. Strong
foreground object, the world receding, a designed sky.
`16:9` or `3:2`. No title lettering.

**Style anchor** (`kind: anchor`, extra). A location that teaches the
light. Empty of a hero. `image_gen` first (or the look-dev winner);
later scenes `image_edit` from this plate.

**Person**. Standing three-quarter figure, one subject, isolated on
**flat black**. Clear silhouette, cutout-ready. Ratio `3:4` or `2:3`.
This is a portrait plate, not a scene with a person in it. First of
each face is `image_gen`; later views `image_edit`.

**Scene**. Painted place in the playable present. No hero in the
foreground. The world's actual light, in the locked school.

**Prop**. An ordinary object of this world, in use or sitting where it
lives. Not a catalog product shot on white.

**Signature**. The unique thing **in use** in this world's light.
Not a MacGuffin on a pedestal.

## Order

```
lock.look → medium + style sentence
  → look-dev (only if inferred / asked)   STOP look-dev: pick
  → style anchor          image_gen, or promote the pick
  → cover                 image_edit from anchor (extra)
  → 3 signature           mixed ratios; in use, not catalog
  → entry-face master     image_gen on flat black, freeze
  → other people          first of each is gen on black; then edit
  → 3 scenes              image_edit from anchor
  → 3 props               image_edit from anchor
```

Parallelize only within one step.

## Prompts

Own the prompt (2–5 sentences). Every prompt starts with the locked
medium stem, then the plate:

```
[medium stem]. [2–3 pigments from palette]. [subject]. [setting].
[composition]. [this world's light].
```

Person plates add: standing three-quarter portrait, isolated on flat
black, one figure, no environment.

Restate fixed traits on every edit. No in-image typography.

## Verify

Describe the image before re-reading the spec. Fail if:

- it reads as a different school than `lock.look.school`
- `oil-box` is only a cracked-varnish filter on a photo
- a person plate has a full environment behind the figure
- it could be another world's city
- the entry face drifted
- all counted plates share one ratio
- a caption is missing
- a signature is a generic MacGuffin
- the plate refuses the locked surface
- a second live style-anchor sits beside the canonical one

One retry, then keep and flag.

Run `{SKILL_ROOT}/scripts/validate.py <world-root>` before W5 accept.
