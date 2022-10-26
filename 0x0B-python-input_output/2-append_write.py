#!/usr/bin/python3
"""module which appends text to a file"""


def append_write(filename="", text=""):
    """function which appends text to a text fie
    Args:
        @filename: name of the destination file
        @text: string to append to file
    Retruns the number of characters added
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
