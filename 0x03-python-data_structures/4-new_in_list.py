#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    copied_list = list(my_list)
    if idx < 0 or idx > len(copied_list) - 1:
        return copied_list
    else:
        copied_list[idx] = element
        return copied_list
