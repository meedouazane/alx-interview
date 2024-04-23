#!/usr/bin/python3
""" 0. Minimum Operations """


def minOperations(n):
    """method that calculates the fewest
    number of operations needed to result in exactly
    n H characters in the file."""
    ope = 0
    if n <= 1:
        return 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            ope += 2
        else:
            n = n - 1
            ope += 1
    return ope
