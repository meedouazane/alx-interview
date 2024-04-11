#!/usr/bin/python3
"""  The Pascal’s triangle of n """


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the n row.
    """
    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = triangle[-1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)
        triangle.append(row)
    return triangle
