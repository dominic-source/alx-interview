#!/usr/bin/python3
"""
This modules creates a prime game.
It contains several functions to handle the game
"""


def buildPrime(num) -> dict:
    """ buildPrime: builds an array of prime numbers
        from 0 to the max number in the given nums for rounds
        and return an object where key is the "prime number"
        in string the value is "true"

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
    newArray = {str(i): i for i in range(num + 1) if array[i] is True}
    return (newArray)


def validPrimeArray(array, prime_obj) -> bool:
    """validPrimeArray: validates array contains at least
    a prime number
    """
    if len(array) == 0:
        return False
    for i in array:
        if prime_obj.get(str(i)):
            return True
    return False


def delMultiples(array, num):
    """delMultiples: remove multiples of a picked number which
    is less than or equal to the max number in the array
    """
    i = 0
    while i < len(array):
        if (array[i] % num) == 0:
            array.remove(array[i])
        i += 1
    return array


def optimalYieldPrime(obj_primes):
    """Yield a prime number optimally"""
    for key, value in obj_primes.items():
        yield value


def isWinner(x, nums):
    """find the winner in the game played by Ben and Maria

    Logic:
    build the prime number based on the max number in the array
    set bensWinCount, set mariaWinCount.
    set rounds = x and reduce it for each time a winner is found.

    loop the given array
    for each number n in the array, create a list ranging from 1 to n
    benMaria = true
    loop benMaria
        set Maria to pick a single number from a max of n,
        if there are no prime
            numbers in the array of n, ben wins that round
            record it for ben, set benMaria to false in order to
            stop the current iteration
         set ben to pick a single number from a max of n, if there are no prime
            numbers in the array of n, Maria wins that round
            record it for ben, set benMaria to false in order to
            stop the current iteration
    """
    if x == 0 or not nums:
        return None
    if x > len(nums):
        return None
    # Build an object of prime numbers based on the max num in nums
    obj_prime = buildPrime(max(nums))

    # set bensWinCount, set mariaWinCount.
    bens_win = 0
    marias_win = 0

    for val in range(x):
        strategy = [i for i in range(1, nums[val] + 1)]
        benMaria = True
        prime_yield = optimalYieldPrime(obj_prime)
        while benMaria:
            if not validPrimeArray(strategy, obj_prime):
                bens_win += 1
                benMaria = False
                break
            mariaPick = next(prime_yield)
            strategy = delMultiples(strategy, mariaPick)
            if not validPrimeArray(strategy, obj_prime):
                marias_win += 1
                benMaria = False
                break
            benPick = next(prime_yield)
            strategy = delMultiples(strategy, benPick)
    if bens_win == marias_win:
        return None
    if bens_win > marias_win:
        return "Ben"
    return "Maria"
