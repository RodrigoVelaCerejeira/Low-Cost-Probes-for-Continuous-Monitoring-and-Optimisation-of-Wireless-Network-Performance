package handlers

import (
	"encoding/json"
	"net/http"

	"example.com/backend-pic/api"
	"example.com/backend-pic/internal/database"

	log "github.com/sirupsen/logrus"
)

func GetFailuresLastHour(w http.ResponseWriter, r *http.Request) {
	var allFailures = make(map[string][]int)

	// Packet Loss
	packetLossFailures := getFailuresPacketLossLastHour()
	allFailures["packet_loss"] = packetLossFailures

	// Round Trip Time
	roundTripTimeFailures := getFailuresRoundTripTimeLastHour()
	allFailures["round_trip_time"] = roundTripTimeFailures

	// Download Speed
	downloadSpeedFailures := getFailureDownloadSpeedLastHour()
	allFailures["download_speed"] = downloadSpeedFailures

	// Latency
	latencyFailures := getFailureLatencyLastHour()
	allFailures["latency"] = latencyFailures

	// Upload Speed
	uploadSpeedFailures := getFailureUploadSpeedLastHour()
	allFailures["upload_speed"] = uploadSpeedFailures

	w.Header().Set("Content-type", "application/json")
	if err := json.NewEncoder(w).Encode(allFailures); err != nil {
		log.Error(err)
		api.InternalErrorHandler(w)
		return
	}
}

func getFailuresPacketLossLastHour() []int {
	threshold := 100 // Mudar

	rows, err := database.DB.Query(`
		SELECT raspberrypi_id, 
		SUM(perda_pacotes) AS total_packet_loss
		FROM dados_rede
		WHERE timestamp >= NOW() -INTERVAL 1 HOUR 
		GROUP BY raspberrypi_id;
		`)

	if err != nil {
		log.Error(err)
		return nil
	}

	defer rows.Close()

	var ids []int
	for rows.Next() {
		var id int
		var totalPacketLoss int
		if err := rows.Scan(&id, &totalPacketLoss); err != nil {
			continue
		}

		// Check if the total packet loss in 1h exceeds the threshold
		if totalPacketLoss > threshold {
			ids = append(ids, id)
		}

	}

	return ids
}

func getFailuresRoundTripTimeLastHour() []int {
	threshold := 200.0

	rows, err := database.DB.Query(`
		SELECT raspberrypi_id, AVG(rtt_avg) AS average_rtt
		FROM dados_rede
		WHERE timestamp >= NOW() - INTERVAL 1 HOUR
		GROUP BY raspberrypi_id;
		`)

	if err != nil {
		log.Error(err)
		return nil
	}

	var ids []int
	for rows.Next() {
		var id int
		var averageRTT float64
		if err := rows.Scan(&id, &averageRTT); err != nil {
			continue
		}

		// Check if the average RTT in 1h exceeds the threshold
		if averageRTT > threshold {
			ids = append(ids, id)
		}
	}

	return ids

}

func getFailureDownloadSpeedLastHour() []int {
	threshold := 10.0

	rows, err := database.DB.Query(`
		SELECT raspberrypi_id, AVG(download_mbps) AS average_download
		FROM dados_rede
		WHERE timestamp >= NOW() - INTERVAL 1 HOUR
		GROUP BY raspberrypi_id;
		`)

	if err != nil {
		log.Error(err)
		return nil
	}

	var ids []int
	for rows.Next() {
		var id int
		var averageDownload float64
		if err := rows.Scan(&id, &averageDownload); err != nil {
			continue
		}

		if averageDownload < threshold {
			ids = append(ids, id)
		}
	}

	return ids
}

func getFailureLatencyLastHour() []int {
	threshold := 50.0

	rows, err := database.DB.Query(`
		SELECT raspberrypi_id, AVG(latencia_ms) AS average_latency
		FROM dados_rede
		WHERE timestamp >= NOW() - INTERVAL 1 HOUR
		GROUP BY raspberrypi_id;
		`)

	if err != nil {
		log.Error(err)
		return nil
	}

	var ids []int
	for rows.Next() {
		var id int
		var averageLatency float64
		if err := rows.Scan(&id, &averageLatency); err != nil {
			continue
		}

		if averageLatency > threshold {
			ids = append(ids, id)
		}
	}

	return ids
}

func getFailureUploadSpeedLastHour() []int {
	threshold := 10.0

	rows, err := database.DB.Query(`
		SELECT raspberrypi_id, AVG(upload_mbps) AS average_upload
		FROM dados_rede
		WHERE timestamp >= NOW() - INTERVAL 1 HOUR
		GROUP BY raspberrypi_id;
		`)

	if err != nil {
		log.Error(err)
		return nil
	}

	var ids []int
	for rows.Next() {
		var id int
		var averageUpload float64
		if err := rows.Scan(&id, &averageUpload); err != nil {
			continue
		}

		if averageUpload < threshold {
			ids = append(ids, id)
		}
	}

	return ids
}
