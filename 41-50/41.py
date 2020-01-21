"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
"""
After solving the lexicographic permutations problem, 
use that to write a generator that generates all the pandigital
numbers, starting from 987654321 and going down.
For each pandigital number, check is_prime and return the first result
"""
import itertools
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

def permute(start, digits):
    """
    Go thorugh the pandigital numbers and check if prime.
    Returns None or the first prime pandigital number
    """
    for p in itertools.permutations(start, digits):
        n = int("".join(p))
        if is_prime(n):
            return n
    return

def main():
    starttime = t.time()
    start = '987654321'
    digits = 9
    result = permute(start, digits)
    while True:
        if not result:
            start = start[1:]
            digits = digits-1
            result = permute(start, digits)
        else:
            print(f"Answer be {result}.")
            print(f"Time: {t.time() - starttime} seconds.")
            break

main()
# 7652413
# 0.6 seconds
# 5/31/2018