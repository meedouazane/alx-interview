#!/usr/bin/python3
"""
Prime Game
"""

def isPrime(n):
    """
    Check if a number is prime.
    :param n: number
    :return: True if n is prime, False otherwise
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def countPrimes(n):
    """
    Count the number of prime numbers up to and including n.
    :param n: number
    :return: number of primes <= n
    """
    if n < 2:
        return 0
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while (p * p <= n):
        if (sieve[p] == True):
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1
    return sum(sieve)

def isWinner(x, nums):
    """
    Determine who the winner of each game is.
    :param x: number of rounds
    :param nums: list of integers representing the set of numbers for each round
    :return: name of the player that won the most rounds or None if it's a tie
    """
    if not nums or x <= 0:
        return None
    
    Maria_wins = 0
    Ben_wins = 0
    
    for num in nums:
        primes_count = countPrimes(num)
        if primes_count % 2 == 1:
            Maria_wins += 1
        else:
            Ben_wins += 1
    
    if Maria_wins > Ben_wins:
        return "Maria"
    elif Ben_wins > Maria_wins:
        return "Ben"
    else:
        return None

