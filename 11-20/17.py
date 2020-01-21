#I COULDA USED A DICTIONARY I'M SO DUMB LMAO
one = 3
two = 3
three = 5
four = 4
five = 4
six = 3
seven = 5
eight = 5
nine = 4
ten = 3
eleven = 6
twelve = 6
thirteen = 8
fourteen = 8
fifteen = 7
sixteen = 7
seventeen = 9
eighteen = 8
nineteen = 8
twenty = 6
thirty = 6
forty = 5
fifty = 5
sixty = 5
seventy = 7
eighty = 6
ninety = 6
hundred = 7
thousand = 8

def thousand_term():
	return one + thousand

def hundred_term(num):
	if num == 100:
		return one + hundred
	elif num == 200:
		return two + hundred
	elif num == 300:
		return three + hundred
	elif num == 400:
		return four + hundred
	elif num == 500:
		return five + hundred
	elif num == 600:
		return six + hundred
	elif num == 700:
		return seven + hundred
	elif num == 800:
		return eight + hundred
	elif num == 900:
		return nine + hundred
	elif num//100 == 1:
		return one + hundred + 3 + last_two_term(num%100)
	elif num//100 == 2:
		return two + hundred + 3 + last_two_term(num%100)
	elif num//100 == 3:
		return three + hundred + 3 + last_two_term(num%100)
	elif num//100 == 4:
		return four + hundred + 3 + last_two_term(num%100)
	elif num//100 == 5:
		return five + hundred + 3 + last_two_term(num%100)
	elif num//100 == 6:
		return six + hundred + 3 + last_two_term(num%100)
	elif num//100 == 7:
		return seven + hundred + 3 + last_two_term(num%100)
	elif num//100 == 8:
		return eight + hundred + 3 + last_two_term(num%100)
	elif num//100 == 9:
		return nine + hundred + 3 + last_two_term(num%100)

def last_two_term(num):
	if num < 10:
		return one_term(num)
	elif num == 10:
		return ten
	elif num == 11:
		return eleven
	elif num == 12:
		return twelve
	elif num == 13:
		return thirteen
	elif num == 14:
		return fourteen
	elif num == 15:
		return fifteen
	elif num == 16:
		return sixteen
	elif num == 17:
		return seventeen
	elif num == 18:
		return eighteen
	elif num == 19:
		return nineteen
	elif num//10 == 2:
		return twenty + one_term(num%10)
	elif num//10 == 3:
		return thirty + one_term(num%10)
	elif num//10 == 4:
		return forty + one_term(num%10)
	elif num//10 == 5:
		return fifty + one_term(num%10)
	elif num//10 == 6:
		return sixty + one_term(num%10)
	elif num//10 == 7:
		return seventy + one_term(num%10)
	elif num//10 == 8:
		return eighty + one_term(num%10)
	elif num//10 == 9:
		return ninety + one_term(num%10)


def one_term(num):
	if num == 0:
		return 0
	elif num == 1:
		return one
	elif num == 2:
		return two
	elif num == 3:
		return three
	elif num == 4:
		return four
	elif num == 5:
		return five
	elif num == 6:
		return six
	elif num == 7:
		return seven
	elif num == 8:
		return eight
	elif num == 9:
		return nine


def main(upper = 1001):
	sum = 0
	for i in range(1, upper): #1,1001 gives us 1 through 1000
		if len(str(i)) == 1:
			sum += one_term(i)
		elif len(str(i)) == 2:
			sum += last_two_term(i)
		elif len(str(i)) == 3:
			sum += hundred_term(i)
		elif len(str(i)) == 4:
			sum += thousand_term()

	print(sum)

#Final answer is 21124