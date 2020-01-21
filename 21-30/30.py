"""
Find the sum of all the numbers that are equal to the sum of the 5th power of their digits.
"""

from functools import reduce
import time

def is_good(num):
	diglist = list(str(num))
	total = reduce(lambda x, y: x+y, [int(x)**5 for x in diglist])
	return total == num

def main():
	start = time.time()
	total = 0
	# the range is arbitrary and it worked. brute force method
	for num in range(2, 1000000):
		if is_good(num):
			total += num

	print(f"Final answer: {total}")
	print(f"This took {time.time() - start} seconds to run.")

main()
# 443839
# runs in 4.5 seconds