#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None;
    mx = 0
    for key, val in a_dictionary.items():
        mx = mx if mx > val else val
    return key
