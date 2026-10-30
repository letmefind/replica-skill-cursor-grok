"""Frontmatter, path checks, and the rules this port must keep."""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Sentences from the upstream skills. Both ports have to keep them.
KEPT = {
    "replica-recon": [
        "Never log into an account that is not the user's, never ask for a password, never get past a paywall or a login by any trick.",
        "No crawlers, no bulk downloads, no loops.",
        "Do not read or save the app's JavaScript bundles, decompile its binary, or log its network calls to copy endpoints.",
        "Screenshots are reference.",
    ],
    "replica-architect": [
        "Only official, public APIs with the user's own keys. Never the original app's private endpoints, even if they are visible in a browser.",
    ],
    "replica-design": [
        "Do not trace theirs.",
        "The signature colour plus the signature layout is trade dress, and it changes before launch.",
    ],
    "replica-build": [
        "Never paste the original's HTML, CSS, JavaScript, SVGs or images",
        "Matching what a button does is parity. Matching its sentence is copying.",
    ],
    "replica-backend": [
        "The agent never signs up for services, never types a password, card or live key.",
        "Official, public APIs only, with the user's own keys.",
    ],
    "replica-test": [
        "Never load test, fuzz, script or hammer the original app's servers.",
    ],
    "replica-diff": [
        "Do not chase pixel parity with the original.",
    ],
    "replica-entrepreneur": [
        "Never fabricate.",
        "No fake reviews, ever.",
        "Reviewers are not your testimonials.",
    ],
    "replica-brand": [
        'Never write "available" for a check nobody ran.',
        "must not resemble the original's mark",
    ],
    "replica-launch": [
        "No fake proof.",
        "The original's name stays out",
    ],
    "replica-deploy": [
        "The agent never buys a domain, enters a card,",
        "Not until it is rebranded.",
        "The sweep must be clean. No exceptions.",
    ],
}

CODE_STEPS = [
    "replica-build",
    "replica-backend",
    "replica-test",
    "replica-design",
    "replica-brand",
    "replica-launch",
    "replica-deploy",
    "replica-diff",
]


class Skills(unittest.TestCase):
    def test_validate_script(self):
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate.py")],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)

    def test_rules_survived_both_ports(self):
        for name, lines in KEPT.items():
            for port in ("cursor", "grok-bot"):
                text = " ".join(
                    (ROOT / port / "skills" / name / "SKILL.md").read_text(encoding="utf-8").split()
                )
                for line in lines:
                    self.assertIn(line, text, "%s %s" % (port, name))

    def test_grok_code_steps_delegate(self):
        for name in CODE_STEPS:
            text = (ROOT / "grok-bot" / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("Cursor cloud coding agent", text, name)
            self.assertIn("Do not edit", text, name)

    def test_orchestrator_lists_the_pipeline(self):
        order = [
            "replica-recon",
            "replica-architect",
            "replica-design",
            "replica-build",
            "replica-backend",
            "replica-test",
            "replica-diff",
            "replica-entrepreneur",
            "replica-brand",
            "replica-launch",
            "replica-deploy",
        ]
        for port in ("cursor", "grok-bot"):
            text = (ROOT / port / "skills" / "replica" / "SKILL.md").read_text(encoding="utf-8")
            cursor = 0
            for name in order:
                found = text.find(name, cursor)
                self.assertGreater(found, -1, "%s missing %s" % (port, name))
                cursor = found
            self.assertIn("replica/recon.md", text)
            self.assertIn("replica/deploy.md", text)
