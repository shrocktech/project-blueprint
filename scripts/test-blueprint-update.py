"""Run with Python's standard library; synthetic repositories only."""
import importlib.util
import json
import io
import os
import sys
from contextlib import redirect_stdout
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

    def test_review_scope_and_updater_notice(self):
        for name in ("README.md", "AGENTS.md", "assets/graphic.png", "scripts/setup-labels.sh",
                     "scripts/blueprint-update.py", ".github/workflows/adopt-release.yml",
                     "template/AGENTS.md", "template/design/README.md"):
            self.write(self.source, name, "changed\n")
        _, review = self.plan()
        self.assertEqual(len(review), 3)
        self.assertEqual(sum("Updater implementation" in x for x in review), 1)
        self.assertTrue(any("template/AGENTS.md" in x for x in review))

    def test_not_configured_is_distinct_from_invalid(self):
        with self.assertRaises(updater.NotConfigured):
            updater.config(self.target, "example/source")
        cfg = {"source": "example/source", "integrationBranch": "develop",
               "adopted": {"tag": "VERIFIED_RELEASE_TAG", "commit": "VERIFIED_RELEASE_COMMIT"}}
        self.write(self.target, ".github/blueprint-update.json", json.dumps(cfg))
        updater.config(self.target, "example/source", adoption=False)
        with self.assertRaises(updater.NotConfigured):
            updater.config(self.target, "example/source")
        cfg["source"] = "wrong/source"
        self.write(self.target, ".github/blueprint-update.json", json.dumps(cfg))
        with self.assertRaises(ValueError):
            updater.config(self.target, "example/source")

    def orchestrated_fixture(self):
        updater.git(self.source, "tag", "v1.0.0", self.base)
        self.write(self.source, "template/standards/checks.md", "incoming\n")
        self.latest = self.commit()
        updater.git(self.source, "tag", "v1.1.0", self.latest)
        updater.git(self.target, "init", "-q", "-b", "main")
        updater.git(self.target, "config", "user.name", "Fixture")
        updater.git(self.target, "config", "user.email", "fixture@example.invalid")
        cfg = {"source": "example/source", "integrationBranch": "develop",
               "adopted": {"tag": "VERIFIED_RELEASE_TAG", "commit": "VERIFIED_RELEASE_COMMIT"}}
        self.write(self.target, ".github/blueprint-update.json", json.dumps(cfg))
        updater.git(self.target, "add", ".")
        updater.git(self.target, "commit", "-qm", "Default routing")
        self.main_head = updater.git(self.target, "rev-parse", "HEAD")
        updater.git(self.target, "checkout", "-qb", "develop")
        cfg["adopted"] = {"tag": "v1.0.0", "commit": self.base}
        self.write(self.target, ".github/blueprint-update.json", json.dumps(cfg))
        updater.git(self.target, "add", ".")
        updater.git(self.target, "commit", "-qm", "Verified integration adoption")
        self.remote = Path(self.tmp.name) / "remote.git"
        updater.run("git", "clone", "--bare", str(self.target), str(self.remote))
        updater.git(self.target, "remote", "add", "origin", str(self.remote))
        self.issue = {"number": 1, "html_url": "https://example.invalid/issues/1", "state": "open",
                      "user": {"login": "github-actions[bot]"},
                      "body": f"<!-- blueprint-update:{self.latest} -->"}
        self.issue_exists = False
        self.pr_exists = False

    def invoke_fixture(self):
        updater.git(self.target, "reset", "--hard", "HEAD")
        updater.git(self.target, "checkout", "--detach", "main")
        real_run = updater.run
        def local_clone(*args, **kwargs):
            if "clone" in args and "https://github.com/example/source.git" in args:
                return real_run("git", "clone", "--bare", str(self.source), args[-1])
            return real_run(*args, **kwargs)
        def mock_api(path, payload=None, method=None):
            if path.startswith("repos/example/source/releases"):
                return [{"draft": False, "prerelease": False, "tag_name": "v1.1.0", "published_at": "2026-01-01"}]
            if "/issues?" in path:
                return [self.issue] if self.issue_exists else []
            if path.endswith("/issues"):
                self.issue_exists = True
                return self.issue
            if "/pulls?" in path:
                return [{"state": "open", "base": {"ref": "develop"}, "html_url": "https://example.invalid/pull/2"}] if self.pr_exists else []
            if path.endswith("/pulls"):
                self.pr_exists = True
                return {"html_url": "https://example.invalid/pull/2"}
            raise AssertionError(path)
        output = io.StringIO()
        with patch.object(updater, "run", side_effect=local_clone), patch.object(updater, "api", side_effect=mock_api), \
             patch.dict(os.environ, {"GITHUB_REPOSITORY": "example/target", "GITHUB_STEP_SUMMARY": ""}), \
             patch.object(sys, "argv", ["updater", "--source", "example/source", "--target", str(self.target)]), redirect_stdout(output):
            updater.main()
        return output.getvalue()

    def test_main_develop_and_waiting_states(self):
        self.orchestrated_fixture()
        self.assertIn("Prepared PR", self.invoke_fixture())
        self.assertIn("Waiting on agent", self.invoke_fixture())
        updater.git(self.target, "reset", "--hard", "HEAD")
        updater.git(self.target, "checkout", "develop")
        self.write(self.target, "application.txt", "active work\n")
        updater.git(self.target, "add", ".")
        updater.git(self.target, "commit", "-qm", "Advance integration")
        updater.git(self.target, "push", "origin", "develop")
        self.assertIn("Waiting on agent", self.invoke_fixture())
        # Waiting does not advance adoption or the default branch.
        self.assertEqual(updater.git(self.target, "rev-parse", "main"), self.main_head)
        self.assertEqual(updater.config(self.target, "example/source")["adopted"]["commit"], self.base)
        self.issue["state"] = "closed"
        self.assertIn("closed maintenance issue", self.invoke_fixture())

    def test_verified_integration_adoption_without_default_promotion(self):
        self.orchestrated_fixture()
        cfg = updater.config(self.target, "example/source")
        cfg["adopted"] = {"tag": "v1.1.0", "commit": self.latest}
        self.write(self.target, ".github/blueprint-update.json", json.dumps(cfg))
        updater.git(self.target, "add", ".")
        updater.git(self.target, "commit", "-qm", "Verified integration update")
        updater.git(self.target, "push", "origin", "develop")
        self.assertIn("Stable guidance current", self.invoke_fixture())
        self.assertEqual(updater.git(self.target, "rev-parse", "main"), self.main_head)
        self.assertFalse(self.issue_exists)

    def test_routing_mismatch_is_not_waiting(self):
        self.orchestrated_fixture()
        cfg = updater.config(self.target, "example/source")
        cfg["integrationBranch"] = "other"
        self.write(self.target, ".github/blueprint-update.json", json.dumps(cfg))
        updater.git(self.target, "add", ".")
        updater.git(self.target, "commit", "-qm", "Routing conflict fixture")
        updater.git(self.target, "push", "origin", "develop")
        with self.assertRaisesRegex(ValueError, "routing disagrees"):
            self.invoke_fixture()

    def test_diverged_source_is_not_waiting(self):
        self.orchestrated_fixture()
        updater.git(self.source, "checkout", "--orphan", "divergent")
        updater.git(self.source, "commit", "-qm", "Unrelated source history")
        updater.git(self.source, "tag", "-f", "v1.1.0", "HEAD")
        with self.assertRaisesRegex(ValueError, "Divergence/rollback"):
            self.invoke_fixture()

    def test_tag_integrity_failure_is_not_waiting(self):
        self.orchestrated_fixture()
        updater.git(self.source, "tag", "-f", "v1.0.0", self.latest)
        with self.assertRaisesRegex(ValueError, "integrity mismatch"):
            self.invoke_fixture()

    def test_pagination(self):
        with patch.object(updater, "api", side_effect=[[{}] * 100, [{"id": 2}]]):
            self.assertEqual(len(updater.pages("repos/example/repo/issues?state=all")), 101)
        with patch.object(updater, "api", return_value={"bad": "response"}):
            with self.assertRaises(ValueError):
                updater.pages("repos/example/repo/issues")


if __name__ == "__main__":
    unittest.main(verbosity=2)
