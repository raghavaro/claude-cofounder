#!/usr/bin/env python3
"""Inline the marketing skill's express positioning pass into flows/position.md.

This skill runs positioning itself rather than handing off, so the express pass
has to live here — but a second hand-maintained copy of it would drift from the
original within a month. So it's generated: the block between the EXPRESS
markers is lifted verbatim from marketing-workshop's positioning flow at build
time, and CI fails if it goes stale.

The result is committed, so an installed copy of this skill is self-contained
and never needs the marketing skill at runtime. The dependency is on the repo,
not on the room.

    python3 cofounder-workshop/scripts/build_express.py          # rewrite
    python3 cofounder-workshop/scripts/build_express.py --check  # verify
"""

import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
TARGET = SKILL_DIR / "flows" / "position.md"
SOURCE = SKILL_DIR.parent / "marketing-workshop" / "flows" / "positioning.md"

MARKER = "EXPRESS"
HEADING = "## Express pass — ten minutes"


def express_pass():
    """The express-pass section of the marketing skill's positioning flow,
    minus its own heading and its closing hand-back line, which belong to that
    flow's context rather than this one."""
    text = SOURCE.read_text()
    start = text.find(HEADING)
    if start == -1:
        raise SystemExit(f"! {SOURCE} has no '{HEADING}' section to lift")
    body = text[start + len(HEADING):]
    end = re.search(r"\n(?=## )", body)
    if end:
        body = body[: end.start()]
    body = body.replace("Then go back to the flow they came for.", "").strip()
    return body


def render():
    return (
        "> Lifted verbatim from `marketing-workshop`'s positioning flow by\n"
        "> `scripts/build_express.py`. Edit it there, not here.\n\n"
        + express_pass()
        + "\n"
    )


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if not SOURCE.exists():
        print(f"skipped: {SOURCE} not present (installed standalone, nothing to sync)")
        return 0

    current = TARGET.read_text()
    pattern = re.compile(
        rf"(<!-- {MARKER}:START[^\n]*-->\n).*?(\n<!-- {MARKER}:END -->)", re.S
    )
    if not pattern.search(current):
        raise SystemExit(f"! {TARGET.name} has no {MARKER} block to fill")
    updated = pattern.sub(lambda m: m.group(1) + render() + m.group(2), current)

    if "--check" in argv:
        if updated != current:
            print("! flows/position.md's express pass is stale — rerun build_express.py")
            return 1
        print("express pass: up to date")
        return 0

    TARGET.write_text(updated)
    print("wrote flows/position.md express pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
