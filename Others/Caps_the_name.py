name = "sanjay"

i = 0
b = 0
c = 0
d = ""
list = []

while i < len(name):
    b = ord(name[i])
    c = b - 32
    d = chr(c)
    list.append(d)
    i += 1

s = ""
e = ""
for e in list:
    s += e

print s 
