y = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
x = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

new_matrix = []

for i in range(len(x)):
    m = []
    for a in range(len(y[0])):
        g = 0
        for b in range(len(y)):
            g += x[i][b] * y[b][a]

        m.append(g)
    new_matrix.append(m)


print new_matrix






