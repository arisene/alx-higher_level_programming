#!/usr/bin/python3
"""
module 1 creating a class
"""


class Square:
    """
    class representing a square
    args:
        size is the length of the sides of a square
    """
    def __init__(self, size):
        """
        initialize square

        attribute:
                size=self.__size
        """
        self.__size = size
