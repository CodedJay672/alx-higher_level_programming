#!/usr/bin/python3

"""
defines the Rectangle class

"""


class Rectangle:
    """
    class sets a private width attribute
    class sets a private height attribute

    """

    def __init__(self, width=0, height=0):
        """constructor to initialize width and height"""
        self.__width = width
        self.__height = height

    def width(self, value):
        """ set width value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def width(self):
        """ get width value """
        return self.__width

    def height(self):
        """ get height value """
        return self.__height

    def height(self, value):
        """ set height value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
