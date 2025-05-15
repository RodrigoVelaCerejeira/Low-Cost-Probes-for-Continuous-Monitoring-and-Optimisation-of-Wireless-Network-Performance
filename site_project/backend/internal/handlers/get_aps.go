package handlers

import (
	"encoding/json"
	"net/http"

	"example.com/backend-pic/api"
	"example.com/backend-pic/internal/database"

	log "github.com/sirupsen/logrus"
)

func GetAPs(w http.ResponseWriter, r *http.Request) {
	rows, err := database.DB.Query("SELECT timestamp, raspberrypi_id, ssid, bssid, rate, sig FROM all_aps")
	if err != nil {
		log.Error(err)
		api.InternalErrorHandler(w)
		return
	}

	var aps []database.Aps
	for rows.Next() {
		var a database.Aps
		if err := rows.Scan(&a.Timestamp, &a.Raspberrypi_id, &a.Ssid, &a.Bssid, &a.Rate, &a.Sig); err != nil {
			continue
		}
		aps = append(aps, a)

	}

	w.Header().Set("Content-type", "application/json")
	err = json.NewEncoder(w).Encode(aps)
	if err != nil {
		log.Error(err)
		api.InternalErrorHandler(w)
		return
	}
}
