#!/usr/bin/python3

"""
module that prints a list of available of
attributes and methods of an object

"""


def lookup(obj):
    """
    function to print the available attributes and methods of an object
    @obj: object argument to be worked with
    Return a list of attributes and methods

    """

    return dir(obj)
