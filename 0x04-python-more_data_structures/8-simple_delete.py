#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key is None or len(key) == 0:
        return a_dictionary
    elif key not in a_dictionary:
        return a_dictionary
    a_dictionary.pop(key)
    return a_dictionary
