#!/usr/bin/python3
"""Square moduule."""


class Square:
    """Define a Square class."""

    def __init__(self, size=0):
        """constructor.

        Args:
            size: size of square

        Raises
            ValueErrror: when size < 0
            TypeError: when size is not int
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else
        self.__size = size

