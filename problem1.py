# problem 1 - multiples of 3 or 5

sum = 0

for i in range(0, 1000, 1):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print(sum)