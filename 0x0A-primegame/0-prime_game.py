#!/usr/bin/python3
"""Prime Game Challenge"""


def isWinner(x, nums):
    """Determines the winner of the prime game.
    Args:
        x (int): Number of rounds.
        nums (list): List of integers for each round.
    Returns:
        str: Name of the winner ('Maria' or 'Ben'), or None if no winner.
    """
    if not nums or x < 1:
        return None

    counting_winner = {"Maria": 0, "Ben": 0}

    for round_num in nums[:x]:
        round_winner = isRoundWinner(round_num)
        if round_winner:
            counting_winner[round_winner] += 1

    if counting_winner["Maria"] > counting_winner["Ben"]:
        return "Maria"
    elif counting_winner["Ben"] > counting_winner["Maria"]:
        return "Ben"
    return None


def isRoundWinner(n):
    """Determines the winner for a single round.
    Args:
        n (int): The upper bound of the range for the round.
    Returns:
        str: Name of the round winner ('Maria' or 'Ben'), or None.
    """
    if n < 1:
        return None

    numbers = list(range(1, n + 1))
    players = ["Maria", "Ben"]
    turn = 0  # Maria starts

    while numbers:
        prime = None
        for n in numbers:
            if isPrime(n):
                prime = n
                break

        if prime is None:
            return players[(turn + 1) % 2]

        numbers = [n for n in numbers if n % prime != 0]
        turn = (turn + 1) % 2  # Switch player

    return None


def isPrime(n):
    """Checks if a number is prime.
    Args:
        num (int): The number to check.
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**(1/2)+1,2):
        if n % i == 0:
            return "Not prime"
    return True
