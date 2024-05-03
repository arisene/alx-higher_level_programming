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
        area(self)
        perimeter(self)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        the instantiation method of width and height
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        the area of rectangle: formula lenght * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        the perimeter of a rectangle: formula 2(length + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """
        print the rectangle using "#"
        """
        if self.__width == 0 or self.__height == 0:
            return
        else:
            rect = '\n'.join(['#' * self.__width
                              for rows in range(self.__height)])
        return f"{rect}"

    def __repr__(self):
        """
        print out the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        delete instances
        """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    def bigger_or_equal(rect_1, rect_2):
        rect_1 = rect_1
        rect_2 = rect_2
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2 == rect_1:
            return rect_1

        area_1 = rect_1.width * rect_1.height
        area_2 = rect_2.width * rect_2.height
        if area_1 >= area_2:
            return area_1
        else:
            return area_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
