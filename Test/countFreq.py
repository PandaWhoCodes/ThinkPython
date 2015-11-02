"""
4.wordfreq:
From test.txt create and print a word frequency table.
A word frequency table consists of a word and the number
of times it occurs in the document

"""

from collections import Counter

Text = []
with open('test.txt') as text:
    for lines in text:
        Text = Text + lines.split()
cnt = Counter(Text)
for word, count in cnt.items():
    print(word + ": " + str(count))

