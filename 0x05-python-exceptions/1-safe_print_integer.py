#!/usr/bin/python3
def safe_print_integer(value):
    try:
        keyValue = int(value)
        print("{:d}".format(keyValue))
        return True
    except ValueError:
        print("{} is not an integer".format(value))
        return False
