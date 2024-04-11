#!/usr/bin/python3
"""
Module 2 creating a class called rectangle
with private attributes width and height
"""


class Rectangle:
    """
    Defines class rectangle with private attribute width and height

    Args:
        width (int): width
        height (int): height

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """
    def __init__(self, width=0, height=0):
        """
        the instantiation method of width and height
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """
        the getter method of the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        the setter method of the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        the getter method of the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        the setter method of the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
