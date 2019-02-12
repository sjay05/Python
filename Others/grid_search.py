def find_sublist(l, s):
    ls = "".join([str(x) for x in l])
    ss = "".join([str(x) for x in s])
    if ss in ls:
        return ls.index(ss)
    else:
        return -1

def search(large, small):
    for row in range(len(large)):
        if row > (len(large) - len(small)):
            return False

        col = find_sublist(large[row], small[0])
        if col == -1:
            continue

        if col == None:
            print col
            return False

        lrow = row + 1
        match = True
        srow = 1
        for x in range(len(small)-1):
            for j, i in enumerate(range(col, col+len(small[0]))):
                if large[lrow][i] != small[srow][j]:
                    match = False
                    break
            if not match:
                break
            lrow += 1
            srow += 1

        if match:
            return True


large = [
    [1,2,3,4,5,6,7,8,9,0],
    [0,9,8,7,6,5,4,3,2,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [2,2,2,2,2,2,2,2,2,2]
]

small = [
    [1,1],
    [1,1],
    [2,2]
]


print search(large, small)







