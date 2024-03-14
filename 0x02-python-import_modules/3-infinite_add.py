#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_arg = len(sys.argv) - 1
    if num_arg == 0:
        print(0)
    else:
        i = 1
        total = 0
        while i < (num_arg + 1):
            number = int(sys.argv[i])
            total += number
            i += 1
        print(total)
