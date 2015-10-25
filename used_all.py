"""
Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once.
"""


def used_all():
    words = input("Enter the string:")
    wordList = words.split()
    letters = input("Enter the characters:")
    count = 0
    for word in wordList:
        for letter in letters:
            for moreLetters in word:
                if (moreLetters == letter):
                    count = count + 1
        if (count < 0):
            print("INVALID")
            exit()
        else:
            count = 0
    print("VALID STRING")


used_all()
