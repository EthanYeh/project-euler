"""
How many different ways can £2 be made using any number of coins?
coin values are:
[1,2,5,10,20,50,100,200]
"""
import time

def memoize(f):
    cache = {}

    def helper(x, y):
        if (x, tuple(y)) not in cache:
            cache[(x, tuple(y))] = f(x,tuple(y))
        return cache[(x,tuple(y))]
    return helper

@memoize
def count_coins(amount, currency):
    if amount == 0:
        return 1
    elif amount < 0:
        return 0
    elif len(currency) == 0:
        return 0
    return count_coins(amount-currency[0], currency) + count_coins(amount, currency[1:])

def main():
    start = time.time()
    coins = [1,2,5,10,20,50,100,200]
    print(f"Final answer: {count_coins(200, coins)}")
    print(f"This took {time.time() - start} seconds to run.")

main()
# 73682
# took 6.3 seconds to run w/o memoization
# took 0.005 seconds to run w/ memoization