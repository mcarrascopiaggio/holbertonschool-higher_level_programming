#!/bin/bash
# Get the request of URL and displays body response
curl -sX POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
