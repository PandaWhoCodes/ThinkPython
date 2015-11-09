cache = {}

def ackermann(m, n):

    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    try:
        return cache[m, n]
    except KeyError:
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
        return cache[m, n]

print (ackermann(3, 4))
print (ackermann(3, 6))
