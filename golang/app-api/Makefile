APP_NAME ?= {{app-name}}
BINARY ?= bin/$(APP_NAME)

.PHONY: setup run build dev test fmt vet tidy clean

setup:
	go mod tidy

run:
	go run ./cmd/http

build:
	mkdir -p bin
	go build -o $(BINARY) ./cmd/http

dev:
	go tool air

test:
	go test ./...

fmt:
	gofmt -w ./cmd ./internal

vet:
	go vet ./...

tidy:
	go mod tidy

clean:
	rm -rf bin
