"""
2. countwords:
Read test.txt  and count the number of words in the file and print the word count
"""


def countWords():
    with open('test.txt') as text:
        wordCount = 0
        for lines in text:
            text1 = lines.split()
            wordCount = wordCount + len(text1)
            
            
    print( wordCount )


countWords()
