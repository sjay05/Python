def towers_of_hanoi(n, x, y, z):

    if n >= 1:
        towers_of_hanoi(n-1, x, z, y)
        print "move from tower %s to top of tower %s" %(x, y)

        towers_of_hanoi(n-1, z, y, x)


def towers_of_hanoi2(n, x, y, z):
    if n == 0:
        return # go back to whoever last called this function

    towers_of_hanoi2(n-1, x, z, y)
    print "move from tower %s to top of tower %s" %(x, y)
    towers_of_hanoi2(n-1, z, y, x)


towers_of_hanoi2(2, "A", "B", "C")








































