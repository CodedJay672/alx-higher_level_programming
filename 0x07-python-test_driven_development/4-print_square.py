#!/usr/bin/python3

"""
module of function which prints a square
function argument is the 'size' of the square

"""

def print_square(size):
    """
    function shich prints a square on stdout
    @size: integer argument showing size of square

    """
    char = "#"

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    for row in range(size):
        for cols in range(size):
            print(char, end="")
        print()
