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
    inverse = {}
    for key, val in d.iteritems():
        inverse.setdefault(val, []).append(key)
    return inverse


if __name__ == '__main__':
    d = dict(a=1, b=2, c=3, z=1)
    inverse = invert_dict(d)
    for val, keys in inverse.items():
        print(val, keys)

invert_dict(hist)
my_invert(hist)
