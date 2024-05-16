#!/usr/bin/python3
"""
Module 1
"""


def write_file(filename="", text=""):
    """
    Method write text to a file
    return the number of characters written
    """
    with open(filename, mode="w+", encoding="utf-8") as my_file:
        my_file.write(text)
        length = my_file.tell()
    return length
