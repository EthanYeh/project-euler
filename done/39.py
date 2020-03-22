"""
If p is the perimeter of a right triangle with integral length sides, 
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
from math import sqrt
import time as t

def num_sols(p):
    """given perimeter P, return the number of solutions"""
    counter = 0
    for a in range(1, (p-3)//3+1):
        for b in range(a+1, p-a):
            if a**2  + b**2 == (p-a-b)**2:
                counter += 1
                break
                # print(f"p: {p}, a: {a}, b: {b}")
    return counter

def main():
    start = t.time()
    max_sf = 0
    bestp = 0
    for p in range(12, 1001):
        sols = num_sols(p)
        if sols > max_sf:
            max_sf = sols
            bestp = p

    print(f"{bestp} has the most solutions, it has {num_sols(bestp)}.")
    print(f"Final Answer: {bestp}")
    print(f"Time: {t.time() - start} seconds.")

main()
# 840
# time: 55 seconds