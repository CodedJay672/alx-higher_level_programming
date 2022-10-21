#!/usr/bin/python3

""" function that divides all elements of a matrix """
def matrix_divided(matrix, div):
    """ 
    matrix divider returns a new divided matrix
    new matrix works with integers and floats.

    """

    if (not isinstance(div, int) and not isinstance(div, float)):
        return TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    size = len(matrix[0])

    for mat_list in matrix:
        if not isinstance(mat_list, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(mat_list) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for l in mat_list:
            if (not isinstance(l, int) and not isinstance(l, float)):
                raise TypeError("matrix must be a  matrix (list of lists) of integers/floats")
    return [[round(j / div, 2) for j in my_list] for my_list in matrix]
