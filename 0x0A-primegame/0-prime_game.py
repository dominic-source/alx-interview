#!/usr/bin/python3
"""
This modules creates a prime game.
It contains several functions to handle the game
"""


def buildPrime(num) -> dict:
    """ buildPrime: builds an array of prime numbers
        from 0 to the max number in the given nums for rounds
        and returns an array of "prime number" of to the maximum num

        Application of SIEVE OF ERATOSTHENES
    """
    array = [True for i in range(num + 1)]
    array[0] = False
    array[1] = False
    for i in range(0, num + 1):
        if i * i > num:
            break
        if array[i] is True:
            mult = 2 * i
            while mult <= num:
                array[mult] = False
                mult = i+mult
    newArray = [i for i in range(num + 1) if array[i] is True]

    return (newArray)


def isWinner(x, nums):
    """find the winner in the game played by Ben and Maria
    """
    if x == 0 or not nums or x is None:
        return None
    if x > len(nums):
        return None
    # Build an object of prime numbers based on the max num in nums
    obj_prime = buildPrime(max(nums))

    # set bensWinCount, set mariaWinCount.
    bens_win = 0
    marias_win = 0

    for val in range(x):
        # Build a new prime from the given prime obj_prime
        newPrime = [prime for prime in obj_prime if prime <= nums[val]]
        if len(newPrime) == 0:
            bens_win += 1
        if len(newPrime) % 2 == 0:
            bens_win += 1
        else:
            marias_win += 1
    if bens_win == marias_win:
        return None
    if bens_win > marias_win:
        return "Ben"
    if bens_win < marias_win:
        return "Maria"
    return None
