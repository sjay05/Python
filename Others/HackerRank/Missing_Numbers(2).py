def missingNumbers(arr, brr):
    i = 0
    j = 0
    diff = []

    def append_to_diff():
        if not diff:
            diff.append(brr[i])  # first element check
        elif diff[-1] != brr[i]: # to avoid duplicates check last index
            diff.append(brr[i])

    while i < len(brr):
        # if not match or if reach end of arr push it to diff
        # but when pushing to diff check the last element is not same
        if j < len(arr):
            if brr[i] != arr[j]:
                append_to_diff()
            else:
                j += 1  # increment arr index only if matches
        else:
            append_to_diff()

        # just increment brr index
        i += 1

    return diff


if __name__ == '__main__':

    arr = map(int, raw_input().rstrip().split())

    brr = map(int, raw_input().rstrip().split())

    result = missingNumbers(sorted(arr), sorted(brr))

    print result
