"""The brilliant mathematician Srinivasa Ramanujan found an infinite series
that can be used to generate a numerical approximation of pi:
Write a function called estimate_pi that uses this formula to compute and
return an estimate of pi. It should use a while loop to compute terms of
the summation until the last term is smaller than 1e-15 (which is Python
notation for 10^−15 ). You can check the result by comparing it to math.pi
"""
import math


def factorial(n):
    if n == 0:
        return 1
    else:
        f = factorial(n - 1)
        f = n * f
        return f


def estimate_pi():
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4 * k) * (1103 + 26390 * k)
        den = factorial(k) ** 4 * 396 ** (4 * k)
        temp = factor * num / den
        total += temp

        if abs(temp) < 1e-15: break
        k += 1

    return 1 / total


print(estimate_pi())
