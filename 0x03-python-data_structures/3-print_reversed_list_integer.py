#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    num_list = len(my_list) - 1
    i = 0
    while i < num_list:
        temp = my_list[i]
        my_list[i] = my_list[num_list]
        my_list[num_list] = temp
        i += 1
        num_list -= 1
        j = 0
    while j <= len(my_list) - 1:
        print("{}".format(my_list[j]))
        j += 1
