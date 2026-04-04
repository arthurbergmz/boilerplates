package http

import (
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestHelloRoute(t *testing.T) {
	r := NewRouter()

	req := httptest.NewRequest(http.MethodGet, "/api/hello", nil)
	res := httptest.NewRecorder()
	r.ServeHTTP(res, req)

	if res.Code != http.StatusOK {
		t.Fatalf("expected status %d, got %d", http.StatusOK, res.Code)
	}

	got := res.Body.String()
	want := "{\"api\":\"works!\"}\n"
	if got != want {
		t.Fatalf("expected body %q, got %q", want, got)
	}
}

func TestHealthRoute(t *testing.T) {
	r := NewRouter()

	req := httptest.NewRequest(http.MethodGet, "/health", nil)
	res := httptest.NewRecorder()
	r.ServeHTTP(res, req)

	if res.Code != http.StatusOK {
		t.Fatalf("expected status %d, got %d", http.StatusOK, res.Code)
	}
}
