#!/bin/bash
# script that semds request and display the status code
curl -so /dev/null -w "%{http_code}" "$1"
