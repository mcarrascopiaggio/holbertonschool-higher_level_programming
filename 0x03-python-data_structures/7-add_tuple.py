#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_add = ()
    a0, a1, b0, b1 = 0, 0, 0, 0
    if len(tuple_a) == 1:
        a0 = tuple_a[0]
    if len(tuple_b) == 1:
        b0 = tuple_b[0]
    if len(tuple_a) > 1:
        a0 = tuple_a[0]
        a1 = tuple_a[1]
    if len(tuple_b) > 1:
        b0 = tuple_b[0]
        b1 = tuple_b[1]
    tuple_add = (a0 + b0, a1 + b1)
    return tuple_add
