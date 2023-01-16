#!/bin/bash
# script that sends JSON POST request and displays the body of response
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
