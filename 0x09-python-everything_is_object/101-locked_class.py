#!/usr/bin/python3
"""locked class module"""

class LockedClass:
    """prevents dynamic cretion of new instances"""

    ___slots__ = ["first_name"]
