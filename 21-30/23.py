"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
from math import sqrt
from functools import reduce
import time

def find_factors(n):
    """ returns a list of proper divisors of N """
    factors = list(filter(lambda div: n%div == 0, range(1,1+int(sqrt(n)))))
    factors.extend([int(n/num) for num in factors[::-1] if int(n/num) not in factors])
    if len(factors) > 1: factors.pop()
    return factors

def find_abundant():
    """ Returns a list of all relevant abundant numbers """
    abundants = list(filter(lambda x: sum(find_factors(x)) > x, range(1, 28123)))
    return abundants

def main():
    start = time.time()
    abundants = find_abundant()
    abundantsums = set()
    for ab in range(len(abundants)):
        for ab2 in range(ab, len(abundants)):
            goddamnsum = abundants[ab]+abundants[ab2]
            if goddamnsum <=28123:
                abundantsums.add(goddamnsum)

    total = int(28123*28124/2)
    print(f"Final answer: {total - sum(abundantsums)}")
    print(f"This took {time.time() - start} seconds to run")


main()
#answer is 4179871