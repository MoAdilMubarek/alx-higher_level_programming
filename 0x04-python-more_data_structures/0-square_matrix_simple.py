#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    Matrix = [[] for n in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            Matrix[i].insert(j, matrix[i][j] ** 2)
#    Matrix = [x[i] ** 2 for x in matrix for i in range(len(x) - 1)]
    return Matrix
