# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    diff = []
    darr = {}
    dbrr = {}
    for aval in arr:
        if aval not in darr:
            darr[aval] = 1
        else:
            darr[aval] += 1

    for bval in brr:
        if bval not in dbrr:
            dbrr[bval] = 1
        else:
            dbrr[bval] += 1

    for x,y in dbrr.items():
        if x in darr.keys():
            if y != darr[x]:
                diff.append(x)
        else:
            diff.append(x)

    return diff


if __name__ == '__main__':

    arr = map(int, raw_input().rstrip().split())

    brr = map(int, raw_input().rstrip().split())

    result = missingNumbers(arr, brr)

    print result