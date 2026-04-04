# {{app-name}}

{{app-description}}
A production-style Go API boilerplate.

## Why this layout

This template uses a common service layout:

- `bin/`: compiled binaries output
- `cmd/`: executable entrypoints
- `internal/`: application code that should not be imported externally
- `configs/`: configuration examples/templates
- `scripts/`: local automation scripts
- `Makefile`: consistent local commands

## Router choice: Chi

This template uses [Chi](https://github.com/go-chi/chi) because it stays close to `net/http` while adding practical routing, middleware composition, and route grouping.

If you prefer zero external dependencies, you can swap Chi for `http.ServeMux` with minimal changes inside `internal/server/router.go`.

## Getting started

Replace the placeholders in this folder first:

- `{{app-name}}`
- `{{app-description}}`
- `example.com/your-org/your-app` with your real module path (example: `github.com/my-org/my-api`)

Then run:

```bash
make setup
make test
make run
```

The default server address is `:8080`.
