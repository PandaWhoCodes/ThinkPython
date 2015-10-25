"""
There is a string method called count that is similar to the function in the previous
exercise. Read the documentation of this method and write an invocation that counts the number of
as in 'banana'
"""

word = "banana"
letter = "a"


def count(word, letter):
    return word.count(letter)


print(count(word, letter))
