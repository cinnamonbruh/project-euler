# problem 69 - totient maximum

"""
use euclids algorithm to find the greatest common divisor
"""

def totient_maximum(n):
    largest = 0
    for x in range(1, n):
        count = 0
        for i in range(1, n):
            upper = n
            lower = i
            remainder = None
            while remainder != 0:
                remainder = upper % lower
                upper = lower
                lower = remainder
            # is relatively prime
            if remainder == 1:
                count += 1
        if (n/count) > largest:
            largest = (n/count)
    return largest

        
print(totient_maximum(5))