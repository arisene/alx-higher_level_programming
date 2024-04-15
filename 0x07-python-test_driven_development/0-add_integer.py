#!/usr/bin/python3
def add_integer(a, b=98):
    """
    provide the sum of a and b
    args:
        a is an integer or float
        b is an integer or float set default 98
    return:
        sum of a + b
    raises:
        TypeError
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return int(a) + int(b)
    else:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        elif not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
