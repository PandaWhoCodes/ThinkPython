"""
Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise.
You can assume (as a precondition) that
the elements of the list can be compared with the relational operators <, >, etc.
"""


def is_sorted(mylist):
    a = 0
    if (mylist[0] > mylist[1]):
        a = 1
    flag = 0
    for i in range(0, len(mylist) - 1):
        if (a == 1):
            if (mylist[i] < mylist[i + 1]):
                flag = 1
                break
        else:
            if (mylist[i] > mylist[i + 1]):
                flag = 1
                break
    if (flag == 1):
        print("False")
    else:
        print("True")


is_sorted(['a','b','c'])
