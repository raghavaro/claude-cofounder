---
title: Building the base
covers: The problem, the premise behind it, the alternatives, and the one you're committing to
triggers: help me think through an idea; is this worth building; what should I build; pressure-test my idea; I have an idea
minutes: 25
pacing: one step per turn
order: 10
adds-header: Problem, Who it's for, Chosen approach
---

# Building the base

Four steps, roughly 25 minutes. Output is a problem stated in one sentence, the
assumptions it rests on written down and agreed, two or three real alternatives
with one chosen, and a next step with a name against it.

The goal is **a better decision, not an implementation.** Nothing gets built in
this module. If the session drifts into writing code or copy, that's the failure
mode — say so and come back.

It's a tight 25 minutes and the temptation is to hurry step 2. Don't: the
premise gate is the only part of this module that can't be repaired later.

Run one step per turn. See the pacing section in `SKILL.md`.

**Suggested reading:** *Zero to One*, Peter Thiel. Step 2's premise gate
borrows its spirit — the contrarian question ("what do you believe that
almost no one else does"), and building toward something defensible rather
than a faster horse in a crowded field of alternatives.

Open by telling them the shape: most of this is about the problem, almost none
of it about solutions, and that's deliberate — most of what makes a build wrong
is decided before anyone opens an editor.

---

## Step 1 — The problem

**Ask:** What are you trying to accomplish?

Then, one at a time, only as far as their answers leave gaps:

- Who is it for?
- What problem does it solve, and why does that matter to them?
- What have they already tried — theirs or someone else's?
- What constraints are real? Time, money, skills, a platform they're stuck on.

Don't propose anything yet. The instinct to say "you could build X" arrives
about ninety seconds in, and acting on it ends the useful part of the module.

**Push back on:** a solution described as a problem. Most people arrive with the
answer already chosen and describe the problem backwards from it.

*They say:* "The problem is there's no AI tool for managing freelance invoices."
*Weak:* "What would the AI tool do?" — a reasonable question that accepts the
solution as the premise and never reaches the problem.
*Better:* "That's a missing product, not a problem. What does a freelancer do
today at the end of the month, and which part of it costs them something?"

**Write to brief:** Problem (header), Who it's for (header) — rough is fine, the
positioning work sharpens it — plus the real constraints.

---

## Step 2 — Challenge the premise

The load-bearing step. Take the assumptions apart before anything is proposed,
one question at a time:

1. Is this the right problem, or a symptom of a different one?
2. Who *specifically* has it? A named person or role, not a category — this
   is a specificity check, not an ICP. "The head of operations at a
   mid-size D2C brand" is a complete answer here. Don't chase it into
   monthly volume, average order value, or an operational setup; that
   segmentation is the ICP module's job, and doing it here means it gets
   redone worse — without a trigger or a disqualifier — when that module
   actually runs.
3. What happens if nothing gets built? If the honest answer is "not much", say
   so out loud.
4. Is the problem observed or hypothetical? What did they see, and when?
5. **What already solves this** — a product, a workaround, a spreadsheet, doing
   nothing? Search rather than working from memory if they don't know; naming
   something that shut down last year costs credibility. Then ask the question
   this really exists for: **is something that already exists good enough?** Be
   willing to answer yes. Someone who leaves having decided not to build has had
   a good session, and it's far cheaper here than in month four.
6. What existing work can be reused — their own code, a library, a service?

**Then state the premises back as a numbered list and stop.**

```
PREMISES
1. [statement] — agree / disagree?
2. [statement] — agree / disagree?
3. [statement] — agree / disagree?
```

Wait for a real answer on each. If they disagree with one, update it and
re-state before moving on. A premise nobody ratified is an assumption that
resurfaces as a rebuild in six weeks.

**Push back on:** evidence that is really enthusiasm.

*They say:* "Everyone I've spoken to says they'd use it."
*Weak:* "Who have you spoken to?" — gets you a list of names and no test.
*Better:* "Saying they'd use it is free. Has anyone asked when it ships, offered
to pay, or been annoyed when something broke? Those are the three that count."

**Write to brief:** the agreed premises, numbered, plus any rejected and what
replaced them.

---

## Step 3 — Alternatives

**Produce at least two, ideally three.** Not optional, and not three variations
of one idea.

- **A — Minimal.** The smallest thing that could work. Fewest moving parts,
  ships soonest.
- **B — Ideal.** The best long-term shape, if the constraints weren't binding.
- **C — Alternative.** A meaningfully different framing. The "something existing
  is good enough" answer from step 2 is often the honest C.

For each, briefly: what it does, effort, main risk, and what it reuses. Brief is
the word — this is four minutes, not a document.

**Then recommend one, in a line, tied to what they said they wanted — and
stop.** Present them and wait. A clearly winning option is still their decision,
and a recommendation accepted by silence gets abandoned the first week it
becomes inconvenient.

**Push back on:** picking B because it's the most interesting. The gap between
what's fun to build and what's worth building is where most first products die.

**Write to brief:** Chosen approach (header), the alternatives in one line each,
and the reason for the choice — which is what lets them revisit it later without
re-running the module.

---

## Step 4 — The next step

Not a plan document. Five lines, and the last one matters most:

- The problem, in one sentence
- The chosen approach, in one sentence
- The core flow — what a person does, start to finish, in the fewest steps
- The open questions that are still genuinely open
- **The next step:** one thing, concrete, doable this week, with a name against
  it and a date

Everything above exists to make that last line right. "Start building" is not a
next step.

**Write to brief:** the five lines, with the next step carrying its owner and
date.

---

## Closing the module

Read back the problem in one sentence and the chosen approach. Nothing else.

Then the checkpoint: ask them to post their problem sentence and their next step
in the chat. A sharp problem with a vague next step is the most common shape,
and it's only obvious next to somebody else's.

**Then what's next.** This module decides *what* to build and roughly who for.
Sharpening who, and what to say to them, is the positioning work that follows.

---

## If they already built it

Some people arrive with the thing already made, wanting the page rather than the
decision. The module still runs and it's usually the most useful twenty-five
minutes of their session, but the tense changes:

- **Step 1** asks what it does and who's using it now, not what they intend.
- **Step 2**'s questions get asked of a product that exists — "what happens if
  nothing gets built" becomes "what happens if you stop working on this", which
  is harder and better.
- **Step 3** compares carrying on, narrowing to something smaller, and stopping.
  Those are real alternatives at any stage, and someone who has never priced the
  third hasn't chosen the first.

Don't let them skip ahead to the page. A page built on an unexamined premise is
a faster way to find out the premise was wrong, not a cheaper one.
