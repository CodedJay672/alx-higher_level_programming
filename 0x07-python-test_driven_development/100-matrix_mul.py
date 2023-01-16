#!/usr/bin/python3

"""
module that multiplies two matrices

"""


def matrix_mul(m_a, m_b):
    """
    function which takes two matrices and multiples them
    @m_a: first matrix
    @m_b: second matrix
    Returns a new matrix holding the product of m_a and m_b

    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for m_a_list in m_a:
        if not isinstance(m_a_list, list):
            raise TypeError("m_a must be a list of lists")
    for m_b_list in m_b:
        if not isinstance(m_b_list, list):
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    for ma_list in m_a:
        if len(ma_list) == 0:
            raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for mb_list in m_b:
        if len(mb_list) == 0:
            raise ValueError("m_b can't be empty")
    for a_list in m_a:
        for element in a_list:
            if (type(element) != int and type(element) != float):
                raise TypeError("m_a should contain only integers or floats")
    for b_list in m_b:
        for element in b_list:
            if (type(element) != int and type(element) != float):
                raise TypeError("m_b should contain only integers or floats")

    a_list_size = len(m_a[0])
    b_list_size = len(m_b[0])


    for a_list in m_a:
        if len(a_list) != a_list_size:
            raise TypeError("each row of m_a must be the same size")
    for b_list in m_b:
        if len(b_list) != b_list_size:
            raise TypeError("each row of m_b must be the same size")

    prod_mat = [[]]


    for a_list in m_a:
        for count in range(m_b):
            prod_mat.append(
                            (m_b[count][count] * a_list[count])
                            +
                            (m_b[count += 1[count] * a_list[count++])
                           )
           
