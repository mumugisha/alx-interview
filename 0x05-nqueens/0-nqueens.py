#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing N non-attacking
queens on an N×N chessboard. Write a program that solves
the N queens problem.
"""

import sys

def is_safe(n_queens, row, column):
    """Check if a queen can be placed at the current row, column."""
    for r, c in n_queens:
        if c == column or abs(c - column) == abs(r - row):
            return False
    return True

def solve_nqueens(n, row=0, n_queens=[], solutions=[]):
    """Recursive function to solve the N-Queens problem."""
    if row == n:
        solutions.append(n_queens[:])
        return

    for column in range(n):
        if is_safe(n_queens, row, column):
            n_queens.append((row, column))
            solve_nqueens(n, row + 1, n_queens, solutions)
            n_queens.pop()  # backtrack

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens(n, solutions=solutions)

    # Print solutions
    for solution in solutions:
        print([[r, c] for r, c in solution])
