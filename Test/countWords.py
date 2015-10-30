"""
2. countwords:
Read test.txt  and count the number of words in the file and print the word count
"""


def countWords():
    with open('test.txt') as text:
        len = 0
        for sentences in text:
            for words in sentences:
                len+=1
            
    print(len)


countWords()
