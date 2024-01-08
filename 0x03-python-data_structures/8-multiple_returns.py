#!/usr/bin/python3
def multiple_returns(sentence):
    c = tuple(sentence)
    return len(c), c[0] if len(c) > 0 else None
