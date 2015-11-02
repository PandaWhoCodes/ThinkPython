"""
4.wordfreq:
From test.txt create and print a word frequency table.
A word frequency table consists of a word and the number
of times it occurs in the document

"""
import re
from collections import Counter

Text = []
with open('test.txt') as text:
    for lines in text:
        Text = Text + re.findall(r"[\w']+", lines)
cnt = Counter(Text)
for word, count in cnt.items():
    print(word + ": " + str(count))
