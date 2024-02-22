#!/usr/bin/python3

"""Tech interview matrix problem
[00, 10, 20, 30]
[01, 11, 21, 31]
[02, 12, 22, 32]
[03, 13, 23, 33]


00 -> 03
03 -> 33
33 -> 30
30 -> 00

10 -> 01
01 -> 13
13 -> 31
31 -> 10

20 -> 02
02 -> 23
23 -> 32
32 -> 20

second circle
11 -> 12
12 -> 22
22 -> 21
21 -> 11
"""


def rotate_2d_matrix(matrix):
    """rotate a two D matrix"""

    # length of matrix
    N = len(matrix)

    # loop through each circle
    for x in range(0, int(N/2)):
        # considering the elements in group of 4 in the current circle
        for y in range(x, N-1-x):
            # store the top value in a temp memory
            temp = matrix[x][y]

            # move the left to the top
            matrix[x][y] = matrix[N-1-y][x]

            # move the bottom to the left
            matrix[N-1-y][x] = matrix[N-1-x][N-1-y]

            # move the right to the bottom
            matrix[N-1-x][N-1-y] = matrix[y][N-1-x]

            # move the temp to the right
            matrix[y][N-1-x] = temp
