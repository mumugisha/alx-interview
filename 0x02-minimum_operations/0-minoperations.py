#!/usr/bin/env python3
"""
This module contains a function to calculate the minimum number of operations
required to reach exactly n 'H' characters in a file, using only two operations:
copy-all and paste.
"""


def minOperations(n):
    """
    Compute the minimum number of operations needed to reach exactly `n` 'H'
    characters using only copy-all and paste operations.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations, or 0 if it's not possible.
    """

    # Number of 'H' characters currently in the file.
    pasted_chars = 1

    # Clipboard stores the copied number of 'H' characters (initially 0).
    clipboard = 0

    # Counter to track the total number of operations.
    counter = 0

    # Loop until the number of pasted characters reaches the target `n`.
    while pasted_chars < n:

        # If the clipboard is empty, perform a copy operation.
        if clipboard == 0:
            clipboard = pasted_chars  # Copy current 'H' to clipboard
            counter += 1  # Increment the counter for the copy operation

        # If only one 'H' character is in the file.
        if pasted_chars == 1:
            pasted_chars += clipboard  # Paste from the clipboard
            counter += 1  # Increment the counter for the paste operation
            continue  # Continue to the next iteration of the loop

        # Calculate how many characters are needed to reach the target.
        remaining = n - pasted_chars

        # If the remaining characters are less than the clipboard content,
        # return 0 as it's not possible to reach n.
        if remaining < clipboard:
            return 0

        # If remaining characters are not divisible by current `pasted_chars`,
        # paste the clipboard content.
        if remaining % pasted_chars != 0:
            pasted_chars += clipboard
            counter += 1  # Increment the counter for the paste operation
        else:
            clipboard = pasted_chars  # Copy the current number of 'H' characters
            pasted_chars += clipboard  # Paste the clipboard content
            counter += 2  # Increment for both copy and paste operations

    # If the target number of characters is reached, return the counter.
    if pasted_chars == n:
        return counter
    else:
        return 0  # Return 0 if it's not possible to reach exactly `n`
