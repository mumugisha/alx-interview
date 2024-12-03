#!/usr/bin/python3
"""
Defines a function to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented by 1s in a grid.

    Args:
        grid (list of list of int): A 2D grid where 0 represents water
                                    and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == 1:
                # Check top
                if row_idx == 0 or grid[row_idx - 1][col_idx] == 0:
                    perimeter += 1
                # Check bottom
                if row_idx == rows - 1 or grid[row_idx + 1][col_idx] == 0:
                    perimeter += 1
                # Check left
                if col_idx == 0 or row[col_idx - 1] == 0:
                    perimeter += 1
                # Check right
                if col_idx == cols - 1 or row[col_idx + 1] == 0:
                    perimeter += 1

    return perimeter
