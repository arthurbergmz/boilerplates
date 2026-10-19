.PHONY: setup run test lint fmt

setup:
	uv venv --python 3.12 .venv
	. .venv/bin/activate && uv pip install -e '.[dev]'

run:
	uv run awesome-app --name dev

test:
	uv run pytest

lint:
	uv run ruff check .

fmt:
	uv run ruff format .
