#!/usr/bin/python3
"""
Determine the fewest number of coins needed
to meet a given amount total.
"""

import sys


def makeChange(coins, total):
    """
    Return the fewest number of coins needed to meet the total.
    If total is 0 or less, return 0.
    If total cannot be met by any number of coins, return -1.
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins needed for each amount
    sample = [sys.maxsize for a in range(total + 1)]
    sample[0] = 0
    max_coins = len(coins)

    # Fill the list with the fewest coins needed for each amount
    for a in range(1, total + 1):
        for b in range(max_coins):
            if coins[b] <= a:
                subres = sample[a - coins[b]]
                if subres != sys.maxsize and subres + 1 < sample[a]:
                    sample[a] = subres + 1

    # Check if the total can be achieved
    if sample[total] == sys.maxsize:
        return -1

    return sample[total]
