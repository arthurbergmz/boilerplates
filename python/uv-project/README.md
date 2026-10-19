# awesome_app

A modern Python boilerplate with `uv`, inspired by production-style layout:

- `pyproject.toml` for metadata + scripts (Python's `package.json` equivalent)
- `src/` package layout
- CLI entrypoint (`awesome-app`)
- linting (`ruff`)
- tests (`pytest`)

## Quick start

```bash
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install -e '.[dev]'
awesome-app --help
pytest
ruff check .
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
    cli.py
  tests/
    test_cli.py
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
