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
- An em dash in a headline, an eyebrow, a button, or a caption — the single
  most common tell in AI-written copy, and one no visual polish covers for.
  Rewrite with a period, a comma, or a colon instead. This applies below the
  fold too, not just the hero.
- An eyebrow label — the small uppercase, wide-tracking word above a section
  headline (`OUR PROCESS`, `WHY IT WORKS`) — sitting above *every* section.
  One eyebrow reads as a section marker; six in a row reads as a template
  ticking its own boxes. Cap it at roughly one eyebrow for every three
  sections, hero included, and drop the rest — the headline alone is enough.
- **Space Grotesk paired with a teal or petrol-green accent.** This looks
  like a deliberate, distinctive choice the first time it's made — which is
  exactly why it's become the second-order default: the safe alternative
  everyone reaches for once Inter and indigo are off the table. Treat it as
  ruled out the same as Inter-everywhere, not as evidence of a decision.

None of these are bad in isolation. Together they are a uniform. If the page
has four of them it reads as generated no matter how good the copy is.

## Check what else exists in this workspace before choosing tokens

If this session has already built another page under this skill — earlier in
the same conversation, or visible as a sibling project on disk — its
choices are now claimed, not just a reference point to differ from once.
Read its `DESIGN.md` and rule out its exact type pairing, its accent hue
family, and its ground temperature (warm vs. cool, light vs. dark), not only
its literal values. "Different from the one page I can see" is how two
pages built in parallel, each told only to differ from a shared reference,
both end up choosing Space Grotesk and teal independently — neither was
wrong to avoid the reference, and both still collided with each other.

Where several pages are being planned or built together (a portfolio of
ideas, a parallel batch), treat distinctiveness as a set to divide up front,
not a per-page decision made in isolation: assign a different type-pairing
character (a warm quirky serif, a heavy industrial grotesk, a certificate
serif, a plain workhorse pair) and a different accent hue family (orange,
navy, lime, rust, magenta — not four shades of teal) to each one before any
of them starts choosing values, the same way a designer handed five
sub-brands would.

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
  it working, a photograph of the person, *if one of those exists* — and for
  most sessions here, pre-launch, none of them do yet. Priority order for that
  default case:
  1. **Generate one, if the session can.** An image-generation tool building a
     bespoke asset for this specific business beats anything hand-rolled —
     use it before reaching for markup. This is a generated asset, not a
     stock photo: it should depict this business's actual thing, not a
     generic stand-in for the category.
  2. **Otherwise, build a diagram, map, or illustration** specific to this
     business — how it works, where to find it, a labelled sketch of the
     product — rather than an abstract shape.
  3. **Otherwise, the founder's own words, set large.**
  Never a "coming soon" placeholder box and never a stock photo standing in
  for a product that doesn't exist. Real-but-modest beats generic-but-polished
  throughout: a rough product screenshot beats an abstract render, and a plain
  diagram of an actual process beats a stock illustration that could belong to
  anyone.
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

- **An outcome headline**, two lines maximum. What the person gets, not what
  the product is.
- **A subhead that says who it's for**, or how it works — one of the two,
  twenty words maximum, four lines maximum. If the value proposition doesn't
  fit, the value proposition is unclear, not the limit too tight.
- **One CTA, visually dominant**, its label short enough to sit on one line at
  desktop width. Not three buttons of equal weight, and not a second button
  making the same offer in different words.
- **Something to look at** above the fold — a screenshot or interactive demo
  where the product exists to demo, otherwise a diagram, a map, or an
  illustration built for this business specifically. Either way, a visitor
  should understand the problem being solved in about fifteen seconds
  without reading a second section.
- **Trust near the action**, not in a strip at the bottom — and only real
  signals.
- **Four text elements in the hero, maximum**: an eyebrow, the headline, the
  subhead, the CTA(s). A tagline under the button, a trust micro-strip, or a
  feature list stuffed into the hero on top of those four is the thing that
  makes it float and stops it fitting the viewport — move it to its own
  section below instead.

The whole hero has to fit the initial viewport without scrolling — if it
doesn't, cut copy or reduce the type scale before adding top padding to make
it look intentional. Load in under two seconds and lazy-load everything below
the fold. A slow page is a design failure before it is a performance one.

## Before it ships — the mechanical check

A handful of these are checkable by counting, not judging, which is exactly
why they're worth running as a final pass rather than trusting the build to
have gotten them right along the way:

- **Em dashes: zero**, anywhere a visitor can read one — headline, eyebrow,
  button, caption, quote attribution. Grep for `—` if unsure.
- **Eyebrows: at most one per three sections**, hero included. Count the
  small-caps labels; if there are more sections using one than that ratio
  allows, cut the extras rather than add a section to dilute the count.
- **No two CTAs make the same offer in different words** — "Get in touch",
  "Let's talk", "Reach out" on the same page is one offer wearing three
  labels. Pick one and repeat it exactly, the way the landing page module
  already repeats the hero's button text at the bottom.
- **Every button and form field passes WCAG AA contrast** against its
  background — no white text on a light accent, no placeholder text lighter
  than the muted ink token.
- **No section repeats the exact layout family** of the section before it —
  the two sections marked to break the stack in Step 1 of the page module
  should be visibly doing something different from each other, not just
  different from the plain sections.

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

## A note on scope

Every "zero" and "at most" rule in this file — the em-dash ban, the eyebrow
ratio, the duplicate-CTA check — applies to what the built page shows a
visitor. It says nothing about how this skill's own modules or references
are written; that prose keeps its own voice. Don't let a mechanical check
meant for shipped copy start editing the skill.

Several of the hard, checkable rules above (the em-dash ban, the eyebrow
ratio, the hero element cap, the duplicate-CTA check, the image-generation
priority order) are adapted from the open-source
[Taste Skill](https://tasteskill.dev) project (MIT, Leonxlnx/taste-skill),
narrowed to the single-route, no-dependency scope this starter actually
builds — its own version covers a much larger surface (dashboards, real
design-system integrations, GSAP scroll choreography) that's out of scope
for what `flows/page.md` ships.
