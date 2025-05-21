package handlers

import (
	"fmt"
	"net/http"
	"time"

	"example.com/backend-pic/api"
	"example.com/backend-pic/internal/database"
	"github.com/go-chi/chi"
	log "github.com/sirupsen/logrus"
	"github.com/xuri/excelize/v2"
)

func ExportToExcelById(w http.ResponseWriter, r *http.Request) {
	id := chi.URLParam(r, "id")
	rows, err := database.DB.Query("SELECT * FROM dados_rede WHERE raspberrypi_id = ?", id)
	if err != nil {
		log.Error(err)
		api.InternalErrorHandler(w)
		return
	}

	defer rows.Close()
	f := excelize.NewFile()
	sheet := "Sheet1"

	// Write headers
	headers := []string{
		"id",
		"raspberrypi_id",
		"timestamp",
		"latencia_ms",
		"perda_pacotes",
		"download_mbps",
		"upload_mbps",
		"rtt_min",
		"rtt_avg",
		"rtt_max",
		"rtt_mdev",
		"num_aps",
	}

	for i, h := range headers {
		cell, _ := excelize.CoordinatesToCellName(i+1, 1)
		f.SetCellValue(sheet, cell, h)
	}

	// Write rows
	rowNum := 2
	for rows.Next() {
		var rawTimestamp []byte
		var time_stamp time.Time
		var id, raspberry_id, num_aps int
		var latencia, perda_pacotes, download, upload, rtt_min, rtt_avg, rtt_max, rtt_mdevs float32
		if err := rows.Scan(&id, &raspberry_id, &rawTimestamp, &latencia, &perda_pacotes, &download, &upload, &rtt_min, &rtt_avg, &rtt_max, &rtt_mdevs, &num_aps); err != nil {
			log.Fatal(err)
		}

		time_stamp, err := time.Parse("2006-01-02 15:04:05", string(rawTimestamp))
		if err != nil {
			log.Error(err)
			api.InternalErrorHandler(w)
			return
		}

		f.SetCellValue(sheet, "A"+string(rune(rowNum+48)), id)
		f.SetCellValue(sheet, "B"+string(rune(rowNum+48)), raspberry_id)
		f.SetCellValue(sheet, "C"+string(rune(rowNum+48)), time_stamp)
		f.SetCellValue(sheet, "D"+string(rune(rowNum+48)), latencia)
		f.SetCellValue(sheet, "E"+string(rune(rowNum+48)), perda_pacotes)
		f.SetCellValue(sheet, "F"+string(rune(rowNum+48)), download)
		f.SetCellValue(sheet, "G"+string(rune(rowNum+48)), upload)
		f.SetCellValue(sheet, "H"+string(rune(rowNum+48)), rtt_min)
		f.SetCellValue(sheet, "I"+string(rune(rowNum+48)), rtt_avg)
		f.SetCellValue(sheet, "J"+string(rune(rowNum+48)), rtt_max)
		f.SetCellValue(sheet, "K"+string(rune(rowNum+48)), rtt_mdevs)
		f.SetCellValue(sheet, "L"+string(rune(rowNum+48)), num_aps)
		rowNum++
	}

	w.Header().Set("Content-Type", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
	w.Header().Set("Content-Disposition", fmt.Sprintf("attachment;filename=dados_rede%s.xlsx", id))
	w.Header().Set("File-Name", fmt.Sprintf("dados_rede%s.xlsx", id)) // optional, for frontend support
	w.Header().Set("Content-Transfer-Encoding", "binary")
	w.Header().Set("Expires", "0")

	if err := f.Write(w); err != nil {
		log.Error("failed to write Excel file to response: ", err)
		api.InternalErrorHandler(w)
		return
	}

	log.Println("Exported to dados_rede%s.xlsx successfully", id)
}
