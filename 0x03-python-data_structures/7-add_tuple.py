#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t1 = len(tuple_a)
    t2 = len(tuple_b)
    res = ((tuple_a[0] if t1 > 0 else 0) + (tuple_b[0] if t2 > 0 else 0),
           (tuple_a[1] if t1 > 1 else 0) + (tuple_b[1] if t2 > 1 else 0))
    return res
