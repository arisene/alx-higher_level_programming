#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_two = {}
    for k, y in a_dictionary.items():
        dict_two[k] = y * 2
    return dict_two
