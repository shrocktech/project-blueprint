#!/usr/bin/env bash
# Requires Bash, jq, and (unless --dry-run) authenticated GitHub CLI.
set -euo pipefail

usage() { printf 'Usage: bash %s OWNER/REPO [--dry-run]\n' "$0" >&2; }
if [[ $# -lt 1 || $# -gt 2 ]]; then usage; exit 2; fi
repo=$1
if [[ ! $repo =~ ^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$ ]]; then usage; exit 2; fi
dry_run=false
if [[ $# -eq 2 ]]; then
  if [[ $2 != --dry-run ]]; then usage; exit 2; fi
  dry_run=true
fi
command -v jq >/dev/null || { printf 'jq is required.\n' >&2; exit 1; }
script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
specs="$script_dir/labels.json"
jq -e '
  type == "array" and length > 0 and
  all(.[]; (.name | type == "string" and length > 0) and
    (.color | type == "string" and test("^[0-9A-Fa-f]{6}$")) and
    (.description | type == "string" and length > 0)) and
  ((map(.name | ascii_downcase) | unique | length) == length)
' "$specs" >/dev/null || { printf 'Invalid or duplicate label definition.\n' >&2; exit 1; }

if [[ $dry_run == false ]]; then
  command -v gh >/dev/null || { printf 'GitHub CLI (gh) is required.\n' >&2; exit 1; }
  gh repo view "$repo" --json nameWithOwner --jq '.nameWithOwner'
fi

# Parse records without splitting spaces or punctuation in label names.
records=$(jq -c '.[]' "$specs")
while IFS= read -r record; do
  name=$(jq -r '.name' <<< "$record")
  color=$(jq -r '.color' <<< "$record")
  description=$(jq -r '.description' <<< "$record")
  if [[ $dry_run == true ]]; then
    printf 'Would create/update %s: %s (#%s)\n' "$repo" "$name" "$color"
  else
    gh label create "$name" --repo "$repo" --color "$color" --description "$description" --force
  fi
done <<< "$records"
printf 'Label definitions processed. No issue labels, Project fields, or existing label deletions were changed.\n'
