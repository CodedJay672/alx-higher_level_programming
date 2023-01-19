#!/bin/bash
# script that makes a request to a server, which in turn, responds in a certain way
curl -sLX PUT -d "user_id=98" 0.0.0.0:5000/catch_me
