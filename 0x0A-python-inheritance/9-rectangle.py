#!/usr/bin/python3

"""Module which inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Derive class which inherits from BaseGeometry"""

    def __init__(self, width, height):
        """constructor"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculates the area of the Rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """returns print() and str() strings"""

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
