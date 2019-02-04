s = "hello world"

ccount = []
icount = []

for c in s:
    if c not in ccount:
        ccount.append(c)
        icount.append(1)
    else:
        index = ccount.index(c)
        icount[index] = icount[index] + 1

for i, c in enumerate(ccount):
    print (c, icount[i])
