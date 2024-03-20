#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_list = sorted(a_dictionary.items())
    sort_dict = {}
    for k, y in a_list:
        sort_dict[k] = y
    for k, y in sort_dict.items():
        print("{}: {}".format(k, y))
