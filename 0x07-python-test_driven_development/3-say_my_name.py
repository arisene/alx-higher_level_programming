#!/usr/bin/python3
"""
Module 3 print my name
"""

def say_my_name(first_name, last_name=""):
    """
    attributes:
        first_name
        last_name
    print:
    all names
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
