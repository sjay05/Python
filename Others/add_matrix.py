matrix1 = [[1, 3, 4], [4, 5, 7], [9, 6, 2]]
matrix2 = [[3, 5, 4], [3, 1, 7]]
new_matrix = []

r = 0
while r < len(matrix1):
    row_list = []
    c = 0
    while c < len(matrix1[r]):
        new = (matrix1[r])[c] + (matrix2[r])[c]
        row_list.append(new)
        c += 1
    new_matrix.append(row_list)
    r += 1

print new_matrix
