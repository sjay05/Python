import random
row = 0
list = []

while row < 10 :
    small = []
    column = 0
    while column < 10:
        small.append(random.randint(1,100))
        column += 1
    list.append(small)
    row += 1

print list 

for c in list:
    print c