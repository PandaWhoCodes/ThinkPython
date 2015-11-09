"""
Read the documentation of the dictionary method setdefault and use it to write a
more concise version of invert_dict

setdefault(key[,default])
If key is in the dictionary
return its value. If not  insert key with a value of default
and return default. default defaults to None.
"""

hist = {1: 2, 3: 4, 5: 6, 7: 8}


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    print(inverse)


def my_invert(d):
    inverse = {}

    for k, v in d.items():
        inverse.update({v: k})

    print(inverse)


invert_dict(hist)
my_invert(hist)
