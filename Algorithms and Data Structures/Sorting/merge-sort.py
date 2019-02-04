data = [2, 4, 1, 6, 3, 5]

def merge_sort(data):
    # base conditipn
    if len(data) == 1:
        return data

    left = merge_sort(data[:len(data)/2])
    right = merge_sort(data[len(data)/2:])

    return merge2(left, right)

def merge(left, right):
    #TODO: Merge two arrays
    i = 0
    l = 0
    final = []
    while i <= len(left) and l <= len(right):
        if i == len(left)-1:
            final.extend(right[l:])
            break
        elif l == len(right)-1:
            final.extend(left[i:])
            break
        elif right[l] < left[i]:
            final.append(right[l])
            l += 1
        elif right[l] > left[i]:
            final.append(left[i])
            i += 1
        elif right[l] == left[i]:
            final.append(left[i])
            final.append(right[l])
            i += 1
            l += 1

    return final

def merge2(left, right):
    li = 0
    ri = 0
    sl = []

    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
           sl.append(left[li])
           li += 1
        elif left[li] > right[ri]:
            sl.append(right[ri])
            ri += 1
        else:
            sl.append(left[li])
            sl.append(right[ri])
            li += 1
            ri += 1

    if li < len(left):
        sl.extend(left[li:])
    if ri < len(right):
        sl.extend(right[ri:])

    return sl

print merge_sort(data)
