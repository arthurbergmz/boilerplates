# {{library-title}}

{{library-description}}
A production-ready Go library boilerplate.

## Structure

- `greeting.go`: exported API surface example
- `greeting_test.go`: unit tests for package internals
- `tests/`: cross-boundary behavior tests
- `scripts/`: helper scripts
- `Makefile`: consistent local commands

## Getting started

1. Replace `{{library-title}}` and `{{library-description}}` in this file.
2. Replace module path `example.com/your-org/your-library` in `go.mod`.
3. Run:

```bash
make setup
make test
```

## Commands

```bash
make test
make fmt
make vet
```
