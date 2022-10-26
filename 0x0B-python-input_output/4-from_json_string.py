#!/usr/bin/python3
"""moodyle which returns python structure from JSON"""
import json


def from_json_string(my_str):
    """function that converts json string to python 
    data structure.
    Args:
        @my_str: json string to convert
    Return: returns the python data structure
    """

    return json.loads(my_str)
