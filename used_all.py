"""
Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once.
"""

def used_all():
    word = input("Enter the word:")
    letters = input("Enter the string of letters:")
    count = 0

    l = len(letters)
    for alphabet in word:
        if alphabet in letters:
            count=count+1
    if count>=l:
        return True
    else:
        return False

print(used_all())
