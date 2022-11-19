#!/usr/bin/python3
"""locked class module"""


class LockedClass(object):
    """prevents dynamic cretion of new instances"""

    __slots__ = ["first_name"]
