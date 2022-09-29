#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    val_list = a_dictionary.values()
    if value not in val_list:
        return a_dictionary
    keys = [k for k, v in a_dictionary.items() if v == value]
    for i in keys:
        del a_dictionary[i]
    return a_dictionary
