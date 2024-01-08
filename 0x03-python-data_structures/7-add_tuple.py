#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    c = []
    i = 0
    while i < 2:
        aa = a[i] if len(a) > i else 0
        bb = b[i] if len(b) > i else 0
        c.append(aa + bb)
        i += 1
    return tuple(c)
