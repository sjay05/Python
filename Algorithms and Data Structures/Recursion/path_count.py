m = 3
n = 2

def paths(m, n):
    def path_count(r, c):
        if r == m-1 and c == n-1:
            return 1
        if r < m and c < n:
            return path_count(r, c+1) + path_count(r+1, c)
        else:
            return 0

    return path_count(0, 0)

print paths(m, n)

