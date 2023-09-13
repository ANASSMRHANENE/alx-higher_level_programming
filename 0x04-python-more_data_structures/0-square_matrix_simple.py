#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = [[n**2 for n in row] for row in matrix]
    return newmatrix
