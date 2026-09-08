# Contributing to the seed

This repository is a Cookiecutter template, not an installable Python package.

| Path | Role |
| --- | --- |
| `{{cookiecutter.project_slug}}/` | Copied into every generated project. Keep Cookiecutter / Jinja2 variables. |
| `hooks/`, `scripts/`, `cookiecutter.json` | Seed-only. |
| Root `README.md`, `LICENSE` | Seed metadata. |

`AGENTS.md` and `.cursor/rules/` belong in the template directory only. They are copied into generated projects.

Do not add an application `src/` or `pyproject.toml` at the seed root unless it is seed tooling.

`project_slug` is the dashed PyPI / repo name. The import package under `src/` is derived from it (dashes become underscores).

## Checks

The integrity check requires [uv](https://docs.astral.sh/uv/) on `PATH`.

```shell
scripts/check-integrity.sh
```

Generates an `application` and a `package` into a temp directory, then runs Ruff, mdformat, and pytest in each. `--keep` leaves those trees in place after the script exits.
