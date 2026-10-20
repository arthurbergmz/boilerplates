from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from awesome_app.structured_output import validate_structured_output


def _timestamp() -> str:
    return datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.write_text(
        "\n".join(json.dumps(row, sort_keys=True) for row in rows) + "\n",
        encoding="utf-8",
    )


def generate_offline_batch(
    prompt: str,
    out_dir: str,
    run_id: str | None,
    seed: int,
    schema_type: str | None,
    schema: str | None,
) -> Path:
    """Generate a tiny offline batch and write DeepInfer-style artifacts."""
    run_name = run_id or f"run-{_timestamp()}"
    run_dir = Path(out_dir) / run_name
    run_dir.mkdir(parents=True, exist_ok=True)

    output = f"hello, {prompt}!"
    ok, reason = validate_structured_output(output, schema_type=schema_type, schema=schema)
    if not ok:
        raise ValueError(reason or "structured output validation failed")

    raw_rows = [
        {
            "task_id": "sample-0",
            "prompt": prompt,
            "output": output,
            "expected_output": output,
            "seed": seed,
        }
    ]

    _write_jsonl(run_dir / "raw.jsonl", raw_rows)
    _write_json(
        run_dir / "meta.json",
        {
            "seed": seed,
            "prompt": prompt,
            "schema_type": schema_type,
            "created_at": _timestamp(),
            "num_tasks": len(raw_rows),
        },
    )
    _write_json(
        run_dir / "summary.json",
        {
            "num_tasks": len(raw_rows),
            "num_rollouts": len(raw_rows),
            "coverage_complete": True,
            "pass_at_1": 1.0,
        },
    )
    return run_dir


def score_offline_batch(input_path: str, out_dir: str | None = None) -> Path:
    """Score rows from raw.jsonl and emit scored.jsonl + summary.json."""
    raw_path = Path(input_path)
    if not raw_path.exists():
        raise FileNotFoundError(f"input file not found: {raw_path}")

    score_dir = Path(out_dir) if out_dir else raw_path.parent / "scoring"
    score_dir.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, Any]] = []
    with raw_path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))

    scored_rows: list[dict[str, Any]] = []
    passed = 0
    for row in rows:
        expected = row.get("expected_output")
        output = row.get("output")
        verdict = bool(expected is not None and output == expected)
        if verdict:
            passed += 1
        scored_rows.append(
            {
                "task_id": row.get("task_id"),
                "output": output,
                "expected_output": expected,
                "verdict": verdict,
            }
        )

    total = len(scored_rows)
    pass_at_1 = (passed / total) if total else 0.0

    _write_jsonl(score_dir / "scored.jsonl", scored_rows)
    summary_path = score_dir / "summary.json"
    _write_json(
        summary_path,
        {
            "num_tasks": total,
            "num_rollouts": total,
            "coverage_complete": True,
            "pass_at_1": pass_at_1,
        },
    )
    return summary_path
