"""
Write a function called most_frequent that takes a
string and prints the letters
in decreasing order of frequency.
Only immutable elements can be used as dictionary keys, and hence only tuples and not lists can be used as keys.
Hence distionary is a combination of Tuples and Lists
"""
import operator
import re
from collections import Counter

Text = []
with open('test.txt') as text:
    for lines in text:
        Text = Text + re.findall(r"[\w']+", lines)
cnt = Counter(Text)
sorted_dict = sorted(cnt.items(), key=operator.itemgetter(1), reverse=True)
for word, count in sorted_dict:
    print(word + ": " + str(count))
# print(sorted_tuple)
