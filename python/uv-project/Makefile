.PHONY: setup run test lint fmt generate score benchmark

setup:
	uv venv --python 3.12 .venv
	. .venv/bin/activate && uv pip install -e '.[dev]'

run:
	uv run awesome-app --name dev

generate:
	uv run awesome-app generate --prompt "smoke" --out-dir artifacts/runs --run-id smoke

score:
	uv run awesome-app score --input artifacts/runs/smoke/raw.jsonl

benchmark:
	uv run awesome-app benchmark --name dev --warmup 3 --iterations 20

test:
	uv run pytest

lint:
	uv run ruff check .

fmt:
	uv run ruff format .
