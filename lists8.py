"""
Write a function called remove_duplicates that takes a list and returns a new
list with only the unique elements from the original.
Hint: they don't have to be in the same order
"""


def remove_duplicates(my_list):
    for i in range(0, len(my_list) - 1):
        for j in range(i + 1, len(my_list)):

            if my_list[i] == my_list[j] and my_list[j] != False:
                my_list[j] = False

    for i in my_list:
        if i != False:
            print(str(i))


remove_duplicates([1, 1, 2, 3, 4, 5, 6, 6, 7, 4, 3, 2, 23, 35, 57, 57])
