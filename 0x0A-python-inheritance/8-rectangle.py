#!/usr/bin/python3
"""Module which inherits BaseGeometry"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Derive class which inherits from BaseGeometry"""

    def __init__(self, width, height):
        """constructor and instance variables"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
