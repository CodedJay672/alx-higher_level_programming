#!/bin/bash
# script that semds request and display the status code
curl -sw "%{http_code}" "$1"
