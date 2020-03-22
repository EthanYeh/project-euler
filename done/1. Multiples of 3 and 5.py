#Multiples of 3 and 5
x = 1
total = 0

while x < 1000:
	if x % 3 == 0:
		total += x
	elif x % 5 == 0:
		total += x
	x+=1
	
print total

#answer is 233168