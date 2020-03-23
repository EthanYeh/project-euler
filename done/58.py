"""
Starting with 1 and spiralling anticlockwise in the following way, 
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, 
but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; 
that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, 
a square spiral with side length 9 will be formed. If this process is continued, 
what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""

import functions as f

@f.timing
def main():
	num_diags = 1	# start with 1 cuz 1 is in the middle
	num_primes = 0
	side_len = 2
	curr = 1
	while True:
		for i in range(4):
			curr += side_len
			num_diags += 1
			if f.isPrime(curr):
				num_primes += 1
			if num_primes/num_diags < 0.1:
				print(f"answer is {side_len+1}")
				return side_len
		side_len += 2

	print(f"num diags is {num_diags}")
	print(f"num primes is {num_primes}")

main()
# answer is 26241
# This took 8.922507524490356 seconds to run
# completed on 3/23/2020 in Tapei during quarantine.