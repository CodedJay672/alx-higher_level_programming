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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height

    @getwidth
    def width(self, value):
        """ set width value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @widthparameter
    def width(self):
        """ get width value """
        return self.__width

    @heightparameter
    def height(self):
        """ get height value """
        return self.__height

    @setheight
    def height(self, value):
        """ set height value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
