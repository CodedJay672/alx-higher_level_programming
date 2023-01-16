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
        self.__width = width
        self.__height = height

    def width(self, value):
        """ set width value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ finds the area of the Rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ find the perimeter of the Rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ prints a graphical represenation of the rectangle using # """

        if self.__width == 0 or self.__height == 0:
            return ""
        rec = []
        for i in range(self.__height):
            [rec.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        """ returns a string representation of the Rectangle """

        rect = "Rectangle(" + str(self.__width)
        rect += "," + str(self.__height) + ")"
        return rect
