list = range(1, 4)

def square_sum(num):
    return num ** 2

def cube_sum(num):
    return num ** 3

def list_sum(list, func):
    a = 0
    for i in list:
        a = a + func(i)

    return a

print list_sum(list, cube_sum)
print list_sum(list, square_sum)

