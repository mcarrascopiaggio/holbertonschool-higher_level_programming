#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ This function divide a matrix by a number
    and retur a new matrix with the result.
    """

    new_matrix = []
    len_matrix = len(matrix[0])

    if div == 0:
        raise("division by zero")
    for i in matrix:
        if len(matrix[i]) != len_matrix:
            raise("Each row of the matrix must have the same size")
    for i in matrix:
        for j in i:
            if type(matrix[i][j]) is not int and
            type(matrix[i][j]) is not float:
                raise("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        new_matrix.append(list(map(lambda x: x/div, i)))
    return new_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
new_matrix = (matrix_divided(matrix, 3))
roun_new_matrix = [round (num, 2) for num in new_matrix]
print(roun_new_matrix)
print("the leng of the matrix is {:d}".format(len(matrix)))
print("the leng of the matrix list 1 is {:d}".format(len(matrix[0])))
print("the leng of the new matrix is {:d}".format(len(new_matrix)))
