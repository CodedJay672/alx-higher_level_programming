#!/usr/bin/python3
"""
python script that sends a request and displays the content of 
a variable.
script should take a web address via the sys library

"""

import sys
import requests

if __name__ == "__main__":
    page = requests.get(sys.argv[1])
    print(page.headers.get("X-Request-Id"))
