"""
Write a function called nested_sum
that takes a nested list of integers and add up
the elements from all of the nested lists.
"""

mylist = [1, [73, 89, 42, 32], 62, [24, 32], 99]


def nested_sum(mylist1):
    total = 0
    for i in mylist1:
        if isinstance(i, list):  # checks if `i` is a list
            total += nested_sum(i)
        else:
            total += i
    return total


print(nested_sum(mylist))
