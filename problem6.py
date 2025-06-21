# problem 6 - sum square difference

def diff(n):
    sum_of_squares = 0
    square_of_sum = 0

    for i in range(1, n+1):
        # sum of squares
        sum_of_squares += i**2

        # square of sum
        square_of_sum += i

    return square_of_sum**2 - sum_of_squares

print(diff(100))