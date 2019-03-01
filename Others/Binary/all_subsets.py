s = ['A', 'B', 'C', 'D']

r = []

for i in range(1 << len(s)): # shifts the binary number by 1 (1 << len(s) -> which is "3" in this case)
    ss = []
    for j in range(len(s)):
        if i & (1 << j): # uses ("+") bitwise operator to check if it doesn't equal 0
                         # 1 << j
            ss.append(s[j])
    r.append(ss)


print r




