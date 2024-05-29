#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """ Rotate 2D Matrix"""
    N = len(matrix)
    new_matrix = [[0]*N for _ in range(N)]
    for i in range(0, N):
        for j in range(0, N):
            new_matrix[i][j] = matrix[N-j-1][i]
    for i in range(0, N):
        for j in range(0, N):
            matrix[i][j] = new_matrix[i][j]
