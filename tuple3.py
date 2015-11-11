"""
Write a function called most_frequent that takes a
string and prints the letters
in decreasing order of frequency.
"""
import operator
import re
from collections import Counter

Text = []
with open('test.txt') as text:
    for lines in text:
        Text = Text + re.findall(r"[\w']+", lines)
cnt = Counter(Text)
sorted_tuple = sorted(cnt.items(), key=operator.itemgetter(1), reverse=True)
for word, count in sorted_tuple:
    print(word + ": " + str(count))
# print(sorted_tuple)
