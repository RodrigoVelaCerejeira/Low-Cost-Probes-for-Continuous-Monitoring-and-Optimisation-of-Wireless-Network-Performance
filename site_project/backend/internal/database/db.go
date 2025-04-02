package database

import (
	"database/sql"
	"log"

	_ "github.com/go-sql-driver/mysql"
)

var DB *sql.DB

type Product struct {
	Id    int     `json:"id"`
	Name  string  `json:"name"`
	Price float32 `json:"price"`
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
