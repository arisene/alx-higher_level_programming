#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for eleh in my_list:
            print(eleh, end='')
            count += 1
            if (count == x):
                break
        print()
        return count
    except ValueError:
        print('unerror occured')
        return 0
