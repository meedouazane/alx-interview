#!/usr/bin/python3
""" 0. Minimum Operations """


def isprime(num):
    """Check number if it's prime or not"""
    for i in range(2, num - 1):
        if num % i == 0:
            return True
    return False


def minOperations(n):
    """method that calculates the fewest
    number of operations needed to result in exactly
    n H characters in the file."""
    ope = 0
    if isprime(n) and n % 2 != 0:
        ope = -1
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
