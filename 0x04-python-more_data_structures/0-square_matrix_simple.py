#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    for i in range(len(matrix)):
        res.append(list(map(lambda x: x**2, matrix[i])))
    return res
