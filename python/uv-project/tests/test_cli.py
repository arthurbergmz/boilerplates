from awesome_app.cli import main


def test_cli_main_returns_zero() -> None:
    assert main(["--name", "tester"]) == 0
