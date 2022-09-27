#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list[:]
    if idx > len(my_list):
        return my_list[:]
    list_cp = my_list[:]
    for i in range(len(list_cp)):
        if i == idx:
            list_cp[i] = element
            return list_cp
