#!/usr/bin/python3
"""The function in this module divides
integer of float numbers in a matrix by a divisior
"""


def matrix_divided(matrix, div):
    """matrix_divided takes two argument(a matrix and a divisor)
    and return a the matrix with each of it integer or float element divided by
    the divisor
    """

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/float")
    size = None
    for leng in matrix:
        if size == None:
            size = len(leng)
        elif size != len(leng):
            raise TypeError("Each row of the matrix must have the same size")
        for i in leng:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrix = [[round((x/div), 2) for x in leng] for leng in matrix]
    return(matrix)
