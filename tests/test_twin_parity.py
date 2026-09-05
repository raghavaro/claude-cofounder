"""The two cofounder skills share most of their content — pin what must match.

`cofounder` hands positioning off to the marketing skill; `cofounder-workshop`
runs an express pass and needs nothing else installed. Everything else is meant
to be the same file. Two near-identical skills drift silently, so the files that
are supposed to match are asserted here and the ones that legitimately differ
are listed explicitly — diverging further is then a deliberate act with a test
to update, not something noticed months later.

Skipped when the twin isn't present, which is the case for an installed copy.
"""

import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
TWIN = SKILL.parent / "cofounder"

SHARED = [
    "AUTHORING.md",
    "flows/_TEMPLATE.md",
    "flows/base.md",
    "portable/README.md",
    "portable/build.py",
    "portable/instructions.md",
    "scripts/build_index.py",
    "scripts/build_skill_zip.py",
    "scripts/flowmeta.py",
    "tests/test_skill_consistency.py",
]

# Why each of these is allowed to differ:
DIVERGENT = {
    "SKILL.md": "names the skill, and explains which twin this is",
    "Makefile": "the workshop twin also syncs the express pass",
    "flows/position.md": "the whole point — delegation versus express pass",
    "flows/copy.md": "workshop twin only",
    "flows/icp.md": "workshop twin only",
    "flows/page.md": "workshop twin only",
    "references/design-system.md": "workshop twin only — the page module's design system",
    "references/nextjs-starter.md": "workshop twin only — the page module's starter",
    "scripts/build_express.py": "workshop twin only",
}


@unittest.skipUnless(TWIN.exists(), "twin skill not present (standalone install)")
class TestTwinParity(unittest.TestCase):
    def test_shared_files_are_identical(self):
        for name in SHARED:
            here, there = SKILL / name, TWIN / name
            with self.subTest(file=name):
                self.assertTrue(there.exists(), f"{name} is missing from the twin")
                self.assertEqual(
                    here.read_text(), there.read_text(),
                    f"{name} differs between cofounder-workshop and cofounder. "
                    "Sync it, or move it to DIVERGENT with a reason.",
                )

    def test_divergent_files_actually_differ(self):
        """A file listed as divergent that has become identical is either a
        stale entry or a sync that shouldn't have happened."""
        for name, reason in DIVERGENT.items():
            here, there = SKILL / name, TWIN / name
            if not there.exists():
                continue
            with self.subTest(file=name, reason=reason):
                self.assertNotEqual(
                    here.read_text(), there.read_text(),
                    f"{name} is listed as divergent ({reason}) but is identical — "
                    "move it to SHARED.",
                )

    def test_no_unlisted_files(self):
        """Every file in either twin is accounted for as shared or divergent,
        so a new file can't quietly appear in one and not the other."""
        def tracked(root):
            return {
                p.relative_to(root).as_posix()
                for p in root.rglob("*")
                if p.is_file()
                and "dist" not in p.parts
                and "__pycache__" not in p.parts
                and "paste" not in p.parts
                and p.name != "test_twin_parity.py"
            }

        accounted = set(SHARED) | set(DIVERGENT)
        for root, label in ((SKILL, "cofounder-workshop"), (TWIN, "cofounder")):
            for name in sorted(tracked(root) - accounted):
                with self.subTest(skill=label, file=name):
                    self.fail(f"{label}/{name} is in neither SHARED nor DIVERGENT")


if __name__ == "__main__":
    unittest.main()
