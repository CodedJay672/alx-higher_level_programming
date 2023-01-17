#!/usr/bin/python3
"""
python script that accepts an email param, and prints
the body of the response.
script takes in a web address and an email

"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    page = requests.post(url, data=email)
    content = page.text
    print(content)
