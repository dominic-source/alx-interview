#!/usr/bin/python3

""" This module documents the implementation of BFS is solving
highland perimeter problem
"""


def island_perimeter(grid):
    """Calculate the perimeter of an highland"""
    queue = []
    perimeter = 0
    n = len(grid)
    m = len(grid[0])
    for row in range(n):
        for col in range(m):
            if grid[row][col] == 1:
                queue.append((row, col))
                grid[row][col] = -2
                break
        if queue:
            break

    while queue:
        try:
            row, col = queue.pop(0)
        except IndexError:
            return perimeter
        indexes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i, j in indexes:
            r = row + i
            c = col + j
            if r >= n or c >= m or r < 0 or c < 0 or grid[r][c] == 0:
                perimeter += 1
            elif grid[r][c] == 1:
                queue.append((r, c))
                grid[r][c] = -2
    return perimeter
