#!/usr/bin/env python3
"""Regenerate the parts of SKILL.md that are derived from the modules.

Four blocks: the module table, the routing list, the brief's header table, and
the session timetable. All four are generated from module frontmatter, so adding
`flows/pricing.md` updates the router, the trigger phrases, the brief header
and the schedule in one step — and none of them can drift from the modules
they describe.

    python3 cofounder/scripts/build_index.py          # rewrite SKILL.md
    python3 cofounder/scripts/build_index.py --check  # verify, change nothing
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from flowmeta import FlowError, modules  # noqa: E402

SKILL_DIR = Path(__file__).resolve().parent.parent
SKILL_MD = SKILL_DIR / "SKILL.md"

EMPTY = "_No modules yet._"
CORE_HEADER = ["Company", "What it does", "Stage", "Objective this quarter"]
TAIL_HEADER = ["Modules completed", "Last updated"]

# Session blocks that aren't modules. The timetable is the sum of these and the
# modules' own minutes, so it stays honest about what the day actually costs.
OPEN_MINUTES = 5
WRAP_MINUTES = 15


def block(name, body):
    return f"<!-- {name}:START", f"<!-- {name}:END -->", body


def replace(text, name, body):
    pattern = re.compile(
        rf"(<!-- {name}:START[^\n]*-->\n).*?(\n<!-- {name}:END -->)", re.S
    )
    if not pattern.search(text):
        raise SystemExit(f"SKILL.md has no {name} block to fill")
    return pattern.sub(lambda m: m.group(1) + body + m.group(2), text)


def flows_table(mods):
    if not mods:
        return EMPTY + "\n"
    rows = ["| Module | Covers | File | Minutes | Pacing |", "|---|---|---|---|---|"]
    for m in mods:
        rows.append(
            f"| {m['title']} | {m['covers']} | `flows/{m['name']}.md` | "
            f"{m['minutes']} | {m['pacing']} |"
        )
    return "\n".join(rows) + "\n"


def routing_list(mods):
    if not mods:
        return EMPTY + "\n"
    lines = []
    for m in mods:
        phrases = " / ".join(f'"{t}"' for t in m["triggers"])
        lines.append(f"- {phrases} → **{m['name']}**")
    return "\n".join(lines) + "\n"


def header_table(mods):
    fields = list(CORE_HEADER)
    for m in mods:
        for extra in m["adds-header"]:
            if extra not in fields:
                fields.append(extra)
    fields += TAIL_HEADER
    rows = "\n".join(f"| {f} | |" for f in fields)
    return (
        "```markdown\n# Company Brief — [company name]\n\n"
        "| Field | Value |\n|---|---|\n" + rows + "\n```\n"
    )


def timetable(mods):
    if not mods:
        return EMPTY + "\n"
    rows = ["| Time | Block | What exists by the end of it |", "|---|---|---|"]
    at = 0

    def stamp(minutes):
        nonlocal at
        start, at = at, at + minutes
        return f"{start // 60}:{start % 60:02d}–{at // 60}:{at % 60:02d}"

    rows.append(f"| {stamp(OPEN_MINUTES)} | Open | The shape of the session, and what exists by the end |")
    for m in mods:
        rows.append(f"| {stamp(m['minutes'])} | {m['title']} ({m['minutes']} min) | {m['covers']} |")
    rows.append(f"| {stamp(WRAP_MINUTES)} | Wrap | Checkpoint round; every decision has an owner and a date |")

    total = at
    note = (
        f"\nTotal: **{total // 60}h {total % 60:02d}m** of session time "
        f"({OPEN_MINUTES} open + {total - OPEN_MINUTES - WRAP_MINUTES} modules "
        f"+ {WRAP_MINUTES} wrap), before any break, demo or show-and-tell. "
        "Subtract those from the session's actual length before promising this "
        "schedule to anyone.\n"
    )
    return "\n".join(rows) + "\n" + note


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    try:
        mods = modules()
    except FlowError as exc:
        print(f"! {exc}")
        return 1

    current = SKILL_MD.read_text()
    updated = current
    for name, body in (
        ("FLOWS", flows_table(mods)),
        ("ROUTING", routing_list(mods)),
        ("HEADER", header_table(mods)),
        ("TIMETABLE", timetable(mods)),
    ):
        updated = replace(updated, name, body)

    if "--check" in argv:
        if updated != current:
            print("! SKILL.md's generated blocks are stale — rerun build_index.py")
            return 1
        print(f"SKILL.md index: up to date ({len(mods)} module{'s' if len(mods) != 1 else ''})")
        return 0

    SKILL_MD.write_text(updated)
    print(f"wrote SKILL.md index ({len(mods)} module{'s' if len(mods) != 1 else ''})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
