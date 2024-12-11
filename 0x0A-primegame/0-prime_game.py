#!/usr/bin/python3
"""
This module contains the implementation of the Prime Game.
"""

def isWinner(x, nums):
    """
    Determines the winner of the prime game after x rounds.

    Args:
        x (int): Number of rounds.
        nums (list of int): Array of integers representing the upper limit of each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben").
             Returns None if the winner cannot be determined.
    """
    if x < 1 or not nums:
        return None

    # Generate primes up to the maximum number in nums using the Sieve of Eratosthenes
    max_num = max(nums)
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    # Precompute prime counts
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
