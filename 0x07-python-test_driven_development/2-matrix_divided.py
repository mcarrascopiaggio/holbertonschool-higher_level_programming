#!/usr/bin/python3
"""
2-matrix_divided.py
divides all elements of a matrix.
Returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix.
    """
    Error = "matrix must be a matrix (list of lists) of integers/floats"
    Msg = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError(Error)
    for row in matrix:
        if len(row) == 0:
            raise TypeError(Error)
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError(Error)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    len_row = len(matrix[0])
    if div == 0:
        raise ZeroDivisionError("division by zero")
    lenght_row = len(matrix[0])
    for row in matrix:
        if len(row) != lenght_row:
            raise TypeError(Msg)
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda x: round(x/div, 2), row)))
    return new_matrix
