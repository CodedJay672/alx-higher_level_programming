#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple_a = []
    new_tuple_b = []
    result = []
    new_tuple_a = list(tuple_a)
    new_tuple_b = list(tuple_b)
    if len(new_tuple_a) == 0:
        return tuple_b
    if len(new_tuple_b) == 0:
        return tuple_a
    if len(new_tuple_a) < 2:
        new_tuple_a.append(0)
    if len(tuple_b) < 2:
        new_tuple_b.append(0)
    for i in range(2):
        result.append(new_tuple_a[i] + new_tuple_b[i])
    return tuple(result)
