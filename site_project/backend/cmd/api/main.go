package main

import (
	"fmt"
	"net/http"

	"example.com/backend-pic/internal/handlers"
	"example.com/backend-pic/internal/database"
	"github.com/go-chi/chi"
	log "github.com/sirupsen/logrus"
)

func main() {
    dsn := "gotester:testpass@tcp(localhost:3306)/gotestdb"
    database.Init(dsn)
    log.SetReportCaller(true)

    var r *chi.Mux = chi.NewRouter()
    handlers.Handler(r)

    fmt.Println("Starting GO API service...")

    err := http.ListenAndServe("0.0.0.0:3000", r)
    if err != nil {
        log.Error(err)
    }
}
