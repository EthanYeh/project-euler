# def paths(row, column):
# 	if row == 0 or column == 0:
# 		return 1
# 	else:
# 		return paths(row-1, column) + paths(row, column-1)

from math import factorial
print factorial(40)/factorial(20)/factorial(20)

#answer is 137846528820