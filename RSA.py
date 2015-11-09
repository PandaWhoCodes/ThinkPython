"""
Exponentiation of large integers is the basis of common algorithms for public-key encryption.
Read the Wikipedia page on the RSA algorithm (http: // en. wikipedia. org/ wiki/
RSA_ ( algorithm) ) and write functions to encode and decode messages.
"""
def gen_keys():
    p = int(input("p: "))
    q = int(input("q: "))
    n = p * q
    m = (p - 1) * (q - 1)
    e = get_e(m)
    print("N = ", n, "and e = ", e)
    d = get_d(e, m)
    while d < 0:
        d += m
    return [n, e, d]


def encode(n, e):
    c = int(input("Number to encode: "))
    print(pow(c, e, n))


def decode(d, n):
    while 1:
        c = int(input("Number to decode: "))
        print(pow(c, d, n))


def even(x):
    return x % 2 == 0


def get_e(m):
    """Finds an e coprime with m."""
    e = 2
    while gcd(e, m) != 1:
        e += 1
    return e


def gcd(a, b):
    """Euclid's Algorithm: Takes two integers and returns gcd."""
    while b > 0:
        a, b = b, a % b

    return a


def get_d(e, m):
    x = lasty = 0
    lastx = y = 1
    while m != 0:
        q = e // m
        e, m = m, e % m
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y
    return lastx


n, e, d = gen_keys()
n = int(input("Public Key(N): "))
e = int(input("e: "))
encode(n, e)
n, e, d = gen_keys()
decode(d, n)
