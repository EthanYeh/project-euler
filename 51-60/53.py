"""
How many, not necessarily distinct, values of n choose r, for 1 \leq n \leq 100, are greater than one-million?
"""

# n choose r = n! / ((n - r)! * r!)
# Brute force?

import time as t
import functions as f
from math import ceil

def main():
    start = t.time()
    total = 0
    for n in range(23, 101):
        total += getNumR(n)
    
    print(f"Answer is {total}.")
    print(f"This took {t.time() - start} seconds to run.")

def getNumR(n):
    """
    Returns the number of values of R that satisfies N choose R > 1 million.
    I just need to find the first value of r that works and return n - r - r + 1, because math.
    """
    for r in range(1, ceil(n/2)):
        if f.factorial(n) / f.factorial(r) / f.factorial(n-r) > 1000000:
            return n - 2*r + 1


# Answer is 4075
# Brute force takes 0.007 seconds to run. Too EZ.
# Completed on 1/9/2019 on the train from SJ to SB. Took roughly 15 minutes
