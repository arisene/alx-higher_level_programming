#!/usr/bin/python3
"""
Based on 0-square.py
a square with a private instance attribute
"""


class Square:
    """
    args: takes the size of the square as a parameter
    return: has no return value
    """
    def __init__(self,size):
        self.__size = size
