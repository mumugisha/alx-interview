#!/usr/bin/python3
"""Prime Game Challenge"""


def isWinner(x, nums):
    """Determines the winner of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the upper bounds of each round.

    Returns:
        str: The name of the winner ('Maria' or 'Ben'), or None if there's no winner.
    """
    if not nums or x < 1:
        return None

    counting_winner = {'Maria': 0, 'Ben': 0}

    for round_num in nums[:x]:
        round_winner = isRoundWinner(round_num)
        if round_winner:
            counting_winner[round_winner] += 1

    if counting_winner['Maria'] > counting_winner['Ben']:
        return 'Maria'
    elif counting_winner['Ben'] > counting_winner['Maria']:
        return 'Ben'
    else:
        return None


def isRoundWinner(n):
    """Determines the winner for a single round.

    Args:
        n (int): The upper bound of the range for the round.

    Returns:
        str: The name of the round winner ('Maria' or 'Ben'), or None if undecided.
    """
    if n < 1:
        return None

    numbers = list(range(1, n + 1))
    players = ['Maria', 'Ben']
    turn = 0  # Maria starts

    while numbers:
        prime = None
        for num in numbers:
            if isPrime(num):
                prime = num
                break

        if prime is None:
            # Current player loses
            return players[(turn + 1) % 2]

        # Remove the prime and its multiples
        numbers = [num for num in numbers if num % prime != 0]
        turn = (turn + 1) % 2  # Switch player

    return None


def isPrime(num):
    """Checks if a number is a prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
