#!/bin/bash
# script that returns mthods allowed by a server
curl -s --head "$1" | grep "Allow" | cut -d " " -f 2-
