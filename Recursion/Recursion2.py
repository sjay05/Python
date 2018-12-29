#Finding GCD for two numbers using Euclid's Method (Recursion):
a = 18
b = 84

def find_gcd(a, b):
    if b % a == 0:
        break 

    return (b % a), a

return find_gcd(a)