"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
from math import *
import time as t

def to_binary(n):
	"""converts N from base 10 to binary"""
	if n <= 0:
		return 0
	if n == 1:
		return 1

	highest_pow = int(log(n, 2))
	
	return 10**highest_pow + to_binary(n-2**highest_pow)

def is_palindrome(num):
	strnum = str(num)
	if strnum == strnum[::-1]:
			return True
	return False

def main():
    start = t.time()
    total = 0
    for n in range(1,1000000):
        if is_palindrome(n) and is_palindrome(to_binary(n)):
            total += n
            print(n, to_binary(n))

    print(f"Final answer: {total}")
    print(f"This took {t.time() - start} seconds to run")

main()
# 872187
# 0.5 seconds
# completed 5/27/2018