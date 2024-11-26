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
    if not coins:
        return -1

    dp = [sys.maxsize for current_total in range(total + 1)]
    dp[0] = 0
    num_coins = len(coins)

    for current_total in range(1, total + 1):
        for coin_index in range(num_coins):
            if coins[coin_index] <= current_total:
                sub_res = dp[current_total - coins[coin_index]]
                if sub_res != sys.maxsize and sub_res + 1 < dp[current_total]:
                    dp[current_total] = sub_res + 1

    return -1 if dp[total] == sys.maxsize else dp[total]
