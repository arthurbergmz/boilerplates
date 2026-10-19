package api

type helloResponse struct {
	API string `json:"api"`
}

func Hello() helloResponse {
	return helloResponse{API: "works!"}
}
