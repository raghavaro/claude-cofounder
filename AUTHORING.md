# Writing a module

A module is one file: `flows/<name>.md`. Add the file, run the build, and the
router, the trigger phrases, the brief's header table, the room timetable and
the ChatGPT paste file all update themselves. Nothing else needs editing.

Run these from the skill directory:

```sh
cp flows/_TEMPLATE.md flows/pricing.md
# write it
python3 scripts/build_index.py       # SKILL.md's generated blocks
python3 portable/build.py            # the paste file
python3 scripts/build_skill_zip.py   # the ChatGPT Skills zip
```

`make` runs them in the right order, and `make check` runs what CI runs.

## The frontmatter contract

| Key | Required | What it does |
|---|---|---|
| `title` | yes | Display name in the module table and the timetable |
| `covers` | yes | One line — the module table and the timetable both print it |
| `triggers` | yes | Semicolon-separated phrases; becomes the routing list |
| `minutes` | yes | Whole number; the timetable is summed from these |
| `pacing` | yes | `one step per turn`, or `one decision per turn` for a module that does real work between stops |
| `order` | no | Sort key for the run order (default 999). Leave gaps — 10, 20, 30 — so a module can be inserted later |
| `after` | no | The module this one needs output from. Documentation for now; state it in the module's own opening too |
| `adds-header` | no | Comma-separated field names this module adds to `company-brief.md`'s header |

`adds-header` is the one worth understanding. The brief's header table in
`SKILL.md` is **generated** from the core fields plus every module's
declaration. That's deliberate: the marketing skill's header forked once —
twelve fields documented in one place and seven in another — because two files
described the same table by hand. Here they can't.

Filenames starting with `_` are never modules, so `_TEMPLATE.md` and any notes
you leave in `flows/` are ignored by every build.

## What a module owes the rest of the skill

- **One question per step.** Two questions in one step gets you an answer to
  the easier one.
- **A push-back where the step has a predictable failure** — with the weak
  follow-up written out next to the better one. The weak version is the useful
  half: it's almost always a reasonable-sounding question that accepts the
  frame it should reject.
- **A `Write to brief:` line on every step**, naming which header fields it
  fills. If a step doesn't produce anything worth keeping, it isn't a step.
- **A `Starting from nothing` note** if the module assumes customers, revenue,
  or staff. Roughly a third of a room won't have them.
- **No invented numbers.** Not a benchmark, not a market rate. Ask for theirs or
  search for a real source and name it.
- **Real minutes.** The timetable is summed from `minutes:` and the total is
  printed with the open and wrap blocks included, so an optimistic module
  inflates the whole day visibly.

## Longer material

Put reference material a module needs — a scorecard, a worked cash model, a
rubric — in `references/<name>.md` and cite it as `` `references/<name>.md` ``.
The paste builder inlines every reference a module cites, so the ChatGPT version
carries it too, and the test suite fails if a module cites one that doesn't
exist.

Anything long that a module *produces* is a draft, not brief content: its own
file, with the brief holding the decision and a pointer.

## Before you commit

```sh
make check
```

CI runs all four. They fail on a stale build, a module missing frontmatter, a
cited reference that doesn't exist, and a paste file whose module was renamed
or removed.
