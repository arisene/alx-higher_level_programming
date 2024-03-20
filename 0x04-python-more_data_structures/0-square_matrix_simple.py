#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_matrix = []
    for row in matrix:
        copy_matrix.append([num ** 2 for num in row])
    return copy_matrix
