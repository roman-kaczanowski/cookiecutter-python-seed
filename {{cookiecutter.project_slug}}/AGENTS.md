# {{ cookiecutter.project_slug }}

{{ cookiecutter.description }}

Python 3.12+ project generated from cookiecutter-python-seed. `pyproject.toml` is the source of truth for dependencies, toolchain, and commands.

## Commands

```shell
{% if cookiecutter.project_type == "package" %}uv sync{% else %}uv sync --no-install-project{% endif %}
poe format        # Ruff format and autofix
poe check         # Ruff format check and lint
poe test          # pytest
poe format_docs   # mdformat write
poe check_docs    # mdformat check
```

Use `uv run poe <task>` if `poe` is not installed.

## Non-negotiables

- Python 3.12+ and uv only. Do not add a dependency unless it is declared in `pyproject.toml`.
- Type-hint every function. Use single quotes and ASCII in code and docs.
- Reuse existing code and the standard library before writing new code. Fix root causes, not symptoms.
- Never read or grep a vendored or generated file whole. Use a capped search such as `grep -o 'pattern' file | head`.
- Run `poe check`, `poe check_docs`, and `poe test` before claiming work is done.
- Do not commit secrets, `.env` files, or local virtualenvs.

## Context

Read the nearest `AGENTS.md` before changing files in that directory. Load a skill when its description matches the task.

- Coding standards: [`.agents/skills/project-standards/SKILL.md`](.agents/skills/project-standards/SKILL.md)
- Markdown: [`.agents/skills/markdown/SKILL.md`](.agents/skills/markdown/SKILL.md)
- Package: [`src/{{ cookiecutter.__folder_slug }}/AGENTS.md`](src/{{ cookiecutter.__folder_slug }}/AGENTS.md)
- Tests: [`tests/AGENTS.md`](tests/AGENTS.md)
