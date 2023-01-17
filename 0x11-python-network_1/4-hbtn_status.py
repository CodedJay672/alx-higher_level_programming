#!/usr/bin/python3
"""
python script that fetches a url using requests package

"""

import requests

if __name__ == "__main__":
    page = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(page.text)))
    print("\t- content: {}".format(page.text))
