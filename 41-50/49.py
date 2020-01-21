"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4 digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

import functions as f
import time as t

def main():
    start = t.time()
    for n in range(1000, 10000):
        if badNum(n):
            continue
        pg = f.permuteGen(n)
        primes = []
        for i in range(24):
            perm = next(pg)
            if f.isPrime(int(perm)):
                primes.append(int(perm))
        primes = set(primes)
        if len(primes) >= 3 and 1487 not in primes and equiSpaced(primes):
            print(f"This took {t.time() - start} seconds to run.")
            return
        primes.clear()

def equiSpaced(lst):
    lst = list(lst)
    lst.sort()
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[j] + lst[j] - lst[i] in lst:
                print(f"The three numbers are {lst[i]}, {lst[j]}, {lst[j] + lst[j] - lst[i]}")
                return True
    return False

def badNum(n):
    """ Return true if N has a 0. """ 
    digitList = [int(d) for d in str(n)]
    if 0 in digitList:
        return True
    return False

# Answer is 296962999629
# Runs in 0.1 seconds
# Completed on 12/20/2018 in Taiwan

