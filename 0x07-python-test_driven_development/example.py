#run test with python3 -m doctest -v ./tests/2-matrix_divided.txt

First import the method to test
>>> matrix_divided = __import__('2-matrix_divided').matrix_divided

SUCCESS CASES:

Test signed and unsigned ints and floats:

    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> print(matrix_divided(matrix, 4))
    [[0.25, 0.5, 0.75], [1.0, 1.25, 1.5]]
    >>> print(matrix_divided(matrix, 9))
    [[0.11, 0.22, 0.33], [0.44, 0.56, 0.67]]

FAILD CASES:

Test if elements of matrix are int/floats:
    >>> print(matrix_divided(None, 2))

    Traceback (most recent call last):

    TypeError: matrix must be a matrix (list of lists) of integers/floats

Test if the  length of rows of matrix is the same:

    >>> matrix3 = [
    ...     [4, 5, 6],
    ...     [5, 6]
    ... ]
    >>> print(matrix_divided(matrix3, 6))
    Traceback (most recent call last):
    ...
    TypeError: Each row of the matrix must have the same size

Test if not div in an int/float:

    >>> matrix1 = [
    ...     [1,4,6],
    ...     [5,6,7]
    ... ]
    >>> print(matrix_divided(matrix1, 'go'))
    Traceback (most recent call last):
    ...
    TypeError: div must be a number

Test if not div is equal to zero:

    >>> print(matrix_divided(matrix1, 0))
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero