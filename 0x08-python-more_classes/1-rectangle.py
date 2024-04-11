#!/usr/bin/python3
"""
Module 2 creating a class called rectangle
"""


class Rectangle:
    """
    Empty class Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        the instantiation method of width and height
        attributes:
            width of the rectangle set to zero as default
            height of the rectangle set to zero as default
        returns:
            has no return value

        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """
        the getter method of the height
        attributes: takes no attribute
        returns:
            the current value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        the setter method of the height
        attributes:
            value the new value of the height
        raises:
            TypeError in case the value is not an int
            ValueError in case the value is less than zero
        returns:
            has no return value
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
        attributes: takes no attribute
        returns:
            the current value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        the setter method of the width
        attributes:
            value the new value of the width
        raises:
            TypeError in case the value is not an int
            ValueError in case the value is less than zero
        returns:
            has no return value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
