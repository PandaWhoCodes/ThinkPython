"""
Write a function called nested_sum
that takes a nested list of integers and add up
the elements from all of the nested lists.
"""


def nested_sum():
    a = int(input("Enter the number of Elements you want to add:"))
    mylist = []
    for i in range(0, a):
        mylist.append(int(input()))
    mysum = sum(mylist)
    print(mysum)


nested_sum()
