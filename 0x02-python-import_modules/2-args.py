#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_arg = len(sys.argv) - 1
    if num_arg == 0:
        print("0 arguments.")
    else:
        plural_suffix = 's' if num_arg > 1 else ''
        print(f"{num_arg} argument{plural_suffix}:")

        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")
