#!/usr/bin/python3
"""Module which writes text into a file"""


def write_file(filename="", text=""):
    """function which writes text into a file
    Args:
        @filename: name of the file
        @text: string to append to the file
    """
    
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
