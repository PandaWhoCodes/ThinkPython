"""
Write a function called is_palindrome that takes a
string argument and returns True if it is a palindrome
and False otherwise. Remember that you can use the
built-in function len to check the length of a string.
"""


def inputs():
    a = input("Enter the String/number to check for palindrome:")
    a = a.lower()
    is_palindrome(a)


def is_palindrome(a):
    g = ""

    for characters in a:
        g = characters + g
    if (g == a):
        print("True")
    else:
        print("False")


inputs()
