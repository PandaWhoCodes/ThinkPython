"""
A number, a, is a power of b if it is divisible by b and
a/b is a power of b. Write a function called is_power that
takes parameters a and b and returns True if a is a power of
b. Note: you will have to think about the base case.
"""


# our Conditions according to the queestion are
# a%b==0
# (a/b)%b==0

# We will write two functions:
# one to find the power for a given number
# and other according to the question

def find_power():
    a = int(input("Enter the Number to get its power:"))
    for i in range(2, a - 1):
        if (a % i == 0 and (a / i) % i == 0):
            print(i)
            break


def is_power(a, b):
    if (a % b == 0 and (a / b) % b == 0):
        print("TRUE")
    else:
        print("False")


def user_input():
    print("Input choice:")
    print("1. Find Power:")
    a = input("2. Find if B is a power of A:")
    if (a == 1):
        find_power()
    else:
        c = int(input("Enter A :"))
        b = int(input("Enter B :"))
        is_power(c, b)


user_input()
