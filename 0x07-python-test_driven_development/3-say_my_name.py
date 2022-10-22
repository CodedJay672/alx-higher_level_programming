#!/usr/bin/python3

"""
module which takes at least one argument
prints "My name is <first_name> <last_name>"

"""


def say_my_name(first_name, last_name=""):
    """
    accepts two strings <first_name> and <last_name>
    prints a greeting string involving both names

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))