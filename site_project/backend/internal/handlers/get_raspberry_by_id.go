package handlers

import (
	"encoding/json"
	"net/http"

	"example.com/backend-pic/api"
	"example.com/backend-pic/internal/database"
	"github.com/go-chi/chi"
	log "github.com/sirupsen/logrus"
)

func GetProductById(w http.ResponseWriter, r *http.Request) {
	id := chi.URLParam(r, "id")

	row := database.DB.QueryRow("SELECT id, mac_address, ultimo_registro, localizacao FROM raspberrypis WHERE id = ?", id)

	var raspberry database.Raspberry
	if err := row.Scan(&raspberry.Id, &raspberry.Mac_Address, &raspberry.Ultimo_registro, &raspberry.Location); err != nil {
		log.Error(err)
		api.InternalErrorHandler(w)
	}

	w.Header().Set("Content-type", "application/json")
	err := json.NewEncoder(w).Encode(raspberry)
	if err != nil {
		log.Error(err)
		api.InternalErrorHandler(w)
		return
	}

}
