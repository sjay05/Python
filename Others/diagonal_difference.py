# Function to find the diagonal difference given a input of a square matrix
array = [[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4], [1, 2, 3, 4]]

def diagonal_difference(array):
    left = 0
    right = 0
    for a in range(0, len(array)):
        left = left + array[a][a]
        right = right + array[a][len(array) - (a + 1)]

    print abs(right - left)

diagonal_difference(array)