"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from math import sqrt
import time as t

def rotations(n):
    """returns list of all rotations of N"""
    lst = [n]

    def helper(num):
        numstr = str(num)
        numstr += numstr[0]
        num = numstr[1:]
        if num == str(n):
            return
        lst.append(int(num))
        helper(num)

    helper(n)

    return lst

def is_prime(n):
    """checks if N is prime in log(n) time"""
    if n < 2:
        return False
    for num in range(2, int(sqrt(n))+1):
        if n % num == 0:
            return False
    return True

def is_circular(n):
    if is_prime(n) and len(list(filter(lambda x: not is_prime(x), rotations(n)))) == 0:
        return True
    return False

def main():
    start = t.time()
    counter = 0
    for n in range(1,1000000):
        if is_circular(n):
            counter += 1
    
    print(f"Final answer: {counter}")
    print(f"This took {t.time() - start} seconds to run")

main()
# 55
# 19 seconds