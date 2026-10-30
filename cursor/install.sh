#!/usr/bin/env bash
# Install Replica skills for Cursor.
# Default: .cursor/skills in the current project.
# --global: ~/.cursor/skills
# --project DIR: that project's .cursor/skills
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: cursor/install.sh [--project DIR | --global]

  (no flag)     install into ./.cursor/skills
  --project DIR install into DIR/.cursor/skills
  --global      install into ~/.cursor/skills

Safe to run again. Replica skill folders and replica-tools/ in the
destination are replaced. Other skills there are left alone.
EOF
}

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MODE=""
PROJECT="$(pwd)"

while [ $# -gt 0 ]; do
  case "$1" in
    --project)
      if [ -n "$MODE" ]; then
        echo "Pass either --project or --global, not both." >&2
        exit 2
      fi
      MODE="project"
      PROJECT="${2:?--project needs a directory}"
      shift 2
      ;;
    --global)
      if [ -n "$MODE" ]; then
        echo "Pass either --project or --global, not both." >&2
        exit 2
      fi
      MODE="global"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [ "$MODE" = "global" ]; then
  DEST="${HOME}/.cursor/skills"
else
  DEST="${PROJECT}/.cursor/skills"
fi

sync_dir() {
  local src="$1" dest="$2"
  mkdir -p "$dest"
  if command -v rsync >/dev/null 2>&1; then
    rsync -a --delete "$src/" "$dest/"
  else
    rm -rf "$dest"
    mkdir -p "$dest"
    cp -a "$src/." "$dest/"
  fi
}

mkdir -p "$DEST"
found=0
for skill in "$ROOT"/cursor/skills/*; do
  [ -d "$skill" ] || continue
  name="$(basename "$skill")"
  sync_dir "$skill" "$DEST/$name"
  found=$((found + 1))
done
sync_dir "$ROOT/tools" "$DEST/replica-tools"

if [ "$found" -lt 12 ]; then
  echo "Expected 12 skills, installed $found from $ROOT/cursor/skills" >&2
  exit 1
fi

echo "Installed $found Replica skills into $DEST"
echo "Tools: $DEST/replica-tools"
echo "In Cursor, type / in chat and choose replica or replica-recon."
