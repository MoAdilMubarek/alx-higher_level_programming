#!/usr/bin/python3
"""Add 2 integers"""

def add_integer(x, y=98):
    """
    Adds 2 integers

    Args:
        a: int or float
        b: int or float

    Raises:
        TypeError: if a and  b are not int or float

    Return:
        sumation of the 2 numbers
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(x) + int(y)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
