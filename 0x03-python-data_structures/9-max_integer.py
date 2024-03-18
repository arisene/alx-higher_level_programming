#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        big = my_list[0]
        for i in range(len(my_list)):
            if big < my_list[i]:
                big = my_list[i]
        return big
