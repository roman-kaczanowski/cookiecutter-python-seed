import shutil
import subprocess
import sys
from pathlib import Path

{% if cookiecutter.project_type != "package" %}
Path('.github/workflows/publish.yml').unlink(missing_ok=True)
Path('.github/workflows/check-tag.yml').unlink(missing_ok=True)
Path('.github/workflows/version-check.yml').unlink(missing_ok=True)
{% endif %}

if shutil.which('uv') is None:
    print('uv is not on PATH. Install it, then run uv sync in this directory:')
    print('curl -LsSf https://astral.sh/uv/install.sh | sh')
    sys.exit(1)

{% if cookiecutter.project_type == "package" %}
sync = ['uv', 'sync']
{% else %}
sync = ['uv', 'sync', '--no-install-project']
{% endif %}


def run(cmd: list[str]) -> None:
    print(f'+ {" ".join(cmd)}')
    subprocess.run(cmd, check=True)


run(sync)
if shutil.which('git') is None:
    print('git is not on PATH; skipped hook install. Run poe hooks after git init.')
else:
    if not (Path() / '.git').exists():
        run(['git', 'init'])
    run(['uv', 'run', 'poe', 'hooks'])
