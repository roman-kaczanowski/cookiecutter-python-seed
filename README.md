# cookiecutter-python-seed

[![CI](https://img.shields.io/github/actions/workflow/status/roman-kaczanowski/cookiecutter-python-seed/integrity-check.yml?branch=main&style=flat-square&label=CI)](https://github.com/roman-kaczanowski/cookiecutter-python-seed/actions/workflows/integrity-check.yml) [![Python](https://img.shields.io/badge/python-3.12%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://docs.python.org/3/) [![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

Start a Python project with its engineering baseline already decided. This Cookiecutter generates an application or publishable package for Python 3.12+, with one coherent workflow from local development to CI and release.

- **One toolchain.** [uv](https://docs.astral.sh/uv/) manages environments, dependencies, locking, builds, and version bumps; Poe provides the everyday commands.
- **Quality built in.** Ruff, pytest, and mdformat run locally, through pre-commit, and in GitHub Actions.
- **A structure that lasts.** A `src` layout, tests, and a focused `pyproject.toml` are ready to grow with the project.
- **Package releases included.** Hatchling builds distributions, and GitHub Actions publishes tagged releases to PyPI with trusted publishing.
- **Clear instructions for AI tools.** `AGENTS.md` and Cursor rules keep generated projects aligned with their conventions.

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
