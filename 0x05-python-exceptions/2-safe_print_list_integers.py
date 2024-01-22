#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0, n =  0
    try:
        while i < x:
            print("{d}".format(my_listt[i]))
            i += 1
        except (ValueError, TypeError):
            pass
        n += 1
    return n
