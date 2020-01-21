# Find the sum of the digits in the number 100!
import time

def factorial(n):
	if n <= 1:
		return 1
	return n * factorial(n-1)

def main(n):
	start = time.clock()
	total = 0
	for num in str(factorial(n)):
		total += int(num)
	print("This took %e milliseconds to run" %((time.clock() - start)*1000))
	return total

main(100)
#answer is 648