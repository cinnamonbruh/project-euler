# problem 7 - 10 001st prime

"""
never going to be an even number, we can rule out 2n
therefore we could just use 2n + 1 and check if prime?
dont know if quick enough
"""

import math

def is_prime(n):
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0 and i != 1:
            return False
    return True


def find_prime(x):
    i = 1
    o = 1
    while o != x:
        p = 2*i + 1
        i += 1
        if is_prime(p):
            o += 1
    return p

print(find_prime(10001))