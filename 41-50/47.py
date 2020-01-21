"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.s

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

import functions as f
import time as t

def main():
    start = t.time()
    i = 2
    gpf = getPrimeFactors
    while True:
        primeFactors = getPrimeFactors(i)
        if (len(primeFactors) == 4 and len(gpf(i + 1)) == 4 
                and len(gpf(i + 2)) == 4 and len(gpf(i + 3)) == 4):
            print(f"Got em, the answer is {i}")
            print(f"This took {t.time() - start} seconds to run.")
            return
        i += 1
 
def getPrimeFactors(n):
    return list(filter(f.isPrime, f.findFactors(n)))

# The answer is 134043
# Takes 8.6 seconds to run
# Completed on 12/18/2018 in Taiwan, took me about 20 mins.

