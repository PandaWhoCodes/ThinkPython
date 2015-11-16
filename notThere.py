"""
Modify the previous program to read a word list  and then print all
the words in the book that are not in the word list.
"""
noiseText = []
with open('test.txt') as noise:
    for lines in noise:
        noiseText = noiseText + lines.split()


def main():
    g = ""
    with open('book.txt') as text:
        for line in text:
            line1 = line.split()
            for words in line1:
                if words not in noiseText:
                    g = g + words + " "

    print(g)


main()
