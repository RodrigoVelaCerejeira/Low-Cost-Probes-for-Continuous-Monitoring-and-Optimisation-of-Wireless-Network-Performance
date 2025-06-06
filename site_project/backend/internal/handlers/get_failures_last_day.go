package handlers

import (
	"encoding/json"
	"net/http"

	"example.com/backend-pic/api"
	"example.com/backend-pic/internal/database"
	"github.com/go-chi/chi"

	log "github.com/sirupsen/logrus"
)

func GetFailuresPerTime(w http.ResponseWriter, r *http.Request) {
	t := chi.URLParam(r, "time_period")
	var time int
	if t == "lastday" {
		time = 24
	} else if t == "lasthour" {
		time = 1
	} else {
		api.InternalErrorHandler(w)
		return
	}
	rows, err := database.DB.Query(`
		SELECT raspberrypi_id, timestamp, latencia_ms, perda_pacotes, download_mbps, upload_mbps, rtt_min, rtt_avg, rtt_max, rtt_mdev, num_aps, err_num
		FROM erros_dados_rede
		WHERE timestamp >= NOW() - INTERVAL ? HOUR
		GROUP BY raspberrypi_id;
		`, time)

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
			&r.Failure,
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
