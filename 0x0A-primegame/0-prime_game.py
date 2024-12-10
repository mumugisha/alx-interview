#!/usr/bin/python3
"""Prime Game Challenge"""


def is_winner(x, nums):
    """Find the winner of the prime game."""
    counting_winner = {'Maria': 0, 'Ben': 0}

    for round_number in range(x):
        round_winner = is_round_winner(nums[round_number])
        if round_winner is not None:
            counting_winner[round_winner] += 1

    if counting_winner['Maria'] > counting_winner['Ben']:
        return 'Maria'
    elif counting_winner['Ben'] > counting_winner['Maria']:
        return 'Ben'
    return None


def is_round_winner(n):
    """Find the round winner."""
    number_list = list(range(1, n + 1))
    players = ['Maria', 'Ben']

    for turn in range(n):
        current_player = players[turn % 2]
        prime = -1
        selected_indices = []

        for index, number in enumerate(number_list):
            if prime != -1 and number % prime == 0:
                selected_indices.append(index)
            elif prime == -1 and is_prime(number):
                selected_indices.append(index)
                prime = number

        if prime == -1:  # If no valid move, current player loses
            return players[1] if current_player == players[0] else players[0]

        # Remove selected numbers from the list
        for index in sorted(selected_indices, reverse=True):
            del number_list[index]

    return None


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for divisor in range(3, int(n**0.5) + 1, 2):
        if n % divisor == 0:
            return False
    return True
