# What is the largest palindrome product of 2 3-digit numbers? A palindrome is like 12321
import time

def main():
	start = time.time()

	largest = 0
	for i in range(100,1000):
		for j in range(100,i):
			if check_palindrome(i*j) and i*j > largest:
				largest = i*j
			
	print("The largest palindrome product of 2 3-digit numbers is", largest)
	print('It took {0} seconds to run this'.format(time.time()-start))

def check_palindrome(num):
	word = str(num)
	for i in range(0, len(word)):
		if word[i] != word[len(word)-1-i]:
			return False
	return True

# lol below doesn't work
# def is_palindrome(num):
# 	""" This is probably what 61A would want me to do
# 		Written after taking 61A
# 	"""

# 	order_of_mag = 10**(len(str(num)) - 1)
# 	if num <= 0:
# 		return True
# 	if num % 10 == num // order_of_mag:
# 		if len(str(num)) == 2:
# 			return True
# 		return is_palindrome(num%order_of_mag - num%10)
# 	return False


main()
#answer is 906609