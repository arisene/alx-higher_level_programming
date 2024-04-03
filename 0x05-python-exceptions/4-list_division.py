#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        newList = []
        for i in range(list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
                newList.append(result)
            except TypeError:
                print("wrong type")
                newList.append(0)
            except ZeroDivisionError:
                print("division by 0")
                newList.append(0)
            except IndexError:
                print("out of range")
                newList.append(0)
    except KeyError:
        print("Unexpected error occured")
    finally:
        return newList
