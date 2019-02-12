# Write a program if a list belongs to a Arithmetic Sequence or not.
array = [2, 4, 6, 8, 10]
i = 0
dif = array[1]-array[0]

while i < len(array):
    if i == len(array)-1:
        print "array is an AS"
        break
    elif array[i+1] - array[i] == dif:
        i += 1
    else:
        print "array is not an AS"
        break

