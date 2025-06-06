package handlers

import (
	"encoding/json"
	"net/http"

	"example.com/backend-pic/api"
	"example.com/backend-pic/internal/database"

	log "github.com/sirupsen/logrus"
)

func GetAllFailures(w http.ResponseWriter, r *http.Request) {
	rows, err := database.DB.Query(`
		SELECT raspberrypi_id, timestamp, latencia_ms, perda_pacotes, download_mbps, upload_mbps, rtt_min, rtt_avg, rtt_max, rtt_mdev, num_aps
		FROM erros_dados_rede
		`)

	if err != nil {
		log.Error(err)
		api.InternalErrorHandler(w)
		return
	}

	var reports []database.Report
	for rows.Next() {
		var r database.Report
		if err := rows.Scan(
			&r.Raspberrypi_id,
			&r.Timestamp,
			&r.Latencia_ms,
			&r.Perda_pacotes,
			&r.Download_mbps,
			&r.Upload_mbps,
			&r.Rtt_min,
			&r.Rtt_avg,
			&r.Rtt_max,
			&r.Rtt_mdev,
			&r.Num_aps,
		); err != nil {
			continue
		}
		reports = append(reports, r)
	}

	w.Header().Set("Content-type", "application/json")
	if err := json.NewEncoder(w).Encode(reports); err != nil {
		log.Error(err)
		api.InternalErrorHandler(w)
		return
	}
}
