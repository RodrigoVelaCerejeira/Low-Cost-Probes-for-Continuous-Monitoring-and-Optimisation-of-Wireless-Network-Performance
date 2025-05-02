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

	row := database.DB.QueryRow("SELECT id, mac_address, Ultimo_registro FROM raspberrypis WHERE id = ?", id)

	var product database.Raspberry
	if err := row.Scan(&product.Id, &product.Mac_Address, &product.Ultimo_registro); err != nil {
		log.Error(err)
		api.InternalErrorHandler(w)
	}

	w.Header().Set("Content-type", "application/json")
	err := json.NewEncoder(w).Encode(product)
	if err != nil {
		log.Error(err)
		api.InternalErrorHandler(w)
		return
	}

}
