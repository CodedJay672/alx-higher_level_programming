#!/usr/bin/python3
"""
python script that sends an email to a URL

"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    email = {"email": sys.argv[2]}
    url = sys.argv[1]

    data = urllib.parse.urlencode(email)
    data = urllib.encode('ascii')
    post = urllib.request.Requesr(url, data)
    with urllib.request.urlopen(post) as e:
        print(e.read().decode('utf-8'))
