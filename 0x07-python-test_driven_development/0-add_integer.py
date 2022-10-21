#!/usr/bin/python3

"""
add_integer(a, b) adds two integers of floats
otherwise it returns a TypeError exception with.
function should return a + b
"""


def add_integer(a, b=98):
    """ Function which adds two integers
    and floas. Returns the sum of its arguments
    raises exception if arguments are not integers
    or floats
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
