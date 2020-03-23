"""
It is possible to show that the square root of two 
can be expressed as an infinite continued fraction.
In the first one-thousand expansions, 
how many fractions contain a numerator with more digits than the denominator?
"""

import functions as f

def num_digits(n):
	return len(str(n))

@f.timing
def main():
	numer = 0
	denom = 0
	num_fracs = 0
	t_ll = 1    # last last term (t_(n-2))
	t_l = 2		# last term (t_(n-1))
	for n in range(3, 1001):
		t_n = 2*t_l + t_ll				# t_n = 2t_(n-1) + t_(n-2)
		denom = t_l
		numer = t_ll + denom
		# print(f"fraction is {numer}/{denom}")
		if num_digits(numer) > num_digits(denom):
			num_fracs += 1
		t_l, t_ll = t_n, t_l

	print(f"answer is {num_fracs}")
	return num_fracs
		
main()
# answer is 153
# This took 0.0039691925048828125 seconds to run
# completed on 3/23/2020 in Taipei
# kinda interesting, took about half an hour to do