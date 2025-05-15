package handlers

import (
	"github.com/go-chi/chi"
	chimiddle "github.com/go-chi/chi/middleware"
	"github.com/go-chi/cors"
)

func Handler(r *chi.Mux) {
	r.Use(chimiddle.StripSlashes)
	r.Use(cors.Handler(cors.Options{
		// AllowedOrigins:   []string{"https://foo.com"}, // Use this to allow specific origin hosts
		AllowedOrigins: []string{"https://*", "http://*"},
		// AllowOriginFunc:  func(r *http.Request, origin string) bool { return true },
		AllowedMethods:   []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
		AllowedHeaders:   []string{"Accept", "Authorization", "Content-Type", "X-CSRF-Token"},
		ExposedHeaders:   []string{"Link"},
		AllowCredentials: false,
		MaxAge:           300, // Maximum value not
	}))

	r.Route("/raspberry", func(router chi.Router) {
		router.Get("/devices", GetRaspberries)
		router.Get("/aps", GetAPs)
		router.Get("/aps/{id}", GetAPsById)
		router.Get("/nulls", GetNullsById)
		router.Get("/{id}", GetProductById)
		router.Get("/lasthour", GetFailuresLastHour)
	})
}
