#!/usr/bin/python3
"""
Prime Game
"""


def isPrime(x):
    """
    verify if number is prime or not
    :param x: number
    :return: True if x is prime, False if not
    """
    for i in range(2, x - 1):
        if x % i == 0:
            return False
    return True


def isMultiples(num, x):
    """
    verify if number is Multiples or not
    :param x: number
    :return: True if x is Multiples, False if not
    """
    if num % x == 0:
        return True
    return False


def isWinner(x, nums):
    """
    Determine who the winner of each game.
    :param x: rounds
    :param nums: set of numbers
    :return: name of the player that won the most rounds
    """
    win = 0
    Ben = 0
    Maria = 0
    for i in nums:
        setNums = []
        setNums = [n for n in range(1, i + 1)]
        for k in setNums:
            if isPrime(k):
                num = k
                setNums.remove(k)
                win += 1
                for m in setNums:
                    if isMultiples(num, m):
                        setNums.remove(m)
        if win % 2 != 0:
            Ben += 1
        else:
            Maria += 1
    if Ben > Maria:
        return 'Ben'
    elif Maria > Ben:
        return 'Maria'
    else:
        return None
