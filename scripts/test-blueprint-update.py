"""Run with Python's standard library; synthetic repositories only."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("updater", Path(__file__).with_name("blueprint-update.py"))
updater = importlib.util.module_from_spec(spec)
spec.loader.exec_module(updater)


class ProposalTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.source = Path(self.tmp.name) / "source"
        self.target = Path(self.tmp.name) / "target"
        self.source.mkdir()
        self.target.mkdir()
        updater.git(self.source, "init", "-q")
        updater.git(self.source, "config", "user.name", "Fixture")
        updater.git(self.source, "config", "user.email", "fixture@example.invalid")
        for name, data in {
            "template/standards/checks.md": "shared rule\n",
            "skills/example/SKILL.md": "skill\n",
            "template/AGENTS.md": "project facts\n",
            "template/design/README.md": "design\n",
        }.items():
            self.write(self.source, name, data)
        self.base = self.commit()
        self.write(self.target, "standards/checks.md", "shared rule\n")
        self.write(self.target, ".agents/skills/example/SKILL.md", "skill\n")
        self.write(self.target, "AGENTS.md", "local facts\n")
        self.write(self.target, "design/README.md", "local design\n")

    def write(self, root, name, data):
        p = root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(data)

    def commit(self):
        updater.git(self.source, "add", ".")
        updater.git(self.source, "commit", "-qm", "Fixture")
        return updater.git(self.source, "rev-parse", "HEAD").decode().strip()

    def plan(self):
        return updater.proposal(self.source, self.base, self.commit(), self.target)

    def test_safe_files_only_and_repeat(self):
        for name in ("template/standards/checks.md", "skills/example/SKILL.md", "template/AGENTS.md", "template/design/README.md"):
            self.write(self.source, name, "incoming\n")
        latest = self.commit()
        writes, review = updater.proposal(self.source, self.base, latest, self.target)
        self.assertEqual(set(writes), {"standards/checks.md", ".agents/skills/example/SKILL.md"})
        self.assertEqual(len(review), 2)
        updater.apply(self.target, writes)
        self.assertEqual((self.target / "AGENTS.md").read_text(), "local facts\n")
        self.assertEqual(updater.proposal(self.source, self.base, latest, self.target)[0], {})

    def test_local_edit_and_missing_file_preserved(self):
        self.write(self.source, "template/standards/checks.md", "incoming\n")
        self.write(self.target, "standards/checks.md", "local exception\n")
        latest = self.commit()
        writes, review = updater.proposal(self.source, self.base, latest, self.target)
        self.assertFalse(writes)
        self.assertIn("local content", review[0])
        (self.target / "standards/checks.md").unlink()
        self.assertFalse(updater.proposal(self.source, self.base, latest, self.target)[0])

    def test_new_skills_require_installation(self):
        self.write(self.source, "skills/new/SKILL.md", "new skill\n")
        writes, review = self.plan()
        self.assertFalse(writes)
        self.assertIn("skill selection/installation", review[0])

    def test_removed_owned_file_not_neighbors(self):
        (self.source / "template/standards/checks.md").unlink()
        self.write(self.target, "standards/custom.md", "custom\n")
        writes, _ = self.plan()
        updater.apply(self.target, writes)
        self.assertFalse((self.target / "standards/checks.md").exists())
        self.assertTrue((self.target / "standards/custom.md").exists())

    def test_new_guide_collision(self):
        self.write(self.source, "template/standards/new.md", "upstream\n")
        self.write(self.target, "standards/new.md", "local\n")
        writes, review = self.plan()
        self.assertFalse(writes)
        self.assertIn("local content", review[0])

    def test_symlink_directory_is_not_followed(self):
        outside = Path(self.tmp.name) / "outside"
        outside.mkdir()
        (self.target / "standards/checks.md").unlink()
        (self.target / "standards").rmdir()
        (self.target / "standards").symlink_to(outside, target_is_directory=True)
        self.write(self.source, "template/standards/checks.md", "incoming\n")
        writes, review = self.plan()
        self.assertFalse(writes)
        self.assertIn("symlink", review[0])
        self.assertFalse(list(outside.iterdir()))

    def test_executable_and_binary_are_not_copied(self):
        self.write(self.source, "skills/example/run.sh", "#!/bin/sh\nexit 0\n")
        (self.source / "skills/example/run.sh").chmod(0o755)
        updater.git(self.source, "add", ".")
        updater.git(self.source, "update-index", "--chmod=+x", "skills/example/run.sh")
        updater.git(self.source, "commit", "-qm", "Executable fixture")
        latest = updater.git(self.source, "rev-parse", "HEAD").decode().strip()
        self.assertFalse(updater.proposal(self.source, self.base, latest, self.target)[0])
        self.write(self.source, "template/standards/checks.md", "\0binary")
        self.assertFalse(self.plan()[0])

    def test_scope_rejects_sensitive_and_workflow_paths(self):
        for name in ("template/.env", "template/.github/workflows/run.yml", "skills/example/../../oops", "skills/example/evil name", "template/standards/../AGENTS.md"):
            self.assertIsNone(updater.mapped(name))

    def test_config_source_and_pin_validation(self):
        good = {"source": "example/source", "integrationBranch": "develop", "adopted": {"tag": "v1.0.0", "commit": self.base}}
        self.write(self.target, ".github/blueprint-update.json", json.dumps(good))
        self.assertEqual(updater.config(self.target, "example/source"), good)
        with self.assertRaises(ValueError):
            updater.config(self.target, "example/other")
        good["adopted"]["commit"] = "main"
        self.write(self.target, ".github/blueprint-update.json", json.dumps(good))
        with self.assertRaises(ValueError):
            updater.config(self.target, "example/source")

    def test_pagination(self):
        with patch.object(updater, "api", side_effect=[[{}] * 100, [{"id": 2}]]):
            self.assertEqual(len(updater.pages("repos/example/repo/issues?state=all")), 101)
        with patch.object(updater, "api", return_value={"bad": "response"}):
            with self.assertRaises(ValueError):
                updater.pages("repos/example/repo/issues")


if __name__ == "__main__":
    unittest.main(verbosity=2)
