"""
3. countclean:
Read words from test.txt and 'noise words' from
noise.txt. Print words from test.txt if it is not a noise word.

"""


def main():
   
    with open('test.txt') as text:
        with open('noise.txt') as noiseText:
            for line in text:
                for word in noiseText:
                    line = line.replace(word, "")
                print(line)


main()
#It Prints all the words
