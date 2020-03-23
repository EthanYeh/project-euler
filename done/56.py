"""
Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""

import functions as f

@f.timing
def main():
	max_sum = 0
	for a in range(1, 101):
		for b in range(1, 101):
			n = a**b
			dig_sum = sum(map(int, str(n)))
			if dig_sum > max_sum:
				max_sum = dig_sum

	print(f"answer is {max_sum}")
	return max_sum

main()
# answer is 972
# This took 0.0892798900604248 seconds to run
# completed on 3/23/2020 in taipei
# took like 2 mins to do lmao