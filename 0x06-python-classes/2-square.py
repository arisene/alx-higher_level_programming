#!/usr/bin/python3
"""
Define  class Square
args:
    size(int) the length of the sides
"""


class Square:

    """
    initialize class Square
    attributes:
        __size a private attribute of size

    """
    def __init__(self, size=0):

        if not type(size) is int:
            raise TypeError("size must be an intege")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
