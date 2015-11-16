"""
Modify the program from the previous exercise to print the 20 most frequently-used
words in the book.
"""
import operator
import re
from collections import Counter

Text = []
with open('book.txt') as text:
    next(text)
    for lines in text:
        Text = Text + re.findall(r"[\w']+", lines)
print(len(Text))
cnt = Counter(Text)

sorted = sorted(cnt.items(), key=operator.itemgetter(1), reverse=True)
count1 = 1
for word, count in sorted:
    if (count1 == 21):
        break;
    else:
        print(word + ":" + str(count))
    count1 = count1 + 1
