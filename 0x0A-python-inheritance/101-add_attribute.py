#!/usr/bin/python3
"""module that adds attribute to objects if possible"""


def add_attribute(obj, attr, value):
    """adds attibute and assign value to an object"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
