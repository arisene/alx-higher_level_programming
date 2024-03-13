#!/usr/bin/python3
def print_last_digit(number):
    num_str = str(number)
    l_num = num_str[-1]
    return print("{}".format(int(l_num)), end="")
