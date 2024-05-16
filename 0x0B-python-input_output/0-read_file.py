#!/usr/bin/python3
"""
Module 0
"""


def read_file(filename=""):
    """
    Reads and print to stdout the content
    of the text-file
    """
    with open(filename, mode="r", encoding="utf-8") as myfile:
        fp = myfile.read()
    print(fp, end="")
