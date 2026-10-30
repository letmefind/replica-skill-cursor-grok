#!/usr/bin/env bash
# Put the Replica pack on this computer and print the skills to save.
# Default location: /home/box/replica-skill (override with REPLICA_HOME).
set -euo pipefail

SRC="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${REPLICA_HOME:-/home/box/replica-skill}"
URL="https://github.com/letmefind/replica-skill-cursor-grok.git"

sync_tree() {
  local from="$1" to="$2"
  mkdir -p "$to"
  if command -v rsync >/dev/null 2>&1; then
    rsync -a --delete --exclude .git "$from/" "$to/"
  else
    rm -rf "$to"
    mkdir -p "$to"
    cp -a "$from/." "$to/"
  fi
}

copy_pack() {
  local from="$1" to="$2"
  sync_tree "$from/tools" "$to/tools"
  sync_tree "$from/cursor" "$to/cursor"
  sync_tree "$from/grok-bot" "$to/grok-bot"
  sync_tree "$from/docs" "$to/docs"
  for f in LICENSE README.md; do
    if [ -f "$from/$f" ]; then
      cp "$from/$f" "$to/$f"
    fi
  done
}

same_dir() {
  [ "$(cd "$1" && pwd)" = "$(cd "$2" && pwd)" ]
}

mkdir -p "$(dirname "$DEST")"

if [ -d "$DEST" ] && same_dir "$SRC" "$DEST"; then
  if [ -d "$DEST/.git" ]; then
    git -C "$DEST" pull --ff-only \
      || echo "Could not fast-forward $DEST. Keeping the files already there." >&2
  fi
else
  if [ ! -d "$DEST/.git" ]; then
    if [ -d "$SRC/.git" ]; then
      git clone "$SRC" "$DEST"
    else
      git clone "$URL" "$DEST"
    fi
  else
    git -C "$DEST" pull --ff-only \
      || echo "Could not fast-forward $DEST. Copying files from $SRC." >&2
  fi
  if [ -f "$SRC/tools/parity.py" ]; then
    copy_pack "$SRC" "$DEST"
  fi
fi

if [ ! -f "$DEST/tools/parity.py" ]; then
  echo "Tools are not at $DEST/tools. Clone $URL and run this script again." >&2
  exit 1
fi

chmod a+r "$DEST"/tools/*.py "$DEST"/tools/*.json 2>/dev/null || true

echo "Replica tools are at $DEST/tools"
echo "REPLICA_HOME=$DEST"
echo
echo "Save each skill below. Use the name, the description, and the body verbatim."
echo "The body is everything after the closing --- line of the frontmatter."
echo "Descriptions are single-quoted. Take the text inside the quotes, and turn each doubled single quote into one single quote."
echo

python3 - "$DEST/grok-bot/skills" << 'PY'
import sys
from pathlib import Path

root = Path(sys.argv[1])
skills = sorted(p for p in root.iterdir() if (p / "SKILL.md").is_file())
if len(skills) != 12:
    sys.stderr.write("Expected 12 skills in %s, found %d\n" % (root, len(skills)))
    sys.exit(1)
for skill in skills:
    name = ""
    for line in (skill / "SKILL.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("name:"):
            name = line.split(":", 1)[1].strip()
            break
    print(name)
    print("  %s" % (skill / "SKILL.md"))
PY
