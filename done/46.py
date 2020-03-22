"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2x1^2
15 = 7 + 2x2^2
21 = 3 + 2x3^2
25 = 7 + 2x3^2
27 = 19 + 2x2^2
33 = 31 + 2x1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
import functions as f
from math import sqrt
import time as t

def main():
    start = t.time()
    i = 9
    while True:
        if not f.isPrime(i) and not isComposite(i):
            print(f"Found the answer, it is {i}")
            print(f"This took {t.time() - start} seconds to run.")
            return
        i += 2

def isComposite(n):
    """ Checks if number N can be written as a composite. """
    pg = f.primeGen()
    nextPrime = next(pg)

    while nextPrime < n:
        square = (n - nextPrime) / 2
        if (sqrt(square) % 1 == 0):
            # print(f"{n} can be written as {nextPrime} + 2 * {square}")
            return True
        nextPrime = next(pg)

    return False

# The answer is 5777
# Runs in 0.75 seconds
# Completed on 12/18/2018 in Taiwan
