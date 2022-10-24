#!/usr/bin/python3

"""Module which is based on 6-base_geometry.py"""


class BaseGeometry(object):
    """class which implements the base geometry"""

    def area(self):
        """function which raises exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates  value"""

        if type(name) is not str:
            raise TypeError("{} must be a string".format(name))
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
