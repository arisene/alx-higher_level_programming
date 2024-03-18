#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            if num is not row[len(row) - 1]:
                print("{}".format(num), end=" ")
            else:
                print("{}".format(num), end="")
        print()
