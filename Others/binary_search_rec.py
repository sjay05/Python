#l = [x for x in range(21, 40)]
l = [4, 6, 8, 9, 10, 11]
n = 15


def binary_search(low, high, item):
    median = (low + high)/2
    if low > high or high < low:
        return -1
    elif item > l[median]:
        return binary_search(median+1, high, item)
    elif item < l[median]:
        return binary_search(low, median-1, item)
    else:
        return item


print binary_search(0, len(l)-1, n)

