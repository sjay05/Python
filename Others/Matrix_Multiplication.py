A = [[1, 0, 2], [1, 4, 3], [2, 5, 6]]
B = [[7, 1, 4], [3, 0, 2], [1, 5, 2]]
result = [[0]*len(A) for x in range(len(A))]

#print result

for x in range(len(A)):
    for y in range(len(A)):
        for n in range(len(A)):
            result[x][y] += A[x][n] * B[n][y]

print result
