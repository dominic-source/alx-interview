#!/usr/bin/python3
"""
This modules creates a prime game. It contains several functions to handle the game

validPrimeArray: validates array contains at least
a prime number

delMultiples: remove multiples of a picked number which
is less than or equal to the max number in the array

Logic:
    build the prime number based on the max number in the array
    set bensWinCount, set mariaWinCount.
    set rounds = x and reduce it for each time a winner is found.

    loop the given array
    for each number n in the array, create a list ranging from 0 to n
    benMaria = true
    loop benMaria
        set Maria to pick a single number from a max of n, if there are no prime
            numbers in the array of n, ben wins that round
            record it for ben, set benMaria to false in order to stop the current iteration
         set ben to pick a single number from a max of n, if there are no prime
            numbers in the array of n, Maria wins that round
            record it for ben, set benMaria to false in order to stop the current iteration
    
"""

def buildPrime(num) -> dict:
    """ buildPrime: builds an array of prime numbers
        from 0 to the max number in the given nums for rounds
        and return an object where key is the "prime number" in string 
        the value is "true" 
    """
    array = [True for i in range(num + 1)];
    arrar[0] = False
    array[1] = False
    for i in range(0, num + 1):
        if i * i > num:
            break
        if array[i] is True:
            mult = 2 * i
            while mult <= num:
                array[mult] = False
                mult = i + mult
    newArray = [i for i in range(num + 1) if array[i] == True];
    print(newArray)

buildPrime(10);



