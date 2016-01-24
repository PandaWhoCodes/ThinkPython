"""
If you did Exercise 10.8, you already have a function named has_duplicates that
takes a list as a parameter and returns True if there is any object
that appears more than once in the
list.
Use a dictionary to write a faster, simpler version of has_duplicates.
"""
def has_duplicates(t):
    # could not make anything better with dictionary
    # Still think the set is a faster method
    # Did not copy method from the book used SET's instead
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False


def has_duplicates2(t):
    return len(set(t)) < len(t)


# sets are lists with no dublicate entries

t = [1, 2, 3]
print(has_duplicates(t))
t.append(1)
print(has_duplicates(t))

t = [1, 2, 3]
print(has_duplicates2(t))
t.append(1)
print(has_duplicates2(t))
