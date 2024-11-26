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

    run_time = [sys.maxsize for a in range(total + 1)]
    run_time[0] = 0
    max_coins = len(coins)

    for a in range(1, total + 1):
        for b in range(max_coins):
            if coins[b] <= a:
                subres = run_time[a - coins[b]]
                if subres != sys.maxsize and subres + 1 < run_time[a]:
                    run_time[a] = subres + 1

    if run_time[total] == sys.maxsize:
        return -1

    return run_time[total]
