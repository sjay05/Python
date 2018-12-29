array = [1, 2, 3, 3, 2]
input = input("Sum?: ")
i = 0

while i < len(array):
    a = i
    g = 0
    while a < len(array):
        g = g + array[a]
        if g > input:
            break
        elif g == input: 
            print "Starting at index %s" % array.index(array[i]) + " and ending at %s" % array.index(array[a])
            i = len(array)
            break
        a += 1
    i += 1

while i < len(array):
    a = i
    g = 0
    while a < len(array):
        g = g + array[a]
        if g > input:
            break
        elif g == input:
            print "Starting at index %s" % array.index(index[i]) + "and ending at %s" % array.index(array[a])



























# while i < len(array):
#     a = i
#     g = 0
#     while a < len(array):
#         g = array[a] + g
#         if g == input:
#             print "Starting at index %s" % array.index(array[i]) + " and ending at %s" % array.index(array[a])
#         a += 1
#     i += 1