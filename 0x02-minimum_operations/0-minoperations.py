#!/usr/bin/env python3
"""
Ccalculate the minimum number of operations
required to  reach exactly n 'H' characters in a file, 
using only two operations: copy-all and paste.
"""


def minOperations(n):
    """
    Compute the minimum number of operations needed to reach exactly `n` 'H'
    characters using only copy-all and paste operations.

    Returns:
        Integer: If n is not possible to reach, return 0
    """
    pasted_chars = 1  # Number of 'H' characters currently in the file.
    clipboard = 0  # Clipboard stores the copied number of 'H' characters.
    counter = 0  # Counter to track the total number of operations.

    while pasted_chars < n:
        # If the clipboard is empty, did not copy any operation.
        if clipboard == 0:
            # Copy-all 'H' to clipboard
            clipboard = pasted_chars
            # Increment the counter for the copy operation
            counter += 1

        # If only one 'H' character is in the file.
        if pasted_chars == 1:
            # Paste from the clipboard
            pasted_chars += clipboard
            # Increment the counter for the paste operation
            counter += 1
            # Continue to the next iteration of the loop
            continue

        
        remaining = n - pasted_chars # Calculate remaining chars to be pasted.
        # If the remaining characters are less than the clipboard content,
        # return 0 as it's not possible to reach n.
        if remaining < clipboard:
            return 0

        # If remaining characters are not divisible by pasted_chars
        if remaining % pasted_chars != 0:
            # Paste current clipboard content
            pasted_chars += clipboard
            # Increment the counter for the paste operation
            counter += 1
        else:
            # Copy all the current number of 'H' characters
            clipboard = pasted_chars
            # Paste the clipboard content
            pasted_chars += clipboard
            # Increment for both copy and paste operations
            counter += 2

    # If the target number of characters is reached
    if pasted_chars == n:

        return counter
    else:

        return 0
