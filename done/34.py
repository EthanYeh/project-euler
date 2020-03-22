"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
import time as t

def factorial(n):
	"""calculate the factorial of N"""
	prod = 1
	for num in range(2,n+1):
		prod *= num
	return prod

def sum_of_fact(n):
	"""calculate the sum of the factorials of digits of N"""
	total = 0
	for dig in str(n):
		total += factorial(int(dig))
	return total

def main():
	start = t.time()
	total = 0
	for num in range(10, 100000):
		if sum_of_fact(num) == num:
			total += num

	print(f"Final answer: {total}")
	print(f"This took {t.time() - start} seconds to run")

main()
# 40730
# 0.4 seconds