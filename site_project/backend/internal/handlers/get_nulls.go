package handlers

import (
	"encoding/json"
	"net/http"

	"example.com/backend-pic/api"
	"example.com/backend-pic/internal/database"
	log "github.com/sirupsen/logrus"
)

func GetNullsById(w http.ResponseWriter, r *http.Request) {
	rows, err := database.DB.Query(`
	SELECT DISTINCT raspberrypi_id
	FROM dados_rede
	WHERE timestamp >= NOW() - INTERVAL 1 DAY
		AND (
			latencia_ms IS NULL OR
			perda_pacotes IS NULL OR
			download_mbps IS NULL OR
			upload_mbps IS NULL OR
			rtt_min IS NULL OR
			rtt_avg IS NULL OR
			rtt_max IS NULL OR
			rtt_mdev IS NULL
		);
	`)
	if err != nil {
		log.Error(err)
		api.InternalErrorHandler(w)
		return
	}

	var ids []int
	for rows.Next() {
		var id int
		if err := rows.Scan(&id); err != nil {
			continue
		}
		ids = append(ids, id)
	}

	w.Header().Set("Content-type", "application/json")
	err = json.NewEncoder(w).Encode(ids)
	if err != nil {
		log.Error(err)
		api.InternalErrorHandler(w)
		return
	}
}
