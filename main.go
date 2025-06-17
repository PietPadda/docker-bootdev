// main.go
package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"time"
)

func main() {
	m := http.NewServeMux() // create new request router

	m.HandleFunc("/", handlePage) // send requests for the root path endpoint to handlePage

	// get port from os via shell (terminal)
	port := os.Getenv("PORT")

	// edge case no port set
	if port == "" {
		port = "8010" // fallback default
	}

	// define the server struct
	srv := http.Server{
		Handler:      m,                // use router as handler
		Addr:         ":" + port,       // :port
		WriteTimeout: 30 * time.Second, // timeout for safety
		ReadTimeout:  30 * time.Second, // timeout for safety
	}
	// writes to/reads from client after X time closes connection

	// this blocks forever, until the server
	// has an unrecoverable error
	fmt.Println("server started on ", port) // start log
	err := srv.ListenAndServe()             // server blocker -- infinite loop
	log.Fatal(err)                          // only ends when fatal err returns
}

// our root path endpoint handler
func handlePage(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "text/html") // set header to html
	w.WriteHeader(200)                          // 200 OK status code

	// simple html page
	const page = `<html> 
<head></head>
<body>
	<p> Hi Docker, I pushed a new version. </p>
</body>
</html>
`
	// html response writer
	w.Write([]byte(page)) // write html const page as byte slice for html response
}
