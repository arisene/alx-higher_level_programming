#!/usr/bin/python3
""" 
Module 5
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is 
    an instance of a class 
    that inherited (directly or indirectly)
    from the specified class
    """
    return type(obj) is a_class
