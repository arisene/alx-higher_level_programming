#!/usr/bin/python3
"""
Module 0 function that returns a list
of methods and attributes of an object
"""


def lookup(obj):
    """ returns a list of att & Meth"""
    list_methods = list()
    list_methods.append(dir(obj))

    return list_methods[0]
