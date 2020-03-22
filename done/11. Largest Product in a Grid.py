# Largest Product in a Grid
# In the 20x20 grid stored in "11.txt", find the greatest product of 4 adjacent numbers in the same direction(vertical, horizontal, diagonal).
import time

data = open("11.txt", "r")

def listify(row):  #turns the row from string to a list of integers
	output_list = []
	for index in [x for x in range(60) if x%3==0]:
		output_list.append(int(row[index]+row[index+1]))

	return output_list

def getmatrix():
	data_list = []    #get a list of lists. Each list is a row.
	for i in range(20):
		data_list.append(listify(data.readline()))
	return data_list


def horizontalmax(datalist):
	largest_horizontal = 1

	for row in range(20):
		for column in range(17):
			product = datalist[row][column]*datalist[row][column+1]*datalist[row][column+2]*datalist[row][column+3]
			if product > largest_horizontal:
				largest_horizontal = product

	return largest_horizontal

def verticalmax(datalist):
	largest_vertical = 1

	for row in range(17):
		for column in range(20):
			product = datalist[row][column]*datalist[row+1][column]*datalist[row+2][column]*datalist[row+3][column]
			if product > largest_vertical:
				largest_vertical = product

	return largest_vertical

def southeastmax(datalist):
	largest_southeast = 1

	for row in range(17):
		for column in range(17):
			product = datalist[row][column]*datalist[row+1][column+1]*datalist[row+2][column+2]*datalist[row+3][column+3]
			if product > largest_southeast:
				largest_southeast = product

	return largest_southeast

def northeastmax(datalist):
	largest_northeast = 1

	for row in range(3,20)[::-1]:
		for column in range(17):
			product = datalist[row][column]*datalist[row-1][column+1]*datalist[row-2][column+2]*datalist[row-3][column+3]
			if product > largest_northeast:
				largest_northeast = product

	return largest_northeast

def main():
	start = time.time()
	list_of_data = getmatrix()
	products = []
	products.append(horizontalmax(list_of_data))
	products.append(verticalmax(list_of_data))
	products.append(southeastmax(list_of_data))
	products.append(northeastmax(list_of_data))
	products.sort()
	print products[3]
	
	end = time.time()
	diff = (end - start)*1000
	print "It took %f milliseconds to solve this problem" %diff

main()
#answer is 70600674

# I think there's an easier way to do this by just looping through each number, and with each number check all appropriate directions.
# Oh well