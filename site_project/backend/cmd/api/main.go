package main

import (
	"fmt"
	"net/http"

	"example.com/backend-pic/internal/database"
	"example.com/backend-pic/internal/handlers"
	"github.com/go-chi/chi"
	log "github.com/sirupsen/logrus"
)

func main() {
	dsn := "monitor:senha_segura@tcp(192.92.147.85:3306)/central_monitoramento"
	database.Init(dsn)
	log.SetReportCaller(true)

	var r *chi.Mux = chi.NewRouter()
	handlers.Handler(r)

	fmt.Println("Starting GO API service...")

	err := http.ListenAndServe("0.0.0.0:3001", r)
	if err != nil {
		log.Error(err)
	}
}
