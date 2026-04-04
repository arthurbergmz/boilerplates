.PHONY: setup test fmt vet tidy

setup:
	go mod tidy

test:
	go test ./...

fmt:
	gofmt -w .

vet:
	go vet ./...

tidy:
	go mod tidy
