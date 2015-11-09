"""
Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn't matter what the values are.
check whether a string is in the dictionary.
"""


def str2dict(filename="test.txt"):
    results = {}
    count = 1
    with open('test.txt') as text:
        for line in text:
            results[count] = line
            count = count + 1
    return results


def checkData(myDict):
    for i in range(1, len(myDict)+1):
        if isinstance(myDict[i],str):
            print("STR")


checkData(str2dict("test.txt"))
