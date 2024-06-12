#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Find the perimeter of the island
    :param grid: list of list of integers represent island
    :return: the perimeter of the island
    """
    perimeter = 0
    for i in range(len(grid)):
        for g in range(len(grid[i])):
            if grid[i][g] == 1:
                if grid[i - 1][g] == 0:
                    perimeter += 1
                if grid[i + 1][g] == 0:
                    perimeter += 1
                if grid[i][g - 1] == 0:
                    perimeter += 1
                if grid[i][g + 1] == 0:
                    perimeter += 1
    return perimeter
