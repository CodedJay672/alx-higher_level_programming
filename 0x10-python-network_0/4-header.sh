#!/bin/bash
# script that sends a custom header with a GET request
curl -sH "X-School-User-Id 98" "$1"
