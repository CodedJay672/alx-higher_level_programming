#!/usr/bin/python3
"""module which creates python object"""

import json


def load_from_json_file(filename):
    """function which creates python object from
    json file.
    Args:
        @filename: json file to work with
    Returns the object
    """

    with open(filename, 'r+', encoding="utf=8") as f:
        obj = f.read()
        obj = str(obj)
        return json.loads(obj)
