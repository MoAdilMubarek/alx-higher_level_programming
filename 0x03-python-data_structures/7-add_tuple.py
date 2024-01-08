#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    c = []
    i = 0
    while i < 2:
        aa = tuple_a[i] if len(tuple_a) > i else 0
        bb = tuple_b[i] if len(tuple_b) > i else 0
        c.append(aa + bb)
        i += 1
    return tuple(c)
