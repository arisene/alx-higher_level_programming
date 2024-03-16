#!/usr/bin/python3
def no_c(my_string):
    last_char = my_string[-1]  # Get the last character before removing 'c's

    for st in my_string:
        if not st.lower() == 'c':
            print("{:s}".format(st), end='')

    return last_char
