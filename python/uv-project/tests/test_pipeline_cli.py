from __future__ import annotations

import json
from pathlib import Path

from awesome_app.cli import main


def test_generate_writes_artifacts(tmp_path: Path) -> None:
    out_dir = tmp_path / "artifacts"
    rc = main(
        [
            "generate",
            "--prompt",
            "tester",
            "--out-dir",
            str(out_dir),
            "--run-id",
            "run-1",
        ]
    )

    assert rc == 0
    run_dir = out_dir / "run-1"
    assert (run_dir / "raw.jsonl").exists()
    assert (run_dir / "meta.json").exists()
    assert (run_dir / "summary.json").exists()


def test_score_reads_generated_raw(tmp_path: Path) -> None:
    out_dir = tmp_path / "artifacts"
    assert (
        main(
            [
                "generate",
                "--prompt",
                "tester",
                "--out-dir",
                str(out_dir),
                "--run-id",
                "run-2",
            ]
        )
        == 0
    )

    raw = out_dir / "run-2" / "raw.jsonl"
    score_dir = out_dir / "run-2" / "scoring"
    assert main(["score", "--input", str(raw), "--out-dir", str(score_dir)]) == 0

    summary = json.loads((score_dir / "summary.json").read_text(encoding="utf-8"))
    assert summary["pass_at_1"] == 1.0


def test_generate_with_unmatched_regex_fails(tmp_path: Path) -> None:
    rc = main(
        [
            "generate",
            "--prompt",
            "tester",
            "--out-dir",
            str(tmp_path),
            "--schema-type",
            "regex",
            "--schema",
            r"^json:.*$",
        ]
    )

    assert rc == 2


def test_benchmark_command_returns_zero() -> None:
    rc = main(["benchmark", "--name", "bench", "--warmup", "1", "--iterations", "5"])
    assert rc == 0
