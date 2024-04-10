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

        if not isinstance(size, int):
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

    @property
    def size(self):
        """
        retrieving the value of size
        return:
            self.__size
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        change the value of size
        attribute:
            value, the new value
        return:
            new value of size
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        prints a square using "#" using the provided length
        attribute:
            takes no attribute
        return:
            has no return value
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#", end="")
                for j in range(self.__size - 1):
                    print("#", end="")
                print()
