#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    Adictionary = a_dictionary.copy()
    for value in Adictionary.values():
        value *= 2
    return Adictionary
