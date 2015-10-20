"""
Fermat's Last Theorem says that there are no positive integers a, b, and c such that
a^n=b^n=c^n
Write a function named check_fermat that takes four parameters-a, b, c
and n-and that checks to see if Fermat's
theorem holds. If n is greater than 2 and it turns out to be true
the program should print, "Holy smokes, Fermat was wrong!"
Otherwise the program should print, "No, that doesn't work."

Write a function that prompts the user to input values
for a, b, c and n, converts them to integers, and uses
check_fermat to check whether they violate Fermat's theorem.

"""


def check_fermat():
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    c = int(input("Enter the third number:"))

    n = int(input("Enter the value of n:"))
    if (a ** n + b ** n == c ** n and n > 2):
        print("HOly Smokes Fermat was wrong")
    else:
        print("Nope, that doesnt work")


check_fermat()
