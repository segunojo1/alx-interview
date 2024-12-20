#!/usr/bin/python3
"""
This module contains a function that calculates the perimeter
of an island represented in a grid.
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A 2D list representing the map.
                                    0 represents water, 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides of the cell
                perimeter += 4

                # Check top cell
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1

                # Check bottom cell
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1

                # Check left cell
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1

                # Check right cell
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

    return perimeter