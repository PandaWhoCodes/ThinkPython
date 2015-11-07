"""
To check whether a word is in the word list, you could use the in operator, but it
would be slow because it searches through the words in order.
Because the words are in alphabetical order, we can speed things up with a bisection search (also
known as binary search), which is similar to what you do when you look a word up in the dictionary
"""


def binary_search(my_list, word):
    if len(my_list) == 0:
        return False
    else:
        midpoint = len(my_list) // 2
        if my_list[midpoint] == word:
            return True
        else:
            if word < my_list[midpoint]:
                return binary_search(my_list[:midpoint], word)
            else:
                return binary_search(my_list[midpoint + 1:], word)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))
