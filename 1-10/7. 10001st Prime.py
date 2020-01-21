# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?
import time
import math
primes = [2]

def main(num):
	start = time.time()
	
	counter = 0
	i = 2
	while counter<num:	#check off by 1
		if check_prime(i):
			counter = counter + 1

		i = i + 1
	#print counter
	print "The 10001st prime number is %d" %(i-1)
	end = time.time()
	elapsed = end-start
	print "It took %f seconds to run this program" %elapsed

def cache_check_prime(num):
	for j in primes:
		if j<= int(math.sqrt(num))+1:
			if num%j == 0:
				return False			
	primes.append(num)
	return True

def check_prime(num):
	for j in range(2, int(math.sqrt(num))+1):
		if num%j == 0:
			return False			
	primes.append(num)
	return True

main(10001)
#answer is 104743