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
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
