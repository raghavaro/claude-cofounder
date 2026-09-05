#!/usr/bin/env python3
"""Reading module frontmatter — shared by the index builder and the paste builder.

A module is `flows/<name>.md` opening with a YAML-ish block. Files starting
with `_` are not modules (`_TEMPLATE.md`), so they're skipped everywhere.
"""

from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
FLOWS_DIR = SKILL_DIR / "flows"

REQUIRED = ("title", "covers", "triggers", "minutes", "pacing")
OPTIONAL = ("order", "after", "adds-header")


class FlowError(ValueError):
    """A module's frontmatter is missing or malformed."""


def split_frontmatter(text):
    """(fields, body). Fields is {} when there's no frontmatter block."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    fields = {}
    for line in text[4:end].split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip()
    return fields, text[end + 5:].lstrip("\n")


def parse(path):
    fields, body = split_frontmatter(path.read_text())
    if not fields:
        raise FlowError(f"{path.name} has no frontmatter block — see AUTHORING.md")
    missing = [k for k in REQUIRED if k not in fields]
    if missing:
        raise FlowError(f"{path.name} frontmatter is missing: {', '.join(missing)}")

    fields["name"] = path.stem
    fields["body"] = body
    fields["path"] = path

    try:
        fields["minutes"] = int(fields["minutes"])
    except ValueError:
        raise FlowError(f"{path.name}: minutes must be a whole number of minutes")
    try:
        fields["order"] = int(fields.get("order", 999))
    except ValueError:
        raise FlowError(f"{path.name}: order must be a number")

    fields["triggers"] = [t.strip() for t in fields["triggers"].split(";") if t.strip()]
    if not fields["triggers"]:
        raise FlowError(f"{path.name}: needs at least one trigger phrase")
    fields["adds-header"] = [
        h.strip() for h in fields.get("adds-header", "").split(",") if h.strip()
    ]
    return fields


def modules():
    """Every module, in the order they run."""
    found = []
    for path in sorted(FLOWS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        found.append(parse(path))
    return sorted(found, key=lambda f: (f["order"], f["name"]))
