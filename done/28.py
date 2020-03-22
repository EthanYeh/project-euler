# so this problem is easy af so i didn't bother writing functions.
import time as t
start = t.clock()

sub = 2
total = 1
base = 3
# when sub is 1000, we do it and then that's the last.
while sub <= 1000:
    topright = base**2
    total += 4*topright - 6*sub
    base += 2
    sub += 2
    # print(total)

print(f"Answer: {total}")
print(f"Time: {t.clock() - start} seconds.")
# 669171001
# 0.0004 seconds
# finished 5/28/2018