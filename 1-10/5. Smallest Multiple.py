#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

primes = []

def main(num):
	for i in range(1,num):
		if check_prime(i):
			primes.append(i)
	print primes

	#exclude 1 in the primes
	primes.remove(1)
	print "all prime factors exluding 1 are as follows: "
	print primes     #should be [2,3,5,7,11,13,17,19]

	powers = []
	result=0
	exponent = 1
	
	for prime in primes:
		while prime**exponent < num:
			exponent = exponent + 1

		powers.append(exponent-1)
		exponent = 1

	print "Raise the prime factors to the powers and multiply them together to get the smallest multiple. Powers are below." 
	print powers

	smallest_multiple = 1
	for i in range(0,len(primes)):
		smallest_multiple = primes[i]**powers[i]*smallest_multiple

	print smallest_multiple

def check_prime(num):
	for j in range(2, num):
		if num%j == 0:
			#print "%d is not prime, it is divisible by %d" %(num,j)
			return False
	return True

main(20)
#answer is 232792560