# problem 5 - smallest multiple

"""
while loop because we dont know the range
loop through and increment n and use mod
"""

def smallest_multiple(r):
    result = 1

    sup = False
    while not sup:
        inf = False
        n = 1
        while not inf:
            if result % n != 0:
                inf = True
                result += 1
            else:
                if n == r:
                    inf = True
                    sup = True
                n += 1
    return result

print(smallest_multiple(20))