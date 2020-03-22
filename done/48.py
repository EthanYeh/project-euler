"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""
import time as t

def main():
    """ Hella brute force. """
    start = t.time()
    total = 10405071317
    for i in range(11, 1001):
        total += i**i
    print(f"Answer is {total % 10000000000}")
    print(f"This took {t.time() - start} seconds to run")

# Answer is 9110846700
# This took 0.03 seconds to run
# Completed on 12/19/2018, took like 3 minutes to write.
# It would be harder to do this on any other language like Java
