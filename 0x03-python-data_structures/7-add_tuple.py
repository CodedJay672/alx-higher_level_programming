#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple_a = []
    new_tuple_b = []
    result = []
    new_tuple_a = list(tuple_a)
    new_tuple_b = list(tuple_b)
    if len(new_tuple_a) < 2:
        for i in range(2 - len(new_tuple_a)):
            new_tuple_a.append(0)
    if len(new_tuple_b) < 2:
        for j in range(2 - len(new_tuple_b)):
            new_tuple_b.append(0)
    for k in range(2):
        result.append(new_tuple_a[k] + new_tuple_b[k])
    return tuple(result)
