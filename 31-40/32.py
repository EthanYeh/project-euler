"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

# the product must have 4 digits

from math import sqrt
import time as t

def find_factors(n):
	factors = list(filter(lambda div: n%div == 0, range(1,1+int(sqrt(n)))))
	factors.extend([int(n/num) for num in factors[::-1]])
	if len(factors) > 1: factors.pop()
	return factors

def is_pandigital(strnum):
	if len(strnum) != 9:
		return False

	lst = []
	for num in strnum:
		if num in lst or num == "0":
			return False
		lst.append(num)
	return True


def main():
	start = t.time()
	total = 0

	for n in range(10000):
		facts = find_factors(n)
		facts = facts[:len(facts)//2 + 1]
		for factor in facts:
			otherfact = str(int(n/factor)) 
			if is_pandigital(str(n) + str(factor) + otherfact):
				print(f"{factor} x {otherfact} = {n}")
				total += n
				break

	print(f"Total: {total}")
	print(f"Took {t.time() - start} seconds to run.")

main()
# 45228
# runs in 0.2 seconds