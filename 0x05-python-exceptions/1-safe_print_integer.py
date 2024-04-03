#!/usr/bin/python3
def safe_print_integer(value):
    try:
        while True:
            int(value)
            print("{:d}".format(value))
            break
        return True
    except ValueError:
        return False
