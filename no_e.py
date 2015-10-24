"""
Write a function called has_no_e that returns True if the given word doesn't have the letter e in
it.
Modify your program from the previous section to print only the words that have no e and compute
the percentage of the words in the list have no e
"""


def input():
    with open('words.txt', 'r') as wd:
        wordList = wd.read().split()
    no_e(wordList)


def no_e(wordList):
    noCount = 0
    totalWords = 0

    for words in wordList:
        totalWords = totalWords + 1
        if (words.find('e') == -1 or words.find('E') == -1):
            noCount = noCount + 1
            print(words + " ")
    # percentage
    percent = (noCount * 100) / totalWords
    print("Percentage of words without E:" + str(percent))

input()
