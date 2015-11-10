"""
Exponentiation of large integers is the basis of common algorithms for public-key encryption.
Read the Wikipedia page on the RSA algorithm (http: // en. wikipedia. org/ wiki/
RSA_ ( algorithm) ) and write functions to encode and decode messages.
"""
import fractions


def gen_keys():
    p = int(input("p: "))
    q = int(input("q: "))
    n = p * q
    phi = (p - 1) * (q - 1)
    e = get_e(phi)

    d = get_d(e, phi)
    print("N = ", n, "and e = ", e)
    print("d = ", d, " and phi = ", phi)
    return [n, e, d]


def encode(e, n):
    c = int(input("Number to encode: "))
    print(pow(c, e, n))


def decode(d, n):
    c = int(input("Number to decode: "))
    print(pow(c, d, n))


def even(x):
    return x % 2 == 0


def get_e(m):
    """Finds an e coprime with m."""
    e = 2
    while fractions.gcd(e, m) != 1:
        e += 1
    return e


def get_d(e, phi):
    count = 1
    while True:
        if ((count * e) % phi) == 1:
            return count
        count = count + 1


n, e, d = gen_keys()
encode(e, n)
decode(d, n)
