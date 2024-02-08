#!/usr/bin/python3

"""Learn about the n queens problem and how to solve it"""

import sys

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
