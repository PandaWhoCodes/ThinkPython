"""
Two words are a "reverse pair" if each is the reverse of the other. Write a program
that finds all the reverse pairs in the word list
"""


def reverse_pair(word_list):
    for i in range(0, len(word_list)-1):
        if word_list[i] == "0":
            continue

        for j in range(i + 1, len(word_list)):
            if word_list[i] == word_list[j][::-1] and word_list[j] != "0":
                print(word_list[i])
                word_list[j] = "0"


reverse_pair(["eel", "monkey", "pi", "hoh", "lee", "hoh"])
