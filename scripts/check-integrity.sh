#!/usr/bin/env bash
set -euo pipefail

root=$(cd "$(dirname "$0")/.." && pwd)
keep=0
for arg in "$@"; do
  case "$arg" in
    --keep) keep=1 ;;
    -h | --help)
      echo "usage: $(basename "$0") [--keep]"
      exit 0
      ;;
    *)
      echo "unknown argument: $arg" >&2
      exit 1
      ;;
  esac
done

if ! command -v uv >/dev/null; then
  echo 'uv is not on PATH. Install it, then re-run this script:'
  echo 'curl -LsSf https://astral.sh/uv/install.sh | sh'
  exit 1
fi

tmp=$(mktemp -d "${TMPDIR:-/tmp}/cookiecutter-python-seed.XXXXXX")
cleanup() {
  if ((keep)); then
    echo "kept $tmp"
  else
    rm -rf "$tmp"
  fi
}
trap cleanup EXIT

check_project() {
  local project_dir=$1
  (
    cd "$project_dir"
    uv run ruff format --check .
    uv run ruff check .
    find . -name '*.md' ! -path './.venv/*' ! -path './.git/*' -exec uv run mdformat --check {} +
    uv run pytest
  )
}

for project_type in application package; do
  echo "==> $project_type"
  uvx cookiecutter "$root" --no-input --output-dir "$tmp/$project_type" "project_type=$project_type"
  if [[ $project_type == package ]]; then
    publish=$tmp/$project_type/my-project/.github/workflows/publish.yml
    grep -F 'https://pypi.org/p/my-project' "$publish"
    grep -F '${{ github.ref_name }}' "$publish"
    if grep -F 'cookiecutter.project_slug' "$publish"; then
      echo 'publish.yml still contains unrendered cookiecutter.project_slug' >&2
      exit 1
    fi
  fi
  check_project "$tmp/$project_type/my-project"
done
