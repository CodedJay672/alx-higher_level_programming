#!/usr/bin/python3

"""Module which is based on 6-base_geometry.py"""


class BaseGeometry(object):
    """class which implements the base geometry"""

    def area(self):
        """function which raises exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates  value"""

        if type(name) != str:
            raise TypeError("<name> must be a string")
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
