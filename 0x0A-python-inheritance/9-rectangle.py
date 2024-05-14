#!/usr/bin/python3
"""
class that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class sub_class of basegeometry
    """
    def __init__(self, width, height):
        """
        validate and initialize width and height
        Args:
            width (int): private
            height (int): private
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
