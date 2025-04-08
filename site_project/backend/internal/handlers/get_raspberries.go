package handlers

import (
	"encoding/json"
	"net/http"

	"example.com/backend-pic/api"
	"example.com/backend-pic/internal/database"

	log "github.com/sirupsen/logrus"
)

func GetRaspberries(w http.ResponseWriter, r *http.Request) {
	rows, err := database.DB.Query("SELECT * FROM central_monitorament")
	if err != nil {
		log.Error(err)
		api.InternalErrorHandler(w)
		return
	}

	var products []database.Product
	for rows.Next() {
		var p database.Product
		if err := rows.Scan(&p.Id, &p.Name, &p.Price); err != nil {
			continue
		}
		products = append(products, p)
	}

	w.Header().Set("Content-type", "application/json")
	err = json.NewEncoder(w).Encode(products)
	if err != nil {
		log.Error(err)
		api.InternalErrorHandler(w)
		return
	   }
}
