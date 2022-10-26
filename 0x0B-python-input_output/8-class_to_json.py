#!/usr/bin/python3
"""Class to json module"""


def class_to_json(obj):
    """function which converts python object to json dict
    Args:
        @obj: object instance of a class
    Returns a dict representation of the object
    """

    return obj.__dict__
