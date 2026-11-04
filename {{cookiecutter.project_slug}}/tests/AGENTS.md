# Tests

Tests use pytest and live at the repository root. `pyproject.toml` sets `testpaths = ["tests"]` and `pythonpath = ["src"]`.

## Commands

```shell
poe test
uv run pytest
uv run pytest tests/test_ping.py
```

## Rules

- Name files `test_<module>.py` and functions `test_<behavior>`.
- Mirror `src/<package>/` modules in `tests/` and test public behavior, not private helpers.
- Every non-trivial logic change adds or updates the smallest test that fails when it breaks.
- Keep tests deterministic and independent. Do not add network access or shared state unless the project already does.
- Use plain `assert` statements. Add a fixture only when setup is shared by multiple tests.
