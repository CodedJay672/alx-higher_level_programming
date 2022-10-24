#!/usr/bin/python3

"""Module which checks the instance of an object"""


def is_kind_of_class(obj, a_class):
    """Function which accepts two arguments a and b
    checks if a is an instance of b
    returns True else False"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
