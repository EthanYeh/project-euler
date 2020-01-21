# The prime factors of 13195 are 5, 7, 13, and 29
# What is the largest prime factor of the number 600851475143?
import time
import math
factors=[]

def find_factors(num):
	for i in range(1, int(math.sqrt(num))+1):
		if num % i == 0:
			factors.append(i)
	factors.reverse()	

def check_prime(num):
	for j in range(2, int(math.sqrt(num))+1):
		if num%j == 0:
			return False
	return True

def main(num):
	start = time.time()
	find_factors(num)
	print "Factors are as follows: " 
	print factors
	for factor in factors:
		if check_prime(factor):
			print "The largest prime of %d is %d" %(num, factor)
			end = time.time()
			diff = end -start
			print "It took %f seconds to run this program" %diff
			break
		
main(600851475143)
#answer is 6857