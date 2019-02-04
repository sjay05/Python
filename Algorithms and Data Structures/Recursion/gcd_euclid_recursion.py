def gcd(n, d):
    r = n % d
    if r == 0:
        return d
    return gcd(d, r)

print gcd(270, 192)
