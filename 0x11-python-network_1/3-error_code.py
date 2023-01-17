#!/usr/bin/python3
"""
python script that accepts URL and displays body of response
script should manage HTTPError and print error code/message

"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]

    page = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(page) as e:
            print(e.read().decode("utf-8"))
    except urllib.request.HTTPError as er:
        print("Error code: {}".format(er.code))
