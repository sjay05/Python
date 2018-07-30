a =  0
b = 1
num = input()

if num == 0:
    print "again."
elif num == 1:
    print "0"
elif num == 2:
    print "0"
    print "1"
else:
    print "0"
    print "1"
    for i in range(1, num+1):
        c = a + b
        a = b
        b = c
        print c

# def fib(a, b, c):
#     for i in range(1, num+1):
#         c = a + b
#         a = b
#         b = c
#         print c,
#
