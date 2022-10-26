#!/usr/bin/python3
"""module which converts objects to JSON representation"""

import json


def to_json_string(my_obj):
    """function which translates objects to JSON
       representation.
       Args:
            @my_obj: python object
        Return: JSON representation of obj
    """

    return json.dumps(my_obj)
