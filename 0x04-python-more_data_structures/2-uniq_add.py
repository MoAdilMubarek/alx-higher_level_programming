#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    List = []
    for i in range(len(my_list)):
        if my_list[i] not in List:
            List.append(my_list[i])
    for n in List:
        res += n
    return res
