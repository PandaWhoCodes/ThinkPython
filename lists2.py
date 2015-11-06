"""
Use capitalize_all to write a function named capitalize_nested that takes
a nested list of strings and returns a new nested list with all strings capitalized
"""


def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


print(capitalize_all(["this", "is", "a", "test"]))
