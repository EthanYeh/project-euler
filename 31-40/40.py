"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
"""
import time as t
def int_gen():
    """generate integers starting from 11"""
    n = 11
    while True:
        yield n
        n+=1

def main():
    start = t.time()
    # I already know d_1 and d_10 are both 1, so start at d_100
    i = 11
    product = 1
    # index is 11 right before calling '11'. It should be 13 after '11'. 
    g = int_gen()

    def helper(index_goal):
        nonlocal i
        nonlocal product
        while True:
            if i < index_goal:
                nextnum = next(g)
                i += len(str(nextnum))
                # print(nextnum, i)
            elif i == index_goal:
                product *= int(str(nextnum)[-1])
                break
            elif i > index_goal:
                extra = i-index_goal
                product *= int(str(nextnum)[len(str(nextnum))-extra-1])
                break
        return
    
    index_goal = 100
    while index_goal <= 1000000:
        helper(index_goal)
        # print(f'product so far: {product}')
        index_goal *= 10

    print(f"Final answer: {product}")
    print(f"This took {t.time() - start} seconds to run.")

main()
# 210
# 0.1 sec
