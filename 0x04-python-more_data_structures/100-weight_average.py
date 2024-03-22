#!/usr/bin/python3
def weight_average(my_list=[]):

    if not my_list:
        return 0
    w_average = 0
    total = 0
    weight = 0
    for lit in my_list:
        if isinstance(lit, tuple):
            value, weight_value = lit
            lit = {value: weight_value}

        for k, y in lit.items():
            total += (k * y)
            weight += y
    w_average = total / weight
    return w_average
