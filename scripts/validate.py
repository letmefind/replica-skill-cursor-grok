#!/usr/bin/env python3
"""Check Replica skill files: frontmatter, names, and paths that must exist."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIMIT = 1024
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
HOME_PREFIX = "${REPLICA_HOME:-/home/box/replica-skill}/"
EM = chr(0x2014)
TEXT_SUFFIXES = {".md", ".py", ".sh", ".yml", ".yaml", ".json", ".csv", ".ts", ".txt"}
SKIP_DIRS = {".git", "__pycache__", ".venv", "replica-tools"}


def parse_frontmatter(text):
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not match:
        raise ValueError("missing frontmatter")
    raw = match.group(1)
    body = match.group(2)
    name = None
    desc = None
    for line in raw.splitlines():
        if line.startswith("name:"):
            name = line.split(":", 1)[1].strip()
        elif line.startswith("description:"):
            value = line.split(":", 1)[1].strip()
            if len(value) >= 2 and value[0] == "'" and value[-1] == "'":
                desc = value[1:-1].replace("''", "'")
            elif len(value) >= 2 and value[0] == '"' and value[-1] == '"':
                desc = value[1:-1]
            else:
                desc = value
    return name, desc, body


def check_skill(path, kind):
    errors = []
    text = path.read_text(encoding="utf-8")
    folder = path.parent.name
    try:
        name, desc, body = parse_frontmatter(text)
    except ValueError as exc:
        return ["%s: %s" % (path.relative_to(ROOT), exc)]
    rel = path.relative_to(ROOT)
    if name != folder:
        errors.append("%s: name %r does not match folder %r" % (rel, name, folder))
    if not name or not NAME_RE.match(name):
        errors.append("%s: name %r must be lowercase letters, numbers, and hyphens" % (rel, name))
    if not desc or not desc.strip():
        errors.append("%s: description is missing" % rel)
    elif len(desc) > LIMIT:
        errors.append("%s: description is %d characters (limit %d)" % (rel, len(desc), LIMIT))
    if desc is not None and "\n" in desc:
        errors.append("%s: description must be one line" % rel)
    if not body.strip().startswith("# "):
        errors.append("%s: body does not start with a heading" % rel)

    for tool in re.findall(r"\$TOOLS/([A-Za-z0-9_.-]+)", text):
        if not (ROOT / "tools" / tool).is_file():
            errors.append("%s: missing tools/%s" % (rel, tool))

    for raw in re.findall(re.escape(HOME_PREFIX) + r"([A-Za-z0-9_./-]+)", text):
        rel_path = raw.rstrip(").,`")
        if not (ROOT / rel_path).exists():
            errors.append("%s: missing %s" % (rel, rel_path))

    if kind == "cursor":
        for sib in sorted(path.parent.iterdir()):
            if not sib.is_file() or sib.name == "SKILL.md":
                continue
            if sib.name not in text:
                errors.append("%s: does not mention %s beside it" % (rel, sib.name))
        if "$TOOLS/" in text and "## Tools" not in text:
            errors.append("%s: uses $TOOLS without a Tools section" % rel)
    else:
        cursor_dir = ROOT / "cursor" / "skills" / folder
        if cursor_dir.is_dir():
            for sib in sorted(cursor_dir.iterdir()):
                if not sib.is_file() or sib.name == "SKILL.md":
                    continue
                needle = "cursor/skills/%s/%s" % (folder, sib.name)
                if needle not in text:
                    errors.append("%s: does not point at %s" % (rel, needle))
        if "$TOOLS/" in text:
            errors.append("%s: uses $TOOLS; Grok Bot skills need the absolute tools path" % rel)
        if "in this folder" in text:
            errors.append("%s: still says a template is in this folder" % rel)

    if EM in text:
        errors.append("%s: contains an em dash" % rel)
    return errors


def scan_tree():
    errors = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = path.relative_to(ROOT)
        if EM in text:
            errors.append("%s: contains an em dash" % rel)
    return errors


def main():
    errors = []
    found = {"cursor": [], "grok-bot": []}
    for kind, base in (("cursor", ROOT / "cursor" / "skills"), ("grok-bot", ROOT / "grok-bot" / "skills")):
        for path in sorted(base.glob("*/SKILL.md")):
            found[kind].append(path.parent.name)
            errors.extend(check_skill(path, "cursor" if kind == "cursor" else "grok"))
    if found["cursor"] != found["grok-bot"]:
        errors.append("skill folders differ: %s vs %s" % (found["cursor"], found["grok-bot"]))
    if len(found["cursor"]) != 12:
        errors.append("expected 12 skills, found %d" % len(found["cursor"]))
    errors.extend(scan_tree())
    if errors:
        for err in errors:
            print(err, file=sys.stderr)
        print("%d problem(s)" % len(errors), file=sys.stderr)
        return 1
    print("ok: %d skills in each port" % len(found["cursor"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
