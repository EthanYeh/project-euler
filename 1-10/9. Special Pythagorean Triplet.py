#Special Pythagorean Triplet
#There exists a pythagorean triplet where a+b+c == 1000, find a*b*c
import math
import time
def main():
	start = time.time()
	triplets = []
	for a in range(1, 1000):
		for b in range(1, 1000):
			sum = a**2 + b**2
			c = math.sqrt(sum)
			if c/ int(c) == 1:
				if a + b + c == 1000:
					print "%d squared plus %d squared equals %d squared" %(a,b,c)
					result = a*b*c
					print "%d*%d*%d equals %d" %(a, b, c, result)
					end = time.time()
					diff = (end-start)*1000
					print "It took %f milliseconds to solve this problem" %diff
					return True

main()
#31875000