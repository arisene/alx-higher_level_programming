#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        countT = 0
        count = 0
        for eleh in my_list:
            if isinstance(eleh, int) or isinstance(eleh, float):
                eleh = str(eleh)
            if eleh.isdigit():
                print("{:d}".format(int(eleh)), end="")
                count += 1
            countT += 1
            if (countT == x):
                break
        print()
        return count
    except IndexError:
        print("The index provided is not available")
