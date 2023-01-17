#!/usr/bin/python3
"""script that sends a request to URL and displays a variable"""

import urllib.request
import sys

if __name__ == "__main__":
    page = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(page) as e:
        page = e.read()
        print(dict(page.headers).get("X-Request-Id"))
