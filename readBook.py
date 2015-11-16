"""
Go to Project Gutenberg (http: // gutenberg. org ) and download your favorite
out-of-copyright book in plain text format.
Modify your program from the previous exercise to read the book you downloaded, skip over the
header information at the beginning of the file, and process the rest of the words as before.
Then modify the program to count the total number of words in the book, and the number of times
each word is used.
Print the number of different words used in the book.
"""
import re
from collections import Counter

Text = []
with open('book.txt') as text:
    next(text)
    for lines in text:
        Text = Text + re.findall(r"[\w']+", lines)
print(len(Text))
cnt = Counter(Text)
for word, count in cnt.items():
    print(word + ": " + str(count))

