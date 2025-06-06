package database

import (
	"database/sql"
	"log"

	_ "github.com/go-sql-driver/mysql"
)

var DB *sql.DB

type Raspberry struct {
	Id              int      `json:"id"`
	Mac_Address     string   `json:"mac"`
	Ultimo_registro string   `json:"ultimo_registro"`
	HasError        bool     `json:"has_error"`
	Failures        []string `json:"failures"`
	Location        string   `json:"location"`
}

type Report struct {
	Raspberrypi_id int     `json:"raspberrypi_id"`
	Timestamp      string  `json:"timestamp"`
	Latencia_ms    float64 `json:"latencia_ms"`
	Perda_pacotes  int     `json:"perda_pacotes"`
	Download_mbps  float64 `json:"download_mbps"`
	Upload_mbps    float64 `json:"upload_mbps"`
	Rtt_min        float64 `json:"rtt_min"`
	Rtt_avg        float64 `json:"rtt_avg"`
	Rtt_max        float64 `json:"rtt_max"`
	Rtt_mdev       float64 `json:"rtt_mdev"`
	Num_aps        int     `json:"num_aps"`
}

type Aps struct {
	Timestamp      string `json:"timestamp"`
	Raspberrypi_id string `json:"raspberrypi_id"`
	Ssid           string `json:"ssid"`
	Bssid          string `json:"bssid"`
	Rate           string `json:"rate"`
	Sig            string `json:"signal"`
}

func Init(dsn string) {
	var err error
	DB, err = sql.Open("mysql", dsn)
	if err != nil {
		log.Fatal("Failed to open DB:", err)
	}

	if err := DB.Ping(); err != nil {
		log.Fatal("Failed to connect to DB:", err)
	}
	DB.SetMaxOpenConns(10)
	DB.SetMaxIdleConns(5)

}
