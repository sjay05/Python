integer = '23'
tel_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'}

s = []
for counter in range(len(integer)):
    temp = tel_dict.get(integer[counter])
    for m in range(len(temp)):
        s.append(temp[m])

main_num = len(integer)

r = []

for i in range(1 << len(s)): # shifts the binary number by 1 (1 << len(s) -> which is "3" in this case)
    ss = []
    for j in range(len(s)):
        if i & (1 << j): # uses ("+") bitwise operator to check if it doesn't equal 0
            # 1 << j
            ss.append(s[j])
    r.append(ss)


final = []
for count in range(len(r)):
    if len(r[count]) == main_num:
        final.append(r[count])

print final

