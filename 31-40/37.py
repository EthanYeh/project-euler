"""
The number 3797 has an interesting property. Being prime itself, 
it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both
truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import time as t
from math import sqrt

def is_prime(n):
    """checks if N is prime in log(n) time"""
    if n < 2:
        return False
    for num in range(2, int(sqrt(n))+1):
        if n % num == 0:
            return False
    return True

def prime_gen():
    """yields successive prime numbers (above 10) forever"""
    n = 10
    while True:
        if is_prime(n):
            yield n
        n+=1

def truncleft(n):
    """check if n truncated from right to left works"""
    def helper(n):
        # print(n)
        if n == 0:
            return True
        if is_prime(n):
            return helper(n//10)
        return False

    return helper(n//10)

def truncright(n):
    """check if n truncated from left to right works"""
    exp = len(str(n)) - 1
    def helper(num, exp):
        # print(num)
        if exp == 0:
            return True
        if is_prime(num):
            return helper(num%(10**(exp-1)), exp-1)
        return False

    return helper(n%(10**exp), exp)

def main():
    start = t.time()
    to_go = 11
    total = 0
    g = prime_gen()
    print("Below are all the truncatable primes:")
    while to_go > 0:
        prime = next(g)
        if truncleft(prime) and truncright(prime):
            to_go -= 1
            total += prime
            print(prime)
    print()
    print(f"Final answer: {total}")
    print(f"This took {t.time() - start} seconds to run.")

main()
# 748317
# 5.3 seconds
# completed 5/27/2018