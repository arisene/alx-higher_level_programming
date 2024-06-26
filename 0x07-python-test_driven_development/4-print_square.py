#!/usr/bin/python3
"""
module 4 square
"""
def print_square(size):
    """
    print a  square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) or size < 0:
        raise TypeError("size must be an integer")
    
    for i in range(size):
        for j in range(size - 1):
            print("#", end="")
        print("#\n", end="")

