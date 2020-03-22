from math import *
from functools import reduce
import itertools
import time

# make a decorator that times how long my functions take to run
def timing(func):
    def inner(*args):
        start = time.time()
        print("timing function")
        result = func(*args)
        time_diff = time.time() - start
        if time_diff > 60:
            minutes = time_diff // 60
            seconds = round(time_diff % 60)
            print(f"This took {minutes} minutes and {seconds} seconds to run")
        else:
            print(f"This took {time_diff} seconds to run")

        return result
    return inner


def isPrime(n):
    """checks if N is prime in log(n) time"""
    if n < 2:
        return False
    for num in range(2, int(sqrt(n))+1):
        if n % num == 0:
            return False
    return 

def primeGen(k):
    """generator that yields successive prime numbers up to K"""
    """Only checks division with primes < N, should be pretty efficient"""
    # Takes about 5 seconds to generate primes up to 1M.
    # asymptotically not good, feels kinda exponential ooop
    primes_so_far = [2]
    not_prime = False
    yield 2

    for n in range(3, k, 2):
        for p in primes_so_far:
            if p > sqrt(n):
                break
            if n % p == 0:
                not_prime = True
                break
        if not_prime:
            not_prime = False
            continue
        else:
            primes_so_far.append(n)
            yield n


    # while n < K:
    #     if isPrime(n):
    #         yield n
    #     n+=1

def findFactors(n):
    """ find factors of N in hella zoomy (log(n)) time. Returns a list."""
    factors = list(filter(lambda div: n%div == 0, range(1,1+int(sqrt(n)))))
    factors.extend([int(n/num) for num in factors[::-1]])
    if len(factors) > 1: factors.pop()
    return factors

    # below line also works, but is roughly 55 times slower
    # return list(filter(lambda div: n%div == 0, range(1,n)))

def memoize(f):
    """memoize recursive function so it goes zoom zoom and save space"""
    cache = {}
    def helper(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]

    return helper

def recursiveFactorial(n):
    """compute the factorial of N recursively."""
    if n <= 1:
        return 1
    return n * factorial(n-1)

def factorial(n):
    """compute the factorial of N iteratively."""
    product = 1
    for num in range(2,n+1):
        product *= num
    return product

def permuteGen(n):
    """ Generates permutations of N. """
    for p in itertools.permutations(str(n), len(str(n))):
        yield "".join(p)

def fibGen():
    """generator that yields the next fibonacci number"""
    pre, curr = 0, 1
    while True:
        yield curr
        pre, curr = curr, pre + curr

def gcd(numer, denom):
    """returns the greatest common denominator between numer and denom"""
    n_facts, d_facts = find_factors(numer), find_factors(denom)
    nset, dset = set(n_facts), set(d_facts)
    return max(nset.intersection(dset))

def isPalindrome(num):
    strnum = str(num)
    if strnum == strnum[::-1]:
            return True
    return False

def isPandigital(strnum):
    if len(strnum) > 9:
        return False

    lst = []
    for num in strnum:
        if num in lst or num == "0":
            return False
        lst.append(num)
    return True

def wordValue(word):
    total = 0
    for letter in word:
        total += alpha_values[letter]
    return total

# this is actually useless, just use int(bin(n)[2:])
def toBinary(n):
    """converts N from base 10 to binary"""
    if n <= 0:
        return 0
    if n == 1:
        return 1

    highest_pow = int(log(n, 2))

    return 10**highest_pow + to_binary(n-2**highest_pow)

alpha_values = {
        "A":1, 
        "B":2, 
        "C":3, 
        "D":4, 
        "E":5,  
        "F":6, 
        "G":7, 
        "H":8, 
        "I":9, 
        "J":10,         
        "K":11, 
        "L":12, 
        "M":13, 
        "N":14, 
        "O":15,         
        "P":16, 
        "Q":17, 
        "R":18, 
        "S":19, 
        "T":20,         
        "U":21, 
        "V":22, 
        "W":23, 
        "X":24, 
        "Y":25, 
        "Z":26
}
