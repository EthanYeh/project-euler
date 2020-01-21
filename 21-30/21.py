"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from math import sqrt
import time

def find_factors(n):
	factors = list(filter(lambda div: n%div == 0, range(1,1+int(sqrt(n)))))
	factors.extend([int(n/num) for num in factors[::-1]])
	if len(factors) > 1: factors.pop()
	return factors

	# below line also works, but is roughly 55 times slower
	# return list(filter(lambda div: n%div == 0, range(1,n)))

def main():
	start = time.time()
	total = 0
	for i in range(1, 10001):
		sum_factors = sum(find_factors(i))
		if sum(find_factors(sum_factors)) == i and i != sum_factors:
			total += sum_factors

	print(f"The sum of all amicable numbers under 10000 is {total}")
	print(f"This took {time.time() - start} seconds to run")

main()
# answer is 31626
# 0.2 seconds