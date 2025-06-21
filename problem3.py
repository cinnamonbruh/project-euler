# problem 3 - largest prime factor
import math

def is_prime(x):
    for i in range(1, int(math.sqrt(x) + 1), 1):
        if x % i == 0 and i != 1:
            return False
    return True

factors = []

def prime_factors(x):
    for i in range(1, int(math.sqrt(x) + 1), 1):
        if is_prime(i):
            if x % i == 0:
                factors.append(i)
                pair = x / i
                if is_prime(pair):
                    factors.append(pair)

prime_factors(600851475143)

print(sorted(factors)[len(factors)-1])