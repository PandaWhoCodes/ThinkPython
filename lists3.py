"""
Write a function that takes a list of numbers and returns the cumulative sum
that is, a new list where the ith element is the sum of the
first i + 1 elements from the original list. For
example, the cumulative sum of [1, 2, 3] is [1, 3, 6]
"""


def nested_sum():
    a = int(input("Enter the number of Elements you want to add:"))
    mylist = []
    for i in range(0, a):
        mylist.append(int(input()))
    mylist2 = []
    mysum = 0
    for i in range(0, a):
        mysum = mysum + mylist[i]
        mylist2.append(mysum)

    print(mylist2)


nested_sum()
