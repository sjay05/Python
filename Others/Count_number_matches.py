# Write a program to count the number of matches of a number

num = 3
list = [1, 5, 6, 3, 5, 6, 8, 5, 3, 2, 5]

def count_matches(n, a):
    i = 0
    count = 0
    while i < len(a):
        if n == a[i]:
            count += 1
        i += 1
    return count

print count_matches(num, list)

a = 10
b = 20
c = a
a = b
b = c
print a
print b 
