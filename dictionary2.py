"""
Dictionaries have a method called keys that returns the keys of the dictionary, in
no particular order, as a list.
Modify print_hist to print the keys and their values in alphabetical order.
"""

hist = {1: 2, 3: 4, 5: 6, 7: 8}


def print_hist():
    for keys in hist:
        print(keys)

print_hist()
