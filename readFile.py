"""
Write a program that reads a file, breaks each line into words, strips whitespace and
punctuation from the words, and converts them to lowercase.
"""
import re

Text = []
with open('test.txt') as text:
    for lines in text:
        Text = Text + re.findall(r"[\w']+", lines)

for line in Text:
    print(line.lower())
