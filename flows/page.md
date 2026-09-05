---
title: The landing page
covers: Section order, a design system that doesn't look generated, and a Next.js project that ships
triggers: build my landing page; put up a page; ship the page; make the site; design the page
minutes: 40
pacing: one step per turn
order: 50
after: copy
adds-header: Landing page
---

# The landing page

Six steps, roughly 40 minutes. The copy module decided what the page says. This
one decides the order it says it in, what it looks like, and gets it built.

Output is a Next.js project — one route, smooth scroll, reveals that reveal
once — built against a design system written down before any markup. Where the
session can't run a terminal, the same project as complete files to paste, with
the commands to run them.

Two rules that hold throughout:

- **A page that is written and ready is a real result. It is never described as
  live.** Live means published, read back, and verified.
- **Never generate a testimonial, a customer name, or a company logo.** If they
  want social proof they don't have, the answer is to go and get some.

Run one step per turn. See the pacing section in `SKILL.md`.

---

## Step 1 — The spine and the first screen

Lay the page out in order before any prose, one line per section:

1. **Hero** — headline, subhead, one button, and something showing the product
2. **Reason one**, the strongest
3. **Reasons two and three**, one section each
4. **The objection**, answered
5. **The action again**, same button text as the hero

Then hold the first screen to what it has to do. A visitor should understand the
problem being solved in about fifteen seconds without reading a second section:

- **An outcome headline** — what they get, not what it is
- **A subhead saying who it's for**, or how it works. One of the two.
- **One CTA, visually dominant.** Not three buttons of equal weight.
- **Something showing the product** — a screenshot, a short loop, a live
  preview. Real and rough beats polished and abstract.
- **Trust near the action**, and only real signals.

**Push back on:** a hero carrying an explanation.

*They say:* "The subhead needs to explain how the calendar sync works, otherwise
people won't get it."
*Weak:* "Let's tighten that to one sentence." — keeps the mechanism above the
fold and just makes it terser.
*Better:* "The top of the page has one job: make someone want the next section.
Mechanism goes in reason one, where it's proof rather than preamble. What does
the person get, in the words they'd use?"

**Write to brief:** the section order.

---

## Step 2 — Credibility for a company nobody knows

**Ask:** What on this page makes it look like a real thing built by real people?

For a new product this does more work than any argument:

- **A name and a face.** The founder, said plainly. Anonymity reads as risk.
- **Something that shows it working** — a screenshot, a clip, real output.
- **Specifics instead of scale.** "Three agencies are using it this month" beats
  "trusted by teams everywhere", and it's true.
- **A way out.** No card required, cancel any time, export your data.

What doesn't: stock photography, invented testimonials, logo strips of companies
that aren't customers, counters that count nothing.

**Write to brief:** what's being used, and anything that needs making first.

---

## Step 3 — The states nobody remembers

The page isn't the only screen. Three more decide whether the action completes:

- **The form.** Fewest fields that let you follow up. Every extra field costs
  conversions — ask why each exists.
- **After they act.** What they see the second they click: what happens next,
  and when. Not a blank page.
- **When it fails.** Duplicate signup, invalid address, a form that errors. Say
  what to do.

Then the one people forget: **the first message they receive.** Write it now, in
the voice from the copy module, in three lines. "Thanks — I'll reply personally
this week" is a fine message and a promise that can be kept.

**Write to brief:** form fields, the thank-you wording, the first message.

---

## Step 4 — The design pass

Read `references/design-system.md` and fill in its token block **before any
markup exists.** This is the step that decides whether the page looks made or
generated, and it takes about eight minutes.

Work it in this order:

1. **Rule out the defaults out loud.** Name them — the indigo gradient, Inter
   everywhere, three icon-topped cards, the pill badge over a centred headline,
   soft-shadowed rounded boxes. A model with no constraints emits the median of
   its training data, and everyone can now recognise that median.
2. **Pick the type.** One display face with a personality, one plain workhorse.
   Two families, maximum. This single choice does more than everything else.
3. **Pick a ground, an ink, and one accent.** Rarely pure white or pure black.
   Say where the accent is allowed to appear.
4. **Commit to values, not ranges.** Actual numbers for the type scale, the
   space scale, the radius. Anything left unchosen gets chosen by the model, and
   it picks the median.
5. **Choose the one idiosyncratic detail.** A hand-drawn arrow, a margin note, a
   footnote, an odd cursor. One. It's the thing that reads as a person.

**Push back on:** deferring the look until after the build.

*They say:* "Let's get it working first and make it look good after."
*Weak:* "Sure — we can restyle it once the structure's there." — the restyle
never happens, and the defaults become the design by inertia.
*Better:* "The tokens take eight minutes now and they can't be retrofitted —
every component gets built against whatever we don't decide. What typeface are
we using?"

**Write to brief:** the filled-in token block, as its own draft — it becomes
`DESIGN.md` in the project.

---

## Step 5 — Build it

Read `references/nextjs-starter.md`. One route, Next.js App Router, Lenis for
smooth scroll, and a fifteen-line reveal component instead of an animation
library.

**If this session can write files and run commands**, scaffold it: the project,
the tokens in `globals.css`, the smooth-scroll wrapper, the reveal component,
`DESIGN.md`, then the page itself section by section from steps 1–3. Run it and
look at it before saying anything about it.

**If it can't** — which on a free ChatGPT account is always — produce the same
project as complete files, each in its own copyable block, with the commands to
run in order. Say plainly that nothing has been created. A person with those
files and twenty minutes has a running page; a person with a description of them
has homework.

Either way the motion rules are not negotiable, because they're what separates a
considered page from a demo reel:

- Light `lerp` — heavier and the page fights the wheel
- Reveals happen **once**, and never on the hero
- `prefers-reduced-motion` disables both, with everything visible
- Content is in the DOM and readable with JavaScript off

**Then publishing.** If the session has real write access to somewhere it can
go live, show the exact destination and content once, get an explicit yes to
that specific preview, publish, and **read the live page back** before saying
it's done. Otherwise: the project plus the deploy commands is the deliverable,
and it is not live.

**Write to brief:** Landing page (header) — the URL if it's live and verified,
otherwise `ready to deploy` and where the project is.

---

## Step 6 — Read it as the person

**Ask:** Read the page out loud as the person from your ICP, on a phone, between
two other things.

- **Does the first screen say what it is?** Not what it's like — what it is.
- **Is there anything they'd need to already know?** Internal vocabulary, a
  category name only insiders use, a feature name that means nothing yet.
- **Is the next step obvious without scrolling back up?**
- **Does the motion get in the way?** If anyone notices the scrolling, the lerp
  is too heavy.

Five minutes, and it routinely catches what the previous thirty-five didn't —
it's the first time anyone reads the whole thing in order at speed.

**Write to brief:** anything changed as a result.

---

## Closing the module

Read back the headline, the button, and whether the page is live or ready.

Then the checkpoint: ask them to post their URL if it's live, or their headline
and button if it isn't. Where most people can't publish, the second is the
normal answer and shouldn't feel like a shortfall — say so, because online
nobody can see that everyone else is in the same position.

**Then what's next.** The page exists; nobody has seen it. Getting it in front
of the segment — communities, directories, newsletters, events, a 30-day
sequence — is the distribution work in `marketing-workshop`, which reads the
segment and the ICP straight out of this brief. **This module doesn't do
outreach or build contact lists**, and neither does that one.

If the page is live, set one date to look at it again with real numbers. A page
nobody revisits is a page that stays wrong.

---

## Starting from nothing

This module assumes a domain and somewhere to host. Plenty of people have
neither, and it's a twenty-minute problem rather than a blocker — say so rather
than letting it derail the step.

With no domain the project still gets built and the deploy commands still get
written; the checklist gains one line at the top. **Don't spend the module's
time choosing a domain name.** It's the most tempting procrastination available
at this exact moment, and the page is worth more than the name.
