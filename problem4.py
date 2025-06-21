# problem 4 - largest palindrome product

"""
range will be from 1*10^(d-1) to 1*10^d
"""

def largest_palindrome(d):
    largest = 0
    for i in range(1 * 10 ** (d - 1), (1 * 10 ** d)):
        for x in range(1 * 10 ** (d - 1), (1 * 10 ** d)):
            product = i*x
            if str(product) == str(product)[::-1] and product > largest:
                largest = product
    return largest


print(largest_palindrome(3))