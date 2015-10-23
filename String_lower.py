"""
The following functions are all intended to check whether
a string contains any
lowercase letters, but at least some
of them are wrong. For each function, describe what the function
actually does (assuming that the parameter is a string).
"""


# First function checks first character for lowercase and
# outputs BOOLEAN true or false respectively
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True

        else:
            return False


# Second  function checks first character for lowercase and
# outputs IN STRING true or false respectively


def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'

        else:
            return 'False'


# Third  function checks last character for lowercase and
# outputs returns BOOLEAN true or false respectively

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
        return flag


# Fourth  function doesnt do anything 

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
        return flag


# fifth  function checks each character for lowercase and
# outputs returns BOOLEAN true or false respectively

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
