#sum the digits of 2^1000

num =  2**1000
numlist = [int(d) for d in str(num)]	#converts the integer to a list

total = 0
for digit in numlist:
	total += digit

print total
#answer is 1366