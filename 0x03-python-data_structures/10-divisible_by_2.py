#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    log_list = []
    i = 0
    while i < len(my_list):
        if my_list[i] % 2 == 0:
            log_list.append(True)
        else:
            log_list.append(False)
        i += 1
    return log_list
