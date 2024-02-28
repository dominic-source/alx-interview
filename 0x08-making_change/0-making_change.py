#!/usr/bin/python3

"""This module manages Changing coins"""


def makeChange(coins, total):
    """get the count of minimum count of coins change"""
    if total <= 0:
        return 0
    sorted_coins = sorted(coins)
    length = len(sorted_coins) - 1
    r_amount = total
    ans = []
    i = 0
    while i <= length and r_amount > 0:
        if r_amount >= sorted_coins[~i]:
            ans.append(sorted_coins[~i])
            r_amount -= sorted_coins[~i]
        else:
            i += 1

    if r_amount > 0:
        return -1
    else:
        return len(ans)
