#!/usr/bin/python3
def max_integer(my_list=[]):
    i = 0
    if len(my_list) == 0:
        return None
    Max = my_list[i]
    while i < len(my_list):
        Max = my_list[i] if my_list[i] > Max else Max
        i += 1
    return Max
