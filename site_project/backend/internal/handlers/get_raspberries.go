package handlers

import (
	"encoding/json"
	"net/http"

	"example.com/backend-pic/api"
	"example.com/backend-pic/internal/database"

	log "github.com/sirupsen/logrus"
)

func GetRaspberries(w http.ResponseWriter, r *http.Request) {
	rows, err := database.DB.Query("SELECT id, mac_address, ip_local, ip_externo FROM raspberrypis")
	if err != nil {
		log.Error(err)
		api.InternalErrorHandler(w)
		return
	}

	var raspberries []database.Raspberry
	for rows.Next() {
		var p database.Raspberry
		if err := rows.Scan(&p.Id, &p.Mac_Address, &p.Local_Ip, &p.Global_Ip); err != nil {
			continue
		}
		raspberries = append(raspberries, p)
	}

	w.Header().Set("Content-type", "application/json")
	err = json.NewEncoder(w).Encode(raspberries)
	if err != nil {
		log.Error(err)
		api.InternalErrorHandler(w)
		return
	   }
}
