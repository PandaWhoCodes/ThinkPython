"""
A string slice can take a third index that specifies the
"step size;" that is, the number
of spaces between successive characters.
A step size of 2 means every other character; 3 means every
third, etc.
Use this idiom to write a one-line version of is_palindrome from Exercise 6
"""


def backwards(x):
    g = ""
    for i in x[::-1]:
        g = g + i
    return g


def palindrome():
    a = input("Enter the String to check for palindrome:")
    a = a.lower()
    b = backwards(a)
    if (a == b):
        print("PALINDROME")
    else:
        print("NOT A PALINDROME")


palindrome()
