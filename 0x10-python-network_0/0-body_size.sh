#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
# curl -sI "$1" : Para traer la informacion del servidor
# grep "Content-Length": Me quedo solo con el campo de los bytes
# cut -d ":" -f 2: quito las comillas
# cut -d " " -f 2 quito los dos primeros espacios
curl -sI "$1" | grep "Content-Length" | cut -d ":" -f 2 | cut -d " " -f 2
