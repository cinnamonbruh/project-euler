# problem 69 - totient maximum

import math

def distinct_prime_factors(x):
    if x == 1:
        return []
    n = 2
    factors = []
    while n**2 < x:
        if x % n == 0:
            x //= n
            if not n in factors:
                factors.append(n)
        else:
            n += 1
    if x > 1:
        factors.append(x)
    return factors


def max_totient(limit):
    maximum = 0
    num = None
    for i in range(1, limit+1):
        totient = get_totient(i)
        if totient > maximum:
            maximum = totient
            num = i
    return num


def get_totient(n):
    # n is the number we want to check up to
    product = 1
    prime_factors = distinct_prime_factors(n)
    for factor in prime_factors:
        product *= 1/(1 - 1/factor)
    return product

print(max_totient(1000000))