#!/usr/bin/python3
"""
 Change comes from within
"""


def makeChange(coins, total):
    """
    Find fewest number of coins needed
    :param coins: set of coins
    :param total: total amount of money
    :return: number of coins needed
    """
    if total <= 0:
        return 0
    count = 0
    i = 0
    coins.sort(reverse=True)
    while i <= len(coins) - 1:
        while total >= coins[i]:
            total -= coins[i]
            count += 1
        i += 1
    if total == 0:
        return count
    return -1
