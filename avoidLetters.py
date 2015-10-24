"""
Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn't use any of the forbidden letters.

Modify your program to prompt the user to enter a string of forbidden letters and then print the
number of words that don't contain any of them.
"""


def avoids():
    words = input("Enter the string:")
    wordList = words.split()
    letters = input("Enter the forbidden characters:")
    count = 0
    for word in wordList:
        for letter in letters:
            for moreLetters in word:
                if (moreLetters == letter):
                    count = count - 1
        count = count + 1
    if (count > 0):
        print("Number of Words without the forbidden Characters:" + str(count))
    else:
        print("0")


avoids()
