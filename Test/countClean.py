"""
3. countclean:
Read words from test.txt and 'noise words' from
noise.txt. Print words from test.txt if it is not a noise word.

"""
noiseText = []
with open('noise.txt') as noise:
    for lines in noise:
        noiseText = noiseText + lines.split()


def main():
    g = ""
    with open('test.txt') as text:
        for line in text:
            line1 = line.split()
            for words in line1:
                if words not in noiseText:
                    g = g + words + " "

    print(g)


main()
