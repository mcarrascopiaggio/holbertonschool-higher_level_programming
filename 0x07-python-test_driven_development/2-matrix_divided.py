#!/usr/bin/python3
"""
this module has a fuction tha divide a matrix in a div
return a new matrix with two decimal
Raise an error matrix has a type different from int and float
Raise an error if the len of list in list are different
Raise an error if div is 0
"""

def matrix_divided(matrix, div):
    """ This function divide a matrix by a number
    and retur a new matrix with the result.
    """

    new_matrix = []
    long_e = 'matrix must be a matrix (list of lists) of integers/floats'
    len_matrix = len(matrix[0])

    if matrix is None:
        raise TypeError(long_e)
    if type(matrix) is not list:
        raise TypeError(long_e)
    if len(matrix) == 1:
        raise TypeError(long_e)
    for lis in matrix:
        if type(lis) != list:
            raise TypeError(long_e)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError(" div must be a number")
    for i in matrix:
        if len(i) != len_matrix:
            raise TypeError("Each row of the matrix must have the same size")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError(long_e)
    for i in matrix:
        new_matrix.append(list(map(lambda x: round(x/div, 2), i)))
    return new_matrix
