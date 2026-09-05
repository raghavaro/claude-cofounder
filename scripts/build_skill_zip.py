#!/usr/bin/env python3
"""Build dist/cofounder.zip — the whole skill, zipped for platforms
that install a skill from a single .zip (e.g. ChatGPT's chatgpt.com/skills
upload dialog, which reads a .zip/.skill file or a bare SKILL.md).

    python3 cofounder/scripts/build_skill_zip.py          # write dist/
    python3 cofounder/scripts/build_skill_zip.py --check  # verify, change nothing

The zip is a generated file — never hand-edit it. Rerun this after any
change under cofounder/ (other than dist/ itself) and commit the
result, the same convention portable/build.py uses for the paste files.
"""

import sys
import zipfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
SKILL_DIR = SCRIPTS.parent
SKILL_NAME = SKILL_DIR.name
DIST = SKILL_DIR / "dist"
ZIP_PATH = DIST / f"{SKILL_NAME}.zip"

EXCLUDE_DIR_NAMES = {"dist", "__pycache__", ".git"}
EXCLUDE_FILE_NAMES = {".DS_Store"}


def source_files():
    """Every file under the skill directory that belongs in the zip, sorted
    for a deterministic member order."""
    files = []
    for path in SKILL_DIR.rglob("*"):
        if not path.is_file():
            continue
        if EXCLUDE_DIR_NAMES & set(path.relative_to(SKILL_DIR).parts):
            continue
        if path.name in EXCLUDE_FILE_NAMES:
            continue
        files.append(path)
    return sorted(files, key=lambda p: p.relative_to(SKILL_DIR).as_posix())


def build(zip_path):
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in source_files():
            arcname = Path(SKILL_NAME) / path.relative_to(SKILL_DIR)
            zf.write(path, arcname.as_posix())


def read_contents(zip_path):
    """arcname -> bytes, for every member. Used for --check instead of a raw
    byte comparison, since zip headers can carry non-deterministic
    timestamps even when the content is identical."""
    with zipfile.ZipFile(zip_path) as zf:
        return {name: zf.read(name) for name in zf.namelist()}


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    check = "--check" in argv

    if not check:
        build(ZIP_PATH)
        print(f"wrote {ZIP_PATH.relative_to(SKILL_DIR.parent)} ({len(source_files())} files)")
        return 0

    if not ZIP_PATH.exists():
        print(f"! {ZIP_PATH.relative_to(SKILL_DIR.parent)} does not exist — run without --check")
        return 1

    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        fresh_path = Path(tmp) / ZIP_PATH.name
        build(fresh_path)
        fresh, current = read_contents(fresh_path), read_contents(ZIP_PATH)

    if fresh == current:
        print(f"{ZIP_PATH.relative_to(SKILL_DIR.parent)}: up to date ({len(fresh)} files)")
        return 0

    added = sorted(set(fresh) - set(current))
    removed = sorted(set(current) - set(fresh))
    changed = sorted(k for k in fresh.keys() & current.keys() if fresh[k] != current[k])
    print(f"! {ZIP_PATH.relative_to(SKILL_DIR.parent)} is stale — rerun without --check")
    for f in added:
        print(f"    + {f}")
    for f in removed:
        print(f"    - {f}")
    for f in changed:
        print(f"    ~ {f}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
