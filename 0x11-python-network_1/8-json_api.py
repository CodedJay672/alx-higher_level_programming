#!/usr/bin/python3
"""
python script that checks for valid JSON responses

"""

import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    page = requests.post("http://0.0.0.0:5000/search_user", data={"q": letter})
    try:
        page = page.json()
        if page == {}:
            print("No result")
        else:
            print("[{}] {}".format(page.get("id"), page.get("name")))
    except ValueError:
        print("Not a valid JSON")
