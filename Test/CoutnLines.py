"""
countlines:
Read test.txt and count the lines and print the line count
"""


def countLines():
    with open('test.txt') as text:
        print(sum(1 for _ in text))


countLines()
