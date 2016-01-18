"""
Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn't matter what the values are.
check whether a string is in the dictionary.
"""

results = {}


def str2dict():
    # count = 1
    with open('test.txt') as text:
        for line in text:
            for words in line.split():
                results[words] = 'Dict'


def hasString():
    for key, value in results.items():
        try:
            key = int(key)
        except ValueError:
            print('Dictionary contains a string')
            return


str2dict()
hasString()
