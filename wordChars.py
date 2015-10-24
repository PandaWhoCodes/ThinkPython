"""
Write a program that reads words.txt and prints only the words with more than 20
characters
"""
with open('words.txt', 'r') as wd:
    wordList = wd.read().split()

for words in wordList:
    if (len(words) > 20):
        print(words + " ")
