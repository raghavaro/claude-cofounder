"""Consistency checks for the cofounder skill.

Most of this skill is markdown pointing at other markdown, and its router,
brief header and timetable are generated from module frontmatter. The failures
that matter are a module that doesn't declare itself properly, a generated
block nobody rebuilt, and a reference cited but never written.
"""

import re
import sys
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL / "scripts"))

from flowmeta import FlowError, modules, parse  # noqa: E402
import build_index  # noqa: E402


def module_paths():
    return [p for p in sorted((SKILL / "flows").glob("*.md")) if not p.name.startswith("_")]


class TestModuleFrontmatter(unittest.TestCase):
    def test_every_module_declares_itself(self):
        for path in module_paths():
            with self.subTest(module=path.name):
                try:
                    parse(path)
                except FlowError as exc:
                    self.fail(str(exc))

    def test_template_is_not_a_module(self):
        names = [p.name for p in module_paths()]
        self.assertNotIn("_TEMPLATE.md", names)

    def test_triggers_are_distinct_across_modules(self):
        seen = {}
        for mod in modules():
            for trigger in mod["triggers"]:
                key = trigger.lower()
                with self.subTest(trigger=trigger):
                    self.assertNotIn(
                        key, seen,
                        f"'{trigger}' routes to both {seen.get(key)} and {mod['name']}",
                    )
                seen[key] = mod["name"]


class TestGeneratedBlocks(unittest.TestCase):
    def test_skill_md_index_is_current(self):
        self.assertEqual(
            build_index.main(["--check"]), 0,
            "SKILL.md's generated blocks are stale — rerun scripts/build_index.py",
        )

    def test_declared_header_fields_reach_the_brief_table(self):
        skill = (SKILL / "SKILL.md").read_text()
        header = re.search(r"# Company Brief.*?```", skill, re.S)
        self.assertIsNotNone(header, "SKILL.md has no brief header block")
        for mod in modules():
            for field in mod["adds-header"]:
                with self.subTest(module=mod["name"], field=field):
                    self.assertIn(
                        f"| {field} |", header.group(0),
                        f"{mod['name']} declares header field '{field}' but the "
                        "generated table doesn't carry it",
                    )


class TestReferencesResolve(unittest.TestCase):
    def test_cited_files_exist(self):
        cited = re.compile(r"`((?:flows|references|templates|scripts|portable)/[A-Za-z0-9_./-]+)`")
        docs = [p for p in sorted(SKILL.rglob("*.md")) if "portable/paste" not in str(p)]
        for doc in docs:
            for path in sorted(set(cited.findall(doc.read_text()))):
                with self.subTest(doc=doc.name, path=path):
                    self.assertTrue(
                        (SKILL / path).exists(),
                        f"{doc.name} cites {path}, which doesn't exist",
                    )


class TestPortableParity(unittest.TestCase):
    def test_every_module_has_a_paste_file(self):
        mods = {p.stem for p in module_paths()}
        pastes = {p.stem for p in (SKILL / "portable" / "paste").glob("*.md")}
        self.assertEqual(
            mods, pastes,
            "portable/paste is out of step with flows/ — rerun portable/build.py",
        )


class TestSkillMetadata(unittest.TestCase):
    def test_description_fits_the_frontmatter_limit(self):
        """1024 chars is the agentskills.io / ChatGPT cap; over it the skill
        can fail to load rather than merely look untidy."""
        text = (SKILL / "SKILL.md").read_text()
        description = re.search(r"^description: (.+)$", text, re.M)
        self.assertIsNotNone(description, "SKILL.md frontmatter has no description")
        self.assertLessEqual(len(description.group(1)), 1024)


if __name__ == "__main__":
    unittest.main()
