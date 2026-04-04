package library

import "testing"

func TestGreeting_WithName(t *testing.T) {
	got := Greeting("arthur")
	want := "Hello, arthur!"

	if got != want {
		t.Fatalf("expected %q, got %q", want, got)
	}
}

func TestGreeting_EmptyNameUsesDefault(t *testing.T) {
	got := Greeting("")
	want := "Hello, world!"

	if got != want {
		t.Fatalf("expected %q, got %q", want, got)
	}
}
