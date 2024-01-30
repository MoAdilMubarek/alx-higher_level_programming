#!/usr/bin/python3
"""module for print_square method"""


def print_square(size):
    """print a square

    Args:
        size: size of square

    Raises:
        ValueError: size must be >= 0
        TypeError: size must be an integer
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#")
        print('\n')
