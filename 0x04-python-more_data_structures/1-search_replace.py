#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_List = my_list[:]
    for i in range(len(my_List)):
        if my_List[i] == search:
            my_List[i] = replace
    return my_List
