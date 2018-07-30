a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = 0

i = 0
s = 0

while i < len(a):
    s += a[i]
    i += 1

print "while sum = ", s    

for i in a:
    c += i

print "for sum = ", c 


