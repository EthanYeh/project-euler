"""
Digit cancelling fractions. Problem is hard to copy over so just https://projecteuler.net/problem=33
"""
from math import sqrt
import time as t

def find_factors(n):
	factors = list(filter(lambda div: n%div == 0, range(1,1+int(sqrt(n)))))
	factors.extend([int(n/num) for num in factors[::-1]])
	return factors

def cancel(numer, denom, repeat):
	"""eliminate repeat from numer and denom. All arguments are ints"""
	
	def helper(number, repeat):
		if number % 10 == repeat:
			return number//10
		return number % 10
	numer = helper(numer, repeat)
	denom = helper(denom, repeat)
	
	return numer,denom

def can_cancel(numer, denom):
	"""checks if a number can be cancelled and if so return it. else return (False, 0)"""
	# BOTH NUMER AND DENOM ARE INTS

	cancels = False
	repeat = 0
	for dig in str(numer):
		if dig in str(denom):
			cancels = True
			repeat = dig

	return cancels, int(repeat)

def gcd(numer, denom):
	"""returns the greatest common denominator between numer and denom"""
	n_facts, d_facts = find_factors(numer), find_factors(denom)
	nset, dset = set(n_facts), set(d_facts)
	return max(nset.intersection(dset))

def simplify(numer, denom):
	"""simply the fraction"""
	largestcd = gcd(numer, denom)
	return int(numer/largestcd), int(denom/largestcd)

def main():
	start = t.time()
	totenumer = 1
	totedenom = 1
	for numer in range(1, 100):
		for denom in range(numer+1, 100):
			if denom % 10 == 0:
				continue
			tup = can_cancel(numer, denom)
			if tup[0]:
				num, den = cancel(numer, denom, tup[1])
				if num/den == numer/denom:
					print(f"{num}/{den}={numer}/{denom}")
					totenumer *= numer
					totedenom *= denom

	simnum, simden = simplify(totenumer,totedenom)

	print(f"Final answer: {simden}")
	print(f"This took {t.time() - start} seconds to run")

main()
# 100
# 0.01 seconds with print, 0.007 wiithout