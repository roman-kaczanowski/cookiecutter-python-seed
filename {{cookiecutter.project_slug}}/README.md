# {{ cookiecutter.project_slug }}

[![CI](https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/quality-checks.yml?branch=main&style=flat-square&label=CI)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/quality-checks.yml){% if cookiecutter.project_type == "package" %} [![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}?style=flat-square)](https://pypi.org/project/{{ cookiecutter.project_slug }}/){% endif %} [![Python](https://img.shields.io/badge/python-3.12%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://docs.python.org/3/) [![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

{{ cookiecutter.description }}

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup{% if cookiecutter.project_type == "package" %} and releases{% endif %}.

MIT. Replace `LICENSE` if you need a different license.
