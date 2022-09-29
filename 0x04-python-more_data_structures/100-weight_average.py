#!/usr/bin/python3
def weight_average(my_list=[]):
    res = []
    denom = []
    avg = 0
    div = 0
    if my_list is None or len(my_list) == 0:
        return 0
    for i in my_list:
        res = list(i)
        avg += (res[0] * res[1])
    for j in my_list:
        denom = list(j)
        div += denom[1]
    return avg/div
