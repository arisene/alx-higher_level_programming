#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    copied_list = list(my_list)
    len_list = len(copied_list) - 1
    if idx < 0:
        return copied_list
    elif idx < len_list:
        copied_list[idx] = element
        return copied_list
    else:
        return copied_list
