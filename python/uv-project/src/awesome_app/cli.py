from __future__ import annotations

import argparse
import json
import sys

from awesome_app.benchmarking import run_benchmark
from awesome_app.determinism import set_deterministic
from awesome_app.pipeline import generate_offline_batch, score_offline_batch


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="awesome-app",
        description="Starter CLI for your new Python project.",
    )
    parser.add_argument("--name", default="world", help="Who to greet (default mode)")

    subparsers = parser.add_subparsers(dest="command")

    generate_parser = subparsers.add_parser(
        "generate",
        help="Run offline generation and write artifacts",
    )
    generate_parser.add_argument("--prompt", required=True, help="Input prompt for generation")
    generate_parser.add_argument(
        "--out-dir",
        default="artifacts/runs",
        help="Directory where run artifacts will be written",
    )
    generate_parser.add_argument("--run-id", default=None, help="Optional run identifier")
    generate_parser.add_argument("--seed", type=int, default=42, help="Deterministic seed")
    generate_parser.add_argument(
        "--schema-type",
        choices=["regex", "json"],
        default=None,
        help="Optional structured-output validator type",
    )
    generate_parser.add_argument(
        "--schema",
        default=None,
        help="Schema payload: regex pattern or JSON schema string",
    )

    score_parser = subparsers.add_parser(
        "score",
        help="Score a generated raw.jsonl and emit summary",
    )
    score_parser.add_argument("--input", required=True, help="Path to raw.jsonl")
    score_parser.add_argument(
        "--out-dir",
        default=None,
        help="Optional output directory for scoring files (defaults near input)",
    )

    benchmark_parser = subparsers.add_parser(
        "benchmark",
        help="Run a tiny benchmark with warmup and stable window",
    )
    benchmark_parser.add_argument("--name", default="world", help="Workload input")
    benchmark_parser.add_argument("--warmup", type=int, default=5, help="Warmup iterations")
    benchmark_parser.add_argument(
        "--iterations",
        type=int,
        default=20,
        help="Measured iterations after warmup",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "generate":
        try:
            set_deterministic(args.seed)
            run_dir = generate_offline_batch(
                prompt=args.prompt,
                out_dir=args.out_dir,
                run_id=args.run_id,
                seed=args.seed,
                schema_type=args.schema_type,
                schema=args.schema,
            )
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2

        print(f"generated artifacts in: {run_dir}")
        return 0

    if args.command == "score":
        summary_path = score_offline_batch(input_path=args.input, out_dir=args.out_dir)
        print(f"score summary: {summary_path}")
        return 0

    if args.command == "benchmark":
        metrics = run_benchmark(
            name=args.name,
            warmup=args.warmup,
            iterations=args.iterations,
        )
        print(json.dumps(metrics, indent=2, sort_keys=True))
        return 0

    print(f"hello, {args.name}!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
