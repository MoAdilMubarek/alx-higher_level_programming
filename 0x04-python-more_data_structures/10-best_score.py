#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None;
    mxv = 0
    mxk = None
    for key, val in a_dictionary.items():
        if val > mxv:
            mxv = val
            mxk = key
    return mxk
