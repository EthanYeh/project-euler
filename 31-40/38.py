"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 
and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 
918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed 
as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
import time as t

def is_pandigital(strnum):
    """check if strnum is pandigital"""
    lst = []
    for num in strnum:
        if num in lst or num == "0":
            return False
        lst.append(num)
    return True

def check_rest(strnum):
    totalstring = strnum
    multiplier = 2

    while len(totalstring) < 9:
        totalstring += str(multiplier*int(strnum))
        multiplier += 1

    if len(totalstring) > 9:
        return False
    if is_pandigital(totalstring):
        return True
    return False

def main():
    start = t.time()
    for n in range(9999, 1, -1):
        strnum = str(n)
        if is_pandigital(strnum):
            if check_rest(strnum):
                print(f"Answer is {int(str(n) + str(n*2))}.")
                print(f"Time: {t.time() - start} seconds.")
                return

main()
# 932718654
# 0.002 seconds
# 5/31/2018