#!/usr/bin/python:
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for colum in range(len(matrix[row])):
            if colum != 0:
                print(" ", end="")
            print("{:d}".format(matrix[row][colum]), end="")
        print()
