# You are given the following information, but you may prefer to do some research for yourself.

# 2016 was leap year
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""start on 1/1/1901, add by 31 and check sunday, add 28, etc"""
import time

def is_leap(year):
	if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
		return True
	return False

def main():
	start = time.time()
	reg = [31,28,31,30,31,30,31,31,30,31,30,31]
	leap = [31,29,31,30,31,30,31,31,30,31,30,31]

	day = 366%7		# this starting day is the day of the week of 1/1/1901
	total = 0
	for year in range(1901,2001):
		if is_leap(year):
			for days_in_month in leap:
				day += days_in_month
				if day % 7 == 0:
					total += 1
		else:
			for days_in_month in reg:
				day += days_in_month
				if day % 7 == 0:
					total += 1
		
	print(f'Final answer is {total}')
	print(f"This took {time.time() - start} seconds to run.")

main()
# 171
# runs in 0.001 seconds