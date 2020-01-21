"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2   =   0.5
1/3   =   0.(3)
1/4   =   0.25
1/5   =   0.2
1/6   =   0.1(6)
1/7   =   0.(142857)
1/8   =   0.125
1/9   =   0.(1)
1/10  =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
# THIS IS HELLA BRUTE FORCE.

import time
from decimal import *
depth = 6000
getcontext().prec = depth   # gets depth digits behind the decimal


def main():
    start = time.time()
    longest = 0
    best_d = 0
    for d in range(2, 1001):
        numlst = get_decimal_list(d)
        for n in range(len(numlst)):
            length = cycle_length(numlst[n:])
            if length > longest:
                longest = length
                best_d = d
            if length:
                break
            
    print(f"{best_d} has the longest cycle of {longest}.")
    print(f"This took {time.time() -start} seconds to run")

def get_decimal_list(denom):
    """Given a denominator DENOM return a list of integers starting at the first non-zero decimal place"""
    numlist = list(str(Decimal(1)/Decimal(denom)))
    numlist.remove('.')

    while numlist[0] == '0':
        numlist.remove('0')

    numlist = [int(num) for num in numlist]

    return numlist

def cycle_length(lst):
    """returns the length of the cycle"""
    
    def cycles(n,comparing):
        m = 0
        # while n+m*len(comparing) < len(lst):

        # the value of m is arbitrary. Switch it up and see if make a diff
        while m < 5:
            if comparing != lst[n + m*len(comparing): n + (m+1)*len(comparing)]:
                return False
            m += 1
        return True

    largest = 0
    for n in range(1, depth):
        comparing = lst[0:n]
        if n + len(comparing) > len(lst):
            return largest
        else:
            if cycles(n,comparing):
                return len(comparing)

main()
# answer is 983, it has a cycle length of 982.
# runs in about 6-9 seconds.
# Completed in the beginning of summer 2018, in Colorado. We were staying at this hella nice hotel.