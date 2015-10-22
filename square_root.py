"""
To test the square root function in this chapter you
could compare it wth math.sqrt
Write a function called test_square_root
that prints out the tale like
1. 0 1 1 o
2. 0 1.4.12 1.414 2.22

The first column is a number, a; the second column is the square root of a computed with the function
from Section 7.5; the third column is the square root computed by math.sqrt; the fourth column is
the absolute value of the difference between the two estimates.
"""

import math


def test_square_root():
    a = int(input("Enter the number of terms to print:"))
    for i in range(1, a + 1):
        sq = math.sqrt(i)
        x = i + 1
        y = ((x + i) / x) / 2
        absValue = abs(y - sq)
        print(str(i) + " " + str(y) + " " + str(sq) + " " + str(absValue))


test_square_root()
