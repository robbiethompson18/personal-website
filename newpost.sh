#!/bin/bash
# Usage: ./newpost.sh <slug> — scaffolds posts/<slug>/FINAL_POST.md as a draft.
set -e
slug=$1
[ -n "$slug" ] || { echo "usage: ./newpost.sh <slug>"; exit 1; }
post=posts/$slug/FINAL_POST.md
[ ! -e "$post" ] || { echo "$post already exists"; exit 1; }
mkdir -p "posts/$slug"
printf -- '---\ntitle: %s\ndate: %s\ndraft: true\n---\n\n' "$slug" "$(date +%F)" > "$post"
echo "$post"
