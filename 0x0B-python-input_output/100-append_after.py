#!/usr/bin/python3
"""search and replace module"""

def append_after(filename="", search_string="", new_string=""):
    """searches for a string in a file
    replaces the search string with new string
    Args:
        @filename: name of file
        @search_string: string to replace
        @new_string: replacement string
    """

    with open(filename, 'r', encoding="utf-8") as f:
        new_file = f.readlines()

    with open(filename, 'w', encoding="utf-8") as fi:
        s = ""
        for line in new_file:
            s += line
            if search_string in new_file:
                s += new_string
        fi.write(s)
