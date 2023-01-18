#!/usr/bin/python3
"""
script to fetch the commits made by a github user

"""

import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])

    response = requests.get(url)
    commit = response.json()
    for i in range(10):
        print("{}: {}".format(commit[i].get("sha"),
            commit[i].get("commit").get("author").get("name")))
