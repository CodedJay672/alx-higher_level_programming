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
