# import time

l = [x for x in range(20, 120003)]
#    0  1  2  3  4  5  6  7  8  9
median = 0
item = 21
# start_time = time.time()
median = (median + len(l)-1)/2
while True:
    if (median == 0 or median == len(l)-1) and l[median] != item:
        # end_time = time.time()
        print "item is not found in list...(:-{) in " # , (end_time - start_time)
        break
    elif l[median] == item:
        # end_time = time.time()
        print "item is found in the list...(:-}) in " # , (end_time - start_time)
        break
    elif l[median] > item:
        median = (0 + median-1)/2
    else:
        median = (median+1 + len(l)-1)/2

    print median
