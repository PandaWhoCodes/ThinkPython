"""
Write a program that reads a wordlist and finds all the rotate pairs.
"""

wordlist=["this","word","list","only","one","malayalam"]
def rotate():
    for items in wordlist:
        if(items == items[::-1]):
            print(items)
rotate()
