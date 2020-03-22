"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one million, can be written as the sum of the most consecutive primes?
"""

import functions as f
import time as t

@f.timing
def brute_force(max_n):
    all_primes = [p for p in f.primeGen(max_n)]   # takes about 5 seconds

    longest = 0
    best_prime = 0
    window = ()
#    for start in range(len(all_primes)):
    for start in range(5):
        total = sum(all_primes[start: start + longest])
        for end in range(start + longest, len(all_primes)):
            total += all_primes[end]
            if total > max_n:
                break
            if total in all_primes:
                if end-start+1 > longest:
                    longest = end-start+1
                    best_prime = total
                    window = (start, end+1)

        total = sum(all_primes[start: start + longest])

    print(f"{best_prime} is the answer, it is the sum of {longest} terms")
    print(f"best window is {window}")

    return longest

brute_force(1000000) 
# 997651 is the answer, it is the sum of 543 terms
# best window is (3, 546)
# This took 3.289536476135254 seconds to run



# ----------------- BELOW IS MY FIRST ATTEMPT, IT'S HELLA SLOW AND DUMB ----------------
@f.timing
def brute_force_dumb(max_n):
    all_primes = [p for p in f.primeGen(max_n)]   # takes about 5 seconds
    print("found primes")
    longest = 0
    best_prime = 0
    window = ()
#    for start in range(len(all_primes)):
    for start in range(5):
        for end in range(start + longest + 1, len(all_primes)):
            primes = all_primes[start:end]
            if primes[-1] > max_n:
                break
            if sum(primes) in all_primes:
                if len(primes) > longest:
                    longest = len(primes)
                    best_prime = sum(primes)
                    window = (start, end)

    print(f"{best_prime} is the answer, it is the sum of {longest} terms")
    print(f"best window is {window}")

    return longest
# 997651 is the answer, it is the sum of 543 terms
# best window is (3, 546)
# This took 13.0 minutes and 38 seconds to run
