# The sum of the primes below 10 is 2+3+5+7=17
# Find sum of all the primes below 2 million
import math
import time
def main():
	start = time.time()
	total = 0
	for i in range(2,2000000):
		if check_prime(i):
			total = total + i

	print "Sum of all primes below 2 million is %d" %total
	end = time.time()
	diff = end-start
	print "It took %f seconds to solve this problem" %diff

def check_prime(num):
	for j in range(2, int(math.sqrt(num))+1):
		if num%j == 0:
			return False			
	return True

main()
#sum is 142913828922