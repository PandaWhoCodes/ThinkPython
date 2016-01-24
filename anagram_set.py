"""
Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of
words that are anagrams.
Here is an example of what the output might look like:
['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']
Hint: you might want to build a dictionary that maps from a set of letters to a list of words
that can be spelled with those letters. The question is, how can you represent the set of letters
in a way that can be used as a key?
2. Modify the previous program so that it prints the largest set of anagrams first, followed by the
second largest set, and so on.
3. In Scrabble a "bingo" is when you play all seven tiles in your rack, along with a letter on
the board, to form an eight-letter word. What set of 8 letters forms the most possible bingos?
"""

import itertools
def signature(s):
    """Returns the signature of this string, which is a string
    that contains all of the letters in order.
    """
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def all_anagrams(filename):
    """Finds all anagrams in a list of words.

    filename: string filename of the word list

    Returns: a map from each word to a list of its anagrams.
    """
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def print_anagram_sets(d):
    """Prints the anagram sets in d.

    d: map from words to list of their anagrams
    """
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)


def print_anagram_sets_in_order(d):
    """Prints the anagram sets in d in decreasing order of size.

    d: map from words to list of their anagrams
    """

    # make a list of (length, word pairs)
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

    # sort in ascending order of length
    t.sort()

    # print the sorted list
    for x in t:
        print(x)


def filter_length(d, n):
    """Select only the words in d that have n letters.

    d: map from word to list of anagrams
    n: integer number of letters

    Returns: new map from word to list of anagrams
    """
    res = {}
    for word, anagrams in d.iteritems():
        if len(word) == n:
            res[word] = anagrams
    return res

def my_anagrams(word):
    word=word.lower()
    t=list(word)
    comb_list = itertools.permutations(t)
    print(comb_list)
    for item in comb_list:
        item = ''.join(item)
        print(item)

"""

d = all_anagrams('words.txt')
print_anagram_sets_in_order(d)

eight_letters = filter_length(d, 8)
print_anagram_sets_in_order(eight_letters)
"""
my_anagrams("CAT")
my_anagrams("MALAYAM")
