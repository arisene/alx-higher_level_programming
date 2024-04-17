#!/usr/bin/python3
"""
module 2 Matrix
"""

def are_integer(matrix):
    """
    check if the matrix's elements
    are all entegers/floats
    """
    for row in matrix:
        for eleh in row:
            if not isinstance(eleh, (int, float)):
                return False
            
    return True

def equal_rows(matrix):
    """ check rows of the matrix"""
    row_sizes = {len(row) for row in matrix}
    return len(row_sizes) == 1

def matrix_divided(matrix, div):

    if not isinstance(type(matrix), list) or are_integer(matrix) != True or len(matrix[0]) == 1:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif equal_rows(matrix) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new_matrix = []
        for row in matrix:
            new_row = []
            for eleh in row:
                new_row.append(round((eleh/div), 2))
            new_matrix.append(new_row)
        return new_matrix
