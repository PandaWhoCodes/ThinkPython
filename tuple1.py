"""
Write a function called sumall that takes any number of
arguments and returns their sum.
"""


def sumall(t=()):
    sum = 0
    for x in t:
        sum = sum + x
    return sum


t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(sumall(t))
