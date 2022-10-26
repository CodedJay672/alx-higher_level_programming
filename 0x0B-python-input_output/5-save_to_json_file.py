#!/usr/bin/python3
"""module which writes an object to text file
using JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """function which write objects to text file
    Description -> using json representation to write
                to a text file
    Args:
        @my_obj: python object
        @filename: text filename
    """

    with open(filename, 'w', encoding="utf-8") as f:
        text = json.dumps(my_obj)
        return f.write(text)
