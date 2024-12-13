#!/usr/bin/python3

def isWinner(x, nums):
    if not nums or x < 1:
        return None
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    counting_winner = {"Maria": 0, "Ben": 0}
    for round_num in nums[:x]:
        round_winner = isRoundWinner(round_num, primes)
        if round_winner:
            counting_winner[round_winner] += 1
    if counting_winner["Maria"] > counting_winner["Ben"]:
        return "Maria"
    elif counting_winner["Ben"] > counting_winner["Maria"]:
        return "Ben"
    return None

def isRoundWinner(n, primes):
    if n < 1:
        return None
    numbers = list(range(1, n + 1))
    players = ["Maria", "Ben"]
    turn = 0
    while numbers:
        prime = next((num for num in numbers if primes[num]), None)
        if prime is None:
            return players[(turn + 1) % 2]
        numbers = [num for num in numbers if num % prime != 0]
        turn = (turn + 1) % 2
    return None

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime

if __name__ == "__main__":
    print(isWinner(3, [4, 5, 1]))
