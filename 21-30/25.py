"""find the index of the first fibonnaci number to contain 1000 digits"""

import time
def fib_gen():
	"""generator that yields the next fibonacci number"""
	pre, curr = 0, 1
	while True:
		yield curr
		pre, curr = curr, pre + curr

def main():
	start = time.time()
	i = 1
	fibs = fib_gen()
	fibrn = next(fibs)
	while len(str(fibrn)) < 1000:
		fibrn = next(fibs)
		i += 1
	print(f"Final answer: {i}")
	print(f"This took {time.time()-start} seconds to run")

main()
# answer is 4782, runs in about 0.14 seconds