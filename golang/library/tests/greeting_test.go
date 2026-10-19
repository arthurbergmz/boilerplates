package tests

import (
	"testing"

	library "example.com/your-org/your-library"
)

func TestGreeting_IsUsableAcrossPackageBoundary(t *testing.T) {
	got := library.Greeting("dev")
	if got == "" {
		t.Fatal("expected non-empty greeting")
	}
}
