#!/usr/bin/python3

"""Learn about the n queens problem and how to solve it"""
from typing import List
import sys
import time

args = sys.argv
if len(args) > 2:
    print("Usage: nqueens N")
    exit(1)

n = args[1]
try:
    N = int(n)
except ValueError:
    print("N must be a number")
    exit(1)

if N < 4:
    print("N must be at least 4")
    exit(1)

matrix = [[0] * N for _ in range(N)]


def valid_row(row: List[int]) -> bool:
    """Validate a row that a queen can be placed"""
    return sum(row) == 0


def valid_column(index: int, matrix: List[List[int]]) -> bool:
    """Validate a column that a queen can be placed"""
    for row in matrix:
        if row[index] == 1:
            return False
    return True


def valid_diagonal(matrix: List[List[int]], row: int, column: int) -> bool:
    """Validate a diagonal that a queen can be placed"""

    if row >= N or column >= N or row < 0 or column < 0:
        return False

    r = row + 1
    c = column + 1
    while c >= 0 and r >= 0 and r < N and c < N:
        if matrix[r][c]:
            return False
        c += 1
        r += 1

    r = row - 1
    c = column - 1
    while c >= 0 and r >= 0 and r < N and c < N:
        if matrix[r][c]:
            return False
        c -= 1
        r -= 1
    
    r = row - 1
    c = column + 1
    while c >= 0 and r >= 0 and r < N and c < N:
        if matrix[r][c]:
            return False
        c += 1
        r -= 1

    r = row + 1
    c = column - 1
    while c >= 0 and r >= 0 and r < N and c < N:
        if matrix[r][c]:
            return False
        c -= 1
        r += 1

    return True


def reset_row(row_ind: int, matrix: List[List[int]]) -> None:
    """This will reset a row to be zero"""
    if row_ind > -1 and matrix:
        i = 0
        while i < N:
            matrix[row_ind][i] = 0
            i += 1

def get_index(row: int, matrix: List[List[int]]) -> int:
    """Get index of position 1"""
    i = 0
    while i < N:
        if matrix[row][i] == 1:
            return i
        i += 1
    return -1


def print_matrix():
    for row in matrix:
        print(row)
    print("")
    time.sleep(1)


def generate_solutions():
    """Generate solutions for the N queens problem"""
    col, row  = 0, 0
    solution = False
    while not solution:
        if valid_column(col, matrix) and valid_row(matrix[row]) and valid_diagonal(matrix, row, col):
            matrix[row][col] = 1
            row += 1
            print_matrix()
        else:
            print_matrix()
            col += 1
            if col == N:
                reset_row(row, matrix)
                row -= 1
                nex = get_index(row, matrix)
                if nex != -1:
                    col = nex + 1
                else:
                    col = 0
        if row == N:
            solution = True
    print(matrix)


if __name__ == '__main__':
    generate_solutions()
