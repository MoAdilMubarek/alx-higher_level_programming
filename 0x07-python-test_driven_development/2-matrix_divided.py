#!/usr/bin/python3
"""Module for matrix_divided method"""

def matrix_divided(matrix, div):
    """Divide matrix elem by div

    Args:
        matrix: list of lists
        div: number

    Raises:
        ZeroDivisionError: if div is zero
        TypeError: if matrix is not list of lists of int or float, and div must be > 0

    Return:
        matrix
    """

    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
            raise ZeroDivisionError("division by zero")
    size = len(matrix[0])

    for sub_list in matrix:
        if not isinstance(sub_list, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if (len(sub_list) == 0):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if size != len(sub_list):
            raise TypeError("Each row of the matrix must have the same size")

        for num in sub_list:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]

if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")



