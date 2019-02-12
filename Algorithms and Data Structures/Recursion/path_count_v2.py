# Initialize 4 * 3 grid
input_grid = [
    [1, 2, 6],
    [3, 4, 7],
    [5, 8, 999]

]

# Find all paths start from 1 to 999

# output would look like another grid
# [[1, 2, 3, 6, 9, 999], [1, 4, 5, 8, 11, 999],....]

# using function closures access m and n
def paths(m, n):
    def path_count(r, c, path_grid, output_grid):
        if r == m-1 and c == n-1:
            output_grid.append(path_grid[:])
            return

        if r < m and c < n:
            path_grid.append(input_grid[r][c])
            path_count(r, c+1, path_grid, output_grid)
            path_count(r+1, c, path_grid, output_grid)
            # backtrack to remove the numbers from pathgrid
            path_grid.remove(input_grid[r][c])

    path_grid = []
    output_grid = []
    path_count(0, 0, path_grid, output_grid)
    return output_grid

print paths(3, 3)

