#!/usr/bin/python3
"""module that reads a file and prints to stdout"""


def read_file(filename=""):
    """function which reads a file and writes to stdout"""

    with open(filename, "r+", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
