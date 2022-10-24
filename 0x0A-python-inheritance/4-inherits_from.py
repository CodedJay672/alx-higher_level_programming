#!/usr/bin/python3

"""Module whcih compares two objects"""


def inherits_from(obj, a_class):
    """function which accpets two arguments a and b
    checks if a is a subclass of b
    returns True else returns False"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
