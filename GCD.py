"""
Write a function called gcd that takes parameters a and b
and returns their greatest common divisor.

Credit: This exercise is based on an example from
Abelson and Sussman's Structure and Interpretation of Computer Programs.

"""


def GCD():
    a = int(input("Enter the first number:"))
    b = int(input("Enter the first number:"))
    small = 0
    gcd = 0
    if (a > b):
        small = b
    else:
        small = a
    for i in range(1, small + 1):
        if (a % i == 0 and b % i == 0):
            if (i > gcd):
                gcd = i
    print("Greatest common factor:")
    print(gcd)


GCD()
