# awesome_app

A modern Python boilerplate with `uv`, inspired by production-style layout:

- `pyproject.toml` for metadata + scripts (Python's `package.json` equivalent)
- `src/` package layout
- CLI entrypoint (`awesome-app`)
- linting (`ruff`)
- tests (`pytest`)
- optional offline generation/scoring pipeline (`generate` -> `score`)
- optional deterministic mode helpers (seeded execution)
- optional structured-output checks (regex / JSON schema-lite)
- optional benchmark command (warmup + stable metrics)

## Quick start

```bash
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install -e '.[dev]'
awesome-app --help
pytest
ruff check .
awesome-app generate --prompt smoke --out-dir artifacts/runs --run-id smoke
awesome-app score --input artifacts/runs/smoke/raw.jsonl
awesome-app benchmark --name smoke --warmup 3 --iterations 20
```

## Node.js mental map

- `package.json` -> `pyproject.toml`
- `npm install` -> `uv pip install ...`
- `npm run <script>` -> `uv run <command>` or console script from `[project.scripts]`
- `npx <tool>` -> `uvx <tool>`

## Project layout

```text
python-uv-boilerplate/
  pyproject.toml
  src/awesome_app/
    __init__.py
    benchmarking.py
    cli.py
    determinism.py
    pipeline.py
    structured_output.py
  tests/
    test_cli.py
    test_pipeline_cli.py
```

## Optional DeepInfer-style workflow (lightweight)

These features are intentionally modular: keep them when useful, delete them if
your project does not need them.

- `generate`: writes run artifacts (`raw.jsonl`, `meta.json`, `summary.json`)
- `score`: reads `raw.jsonl`, writes `scored.jsonl` and score summary
- `benchmark`: executes warmup then stable measurement window

Examples:

```bash
uv run awesome-app generate --prompt "Arthur" --out-dir artifacts/runs --run-id demo
uv run awesome-app score --input artifacts/runs/demo/raw.jsonl
uv run awesome-app benchmark --name "Arthur" --warmup 5 --iterations 50
```

Structured-output checks are optional during generation:

```bash
# regex
uv run awesome-app generate --prompt world --schema-type regex --schema '^hello, .*!$'

# JSON schema-lite (expects generated text to be valid JSON)
uv run awesome-app generate --prompt world --schema-type json --schema '{"type":"object","required":["message"],"properties":{"message":{"type":"string"}}}'
```

## Running without activation

You can skip `source .venv/bin/activate` if you prefer explicit commands:

```bash
uv run awesome-app --name Arthur
uv run pytest
uv run ruff check .
```

## Verification checklist

Use this quick checklist when you bootstrap a new project from this template:

```bash
# 1) Create env + install deps
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install -e '.[dev]'

# 2) Smoke test CLI
uv run awesome-app --name smoke

# 3) Run tests
uv run pytest

# 4) Run lint
uv run ruff check .
```

If `uv` is unavailable in your environment, install it first and then run the
checklist above.

After installing `uv`, make sure `~/.local/bin` is on your `PATH` (or restart
your shell), otherwise `uv` and `uvx` may not be found.
