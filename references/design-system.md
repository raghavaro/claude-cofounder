# Landing page design system

Two jobs. Stop the page looking generated, and satisfy what a landing page has
to do in the first five seconds. They pull in the same direction more often than
people expect.

## Why generated pages look the same

A model asked to "build a landing page" with no constraints emits the median of
its training data — which is every Tailwind tutorial scraped from GitHub since
2019. That median has a look, and everyone can now recognise it.

**Rule out the defaults explicitly.** These are the tells, and every one of them
should be a deliberate choice if it appears at all:

- A purple or indigo gradient — especially a blurred orb behind the hero
- Inter for everything, at every weight, with no second family
- Rounded cards with a thin grey border and a soft drop shadow
- Three feature cards in a row, icon on top, equal width
- A small pill badge floating above a centred headline
- Glassmorphism, and gradient text on the headline
- Emoji standing in for icons
- A "Trusted by" strip with logos of companies that aren't customers

None of these are bad in isolation. Together they are a uniform. If the page
has four of them it reads as generated no matter how good the copy is.

## What makes a page feel made by a person

Not polish — polish is what the defaults already have. What reads as handmade is
**evidence of a decision**:

- **One opinionated typeface.** A real display face for headlines against a
  plain workhorse for body. Two families, maximum. The choice should be legible
  as a choice — a page set in something with a personality reads as authored
  even when the layout is simple.
- **Asymmetry somewhere.** Everything centred is the default. Left-aligned
  headlines, an off-centre hero, a section that breaks the grid on purpose.
  A principle stated here and never assigned to a section stays a principle —
  `flows/page.md`'s spine step is where it has to become a decision about
  which two sections actually break the stack.
- **Uneven whitespace.** Generous, and *not* uniform. Space should mark where
  ideas end, not sit at 96px between every section.
- **Something real in the first screen.** A product screenshot, a short loop of
  it working, a photograph of the person. Real beats illustrated, and a
  screenshot of a rough product beats a beautiful abstract render.
- **One idiosyncratic detail.** A hand-drawn arrow, a footnote, an aside in the
  margin, a slightly odd cursor. One. It signals a person was here.
- **Restraint in colour.** A ground, an ink, and exactly one accent used
  sparingly enough to mean something.

## The token block

Fill this in before writing any markup. It is the whole design system; keep it
in the project as `DESIGN.md` so later work stays consistent with it.

```markdown
# DESIGN.md

## Type
Display:      [family, weight, and where it's allowed]
Body:         [family, weight]
Scale:        [4–5 sizes, actual values — e.g. 14 / 17 / 22 / 34 / 56]
Measure:      [max line length for body, 60–75 characters]

## Colour
Ground:       [page background — off-white or near-black, rarely pure]
Ink:          [body text, and a muted variant for secondary]
Accent:       [one, with where it is allowed to appear]
Rule:         [border colour, if borders are used at all]

## Space
Scale:        [4–6 steps, e.g. 8 / 16 / 32 / 64 / 120]
Section rhythm: [what separates sections — space, a rule, a ground change]

## Shape
Radius:       [one value, used everywhere, or none]
Border:       [width and where — or "none, space does the separating"]
Shadow:       [usually "none"]

## Motion
Reveal:       [one direction, one distance, one duration]
Scroll:       [lerp value]
Reduced:      [what happens under prefers-reduced-motion]
```

**Pick values, not ranges.** "Somewhere between 16 and 24" produces
inconsistency; 16 produces a system. Every value that isn't chosen gets chosen
by the model, and it will pick the median.

## What the first screen must do

From how strong landing pages are actually built — and what YC-shaped early
pages consistently get right:

- **An outcome headline.** What the person gets, not what the product is.
- **A subhead that says who it's for**, or how it works. One of the two.
- **One CTA, visually dominant.** Not three buttons of equal weight.
- **Something showing the product** above the fold — a screenshot, a short
  demo, an interactive preview. A visitor should understand the problem being
  solved in about fifteen seconds without reading a second section.
- **Trust near the action**, not in a strip at the bottom — and only real
  signals.

Load in under two seconds and lazy-load everything below the fold. A slow page
is a design failure before it is a performance one.

## Motion rules

Slow scroll and reveals are the easiest way to make a page feel considered and
the easiest way to make it feel like a demo reel. The line is that **motion
should be felt, not noticed**.

These are values rather than ranges, on the same principle as the tokens above —
the starter uses exactly these, and if you change one, change it once and
everywhere:

- **Smooth scroll**: `lerp: 0.1`. Heavier and the page feels like it's fighting
  the wheel, which is the single most common complaint about smooth-scroll
  sites.
- **Reveals**: one direction, `16px`, `400ms`, one easing. Stagger siblings by
  `80ms`.
- **Once.** Elements reveal on first view and stay revealed. Re-animating on
  every scroll past is the tell that separates a designed page from a template.
- **Never the hero.** The first screen renders immediately. Animating the
  headline in delays the only content most visitors will read.
- **`prefers-reduced-motion`** disables both the smooth scroll and the reveals.
  Not "reduces" — disables, with everything visible.
- **Nothing important waits on JavaScript.** Content is in the DOM and visible
  by default; motion is added to it. A reveal implemented as "hidden until JS
  runs" is a page that renders blank when the script fails.
