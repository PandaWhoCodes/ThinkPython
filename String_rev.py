"""
Write a function that takes a string as an
argument and displays the letters backward,
one per line.
"""

def rev(x):
    for i in x[::-1]:
        print(i)
rev("ASHISH")
