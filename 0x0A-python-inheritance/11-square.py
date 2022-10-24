#!/usr/bin/python3

"""Module which inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Derived class inherits from rectangle class"""

    def __init__(self, size):
        """constuctor"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculates the area of the square"""

        return self.__size**2

    def __str__(self):
        """implementation of print() and str()"""

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
