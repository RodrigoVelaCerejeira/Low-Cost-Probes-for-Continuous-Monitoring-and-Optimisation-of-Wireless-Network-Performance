package database

import (
	"database/sql"
	"log"

	_ "github.com/go-sql-driver/mysql"
)

var DB *sql.DB

type Raspberry struct {
	Id              int    `json:"id"`
	Mac_Address     string `json:"mac"`
	Ultimo_registro string `json:"ultimo_registro"`
	HasError        bool   `json:"has_error"`
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
