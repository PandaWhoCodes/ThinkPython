"""
Write a function called middle that takes a list and returns a
new list that contains
all but the first and last elements.
So middle([1,2,3,4]) should return [2,3].
"""

def middle():
    a = int(input("Enter the number of Elements you want to add:"))
    mylist = []
    for i in range(0, a):
        mylist.append(input())
    mylist2=[]

    for i in range(1,a-1):
        mylist2.append(mylist[i])
    print(mylist2)

middle()
