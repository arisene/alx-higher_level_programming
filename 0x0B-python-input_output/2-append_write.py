#!/usr/bin/python3
"""
Write a function that appends 
a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    Append the text to the file
    return: the number of bytes
    """
    with open(filename, mode="a+", encoding="utf-8") as my_file:
        my_file.write(text)
        length = my_file.tell()
    return length
