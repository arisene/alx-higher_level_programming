#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = 0
        result = int(a) / int(b)
        print("Inside result: {}".format(result))
    except ZeroDivisionError:
        result = None
        print("Inside result: {}".format(result))
    finally:
        return result
