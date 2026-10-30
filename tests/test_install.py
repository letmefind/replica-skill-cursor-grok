"""Run both installers in a temp directory and check they can run twice."""

import hashlib
import os
import stat
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def tree_hash(path):
    digest = hashlib.sha256()
    for file in sorted(p for p in Path(path).rglob("*") if p.is_file()):
        digest.update(str(file.relative_to(path)).encode())
        digest.update(file.read_bytes())
    return digest.hexdigest()


class Install(unittest.TestCase):
    def test_cursor_project_install_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "app"
            script = ROOT / "cursor" / "install.sh"
            self.assertTrue(script.stat().st_mode & stat.S_IXUSR)
            for _ in range(2):
                subprocess.check_call(["bash", str(script), "--project", str(project)], cwd=str(ROOT))
            dest = project / ".cursor" / "skills"
            self.assertTrue((dest / "replica-recon" / "SKILL.md").is_file())
            self.assertTrue((dest / "replica" / "SKILL.md").is_file())
            self.assertTrue((dest / "replica-tools" / "parity.py").is_file())
            self.assertTrue((dest / "replica-tools" / "themes.json").is_file())
            self.assertTrue((dest / "replica-design" / "tokens.json").is_file())
            self.assertFalse((dest / "replica-tools" / "SKILL.md").exists())
            first = tree_hash(dest)
            subprocess.check_call(["bash", str(script), "--project", str(project)], cwd=str(ROOT))
            self.assertEqual(first, tree_hash(dest))
            subprocess.check_call(
                [
                    "python3",
                    str(dest / "replica-tools" / "contrast.py"),
                    str(dest / "replica-design" / "tokens.json"),
                ],
                cwd=str(project),
            )
            subprocess.check_call(
                [
                    "python3",
                    str(dest / "replica-tools" / "parity.py"),
                    str(dest / "replica-recon" / "features.csv"),
                ],
                cwd=str(project),
            )

    def test_cursor_global_install(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = os.environ.copy()
            env["HOME"] = tmp
            subprocess.check_call(["bash", str(ROOT / "cursor" / "install.sh"), "--global"], cwd=str(ROOT), env=env)
            dest = Path(tmp) / ".cursor" / "skills" / "replica-backend" / "SKILL.md"
            self.assertTrue(dest.is_file())
            proc = subprocess.run(
                ["bash", str(ROOT / "cursor" / "install.sh"), "--global", "--project", tmp],
                cwd=str(ROOT),
                env=env,
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(proc.returncode, 0)

    def test_grok_install_copies_tools_and_lists_skills(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "replica-skill"
            env = os.environ.copy()
            env["REPLICA_HOME"] = str(dest)
            script = ROOT / "grok-bot" / "install.sh"
            proc = subprocess.run(
                ["bash", str(script)],
                cwd=str(ROOT),
                env=env,
                capture_output=True,
                text=True,
                check=True,
            )
            self.assertIn("replica-recon", proc.stdout)
            self.assertIn("\nreplica\n", "\n" + proc.stdout)
            self.assertTrue((dest / "tools" / "parity.py").is_file())
            self.assertTrue((dest / "tools" / "themes.json").is_file())
            self.assertTrue((dest / "grok-bot" / "skills" / "replica-build" / "SKILL.md").is_file())
            self.assertTrue((dest / "cursor" / "skills" / "replica-launch" / "listing.example.json").is_file())
            first = tree_hash(dest / "tools")
            subprocess.check_call(["bash", str(script)], cwd=str(ROOT), env=env)
            self.assertEqual(first, tree_hash(dest / "tools"))
            subprocess.check_call(
                [
                    "python3",
                    str(dest / "tools" / "listing.py"),
                    str(dest / "cursor" / "skills" / "replica-launch" / "listing.example.json"),
                ]
            )
