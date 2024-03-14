#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_arg = len(sys.argv) - 1
    i = 1
    if num_arg == 0:
        print("0 arguments.")
    elif num_arg == 1:
        print("{} argument: ".format(num_arg))
    else:
        print("{} arguments: ".format(num_arg))
    while i < (num_arg + 1):
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
