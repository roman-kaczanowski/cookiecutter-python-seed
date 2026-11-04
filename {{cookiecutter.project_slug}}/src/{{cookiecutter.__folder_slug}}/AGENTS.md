# Source package

Import package `{{ cookiecutter.__folder_slug }}` for `{{ cookiecutter.project_slug }}`.

## Layout

- `__init__.py` marks the package. Keep it empty unless a public re-export is required.
- `ping.py` is the example module and exposes `ping() -> str`.

## Flow

Tests import modules from `{{ cookiecutter.__folder_slug }}` directly. `pyproject.toml` sets `pythonpath = ["src"]`, so `src/` is the import root.

## Rules

- Add new modules in this directory and mirror each one with a focused test in `tests/`.
- Keep imports absolute from the package name. Do not add `sys.path` changes.
- Public functions need type hints and a test that fails when the behavior breaks.
- Update this map when the package layout or flow changes.
