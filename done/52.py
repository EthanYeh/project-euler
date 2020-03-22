"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

# Looks like a brute force problem but ok.

import time as t

def main():
    start = t.time()
    i = 1
    while not sameDigits(i):
        i += 1
    print(f"Hey the answer is {i} wow.")
    print(f"This brute force took {t.time() - start} seconds to run.")

def sameDigits(n):
    """ Returns true if N, 2N, 3N, ..., 6N all contain the same digits.
    Pretty much constant time. """

    multiples = [n*i for i in range(2, 7)]
    # The below for loop isn't very readable but basically it sorts all the numbers in the list and put them into a set. 
    numSet = set([])
    for num in multiples:
        numList = sorted([int(d) for d in str(num)])
        sortedNum = int(''.join(map(str, numList)))
        numSet.add(sortedNum)
        if len(numSet) > 1:
            return False
    
    return True

main()

# Answer is 142857
# Takes around 1 seconds
# Completed on 1/9/2019 on the train from SJ to SB, took like 30 minutes