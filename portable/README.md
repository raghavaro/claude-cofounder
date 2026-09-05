# Running this skill on ChatGPT

ChatGPT's own Skills feature would carry the whole skill, `dist/` zip and all —
but it's a Business / Enterprise / Healthcare / Edu feature, not in the Free,
Plus or Pro rollout. This directory is the backup that works anyway, and it
carries **the same skill, not a reduced one**.

## What "the same" means

Each file in `paste/` is built by `build.py` from the real source, verbatim:

```
instructions.md      the platform adapter — free-tier deltas only
../SKILL.md          the whole router, unabridged (frontmatter stripped)
../references/*.md   the ones this module cites, in full
../flows/<name>.md   the module itself
```

Nothing is summarised or trimmed to fit. One paste file per module, discovered
from `flows/`, so a module that exists on Claude exists here the moment you
rebuild. `instructions.md` is the only file written for this platform.

## The three routes

| | Setup | Free account | Best for |
|---|---|---|---|
| **Paste-in prompt** | none | yes | the room |
| **Project** | 2 min, per person | yes, within a small upload allowance | continuing afterwards |
| **Custom GPT** | instructor builds once, needs a paid plan | attendees can use one | handing out a link |

**Paste-in.** Open a new chat, paste the whole of `paste/<module>.md` as the
first message, answer the question it asks back. Host the files somewhere
copyable before the session — asking a room to clone a repo costs more minutes
than the module you're trying to run.

**Project.** `instructions.md` in the Instructions box; `../SKILL.md`, the
module, and any references it cites attached as files. Free accounts have a
small daily upload allowance, so attach one module at a time.

**Custom GPT.** Same shape, built once and shared as a link. The Instructions
box caps at 8,000 characters; `build.py` fails the build if `instructions.md`
goes over.

## What a free account can't do

Not omissions from the skill — capabilities the platform doesn't have. The
adapter states them up front so modules behave like a Claude session with no
tools rather than like a different skill:

- **Search works.** Everything else doesn't: no file writing, no connected
  accounts, no scheduled tasks.
- **Nothing outside the chat changes.** Where a module would create or send
  something, it produces the exact thing a person needs to do it by hand and
  says plainly that it isn't done.
- **Context is small.** `build.py` prints each paste file's budget on every
  run. One module per chat, never reprint a draft, keep the header table
  current so a fresh chat can resume from a pasted brief.

Tier boundaries move — test the route you're depending on with an actual free
account a day before, not at the start of the session.

## Maintaining it

From the skill directory:

```sh
python3 portable/build.py          # regenerate paste/
python3 portable/build.py --check  # verify, change nothing
```

Edit `../SKILL.md`, `../flows/*.md`, `../references/*.md` or
`instructions.md` — never `paste/`, which is generated and says so at the top
of every file. `--check` runs in CI and fails on a stale build, a module
missing frontmatter, a module citing a reference that doesn't exist, or a
leftover paste file whose module was renamed or removed.

The paste files work in any chat assistant, not just ChatGPT.
