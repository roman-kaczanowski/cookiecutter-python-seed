from {{ cookiecutter.__folder_slug }}.ping import ping


def test_ping() -> None:
    assert ping() == 'pong'
