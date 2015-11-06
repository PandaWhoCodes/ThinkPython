"""
Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns
True if they are anagrams.
"""


def is_anagram():
    s1 = input("Enter the first String:")
    s2 = input("Enter the second String:")
    s3 = ""
    s1_list = list(s1)
    s1_list.sort()
    s2_list = list(s2)
    s2_list.sort()
    if (s1_list == s2_list):
        print("Anagram Found")
    else:
        print("Anagrams not found")


is_anagram()
