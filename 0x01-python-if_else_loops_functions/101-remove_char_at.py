#!/usr/bin/python3
def remove_char_at(str, n):
    j = len(str)
    str2 = ""
    for i in range(0, j):
        if i == n:
            continue
        else:
            str2 += str[i]
    return str2
