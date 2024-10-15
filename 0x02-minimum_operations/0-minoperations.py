#!/usr/bin/env python3

# Function to calculate the minimum number of operations required to
# obtain exactly `n` 'H' characters in a file, using only the operations
# of copy-all and paste. This problem is based on the idea of optimizing
# the copy-paste operations to get the target number of characters.

def minOperations(n):
    """
    Function to compute the minimum number of operations needed
    to reach exactly n 'H' characters using only copy-all and paste operations.

    Parameters:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations, or 0 if it's not possible.
    """

    # The number of 'H' characters currently in the file.
    pasted_chars = 1

    # Clipboard stores the copied number of 'H' characters (initially 0).
    clipboard = 0

    # A counter to track the total number of operations.
    counter = 0

    # Loop until the number of pasted characters reaches the target n.
    while pasted_chars < n:

        # If the clipboard is empty, perform a copy operation.
        if clipboard == 0:
            # Copy the current 'H' to clipboard
            clipboard = pasted_chars
            # Increment the counter for the copy operation.
            counter += 1

        # If only one 'H' character is in the file.
        if pasted_chars == 1:
            # Paste the current clipboard content to increase the characters.
            pasted_chars += clipboard
            # Increment the counter for the paste operation.
            counter += 1
            # Continue to the next iteration of the loop.
            continue

        # Calculate how many characters are needed to reach the target.
        remaining = n - pasted_chars

        # If the remaining characters are less than the clipboard content,
        # return 0 as it's not possible to reach n.
        if remaining < clipboard:
            return 0

        # If the remaining characters are not divisible by the current
        # number of parsed characters, paste the clipboard content.
        if remaining % pasted_chars != 0:
            pasted_chars += clipboard
            # Increment the counter for the paste operation.
            counter += 1
        else:
            # Otherwise, copy the current number of 'H' characters.
            clipboard = pasted_chars
            # Paste the clipboard content.
            pasted_chars += clipboard
            # Increment the counter for both copy and paste operations.
            counter += 2

    # If the target number of characters is reached, return the counter.
    if pasted_chars == n:
        return counter
    else:
        # Return 0 if it’s not possible to reach exactly n.
        return 0
