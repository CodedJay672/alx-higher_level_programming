#!/bin/bash
# script that sends a POST request with some pameters
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLS" "$1"
