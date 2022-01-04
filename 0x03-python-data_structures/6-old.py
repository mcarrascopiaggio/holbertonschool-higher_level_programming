#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    for row in matrix:
        col = 0
        for i in row:
            if col != 0:
                print(' ', end="")
            print("{:d}".format(i), end='')
            col = col + 1
        print()
