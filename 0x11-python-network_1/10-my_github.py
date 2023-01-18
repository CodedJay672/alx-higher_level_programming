#!/usr/bin/python3
"""Python script that prints a github user ID
script takes a username and password as arguments"""

import sys
import requests
from from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    login = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    page = requests.get("https://api.github.com/user", auth=login)
    print(r.json().get("id"))
