#!/usr/bin/python3
def multiple_returns(sentence):
    c = tuple(sentence)
    return len(c), c[0]
