"""
f = n^2 + an + b. 
find values of a and b between -1000 and 1000 such that
f produces the most consecutive primes. Return abs(a*b)
"""
from math import sqrt
import time

def is_prime(num):
	"""cheks if NUM is prime"""
	if num < 2:
		return False
	for x in range(2,int(sqrt(num))+1):
		if num % x == 0:
			return False
	return True

def biggest_n(a, b):
	""" Return the largest consecutive value of N that works"""
	n = 0
	val = n**2 + a*n + b
	while is_prime(val):
		n += 1
		val = n**2 + a*n + b 
	return n-1

def main():
	start = time.time()
	best_a, best_b, best_n = 0, 0, 0
	# only needs to loop through odd numbers
	for a in range(-1001,1002,2):
		for b in range(-1001, 1002,2):
			n = biggest_n(a, b)
			if n > best_n:
				best_a, best_b, best_n = a, b, n
	print(f"Best function is n^2 + ({best_a})*n + {best_b}, which produces prime numbers from 0 <= n <= {best_n}")
	print(f"Final answer: {best_a*best_b}")
	print(f"This took {time.time() - start} seconds to run")

main()
# answer is -59231
# takes about 1.5 seconds to run