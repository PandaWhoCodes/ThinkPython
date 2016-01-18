"""
Dictionaries have a method called keys that returns the keys of the dictionary, in
no particular order, as a list.
Modify print_hist to print the keys and their values in alphabetical order.
"""

hist = {1: 2, 3: 4, 5: 6, 7: 8}
mydict = {'carl': 40,
          'alan': 2,
          'bob': 1,
          'danny': 3}


def print_hist():
    for key in sorted(hist):
        print(key)
    for key in sorted(mydict):
        print(key)


print_hist()
