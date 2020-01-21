# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385=2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def main(num):
	sum_of_squares = 0
	for i in range(1,num+1):
		sum_of_squares = sum_of_squares+ i**2

	print "sum of squares is %d" %sum_of_squares

	sum = 0
	for j in range(1, num+1):
		sum = sum +j
	
	square_of_sum = sum**2
	print "square of sum is %d" %square_of_sum
	difference = square_of_sum - sum_of_squares
	print "difference is %d" %difference

main(100)
#answer is 25164150