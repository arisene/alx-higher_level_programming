#!/usr/bin/python3
"""
Module 2
A class that defines a square
"""


class Square:

    """
    Define  class Square
    args:
        size(int) the length of the sides
    """
    def __init__(self, size=0):

        """
        initialize class Square
        attributes:
            __size a private attribute of size set default to zero
        """

        if not type(size) is int:
            raise TypeError("size must be an intege")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):

        """
        arguments:
            takes no argument
        returns:
            area of the square
            uses the value of self.__size to calculate the area
        """
        return (self.__size ** 2)
