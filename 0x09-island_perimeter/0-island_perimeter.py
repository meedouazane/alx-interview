#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Find the perimeter of the island
    :param grid: list of list of integers representing the island
    :return: the perimeter of the island
    """
    perimeter = 0
    if not grid:
        return 0
    row = len(grid)
    col = len(grid[0])

    for i in range(row):
        for g in range(col):
            if grid[i][g] == 1:
                if i == 0 or grid[i - 1][g] == 0:
                    perimeter += 1
                if i == row - 1 or grid[i + 1][g] == 0:
                    perimeter += 1
                if g == 0 or grid[i][g - 1] == 0:
                    perimeter += 1
                if g == col - 1 or grid[i][g + 1] == 0:
                    perimeter += 1
    return perimeter
