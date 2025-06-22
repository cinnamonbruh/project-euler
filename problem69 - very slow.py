# problem 69 - totient maximum

"""
use euclids algorithm to find the greatest common divisor
"""

def totient_maximum(n):
    debug = False
    maximum = 0
    for i in range(2, n+1):
        relatives = 1
        for x in range(2, i):
            if i == 2:
                break

            upper_bound = i
            lower_bound = x
            remainder = None
            previous = None
            while remainder != 0:
                previous = remainder
                remainder = upper_bound % lower_bound
                upper_bound = lower_bound
                lower_bound = remainder
            if previous == 1:
                relatives += 1
        totient = i/relatives
        if totient > maximum:
            maximum = totient
        if debug:
            print("totient:", totient, "/ amount:", relatives)
    return maximum

print(totient_maximum(1000000))