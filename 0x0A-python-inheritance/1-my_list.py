#!/usr/bin/python3
"""
Module 1 Inheritance
"""


class MyList(list):
    """ child class sorting in asc. ord"""

    def print_sorted(self):
        """sort the list of int and print them"""
        sorted_list = sorted(self)
        print(sorted_list)
