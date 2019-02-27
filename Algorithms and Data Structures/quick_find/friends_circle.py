# Friends Circle problem in Leetcode.com.
# Union-Find algorithm used to solve this problem. Function (find) and function (union).

M = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]

id = [i for i in range(len(M))]

def find(p, q):
    find = False
    if id[p-1] == id[q-1]:
        find = True

    return find

def union(p, q):
    i = 0
    pid = id[p-1]
    while i < len(id):
        if id[i] == pid:
            id[i] = id[q-1]

        i += 1

    return id

for i in range(len(M)):
    for j in range(len(M)):
        if M[i][j] == 1:
            union(i, j)


print id

print len(set([id[x] for x in range(len(id))]))