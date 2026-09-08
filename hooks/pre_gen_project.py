import keyword
import re
import sys

project_slug = {{ cookiecutter.project_slug | tojson }}
folder_slug = project_slug.replace('-', '_')
author_email = {{ cookiecutter.author_email | tojson }}
github_username = {{ cookiecutter.github_username | tojson }}

dashed = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
email = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')
github = re.compile(r'^[A-Za-z0-9]+(-[A-Za-z0-9]+)*$')

errors: list[str] = []

if not dashed.match(project_slug):
    errors.append(
        f'project_slug must be lowercase alphanumeric with dashes '
        f'(got {project_slug!r}; example: my-project)'
    )

if not folder_slug.isidentifier() or keyword.iskeyword(folder_slug):
    errors.append(
        f'import package derived from project_slug must be a valid Python '
        f'identifier (got {folder_slug!r})'
    )

if not email.match(author_email):
    errors.append(f'author_email is not a valid email (got {author_email!r})')

if not github.match(github_username):
    errors.append(
        f'github_username must be alphanumeric with optional dashes '
        f'(got {github_username!r})'
    )

if errors:
    print('Cookiecutter validation failed:')
    for item in errors:
        print(f'- {item}')
    sys.exit(1)
