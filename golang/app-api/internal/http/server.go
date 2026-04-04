package http

import (
	"log"
	"net/http"
	"os"
)

func CreateHttpServer() {
	addr := ":8080"
	if port := os.Getenv("PORT"); port != "" {
		addr = ":" + port
	}

	r := NewRouter()

	log.Printf("starting %s on %s", "{{app-name}}", addr)
	if err := http.ListenAndServe(addr, r); err != nil {
		log.Fatal(err)
	}
}
