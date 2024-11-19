#!/usr/bin/python3
"""
Rotate a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The 2D matrix to be rotated.
    """
    # Initialize pointers to the leftmost and rightmost columns
    left, right = 0, len(matrix) - 1

    # Loop until the pointers meet in the middle
    while left < right:
        # Iterate over each layer in the current boundary
        for a in range(right - left):
            # Define top and bottom row indices
            top, bottom = left, right

            # Save the top-left element temporarily
            top_left = matrix[top][left + a]

            # Move bottom-left into top-left
            matrix[top][left + a] = matrix[bottom - a][left]

            # Move bottom-right into bottom-left
            matrix[bottom - a][left] = matrix[bottom][right - a]

            # Move top-right into bottom-right
            matrix[bottom][right - a] = matrix[top + a][right]

            # Move the temporarily saved top-left into top-right
            matrix[top + a][right] = top_left

        # Move the pointers inward for the next layer
        right -= 1
        left += 1
