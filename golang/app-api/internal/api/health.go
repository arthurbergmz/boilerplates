package api

type healthResponse struct {
	Status string `json:"status"`
}

func Health() healthResponse {
	return healthResponse{Status: "ok"}
}
