# Largest Collatz Sequence
# if n is even, n/2
# if n is odd, 3n+1
# Which starting number, under one million, produces the longest chain?
import time
def main():
	start = time.time()
	best_starting_num = 1
	current_largest = 0
	for starting_num in range(1,1000000):
		chain = collatz_length(starting_num)
		if chain > current_largest:
			current_largest = chain
			best_starting_num = starting_num
	
	print "Best starting num is %d" %best_starting_num
	print "The chain length is %d" %current_largest
	end = time.time()
	diff = end-start
	print "It took %f seconds to solve this problem" %diff


def collatz_length(num):	#returns the length of chain from starting number num
	counter = 1
	while num != 1:
		if num % 2 == 0:
			num = num / 2
		else:
			num = num * 3 + 1
			
		counter += 1

	return counter

main()
#answer is 837799