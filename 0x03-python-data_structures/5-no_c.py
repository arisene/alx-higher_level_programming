#!/usr/bin/python3
def no_c(my_string):

    for st in my_string:
        if st == 'c' or st == 'C':
            continue
        else:
            print("{:s}".format(st), end='')
    return (st)
