# Work out the first 10 digits of the sum of the following 100 50-digit numbers

def sum_vertical(column):
	data = open("13.txt", "r")

	sums = 0
	for row in range(0,100):
		sums += int(data.readline()[column])

	return sums

	data.close()

def main():
	
	digits = [0] *52
	addingindex = 0

	for column in range(49,-1,-1):  #the range is a list from 49 to 0
		colsum = sum_vertical(column)

		right_digit = (colsum%100)%10
		middle_digit = (colsum%100)/10
		left_digit = colsum/100

		digits[addingindex] += right_digit
		digits[addingindex+1] += middle_digit
		digits[addingindex+2] =+ left_digit
		
		addingindex += 1

	print digits
	
	for i in range(len(digits)):
		if digits[i] > 9:
			digits[i+1] += digits[i]/10
			digits[i] = digits[i]%10
			

	print digits

main()
#answer is 5537376230