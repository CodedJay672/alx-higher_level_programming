#!/bin/bash
# script that displays the size of the body of a server request
curl -s "$1" | wc -c
