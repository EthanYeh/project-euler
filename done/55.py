"""
How many Lychrel numbers are there below ten-thousand?
"""
import functions as f

def add_reverse(n):
	"""
	Takes in number N, and adds it by its reverse
	"""
	rev = int(str(n)[-1::-1])
	return n + rev

@f.timing
def main():
	lychrels = []
	palin = False
	max_iter = 50
	for seed in range(1, 10000):
		n = seed
		for _ in range(max_iter):
			n = add_reverse(n)
			if f.isPalindrome(n):
				palin = True
				break
		if not palin:
			lychrels.append(seed)
		palin = False
	print(f"These are the lychrel numbers: {lychrels}")
	print(f"There are {len(lychrels)} of them.")
	return len(lychrels)
		
main()
# Answer is 249
# Runs in 0.05 seconds
# Took about 30 min to write