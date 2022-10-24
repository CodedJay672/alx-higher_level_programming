#!/usr/bin/python3

""" Module to check the instance of a specified class"""

def is_same_class(obj, a_class):
    """function which accepts two arguements a and b
    checks if a is an instance of b
    Returns True if a isinstance of b else False"""

    if type(obj) == a_class:
        return True
    else:
        return False
