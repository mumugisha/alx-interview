#!/usr/bin/python3
'''Calculate the minimum number of operations
required to reach exactly n 'H' characters in a file,
using only two operations: copy-all and paste.
'''


def minOperations(n):
    '''Compute the minimum number of operations
    needed to reach exactly `n` 'H' characters using
    only copy-all and paste operations.
    Returns:
        Integer : if n is impossible to achieve, return 0
    '''
    past_chars = 1  # Number of 'H' characters currently in the file
    new_clipboard = 0  # Clipboard stores the copied number of 'H' characters
    first_counter = 0  # Counter to track the total number of operations.

    while past_chars < n:
        # If the clipboard is empty
        if new_clipboard == 0:
            # Copy-all 'H' to clipboard
            new_clipboard = past_chars
            # Increment the counter for the copy operation
            first_counter += 1

        # If only one 'H' character is in the file.
        if past_chars == 1:
            # Paste from the clipboard
            past_chars += new_clipboard
            # Increment the counter for the paste operation
            first_counter += 1
            # Continue to the next iteration of the loop
            continue

        remaining = n - past_chars  # Calculate remaining chars to be pasted.
        # If the remaining characters are less
        # than the clipboard content,
        # return 0 as it's not possible to reach n.
        if remaining < new_clipboard:
            return 0

        # If can't be divided
        if remaining % past_chars != 0:
            # Paste current clipboard
            past_chars += new_clipboard
            # Increment operations counter
            first_counter += 1
        else:
            # Copy all
            new_clipboard = past_chars
            # Paste
            past_chars += new_clipboard
            # Increment operations counter
            first_counter += 2

    # If got the desired result
    if past_chars == n:
        return first_counter
    else:
        return 0
