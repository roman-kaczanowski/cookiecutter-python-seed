# cookiecutter-python-seed

[![CI](https://img.shields.io/github/actions/workflow/status/roman-kaczanowski/cookiecutter-python-seed/integrity-check.yml?branch=main&style=flat-square&label=CI)](https://github.com/roman-kaczanowski/cookiecutter-python-seed/actions/workflows/integrity-check.yml) [![Python](https://img.shields.io/badge/python-3.12%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://docs.python.org/3/) [![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

Cookiecutter template for Python 3.12 applications and PyPI packages. Generated projects use [uv](https://docs.astral.sh/uv/), Ruff, pytest, pre-commit, and GitHub Actions. They also ship `AGENTS.md` and Cursor rules so an AI IDE can work in the repo immediately.

## Generate

```shell
uvx cookiecutter gh:roman-kaczanowski/cookiecutter-python-seed
```

From a local clone: `uvx cookiecutter /path/to/cookiecutter-python-seed`.

```text
my-project/         # git / PyPI name (project_slug)
  src/my_project/   # import package (derived)
  tests/
  pyproject.toml
```

The import package is `project_slug` with dashes turned into underscores.

- **application:** `[tool.uv] package = false`. No project install, no PyPI publish workflow.
- **package:** installable src layout. Every PR to `main` must bump the version. Pushing tag `vX.Y.Z` on `main` publishes to PyPI via trusted publishing.

See [CONTRIBUTING.md](CONTRIBUTING.md) if you are changing this template.

## License

MIT. Generated projects ship MIT too; replace `LICENSE` after generation if you need a different license.
