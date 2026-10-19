from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="awesome-app",
        description="Starter CLI for your new Python project.",
    )
    parser.add_argument("--name", default="world", help="Who to greet")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    print(f"hello, {args.name}!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
